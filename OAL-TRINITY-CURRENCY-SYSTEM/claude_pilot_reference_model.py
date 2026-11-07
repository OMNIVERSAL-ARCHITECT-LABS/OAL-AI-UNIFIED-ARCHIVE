"""Reference model for OAL Run Card 001 (Claude's independent pass).

Usage: python3 -I claude_pilot_reference_model.py results.json   (prints the run log; writes results.json)
Standard library only. Deterministic: no randomness, no network.


EVIDENCE LABEL: EXECUTED. This program executes the transition rules written in
the Run Card. It shows that those rules are internally consistent and that the
assertions can detect deliberately defective variants. It does NOT show that a
real Quantum Credit can transfer, create or enact anything.
"""
import json, copy, sys

# ---------------------------------------------------------------- F01 model
def fresh(a_units=10):
    return {"A": [f"u{i}" for i in range(1, a_units + 1)], "B": [], "next": a_units + 1,
            "log": [], "receipt": None, "ncoin": [], "done": {}}

def total(s): return len(s["A"]) + len(s["B"])

def run(cfg, s, req, auth="GRANTED", dup="DEDUP", interrupt_after=None,
        receipt_mode="AT_COMPLETION", defect=None, qty_defined=True):
    """cfg in EVAL, TRANSFER, CREATE, ENACT_SRC, ENACT_NOSRC, ENACT_UNDECL.
    Returns (status, reason). Mutates s."""
    rid = req["id"]
    # Gate 1: target resolution (early exit before any capability is used)
    if not qty_defined:
        s["log"].append(f"{rid}:GATE1 UNDEFINED_TARGET")
        return "UNDEFINED_TARGET", "QUANTITY_UNIT_UNSPECIFIED"
    # Duplicate-request policy
    if rid in s["done"] and dup == "DEDUP":
        s["log"].append(f"{rid}:DUPLICATE returned prior result")
        return s["done"][rid], "DUPLICATE_NOT_REEXECUTED"
    n = req["n"]
    if cfg == "EVAL":
        s["log"].append(f"{rid}:EVALUATE V(T)={n} test-units")
        s["done"][rid] = "EVALUATED"
        return "EVALUATED", "NO_RESOURCE_MOVEMENT_CLAIMED"
    # Gate: authority (distinguish denied from unknown)
    if auth == "DENIED":
        s["log"].append(f"{rid}:AUTH DENIED")
        return "UNAUTHORIZED", "AUTHORITY_DENIED"
    if auth == "UNKNOWN":
        s["log"].append(f"{rid}:AUTH UNKNOWN")
        return "AUTHORITY_UNKNOWN", "AUTHORITY_NOT_ESTABLISHED"
    if cfg == "ENACT_UNDECL":
        s["log"].append(f"{rid}:ENACT accounting undeclared")
        return "UNDERSPECIFIED", "ACCOUNTING_EFFECTS_UNDECLARED"
    moves_from_A = cfg in ("TRANSFER", "ENACT_SRC")
    if moves_from_A and len(s["A"]) < n:
        s["log"].append(f"{rid}:INSUFFICIENT_INVENTORY A={len(s['A'])} need {n}")
        return "REJECTED", "INSUFFICIENT_INVENTORY"
    if receipt_mode == "AT_START" or defect == "RECEIPT_AT_START":
        s["receipt"] = "ISSUED"          # defective: certifies before delivery
    delivered = 0
    for k in range(n):
        if interrupt_after is not None and k >= interrupt_after:
            break
        if moves_from_A:
            u = s["A"].pop()
            s["B"].append(u)
            s["log"].append(f"{rid}:MOVE {u} A->B")
        else:
            u = f"u{s['next']}"; s["next"] += 1
            s["B"].append(u)
            s["log"].append(f"{rid}:CREATE {u} in B")
        delivered += 1
    if defect == "TRANSFER_CREATES" and moves_from_A:
        # defective transfer: also creates a duplicate, breaking conservation
        u = f"u{s['next']}"; s["next"] += 1; s["B"].append(u)
        s["log"].append(f"{rid}:DEFECT extra unit {u}")
    if delivered < n:
        status, reason = "PARTIAL", f"DELIVERED_{delivered}_OF_{n}"
    else:
        status, reason = "RESOLVED_SETTLED", "COMPLETION_PREDICATE_MET"
        if receipt_mode == "AT_COMPLETION" and defect != "RECEIPT_AT_START":
            s["receipt"] = "ISSUED"
    if defect == "NCOIN_ON_FAILURE" and status != "RESOLVED_SETTLED":
        s["ncoin"].append({"trigger": "failure_only"})
    s["done"][rid] = status
    return status, reason

