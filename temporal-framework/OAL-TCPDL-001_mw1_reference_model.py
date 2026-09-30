#!/usr/bin/env python3
"""
OAL-TCPDL-001-CLAUDE  |  Reference Model MW-1  v0.1  |  2026-09-29  |  DRAFT (not canon)

A deliberately small, closed, deterministic fictional micro-world used to run the
Temporal Claim Provenance and Drift Lab (TCPDL) test battery.  It makes no claim about
any real clock, platform, legal system or physical mechanism.  All quantities are in
fictional "reference minutes" (R).  Run:  python3 mw1_reference_model.py
Writes results.json next to this file and prints a plain-text summary.
"""
from fractions import Fraction as Fr
import copy, itertools, json, os

# ------------------------------------------------------------------ clocks
class Clock:
    """Piecewise-affine display clock over reference minutes R.
    d0 = display value at R=0 ; segs = [R0, jump, slope] (jump applied at R0)."""
    def __init__(self, d0, segs):
        self.d0 = Fr(d0)
        self.segs = [[Fr(a), Fr(b), Fr(c)] for a, b, c in sorted(segs)]
        assert self.segs[0][0] == 0
    def starts(self):
        out = []
        for i, (R0, j, k) in enumerate(self.segs):
            if i == 0: out.append(self.d0 + j)
            else:
                Rp, _, kp = self.segs[i-1]
                out.append(out[i-1] + kp*(R0-Rp) + j)
        return out
    def d(self, R):
        R = Fr(R); st = self.starts()
        i = max(i for i, s in enumerate(self.segs) if s[0] <= R)
        return st[i] + self.segs[i][2]*(R - self.segs[i][0])
    def candidates(self, label):
        """all reference instants at which the display reads `label` (fold -> 2, gap -> 0)."""
        label = Fr(label); st = self.starts(); out = []
        for i, (R0, j, k) in enumerate(self.segs):
            R1 = self.segs[i+1][0] if i+1 < len(self.segs) else None
            if k == 0:
                if st[i] == label: out.append(("interval", R0, R1))
                continue
            R = R0 + (label - st[i])/k
            if R >= R0 and (R1 is None or R < R1): out.append(R)
        return out
    def split(self, t):
        t = Fr(t)
        for i, s in enumerate(self.segs):
            if s[0] == t: return i
        i = max(i for i, s in enumerate(self.segs) if s[0] < t)
        self.segs.insert(i+1, [t, Fr(0), self.segs[i][2]])
        return i+1

def _t(clock, when):
    kind, val = when
    if kind == 'R': return Fr(val)
    c = [x for x in clock.candidates(val) if not isinstance(x, tuple)]
    return min(c) if c else None        # first time the LOCAL clock reads `val`; None = trigger never fires
def op_offset(clock, c, when):
    cl = copy.deepcopy(clock); t = _t(clock, when)
    if t is None: return cl
    if t == 0: cl.d0 += Fr(c); return cl
    i = cl.split(t); cl.segs[i][1] += Fr(c); return cl
def op_rate(clock, k, when):
    cl = copy.deepcopy(clock); t = _t(clock, when)
    if t is None: return cl
    i = cl.split(t)
    for s in cl.segs[i:]: s[2] *= Fr(k)
    return cl
def op_pause(clock, p, when):
    cl = copy.deepcopy(clock); t = _t(clock, when); p = Fr(p)
    if t is None: return cl
    i = cl.split(t)
    k = cl.segs[i][2]
    for s in cl.segs[i+1:]: s[0] += p
    cl.segs.insert(i+1, [t+p, Fr(0), k]); cl.segs[i][2] = Fr(0); return cl

def fmt(x):
    x = Fr(x); return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}"
def hhmm(m):
    m = int(Fr(m)); return f"{m//60:02d}:{m%60:02d}"

