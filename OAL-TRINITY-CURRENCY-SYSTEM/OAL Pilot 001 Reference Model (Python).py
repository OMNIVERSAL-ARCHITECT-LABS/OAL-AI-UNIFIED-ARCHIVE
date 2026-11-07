"""
OAL Currency Laboratory - Pilot Packet 001 reference model
Namespace: perplexity/pilot-packet-001-v0.1
Prepared by: Perplexity Computer (session orchestrator model reported by platform: Claude Opus 5.5)
Status: PROPOSED / PRE-ADOPTION REFERENCE EXECUTION. Not an owner-adopted laboratory run.

Evidence level of every output produced by this file: E2-EXECUTED (the program ran).
An E2 result shows what the stated rules imply when executed. It is NOT evidence that any
real Quantum Credit capability exists (that would require E3-EXTERNAL, which is out of scope).
"""
from __future__ import annotations
import copy, itertools, json, sys
from dataclasses import dataclass, field

UNIT_TYPE = "R"            # the only declared resource type in the fixture
REQUEST_QTY = 3

# ---------------------------------------------------------------- state
@dataclass
class Unit:
    uid: str
    utype: str
    origin: str            # "fixture" | "minted:<run>" | "enacted:<run>"
    encumbered: bool = False

@dataclass
class World:
    holdings: dict          # party -> list[Unit]
    consent_A: bool = True
    fulfilled: set = field(default_factory=set)   # request ids already DELIVERED
    log: list = field(default_factory=list)

    def count(self, p): return len(self.holdings.get(p, []))
    def total(self): return sum(len(v) for v in self.holdings.values())
    def snapshot(self):
        return {p: sorted(u.uid for u in us) for p, us in self.holdings.items()}

def fixture(a_units=10):
    return World(holdings={"A": [Unit(f"A{i:02d}", UNIT_TYPE, "fixture") for i in range(1, a_units+1)],
                           "B": []})

# ---------------------------------------------------------------- request
@dataclass
class Request:
    rid: str
    recipient: str = "B"
    qty: object = REQUEST_QTY      # int, or None if unspecified
    utype: object = UNIT_TYPE      # str, or None if unspecified
    extra_predicates: list = field(default_factory=list)  # additional end-state predicates (for F03)
    interrupt_after: object = None # inject a delivery fault after n units (F01-c)

# ---------------------------------------------------------------- validation gates (shared by all configs)
DECLARED_TYPES = {UNIT_TYPE}

def gate_definition(req):
    if req.qty is None or req.utype is None:
        return "UNDEFINED_TARGET", "quantity or unit type not specified"
    if req.utype not in DECLARED_TYPES:
        return "UNDEFINED_TARGET", f"unit type {req.utype!r} is not declared in the fixture"
    if not isinstance(req.qty, int) or req.qty <= 0:
        return "UNDEFINED_TARGET", "quantity is not a positive integer"
    return None

def gate_coherence(req, w):
    """Detect end-state predicates that cannot all hold under the fixture's DEFINITIONS.
    Definitional identity: total == sum of holdings (true by definition of 'total').
    That identity is not a conservation law; creation may change the total, nothing can make
    total differ from the sum of holdings without redefining 'total'."""
    preds = req.extra_predicates
    fixed = {}
    for kind, party, val in preds:
        if kind == "count":
            if party in fixed and fixed[party] != val:
                return "INCOHERENT_TARGET", f"{party} required to hold both {fixed[party]} and {val}"
            fixed[party] = val
    want_B = w.count(req.recipient) + req.qty
    if req.recipient in fixed and fixed[req.recipient] != want_B:
        return "INCOHERENT_TARGET", f"request requires {req.recipient}={want_B} and {req.recipient}={fixed[req.recipient]}"
    for kind, party, val in preds:
        if kind == "total":
            parties = set(w.holdings) | set(fixed)
            known = {p: fixed.get(p) for p in parties}
            if all(v is not None for v in known.values()) or (req.recipient not in fixed):
                # fill recipient from request
                known[req.recipient] = want_B
                if all(v is not None for v in known.values()):
                    s = sum(known.values())
                    if s != val:
                        return "INCOHERENT_TARGET", f"total required {val} but required holdings sum to {s}"
    return None

# ---------------------------------------------------------------- configurations
class Config:
    cid = "BASE"
    capability = "BASE"
    def run(self, w: World, req: Request, run_id: str) -> dict: raise NotImplementedError