def verdicts(cfg, s0_B, s, status, n=3):
    """Verdict A: internal consistency vs declared rules (assertions).
       Verdict B: outcome satisfaction (B gained >= n usable units)."""
    gained = len(s["B"]) - s0_B
    b = "SATISFIED" if gained >= n else ("PARTIAL" if gained > 0 else "NOT_SATISFIED")
    return b

def assertions(cfg, s, status, a0, b0, declared_conservation):
    res = {}
    # A1 conservation applies only where the configuration declares it
    if declared_conservation:
        res["A1_conservation_declared"] = (total(s) == a0 + b0)
    # A2 completion: SETTLED/RESOLVED only if completion predicate met
    res["A2_no_settled_without_delivery"] = (status != "RESOLVED_SETTLED") or (len(s["B"]) - b0 >= 3)
    # A3 receipt only at completion
    res["A3_receipt_only_when_complete"] = (s["receipt"] is None) or (len(s["B"]) - b0 >= 3)
    # A4 no NCOIN without a separately evidenced consequence record
    res["A4_no_automatic_NCOIN"] = (len(s["ncoin"]) == 0)
    return res

CFGS = [("EVAL", False), ("TRANSFER", True), ("CREATE", False),
        ("ENACT_SRC", True), ("ENACT_NOSRC", False), ("ENACT_UNDECL", False)]

def as_cfg(c): return "CREATE" if c == "ENACT_NOSRC" else c

def case(label, a_units=10, auth="GRANTED", dup="DEDUP", interrupt=None, qty_defined=True,
         repeat=False, receipt_mode="AT_COMPLETION", defect=None, only=None):
    rows = []
    for cfg, cons in CFGS:
        if only and cfg not in only: continue
        s = fresh(a_units); a0, b0 = len(s["A"]), 0
        req = {"id": "R1", "n": 3}
        st, why = run(as_cfg(cfg) if cfg != "ENACT_NOSRC" else "CREATE", s, req, auth, dup,
                      interrupt, receipt_mode, defect, qty_defined) if cfg != "ENACT_UNDECL" else \
                  run("ENACT_UNDECL", s, req, auth, dup, interrupt, receipt_mode, defect, qty_defined)
        if repeat:
            st, why = run(as_cfg(cfg) if cfg not in ("ENACT_NOSRC", "ENACT_UNDECL") else
                          ("CREATE" if cfg == "ENACT_NOSRC" else "ENACT_UNDECL"),
                          s, req, auth, dup, interrupt, receipt_mode, defect, qty_defined)
        vb = verdicts(cfg, b0, s, st)
        asr = assertions(cfg, s, st, a0, b0, cons)
        rows.append({"case": label, "config": cfg, "status": st, "reason": why,
                     "A": len(s["A"]), "B": len(s["B"]), "total": total(s),
                     "delta_total": total(s) - (a0 + b0), "receipt": s["receipt"],
                     "ncoin": len(s["ncoin"]), "verdict_B": vb,
                     "verdict_A": "CONSISTENT" if all(asr.values()) else "ASSERTION_FAILED",
                     "assertions": asr, "B_units": list(s["B"]), "log": list(s["log"])})
    return rows

F01 = {}
F01["B0 baseline"] = case("RC-001A/B0")
F01["P1 insufficient inventory (A=2)"] = case("RC-001A/P1", a_units=2)
F01["P2 authority denied"] = case("RC-001A/P2", auth="DENIED")
F01["P3 authority unknown"] = case("RC-001A/P3", auth="UNKNOWN")
F01["P4 quantity unit unspecified"] = case("RC-001A/P4", qty_defined=False)
F01["P5 replay, DEDUP policy"] = case("RC-001A/P5", repeat=True, dup="DEDUP")
F01["P6 replay, REEXECUTE policy"] = case("RC-001A/P6", repeat=True, dup="REEXEC")
F01["P7 delivery interrupted after 2"] = case("RC-001A/P7", interrupt=2)

# Defective-implementation checks (must be caught by the assertions)
DEFECTS = []
for name, kw, only in [
    ("D1 receipt issued at start of delivery", dict(interrupt=2, receipt_mode="AT_START"), ["TRANSFER"]),
    ("D2 transfer that also creates a unit", dict(defect="TRANSFER_CREATES"), ["TRANSFER"]),
    ("D3 NCOIN emitted on any failure", dict(interrupt=2, defect="NCOIN_ON_FAILURE"), ["TRANSFER"]),
]:
    r = case(name, only=only, **kw)[0]
    failed = [k for k, v in r["assertions"].items() if not v]
    DEFECTS.append({"defect": name, "caught_by": failed, "caught": bool(failed)})
# control: the correct implementation under the same perturbation passes
ctrl = case("control interrupt", interrupt=2, only=["TRANSFER"])[0]
CONTROL = {"status": ctrl["status"], "assertions": ctrl["assertions"]}