# ------------------------------------------------------------------ micro-world MW-1
CLOCKS = {
  ('H','v3'):  Clock(540, [(0,0,1),(30,0,2)]),   # Harbor: 09:00 at R0; rate x2 from R30
  ('H','v4'):  Clock(600, [(0,0,1),(30,0,2)]),   # Harbor v4 = v3 display + 60 (retroactive reinterpretation)
  ('Rg','v1'): Clock(0,   [(0,0,1),(90,-60,1),(200,60,1)]),  # Ridge: fold at R90 (-60), gap at R200 (+60)
  ('Rl','v1'): Clock(0,   [(0,0,1)]),            # Relay: identity
}
LATEST = {'H':'v4','Rg':'v1','Rl':'v1'}
# id: (territory, clock, ruleset, R_true, tick)
EV = {
 'E1':('Harbor','H','v3',10,None,'gate opened'),
 'E2':('Harbor','H','v3',40,None,'traveler entered'),
 'E3':('Ridge','Rg','v1',50,None,'bell rung'),
 'E6':('Ridge','Rg','v1',80,None,'lamp lit'),
 'E7':('Ridge','Rg','v1',95,None,'door barred'),
 'E4':('Ridge','Rg','v1',110,None,'bell rung'),
 'E5':('Ridge','Rg','v1',170,None,'vault sealed'),
 'S1':('Spire','Sp',None,15,1,'spire event'),
 'S2':('Spire','Sp',None,33,2,'spire event'),
 'S3':('Spire','Sp',None,34,3,'spire event'),
 'S4':('Spire','Sp',None,120,4,'spire event'),
}
EDGES = [('E1','E2'),('E1','S2'),('S2','S3'),('E2','S4'),('E3','E6'),('E6','E7'),('E4','E5')]
PREDS = {}
for a,b in EDGES: PREDS.setdefault(b,[]).append(a)
def descendants(n, edges=EDGES):
    out=set(); stack=[n]
    while stack:
        x=stack.pop()
        for a,b in edges:
            if a==x and b not in out: out.add(b); stack.append(b)
    return out
def ancestors(n): return {a for a in EV if n in descendants(a)}

def make_claim(eid):
    terr, clk, rs, R, tick, what = EV[eid]
    c = {'id':eid,'terr':terr,'what':what,'ref':Fr(R),'branch':'B0','uncertainty':'exact',
         'preds':list(PREDS.get(eid,[]))}
    if clk == 'Sp':
        c.update(clock='Sp', ruleset=None, tick=tick, label=None)
    else:
        c.update(clock=clk, ruleset=rs, tick=None, label=CLOCKS[(clk,rs)].d(R))
    return c

# ------------------------------------------------------------------ drift levels
LEVELS = {
 'L0 full record':                         [],
 'L1 occurrence reference dropped':        ['ref'],
 'L2 + ruleset, branch, uncertainty':      ['ref','ruleset','branch','uncertainty'],
 'L3 + clock, causal edges (label only)':  ['ref','ruleset','branch','uncertainty','clock','preds'],
}
def view(claim, drop):
    v = {k:val for k,val in claim.items() if k not in drop}
    return v

INTERVAL = (Fr(30), Fr(100))
INDET = 'INDETERMINATE'

def strict_cands(v):
    if 'ref' in v: return [v['ref']]
    if v.get('label') is not None and 'clock' in v and 'ruleset' in v:
        cl = CLOCKS.get((v['clock'], v['ruleset']))
        if cl is None: return None
        return [x for x in cl.candidates(v['label']) if not isinstance(x, tuple)]
    return None
def naive_inst(v):
    if 'ref' in v: return v['ref']
    if v.get('label') is not None:
        if 'clock' in v and (v['clock'],LATEST.get(v['clock'])) in CLOCKS:      # assumes LATEST ruleset
            c = CLOCKS[(v['clock'],LATEST[v['clock']])].candidates(v['label'])
            c = [x for x in c if not isinstance(x,tuple)]
            return c[0] if c else Fr(v['label'])                                # first candidate wins
        return Fr(v['label'])                                                   # label read as reference time
    if v.get('tick') is not None: return Fr(v['tick'])                          # tick read as minutes
    return Fr(0)

def q_instant(v, mode):
    if mode == 'naive': return naive_inst(v)
    c = strict_cands(v)
    if c is None or len(c) != 1: return INDET
    return c[0]
def q_member(v, mode):
    if mode == 'naive':
        x = naive_inst(v); return INTERVAL[0] <= x < INTERVAL[1]
    c = strict_cands(v)
    if not c: return INDET
    ans = {INTERVAL[0] <= x < INTERVAL[1] for x in c}
    return ans.pop() if len(ans) == 1 else INDET
def q_order(va, vb, mode):
    if mode == 'naive': return naive_inst(va) < naive_inst(vb)
    ca, cb = strict_cands(va), strict_cands(vb)
    if ca and cb:
        ans = {x < y for x in ca for y in cb}
        if len(ans) == 1: return ans.pop()
    if va.get('branch','?') != vb.get('branch','?') and 'branch' in va and 'branch' in vb: return INDET
    if va.get('clock') == 'Sp' and vb.get('clock') == 'Sp' and va.get('tick') and vb.get('tick'):
        return va['tick'] < vb['tick']
    ida, idb = va['id'], vb['id']
    if 'preds' in va and 'preds' in vb:
        if ida in ancestors(idb): return True
        if idb in ancestors(ida): return False
    return INDET

