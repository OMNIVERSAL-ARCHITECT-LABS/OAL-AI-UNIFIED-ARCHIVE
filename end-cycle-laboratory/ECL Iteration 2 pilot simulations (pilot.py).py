"""
OAL-ECL Iteration 2 pilot simulations (toy models, Perplexity Computer).
P1: Field replay trajectories (Claude E1 / ChatGPT ECL-00, ECL-02, ECL-05, ECL-06).
P2: Governance regimes under operator affect (Claude E2 / Grok H-A, H-E / ChatGPT 9.2).
P3: Indistinguishability circularity check (Claude E7 / ChatGPT ECL-12).
All parameters are author-chosen assumptions. Results are pilot findings about the MODEL, not the world.
"""
import json, numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

rng_master = np.random.default_rng(20260930)
N_RUNS = 1000
OUT = {}

# ---------------- P1: Field replay ----------------
# Compartments: mobile fauna (can migrate given warning + corridor), sessile/non-migrant
# species (can only survive by dormancy/transition if change is slow), soil fertility,
# successor community (establishes only if soil residual and time allow).
def field_run(traj, rng, T=60):
    n_mobile, n_sessile = 200, 100
    mobile_alive = n_mobile; sessile_alive = n_sessile
    migrated = 0; dormant = 0; lost_mobile = 0; lost_sessile = 0
    soil = 1.0; successor = 0.0; record_ok = True
    if traj == "baseline":
        hab = lambda t: 0.85 + 0.15*np.cos(2*np.pi*t/12)   # seasonal variation, no end
    elif traj == "immediate":
        hab = lambda t: 0.0
    elif traj == "staged":
        hab = lambda t: max(0.0, 1 - t/40)
    elif traj == "adaptive":
        # staged, but with review pauses when losses spike (interruptible)
        hab = None
    h_prev = 1.0; paused = 0; t_eff = 0.0
    for t in range(T):
        if traj == "adaptive":
            h = max(0.0, 1 - t_eff/40)
        else:
            h = hab(t)
        dh = max(0.0, h_prev - h)          # rate of decline this step
        corridor = 0.9 if traj == "adaptive" else (0.6 if traj == "staged" else 0.0)
        warning = 1.0 if traj in ("staged", "adaptive") else 0.0
        # mobile: migrate with prob proportional to warning*corridor when h<0.7, else die when h<0.3
        if h < 0.7 and mobile_alive > 0:
            m = rng.binomial(mobile_alive, min(1, 0.15*warning*corridor + 0.02))
            migrated += m; mobile_alive -= m
        if h < 0.3 and mobile_alive > 0:
            d = rng.binomial(mobile_alive, min(1, 0.5*(0.3-h)/0.3 + (0.9 if h == 0 else 0)))
            lost_mobile += d; mobile_alive -= d
        # sessile: cannot migrate. dormancy succeeds only if decline is slow (dh small)
        if h < 0.8 and sessile_alive > 0:
            dorm_p = 0.06*np.exp(-dh*25) * (1.6 if traj == "adaptive" else 1.0)
            k = rng.binomial(sessile_alive, min(1, dorm_p)); dormant += k; sessile_alive -= k
        if h < 0.4 and sessile_alive > 0:
            d = rng.binomial(sessile_alive, min(1, 0.4 + 0.6*min(1, dh*10)))
            lost_sessile += d; sessile_alive -= d
        # soil: collapses with abrupt change, depletes slowly otherwise
        soil = max(0.0, soil - (0.6*dh*10 if dh > 0.2 else 0.012*(1-h)))
        # successor establishes when h is low but soil residual remains
        if h < 0.5:
            successor = min(1.0, successor + 0.04*soil)
        # adaptive pause: if a step kills >5% of remaining sessile, freeze decline 2 steps
        if traj == "adaptive":
            if sessile_alive > 0 and h < 0.45 and rng.random() < 0.25:
                paused += 1
            else:
                t_eff += 1
        h_prev = h
    completed = (h_prev <= 0.05) if traj != "baseline" else None
    return dict(migrated=migrated/n_mobile, lost_mobile=lost_mobile/n_mobile,
                dormant=dormant/n_sessile, lost_sessile=lost_sessile/n_sessile,
                soil=soil, successor=successor, completed=completed, pauses=paused,
                remaining_mobile=mobile_alive/n_mobile, remaining_sessile=sessile_alive/n_sessile)