def valuation(req):
    # Pilot-only synthetic convention (1 R-unit delivered == 1 valuation unit). NOT a permanent QC rule.
    return {"domain": "synthetic-R-equivalence", "amount": req.qty, "unit": f"{req.utype}-unit",
            "evidence": "E0-STIPULATED convention"}

class Eval(Config):
    cid = "C-EVAL"; capability = "EVALUATE"
    def run(self, w, req, run_id):
        return {"status": "VALUED", "value_object": valuation(req), "delivered": 0}

class Transfer(Config):
    cid = "C-XFER"; capability = "TRANSFER"
    atomic = True
    def run(self, w, req, run_id):
        if not w.consent_A:
            return {"status": "REJECTED_UNAUTHORIZED", "delivered": 0, "reason": "A's consent is not granted"}
        if w.count("A") < req.qty:
            return {"status": "REJECTED_INSUFFICIENT", "delivered": 0,
                    "reason": f"A holds {w.count('A')} < {req.qty}; no other pool exists"}
        moved = []
        for i in range(req.qty):
            if req.interrupt_after is not None and i == req.interrupt_after:
                if self.atomic:
                    for u in moved:  # roll back
                        w.holdings[req.recipient].remove(u); w.holdings["A"].append(u)
                    return {"status": "FAILED_ROLLED_BACK", "delivered": 0,
                            "reason": f"fault after {i} units; atomic rule restored initial state"}
                return {"status": "PARTIAL", "delivered": len(moved),
                        "reason": f"fault after {i} units; non-atomic rule leaves partial state"}
            u = w.holdings["A"].pop(0); w.holdings[req.recipient].append(u); moved.append(u)
        return {"status": "DELIVERED", "delivered": len(moved), "moved_uids": [u.uid for u in moved]}

class TransferNonAtomic(Transfer):
    cid = "C-XFER-NA"; atomic = False

class Create(Config):
    cid = "C-CREATE"; capability = "CREATE"
    def run(self, w, req, run_id):
        made = []
        for i in range(req.qty):
            if req.interrupt_after is not None and i == req.interrupt_after:
                # declared rule: minted units that were not delivered are void; delivered ones remain
                return {"status": "PARTIAL", "delivered": len(made),
                        "reason": f"fault after {i} units; creation is not rolled back under the declared rule"}
            u = Unit(f"M-{run_id}-{i+1}", req.utype, f"minted:{run_id}")
            w.holdings[req.recipient].append(u); made.append(u)
        return {"status": "DELIVERED", "delivered": len(made), "minted_uids": [u.uid for u in made]}

class EnactUnspecified(Config):
    """ENACT with no declared side-effect rule. The packet requires this configuration to
    report UNDERSPECIFIED_CONFIG rather than silently choosing transfer or creation."""
    cid = "C-ENACT-U"; capability = "ENACT-UNSPECIFIED"
    def run(self, w, req, run_id):
        return {"status": "UNDERSPECIFIED_CONFIG", "delivered": 0,
                "reason": "target predicate 'B gains 3' does not determine A, the total, or unit provenance"}

class EnactMinimal(Config):
    """ENACT with a declared minimal-change rule: only variables named in the target predicate
    change; every other variable is frozen. Unit provenance label: enacted."""
    cid = "C-ENACT-M"; capability = "ENACT-MINIMAL"
    def run(self, w, req, run_id):
        made = []
        for i in range(req.qty):
            if req.interrupt_after is not None and i == req.interrupt_after:
                return {"status": "PARTIAL", "delivered": len(made), "reason": "fault injected"}
            u = Unit(f"E-{run_id}-{i+1}", req.utype, f"enacted:{run_id}")
            w.holdings[req.recipient].append(u); made.append(u)
        return {"status": "DELIVERED", "delivered": len(made), "enacted_uids": [u.uid for u in made]}

class EnactNamedSource(Config):
    """ENACT whose target predicate also names A: 'B gains 3 AND A loses 3'."""
    cid = "C-ENACT-S"; capability = "ENACT-NAMED-SOURCE"
    def run(self, w, req, run_id):
        if w.count("A") < req.qty:
            return {"status": "INCOHERENT_TARGET", "delivered": 0,
                    "reason": f"predicate 'A loses {req.qty}' cannot hold when A holds {w.count('A')} (holdings are non-negative by definition)"}
        r = Transfer().run(w, req, run_id)
        return r