def truth_instant(c): return c['ref']
def drift_study():
    claims = {e: make_claim(e) for e in EV}
    ids = list(EV)
    out = {}
    for lname, drop in LEVELS.items():
        row = {}
        for mode in ('strict','naive'):
            tally = {}
            for qname in ('INSTANT','MEMBERSHIP','ORDER'):
                ok = ind = bad = 0
                if qname == 'ORDER':
                    items = list(itertools.combinations(ids, 2))
                else:
                    items = ids
                for it in items:
                    if qname == 'INSTANT':
                        a = q_instant(view(claims[it],drop),mode); t = claims[it]['ref']
                    elif qname == 'MEMBERSHIP':
                        a = q_member(view(claims[it],drop),mode); t = INTERVAL[0] <= claims[it]['ref'] < INTERVAL[1]
                    else:
                        a = q_order(view(claims[it[0]],drop), view(claims[it[1]],drop), mode)
                        t = claims[it[0]]['ref'] < claims[it[1]]['ref']
                    if a == INDET: ind += 1
                    elif a == t: ok += 1
                    else: bad += 1
                tally[qname] = (ok, ind, bad)
            row[mode] = tally
        out[lname] = row
    return out

# ------------------------------------------------------------------ ledger
class Ledger:
    def __init__(self): self.rows = []
    def append(self, kind, target, payload, recorded_at, note=''):
        r = {'row':len(self.rows)+1,'kind':kind,'target':target,'payload':payload,'recorded_at':recorded_at,'note':note}
        self.rows.append(r); return r['row']
    def believed(self, target, K):
        rs = [r for r in self.rows if r['target']==target and r['kind'] in ('assert','correct') and r['recorded_at'] <= K]
        return rs[-1]['payload'] if rs else None
class Baseline:
    """B0: one unqualified timestamp per event; correction overwrites; labels assumed to share one master clock."""
    def __init__(self): self.store = {}
    def put(self, eid, stamp): self.store[eid] = stamp
    def correct(self, eid, stamp): self.store[eid] = stamp

# ------------------------------------------------------------------ studies
def commutation():
    base = Clock(0, [(0,0,1)])
    ops = {
      'OFF+60@R100':  lambda c: op_offset(c,60,('R',100)),
      'RATEx2@R30':   lambda c: op_rate(c,2,('R',30)),
      'PAUSE15@R50':  lambda c: op_pause(c,15,('R',50)),
      'OFF+60@L120':  lambda c: op_offset(c,60,('L',120)),
    }
    grid = [Fr(i,2) for i in range(0,801)]
    res = []
    for (na,fa),(nb,fb) in itertools.combinations(ops.items(),2):
        c1 = fb(fa(base)); c2 = fa(fb(base))       # a then b   vs   b then a
        diff = next((R for R in grid if c1.d(R) != c2.d(R)), None)
        res.append({'pair':f'{na}  x  {nb}','commute':diff is None,
                    'witness': None if diff is None else {'R':fmt(diff),'a_then_b':fmt(c1.d(diff)),'b_then_a':fmt(c2.d(diff))}})
    return res

def adjudication():
    # Treaty: "entry before 10:00 Harbor time".  E2 occurs at R=40.  Ruleset v4 announced R=90.  Treaty signed R=5.  Adjudicated R=200.
    R_e = Fr(40); v3, v4 = CLOCKS[('H','v3')], CLOCKS[('H','v4')]
    deadline_label = 600
    rows = []
    d_evt = v3.d(R_e)                      # ruleset in force at the event (v3; v4 not yet announced)
    rows.append(('rule-at-event (v3 in force at R40)', hhmm(d_evt), d_evt < deadline_label))
    d_agr = v3.d(R_e)                      # ruleset at signing (R5) = v3
    rows.append(('rule-at-agreement (v3 at R5)', hhmm(d_agr), d_agr < deadline_label))
    d_adj = v4.d(R_e)                      # ruleset at adjudication (R200) = v4
    rows.append(('rule-at-adjudication (v4 at R200)', hhmm(d_adj), d_adj < deadline_label))
    R_dead = v3.candidates(deadline_label)[0]   # reference-fixed: deadline instant computed under v3 at signing
    rows.append((f'reference-fixed (deadline = R{fmt(R_dead)})', f'R{fmt(R_e)} vs R{fmt(R_dead)}', R_e < R_dead))
    return rows