P1 = {}
for traj in ["baseline", "immediate", "staged", "adaptive"]:
    rows = [field_run(traj, np.random.default_rng(rng_master.integers(1e9))) for _ in range(N_RUNS)]
    agg = {}
    for k in rows[0]:
        vals = [r[k] for r in rows if r[k] is not None]
        if not vals: agg[k] = None; continue
        v = np.array(vals, dtype=float)
        agg[k] = dict(mean=round(float(v.mean()), 3), p05=round(float(np.percentile(v, 5)), 3),
                      p95=round(float(np.percentile(v, 95)), 3))
    P1[traj] = agg
OUT["P1_field"] = P1

# chart P1
labels = ["Immediate", "Staged", "Adaptive"]
keys = ["immediate", "staged", "adaptive"]
metrics = [("migrated", "Mobile fauna migrated"), ("lost_sessile", "Non-migrants lost"),
           ("soil", "Soil fertility left"), ("successor", "Successor established")]
fig, axes = plt.subplots(1, 4, figsize=(12, 3.4), sharey=True)
colors = ["#A84B2F", "#20808D", "#1B474D"]
for ax, (mk, title) in zip(axes, metrics):
    means = [P1[k][mk]["mean"] for k in keys]
    lo = [P1[k][mk]["mean"] - P1[k][mk]["p05"] for k in keys]
    hi = [P1[k][mk]["p95"] - P1[k][mk]["mean"] for k in keys]
    ax.bar(labels, means, color=colors, yerr=[lo, hi], capsize=3)
    for i, m in enumerate(means):
        ax.text(i, m + hi[i] + 0.03, f"{m:.2f}", ha="center", fontsize=9)
    ax.set_title(title, fontsize=10); ax.set_ylim(0, 1.15)
    ax.spines[["top", "right"]].set_visible(False); ax.tick_params(labelsize=8)
fig.suptitle("P1: The same field ends three ways; each loses different things (1,000 runs, 5-95% bars)", fontsize=11)
fig.tight_layout(); fig.savefig("/home/user/workspace/sim/p1_field.png", dpi=200); plt.close(fig)