CONFIGS = [Eval(), Transfer(), TransferNonAtomic(), Create(), EnactUnspecified(), EnactMinimal(), EnactNamedSource()]

# ---------------------------------------------------------------- engine wrapper (shared gates, replay rule)
def execute(config: Config, w: World, req: Request, run_id: str):
    before = {"A": w.count("A"), "B": w.count("B"), "total": w.total()}
    g = gate_definition(req) or gate_coherence(req, w)
    if g:
        res = {"status": g[0], "delivered": 0, "reason": g[1]}
    elif req.rid in w.fulfilled and not isinstance(config, Eval):
        res = {"status": "DUPLICATE_SUPPRESSED", "delivered": 0,
               "reason": f"request {req.rid} already DELIVERED; replay rule: same request id is idempotent"}
    else:
        res = config.run(w, req, run_id)
        if res["status"] == "DELIVERED":
            w.fulfilled.add(req.rid)
    after = {"A": w.count("A"), "B": w.count("B"), "total": w.total()}
    res.update({"config": config.cid, "rid": req.rid, "before": before, "after": after})
    res["completion_predicate"] = completion(before, after, res, req)
    res["verdict_A_internal_consistency"] = check_invariants(config, before, after, res, w)
    res["verdict_B_requested_outcome"] = "SATISFIED" if res["completion_predicate"] else "NOT SATISFIED"
    res["consequence_record"] = "NONE (consequence model not active in Pilot 001; no NCOIN emitted)"
    res["settlement_record"] = "ordinary log entry only (1COIN not active in Pilot 001)"
    w.log.append(res)
    return res

def completion(before, after, res, req):
    """Completion predicate CP-001: B's holdings increased by exactly qty units of the declared
    type, all unencumbered, in this run, with status DELIVERED."""
    return res["status"] == "DELIVERED" and (after["B"] - before["B"]) == (req.qty if isinstance(req.qty, int) else -1)

BIND_BY_LABEL = False   # True reproduces the v0.1-draft defect (invariants bound to config labels)

def _is(config, label_ids, capabilities):
    if BIND_BY_LABEL:
        return config.cid in label_ids
    return config.capability in capabilities

def check_invariants(config, before, after, res, w):
    issues = []
    if after["total"] != after["A"] + after["B"]:
        issues.append("definitional identity total==A+B violated (undeclared party holds units)")
    d = res.get("delivered", 0)
    if res["status"] in ("DELIVERED", "PARTIAL") and after["B"] - before["B"] != d:
        issues.append("reported delivery does not match B's change")
    if res["status"] not in ("DELIVERED", "PARTIAL") and (after != before):
        issues.append("state changed although status reports no delivery")
    if _is(config, ("C-XFER", "C-XFER-NA", "C-ENACT-S"), ("TRANSFER", "ENACT-NAMED-SOURCE")):
        if res["status"] in ("DELIVERED", "PARTIAL") and after["total"] != before["total"]:
            issues.append("transfer changed the total")
        if res["status"] in ("DELIVERED", "PARTIAL") and (before["A"] - after["A"]) != d:
            issues.append("A's debit does not equal B's credit")
    if _is(config, ("C-CREATE", "C-ENACT-M"), ("CREATE", "ENACT-MINIMAL")) and res["status"] in ("DELIVERED", "PARTIAL"):
        if after["A"] != before["A"]: issues.append("creation/minimal enactment changed A")
        if after["total"] - before["total"] != d: issues.append("total did not rise by the created amount")
    if _is(config, ("C-EVAL",), ("EVALUATE",)) and after != before:
        issues.append("evaluation-only config moved resources")
    return "CONSISTENT" if not issues else "INCONSISTENT: " + "; ".join(issues)

def check_log_idempotency(log):
    """Cross-step assertion R-ID: a request id may reach DELIVERED at most once per world."""
    seen, dup = set(), []
    for e in log:
        if e["status"] == "DELIVERED":
            if e.get("rid") in seen: dup.append(e.get("rid"))
            seen.add(e.get("rid"))
    return "CONSISTENT" if not dup else f"INCONSISTENT: request id(s) delivered more than once: {dup}"