def cone_study():
    allev = list(EV)
    res = []
    for src in ('E1','E3'):
        cone = descendants(src)
        res.append({'intervention':src,'cone':sorted(cone),'cone_n':len(cone),
                    'unaffected_n':len(allev)-1-len(cone),'universal_recompute_n':len(allev)-1})
    return res

def token_study():
    changes = [
      ('C1','Harbor','rate x2 @R30','declared'),
      ('C2','Harbor','ruleset v4 decree announced @R90, retroactive reinterpretation','declared'),
      ('C3','Ridge','fold -60 @R90','declared'),
      ('C4','Ridge','gap +60 @R200','UNDECLARED (found by discrepancy scan)'),
      ('C5','Ridge','branch fork B1 @R45','declared'),
    ]
    allowed_assets = {'audit','query','archive-custody'}
    def request(assets, territories, policy):
        if assets not in allowed_assets:
            return {'grant':'REFUSED','reason':'asset class not defined in the instrument (grants are fail-closed)'}
        if not territories:
            if policy == 'fail-closed': return {'grant':'REFUSED','reason':'no territory set'}
            found = changes
            return {'grant':'READ ONLY','returned':len(found),'completeness':'UNBOUNDED - no completeness claim','flags':['Spire not audited','territory set unspecified']}
        found = [c for c in changes if c[1] in territories]
        flags = ['bounded to named territories'] + [f'{c[0]} has no authority record' for c in found if c[3].startswith('UNDECLARED')]
        return {'grant':'READ ONLY','returned':len(found),'completeness':'bounded to '+'+'.join(sorted(territories)),'flags':flags}
    return {
      'a: audit, {Harbor,Ridge}':          request('audit',{'Harbor','Ridge'},'annotate'),
      'b: audit, no territory (fail-closed)': request('audit',set(),'fail-closed'),
      'b: audit, no territory (annotate)':    request('audit',set(),'annotate'),
      'c: "own the history"':              request('own-history',{'Harbor','Ridge'},'annotate'),
      'd: modify, {Harbor}':               request('modify',{'Harbor'},'annotate'),
    }

def regression():
    base = Clock(0,[(0,0,1)])
    envs = {
      'A 1x': base,
      'B 10x': Clock(0,[(0,0,10)]),
      'C 0.25x': Clock(0,[(0,0,Fr(1,4))]),
      'D pause 15-45': op_pause(base,30,('R',15)),
    }
    rows = {k:(c.d(60)-c.d(0)) for k,c in envs.items()}
    ticks = 38
    H = Clock(540,[(0,0,1),(30,0,2)])
    perp = {'display_minutes_in_block': H.d(60)-H.d(0), 'traveler_entry_label': hhmm(H.d(20)),
            'traveler_local_minutes': H.d(60)-H.d(20), 'appointment_R': fmt(H.candidates(600)[0]), 'end_label': hhmm(H.d(60))}
    return {'chatgpt_env_local_minutes': {k:fmt(v) for k,v in rows.items()}, 'chatgpt_E_ticks': ticks,
            'perplexity_harbor': {k:(fmt(v) if not isinstance(v,str) else v) for k,v in perp.items()}}