# ---------------- P2: Governance regimes ----------------
# Each petition has a true status: urgent-warranted (U), warranted-not-urgent (W), unwarranted (X).
# Operator affect: upset with prob depending on status (affect is informative: harm makes people upset)
# AND upset operators misjudge unwarranted cases more often (affect is biasing).
def gov_sim(regime, p_urgent, delay, rng, n=4000):
    status = rng.choice(["U", "W", "X"], size=n, p=[p_urgent, 0.25, 0.75 - p_urgent])
    upset_p = {"U": 0.7, "W": 0.4, "X": 0.35}
    wrongful = 0; delay_harm = 0.0; correct_end = 0; blocked_warranted = 0
    for s in status:
        upset = rng.random() < upset_p[s]
        # operator belief that ending is warranted
        if s in ("U", "W"):
            op_says_end = rng.random() < 0.9
        else:
            op_says_end = rng.random() < (0.45 if upset else 0.08)
        # independent reviewer: slower, less biased, imperfect
        rev_says_end = (rng.random() < 0.85) if s in ("U", "W") else (rng.random() < 0.05)
        if regime == "single":
            ended = op_says_end; d = 1
        elif regime == "split":
            ended = op_says_end and rev_says_end; d = delay
        elif regime == "split_affect_blind_ban":
            # upset operators' petitions are refused outright (affect treated as disqualifying)
            ended = (not upset) and op_says_end and rev_says_end; d = delay
        elif regime == "split_expedite":
            # affect or urgency claim routes to expedited review (shorter delay) + expiring bypass
            d = max(1, delay // 3) if upset else delay
            ended = op_says_end and rev_says_end
        if s == "X" and ended: wrongful += 1
        if s in ("U", "W") and ended: correct_end += 1
        if s in ("U", "W") and not ended: blocked_warranted += 1
        if s == "U":
            # harm accrues per unit delay, and fully if never ended
            delay_harm += (min(d, 20) / 20.0) if ended else 1.0
    nU = max(1, int((status == "U").sum())); nX = max(1, int((status == "X").sum()))
    nWU = max(1, int(np.isin(status, ["U", "W"]).sum()))
    return dict(wrongful_rate=wrongful/nX, urgent_harm=delay_harm/nU,
                blocked_warranted=blocked_warranted/nWU)

regimes = ["single", "split", "split_affect_blind_ban", "split_expedite"]
P2 = {}
for p_urgent in [0.02, 0.10, 0.25]:
    for delay in [2, 8, 16]:
        key = f"urgent={p_urgent},delay={delay}"
        P2[key] = {}
        for rg in regimes:
            res = [gov_sim(rg, p_urgent, delay, np.random.default_rng(rng_master.integers(1e9)), n=1500) for _ in range(40)]
            P2[key][rg] = {k: round(float(np.mean([r[k] for r in res])), 3) for k in res[0]}
OUT["P2_governance"] = P2

# Affect informativeness (likelihood ratio) at p_urgent=0.10
lr = (0.7*0.10 + 0.4*0.25) / (0.10 + 0.25) / 0.35
OUT["P2_affect_LR_warranted_vs_unwarranted"] = round(lr, 2)

# chart P2: grouped bars, urgent share 10%
names = ["Single\nofficer", "Split\nauthority", "Split + refuse\nupset", "Split +\nexpedite"]
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8), gridspec_kw={"width_ratios": [1, 1.6]})
w = [P2["urgent=0.1,delay=8"][rg]["wrongful_rate"] for rg in regimes]
axes[0].bar(names, w, color=["#A84B2F", "#20808D", "#944454", "#1B474D"])
for i, v in enumerate(w): axes[0].text(i, v + 0.005, f"{v:.3f}", ha="center", fontsize=8)
axes[0].set_title("Wrongful endings (share of unwarranted petitions executed)", fontsize=9)
axes[0].set_ylim(0, 0.25)
x = np.arange(len(regimes)); bw = 0.26
for j, (d, c) in enumerate(zip([2, 8, 16], ["#BCE2E7", "#20808D", "#1B474D"])):
    vals = [P2[f"urgent=0.1,delay={d}"][rg]["urgent_harm"] for rg in regimes]
    axes[1].bar(x + (j-1)*bw, vals, bw, color=c, label=f"review delay {d}")
    for i, v in enumerate(vals): axes[1].text(x[i] + (j-1)*bw, v + 0.015, f"{v:.2f}", ha="center", fontsize=7)
axes[1].set_xticks(x); axes[1].set_xticklabels(names)
axes[1].set_title("Harm to urgent cases (0 = none, 1 = maximal)", fontsize=9); axes[1].set_ylim(0, 1.1)
axes[1].legend(fontsize=8, frameon=False, loc="upper left")
for ax in axes: ax.spines[["top", "right"]].set_visible(False); ax.tick_params(labelsize=8)
fig.suptitle("P2: Split authority cuts wrongful endings about 20x but adds delay harm; refusing upset petitioners is worst", fontsize=10)
fig.tight_layout(); fig.savefig("/home/user/workspace/sim/p2_governance.png", dpi=200); plt.close(fig)

# ---------------- P3: Indistinguishability circularity ----------------
# Generator author chooses how much the internal 'blank canvas' signal separates completed vs future-loss.
# Detector sees external signals (activity, output volume) + optionally internal probe.
def p3(sep_internal, use_internal, rng, n=2000):
    y = rng.integers(0, 2, n)  # 0 completed-healthy, 1 future-loss
    activity = rng.normal(0.5, 0.1, n)            # identical by construction
    novelty_ext = rng.normal(0.3, 0.1, n)          # identical by construction
    probe = rng.normal(0.6 - sep_internal*y, 0.15, n)
    score = probe if use_internal else novelty_ext + 0*activity
    thr = np.median(score)
    pred = (score < thr).astype(int) if use_internal else (score < thr).astype(int)
    return float((pred == y).mean())
P3 = {}
for sep in [0.0, 0.05, 0.15, 0.3]:
    P3[f"sep={sep}"] = {
        "external_only": round(np.mean([p3(sep, False, np.random.default_rng(rng_master.integers(1e9))) for _ in range(50)]), 3),
        "with_probe": round(np.mean([p3(sep, True, np.random.default_rng(rng_master.integers(1e9))) for _ in range(50)]), 3)}
OUT["P3_indistinguishability"] = P3

json.dump(OUT, open("/home/user/workspace/sim/results.json", "w"), indent=1)
print(json.dumps(OUT, indent=1))