# ---------------------------------------------------------------- cases
def cases():
    return [
        ("P001-F01-BASE", lambda: fixture(10), lambda: [Request("REQ-1")]),
        ("P001-F01-a (A holds 2)", lambda: fixture(2), lambda: [Request("REQ-1")]),
        ("P001-F01-b (replay same id)", lambda: fixture(10), lambda: [Request("REQ-1"), Request("REQ-1")]),
        ("P001-F01-b2 (same content, new id)", lambda: fixture(10), lambda: [Request("REQ-1"), Request("REQ-2")]),
        ("P001-F01-c (fault after 2)", lambda: fixture(10), lambda: [Request("REQ-1", interrupt_after=2)]),
        ("P001-F01-d (consent revoked)", lambda: (lambda w: (setattr(w, "consent_A", False), w)[1])(fixture(10)), lambda: [Request("REQ-1")]),
        ("P001-F01-e (unit type unstated)", lambda: fixture(10), lambda: [Request("REQ-1", utype=None)]),
        ("P001-F03-U1 (undeclared type Q)", lambda: fixture(10), lambda: [Request("REQ-1", utype="Q")]),
        ("P001-F03-U2 (quantity unstated)", lambda: fixture(10), lambda: [Request("REQ-1", qty=None)]),
        ("P001-F03-I1 (B=3 and B=0)", lambda: fixture(10), lambda: [Request("REQ-1", extra_predicates=[("count", "B", 0)])]),
        ("P001-F03-I2 (A stays 10, total stays 10)", lambda: fixture(10), lambda: [Request("REQ-1", extra_predicates=[("count", "A", 10), ("total", None, 10)])]),
    ]

def run_all():
    rows = []
    for (case_id, mkworld, mkreqs) in cases():
        for cfg in CONFIGS:
            w = mkworld()
            reqs = mkreqs()
            outs = []
            for k, r in enumerate(reqs):
                outs.append(execute(cfg, w, r, f"{case_id.split()[0]}-{cfg.cid}-{k+1}"))
            rows.append({"case": case_id, "config": cfg.cid, "steps": outs})
    return rows

# ---------------------------------------------------------------- mutation tests
# Deliberately defective implementations. A useful assertion set must flag each one.
class BugNoDebit(Transfer):
    cid = "MUT-1 transfer-without-debit"
    def run(self, w, req, run_id):
        for i in range(req.qty):
            w.holdings["B"].append(Unit(f"X{i}", req.utype, "fixture"))
        return {"status": "DELIVERED", "delivered": req.qty}

class BugReceiptBeforeDelivery(Transfer):
    cid = "MUT-2 certify-before-delivery"
    def run(self, w, req, run_id):
        # reports DELIVERED, but the fault stops movement after 2 units
        moved = 0
        for i in range(req.qty):
            if req.interrupt_after is not None and i == req.interrupt_after: break
            w.holdings["B"].append(w.holdings["A"].pop(0)); moved += 1
        return {"status": "DELIVERED", "delivered": req.qty}

class BugHiddenPool(Transfer):
    cid = "MUT-3 hidden-third-party-pool"
    def run(self, w, req, run_id):
        if w.count("A") < req.qty:
            w.holdings["POOL"] = []
            for i in range(req.qty):
                w.holdings["B"].append(Unit(f"P{i}", req.utype, "pool"))
            w.holdings["POOL"] = []  # pool silently drained/hidden
            return {"status": "DELIVERED", "delivered": req.qty}
        return super().run(w, req, run_id)

class BugEvalMoves(Eval):
    cid = "MUT-4 evaluation-that-moves"
    def run(self, w, req, run_id):
        w.holdings["B"].append(w.holdings["A"].pop(0))
        return {"status": "VALUED", "value_object": valuation(req), "delivered": 0}

class BugCreateDebits(Create):
    cid = "MUT-5 creation-that-debits-A"
    def run(self, w, req, run_id):
        r = super().run(w, req, run_id)
        w.holdings["A"].pop(0)
        return r

def execute_no_replay_guard(config, w, req, run_id):
    before = {"A": w.count("A"), "B": w.count("B"), "total": w.total()}
    res = config.run(w, req, run_id)
    after = {"A": w.count("A"), "B": w.count("B"), "total": w.total()}
    res.update({"config": config.cid + " (MUT-6 replay-guard removed)", "rid": req.rid, "before": before, "after": after})
    w.log.append(res)
    res["verdict_A_internal_consistency"] = check_invariants(config, before, after, res, w)
    return res