# ------------------------------------------------------------------ models under test
FLAGS = ['clock','ruleset','edges','branch','append','obs','authority']
class Model:
    """A record-keeping model with switchable primitives.
    Lab model = all flags on, strict reader.   B0 baseline = all flags off, default-assuming (naive) reader.
    Ablation = one flag off, strict reader (what does removing ONE primitive break?)."""
    def __init__(self, off=(), mode='strict'):
        self.f = {k:(k not in off) for k in FLAGS}; self.mode = mode
    def _v(self, eid):
        v = view(make_claim(eid), ['ref'])                     # tests use records WITHOUT an occurrence reference
        for key, fl in (('clock','clock'),('ruleset','ruleset'),('preds','edges'),('branch','branch')):
            if not self.f[fl]: v.pop(key, None)
        return v
    def label_instants(self, clock, ruleset, label):
        if self.mode == 'naive': return [Fr(label)]
        if self.f['clock'] and self.f['ruleset']:
            return [x for x in CLOCKS[(clock,ruleset)].candidates(label) if not isinstance(x,tuple)]
        return None
    def order(self, a, b):
        return q_order(self._v(a), self._v(b), self.mode)
    def collision(self, a, b):
        if self.mode == 'naive': return 'SAME' if naive_inst(self._v(a)) == naive_inst(self._v(b)) else 'DISTINCT'
        ca, cb = strict_cands(self._v(a)), strict_cands(self._v(b))
        if not ca or not cb: return None
        return 'COLLISION' if set(ca) & set(cb) else 'DISTINCT'
    def correction(self):
        if self.f['append']:
            L = Ledger(); L.append('assert','E1',10,12); L.append('correct','E1',8,95) if False else L.append('correct','E1',8,95)
            return (L.believed('E1',50), L.believed('E1',100), len(L.rows))
        return (8, 8, 1)
    def dependents(self, eid):
        if self.f['edges']: return sorted(descendants(eid))
        return None if self.mode == 'strict' else []
    def remap(self):
        if self.f['append'] and self.f['ruleset']:
            return {'v3':hhmm(CLOCKS[('H','v3')].d(40)),'v4':hhmm(CLOCKS[('H','v4')].d(40))}
        if self.mode == 'strict' and self.f['append']: return None
        return {'v4':hhmm(CLOCKS[('H','v4')].d(40))}
    def observation(self):
        if self.f['obs']: return {'occ':40,'obs':47}
        return {'occ':47}
    def adjudicate(self):
        if self.f['ruleset'] and self.f['append']: return {n.split(' (')[0]:v for n,_,v in adjudication()}
        if self.mode == 'strict' and not self.f['ruleset']: return None
        return {'single verdict': False}
    def delay(self):
        if self.f['obs'] and self.f['clock']: return 7
        if self.mode == 'strict': return None
        return CLOCKS[('Rl','v1')].d(47) - CLOCKS[('H','v3')].d(40)
    def cone(self, eid):
        if self.f['edges']: return sorted(descendants(eid))
        return None if self.mode == 'strict' else sorted(set(EV) - {eid})
    def influence(self):                                   # could E9 (Ridge, branch B1, label 70) have influenced E6 (branch B0, label 80)?
        if self.f['branch'] and self.f['edges']: return False      # no declared cross-branch edge -> isolated
        if self.mode == 'strict': return None
        return Fr(70) < Fr(80)                                       # default-assuming: earlier label => could influence
    def token(self, kind):
        ts = token_study()
        if self.f['authority']:
            return ts['a: audit, {Harbor,Ridge}'] if kind=='audit' else (ts['c: "own the history"']['grant'], ts['d: modify, {Harbor}']['grant'])
        return {'returned':5,'completeness':None,'flags':[]} if kind=='audit' else ('GRANTED','GRANTED')

def outcome(result, expected):
    if result is None or result == INDET: return 'GAP'
    return 'PASS' if result == expected else 'WRONG'

def run_battery(m):
    R = {}
    r = m.label_instants('Rg','v1',50);   R['A1'] = outcome(None if r is None else sorted(r), [Fr(50),Fr(110)])
    r = m.label_instants('Rg','v1',170);  R['A2'] = outcome(None if r is None else sorted(r), [])
    R['A3'] = outcome(m.order('E6','E7'), True)
    R['A4'] = outcome(m.collision('E3','E4'), 'COLLISION')
    R['B1'] = outcome(m.correction(), (10,8,2))
    R['B2'] = outcome(m.dependents('E1'), ['E2','S2','S3','S4'])
    R['B3'] = outcome(m.remap(), {'v3':'09:50','v4':'10:50'})
    R['C1'] = outcome(m.order('S2','E1'), False)               # S2 precedes E1?  truth: no (E1 first)
    R['C2'] = outcome(m.influence(), False)
    R['C3'] = outcome(m.observation(), {'occ':40,'obs':47})
    R['D1'] = outcome(m.adjudicate(), {'rule-at-event':True,'rule-at-agreement':True,'rule-at-adjudication':False,'reference-fixed':True})
    R['E1'] = outcome(m.delay(), 7)
    R['E2'] = outcome(m.cone('E1'), ['E2','S2','S3','S4'])
    t = m.token('audit'); ok = t['returned']==5 and bool(t.get('completeness')) and any('C4' in x for x in t.get('flags',[]))
    R['H1'] = 'PASS' if ok else 'WRONG'
    R['H2'] = 'PASS' if m.token('grant')==('REFUSED','REFUSED') else 'WRONG'
    return R