# --------------------------------------------------------- F03 / F04 returns
TARGETS = [
    ("T1 undefined",   "target referent unspecified",             "UNDEFINED_TARGET",  False),
    ("T2 contradiction",  "object must hold X=3 and X=5 in one state", "INCOHERENT_TARGET", False),
    ("T3 no-seller",   "title to a natural star system (no party can sell)", "NO_SELLER", True),
    ("T4 unknown-seller", "encrypted artifact, owner exists but unindexed", "SELLER_UNKNOWN", True),
    ("T5 non-transferable", "valued personal credential, bound to holder", "NON_TRANSFERABLE", True),
    ("T6 unauthorized", "valued asset, seller exists, authority denied", "UNAUTHORIZED", True),
]
def ret(rule, status, valued):
    base = {"status": status, "gate": 1 if status in ("UNDEFINED_TARGET", "INCOHERENT_TARGET") else 9,
            "valuation": None, "null_record": False, "token_issued": False,
            "consequence_record": None, "ncoin": 0}
    if rule == "R1":
        pass
    elif rule == "R2":
        if valued: base["valuation"] = "VALUED_NOT_TRANSACTABLE"
    elif rule == "R3":
        base["null_record"] = True
        base["status"] = None          # as originally worded: NULL only, no reason code
    elif rule == "R3+code":
        base["null_record"] = True     # amended: NULL record carries the reason code
    elif rule == "R4":
        if valued: base["valuation"] = "VALUED_NOT_TRANSACTABLE"
        base["consequence_record"] = None   # no independent trigger met in fixture
    return base
F03 = {}
for rule in ["R1", "R2", "R3", "R3+code", "R4"]:
    rows = []
    for tid, desc, status, valued in TARGETS:
        rows.append({"target": tid, **ret(rule, status, valued)})
    sigs = {json.dumps({k: v for k, v in r.items() if k not in ("target", "gate")}, sort_keys=True) for r in rows}
    F03[rule] = {"rows": rows, "distinct_returns": len(sigs),
                 "valued_info_kept": sum(1 for r in rows if r["valuation"]),
                 "ncoin_total": sum(r["ncoin"] for r in rows)}

# ------------------------------------------------------------------- M04
B = 100.0
def sim(alpha, T=20, I0=None):
    I = 2 * B if I0 is None else I0   # I_0 = 2B (Year 0, no prior investment)
    out = [I]
    for _ in range(T):
        I = 2 * (B + alpha * I)
        out.append(I)
    return out
ALPHAS = [0.0, 0.25, 0.4, 0.5, 0.6, -0.5, 1.0]
M04 = []
for a in ALPHAS:
    fp = None if abs(1 - 2 * a) < 1e-12 else 2 * B / (1 - 2 * a)
    tr = sim(a, 20)
    # closed form check: I_t = 2B * sum_{k=0..t} (2a)^k
    cf = [2 * B * sum((2 * a) ** k for k in range(t + 1)) for t in range(21)]
    assert all(abs(x - y) < 1e-6 * max(1, abs(y)) for x, y in zip(tr, cf)), a
    tr150 = sim(a, 149)
    if abs(2 * a) < 1:
        verdict = "CONVERGES to fixed point"
    elif abs(2 * a) == 1 and a > 0:
        verdict = "DIVERGES linearly (no finite fixed point)"
    elif abs(2 * a) == 1:
        verdict = "OSCILLATES (2-cycle), fixed point exists but is not reached"
    else:
        verdict = "DIVERGES geometrically"
    M04.append({"alpha": a, "fixed_point": fp, "admissible": (fp is not None and fp >= 0),
                "I_5": tr[5], "I_20": tr[20], "I_149": tr150[149], "verdict": verdict,
                "traj": tr})

json.dump({"F01": F01, "DEFECTS": DEFECTS, "CONTROL": CONTROL, "F03": F03, "M04": M04},
          open(sys.argv[1], "w"), indent=1, default=str)

# --------------------------------------------------------------- print log
print("== F01 ==")
for name, rows in F01.items():
    print(name)
    for r in rows:
        print(f"  {r['config']:13s} {r['status']:18s} {r['reason']:32s} A={r['A']:2d} B={r['B']:2d} "
              f"tot={r['total']:2d} d={r['delta_total']:+d} V_A={r['verdict_A']} V_B={r['verdict_B']}")
print("== defects ==")
for d in DEFECTS: print(" ", d)
print("control", CONTROL)
print("== F03 ==")
for k, v in F03.items(): print(k, v["distinct_returns"], v["valued_info_kept"], v["ncoin_total"])
print("== M04 ==")
for m in M04: print(m["alpha"], m["fixed_point"], round(m["I_5"], 1), m["I_20"], m["I_149"], m["verdict"])