def mutation_suite():
    out = []
    def one(label, cfg, world, req, detect):
        r = execute(cfg, world, req, "MUT")
        flagged = detect(r)
        out.append({"mutant": label, "status": r["status"], "after": r["after"],
                    "verdict_A": r["verdict_A_internal_consistency"], "detected": flagged})
    one("MUT-1 transfer-without-debit", BugNoDebit(), fixture(10), Request("REQ-1"),
        lambda r: r["verdict_A_internal_consistency"] != "CONSISTENT")
    one("MUT-2 certify-before-delivery", BugReceiptBeforeDelivery(), fixture(10), Request("REQ-1", interrupt_after=2),
        lambda r: r["verdict_A_internal_consistency"] != "CONSISTENT" or not r["completion_predicate"])
    one("MUT-3 hidden-third-party-pool", BugHiddenPool(), fixture(2), Request("REQ-1"),
        lambda r: r["verdict_A_internal_consistency"] != "CONSISTENT")
    one("MUT-4 evaluation-that-moves", BugEvalMoves(), fixture(10), Request("REQ-1"),
        lambda r: r["verdict_A_internal_consistency"] != "CONSISTENT")
    one("MUT-5 creation-that-debits-A", BugCreateDebits(), fixture(10), Request("REQ-1"),
        lambda r: r["verdict_A_internal_consistency"] != "CONSISTENT")
    # MUT-6: replay guard removed -> second identical request delivers again
    w = fixture(10); t = Transfer()
    r1 = execute_no_replay_guard(t, w, Request("REQ-1"), "M6a")
    r2 = execute_no_replay_guard(t, w, Request("REQ-1"), "M6b")
    idem = check_log_idempotency(w.log)
    dup = idem != "CONSISTENT"
    # detection rule: a request id may reach DELIVERED at most once (CP-001 + replay rule R-ID)
    out.append({"mutant": "MUT-6 replay-guard-removed", "status": f"{r1['status']} then {r2['status']}",
                "after": r2["after"], "verdict_A": r2["verdict_A_internal_consistency"],
                "detected": dup, "log_assertion": idem, "note": "per-step invariants pass; only the cross-step idempotency assertion detects it"})
    return out

# ---------------------------------------------------------------- M04 numeric check
def m04(B=100.0, alphas=(0.0, 0.25, 0.4, 0.49, 0.5, 0.51, 0.75, 1.0, -0.5), T=150):
    res = []
    for a in alphas:
        fixed = None if abs(1 - 2*a) < 1e-12 else 2*B/(1 - 2*a)
        I = 2*B                       # I_0 = 2B (Gemini's initial condition)
        traj = [I]
        for t in range(1, T+1):
            I = 2*B + 2*a*I
            traj.append(I)
        res.append({"alpha": a, "fixed_point": fixed, "I_1": traj[1], "I_10": traj[10],
                    "I_150": traj[150], "I_149": traj[149]})
    return res

if __name__ == "__main__":
    global_mod = sys.modules[__name__]
    global_mod.BIND_BY_LABEL = True
    muts_label = mutation_suite()
    global_mod.BIND_BY_LABEL = False
    rows = run_all()
    muts = mutation_suite()
    m = m04()
    json.dump({"runs": rows, "mutations_label_bound_draft": muts_label, "mutations": muts, "m04": m}, open("pilot001_reference_results.json", "w"), indent=1, default=str)
    # compact console log
    for r in rows:
        for k, s in enumerate(r["steps"]):
            print(f"{r['case']:<42} {r['config']:<10} step{k+1} {s['status']:<22} A {s['before']['A']}->{s['after']['A']} "
                  f"B {s['before']['B']}->{s['after']['B']} T {s['before']['total']}->{s['after']['total']} "
                  f"CP={'Y' if s['completion_predicate'] else 'N'} VA={s['verdict_A_internal_consistency'][:12]}")
    print()
    print("MUTATION SUITE - draft harness (invariants bound to config labels)")
    for x in muts_label: print(" ", x["mutant"], "| detected:", x["detected"], "|", x["verdict_A"])
    print("MUTATION SUITE - corrected harness (invariants bound to declared capability)")
    for x in muts: print(" ", x["mutant"], "| detected:", x["detected"], "|", x["verdict_A"], "|", x.get("log_assertion",""))
    print()
    for x in m: print(x)