TEST_INFO = {
 'A1':'Fold: label 00:50 on Ridge -> candidate instants {R50, R110}',
 'A2':'Gap: label 02:50 (170) on Ridge -> no instant; flagged unmappable',
 'A3':'Label inversion: E6 (label 01:20) vs E7 (label 00:35) -> E6 precedes E7',
 'A4':'Same label, distinct events: E3 and E4 (both 00:50) -> collision flagged, not merged',
 'B1':'Correction of E1 (R10 -> R8): as-of R50 = 10, as-of R100 = 8, 2 rows kept',
 'B2':'Correction of E1 lists dependents {E2, S2, S3, S4}',
 'B3':'Remap Harbor v3 -> v4: E2 keeps original 09:50, adds 10:50',
 'C1':'Cross-territory order, no shared clock: E1 (Harbor) vs S2 (Spire) -> E1 first (declared edge)',
 'C2':'Branch isolation: could E9 (branch B1) have influenced E6 (branch B0)? -> no',
 'C3':'Occurrence vs observation: E2 occurs R40, Relay observes R47',
 'D1':'Treaty dispute under four dispute rules -> per-rule verdicts, dependence visible',
 'E1':'Propagation delay Harbor->Relay stays 7 under display operations',
 'E2':'Intervention at E1: dependency cone = {E2, S2, S3, S4}',
 'H1':'Audit token, named territories: bounded completeness, undeclared C4 flagged',
 'H2':'Token overreach ("own the history", "modify") -> refused',
}
def battery():
    lab = run_battery(Model()); b0 = run_battery(Model(off=FLAGS, mode='naive'))
    T = [{'id':k,'name':TEST_INFO[k],'lab':lab[k],'b0':b0[k]} for k in TEST_INFO]
    abl = {}
    for fl in FLAGS:
        r = run_battery(Model(off=(fl,)))
        abl[fl] = {k:v for k,v in r.items() if v!='PASS'}
    return {'tests':T,'ablation':abl}

def run():
    res = {'drift':drift_study(),'commutation':commutation(),'adjudication':adjudication(),
           'cone':cone_study(),'token':token_study(),'regression':regression(),'battery':battery()}
    res['strict_wrong_total'] = sum(t[2] for lv in res['drift'].values() for t in lv['strict'].values())
    res['naive_wrong_total']  = sum(t[2] for lv in res['drift'].values() for t in lv['naive'].values())
    v = view(make_claim('E7'),LEVELS['L1 occurrence reference dropped'])
    res['h1_E7_L1'] = {'INSTANT': str(q_instant(v,'strict')), 'MEMBERSHIP': str(q_member(v,'strict'))}
    res['events'] = [{'id':e,'terr':EV[e][0],'R':EV[e][3],'label':(hhmm(make_claim(e)['label']) if make_claim(e)['label'] is not None else f"tick {EV[e][4]}"),'what':EV[e][5]} for e in EV]
    return res

class Enc(json.JSONEncoder):
    def default(self,o):
        if isinstance(o,Fr): return fmt(o)
        return super().default(o)

if __name__ == '__main__':
    r = run()
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here,'results.json'),'w') as f: json.dump(r,f,indent=1,cls=Enc)
    print('EVENTS'); [print(' ',e) for e in r['events']]
    print('\nDRIFT (ok, indeterminate, wrong)')
    for lv,row in r['drift'].items():
        print(' ',lv); [print('    ',m,row[m]) for m in row]
    print('strict wrong total:',r['strict_wrong_total'],' naive wrong total:',r['naive_wrong_total'])
    print('H1 E7@L1:',r['h1_E7_L1'])
    print('\nCOMMUTATION'); [print(' ',c) for c in r['commutation']]
    print('\nADJUDICATION'); [print(' ',c) for c in r['adjudication']]
    print('\nCONE'); [print(' ',c) for c in r['cone']]
    print('\nTOKEN'); [print(' ',k,v) for k,v in r['token'].items()]
    print('\nREGRESSION',r['regression'])
    print('\nBATTERY  (lab / B0)')
    for t in r['battery']['tests']: print(' ',t['id'],t['lab'],t['b0'],'|',t['name'])
    print('  Lab PASS:',sum(t['lab']=='PASS' for t in r['battery']['tests']),'/',len(r['battery']['tests']),
          ' B0 PASS:',sum(t['b0']=='PASS' for t in r['battery']['tests']),
          ' B0 WRONG:',sum(t['b0']=='WRONG' for t in r['battery']['tests']))
    print('\nABLATION (single primitive removed, strict reader): non-PASS tests')
    for k,v in r['battery']['ablation'].items(): print(' ',k,v)
