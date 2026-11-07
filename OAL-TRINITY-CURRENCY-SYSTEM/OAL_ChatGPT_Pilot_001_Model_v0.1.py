#!/usr/bin/env python3
"""OAL / ChatGPT deterministic speculative pilot. Standard-library only.

This is an explicitly stipulated state-machine model, NOT evidence of real QC capability.
Created 2026-11-07 for OAL-CURR-PILOT-001. Independent authoring by ChatGPT.
Run: python OAL_ChatGPT_Pilot_001_Model_v0.1.py
"""
from dataclasses import dataclass, asdict
from pathlib import Path
import json, hashlib

@dataclass(frozen=True)
class Fixture:
    case_id: str
    a: int = 10
    b: int = 0
    qty: int = 3
    unit: str | None = 'resource_unit'
    recipient_authorized: bool = True
    transfer_authorized: bool = True
    processed: bool = False
    target_status: str = 'COHERENT'  # or INCOHERENT / REFERENT_UNDEFINED
    valuation_available: bool = True
    seller_status: str = 'PRESENT'  # PRESENT / UNKNOWN / ABSENT
    transferable: bool = True
    reason: str = ''

BASE_CASES = [
    Fixture('RB-BASE',reason='F01 baseline'),
    Fixture('RB-SHORT',a=2,reason='insufficient existing resource'),
    Fixture('RB-DENIED',recipient_authorized=False,reason='recipient authorization refused'),
    Fixture('RB-UNTYPED',unit=None,reason='requested 3 of unspecified unit'),
    Fixture('RB-REPLAY',processed=True,reason='identical request already fulfilled'),
    Fixture('BR-UNDEFINED',target_status='REFERENT_UNDEFINED',reason='undefined referent'),
    Fixture('BR-INCOHERENT',target_status='INCOHERENT',reason='contradiction under fixed definitions'),
    Fixture('BR-NOVALUE',valuation_available=False,reason='coherent target with unavailable valuation'),
    Fixture('BR-SELLER-UNKNOWN',seller_status='UNKNOWN',reason='seller identity unknown'),
    Fixture('BR-NO-SELLER',seller_status='ABSENT',reason='no seller exists'),
    Fixture('BR-NONTRANSFER',transferable=False,reason='coherent non-transferable target'),
]
MODES = ('P0_EVALUATE','P1_TRANSFER','P2_CREATE','P3_ENACT_UNDERSPECIFIED')

def execute(f, mode):
    before = {'A': f.a, 'B': f.b, 'total': f.a + f.b}
    out = {'case_id': f.case_id, 'mode': mode, 'before': before, 'after': dict(before),
           'status': 'INDETERMINATE', 'valuation': None, 'event': None,
           'assumed_capability': mode, 'settled': False, 'qc_state': 'UNRESOLVED',
           'onecoin_issued': False, 'ncoin_issued': False, 'evidence_type': 'EXECUTED_STIPULATED_MODEL',
           'note': ''}
    def stop(status, note):
        out['status'] = status; out['note'] = note
        return out
    if f.target_status == 'REFERENT_UNDEFINED' or f.unit is None:
        return stop('UNDEFINED_TARGET','No typed referent; neither valuation nor transfer is assumed.')
    if f.target_status == 'INCOHERENT':
        return stop('INCOHERENT_TARGET','Contradiction with unchanged target definitions.')
    if not f.valuation_available:
        return stop('VALUATION_UNAVAILABLE','Coherent but no declared value function output.')
    out['valuation'] = {'quantity': f.qty, 'unit': f.unit, 'domain': 'synthetic_resource_quantity',
                        'conversion': 'one unit of resource target maps to one synthetic resource-equivalence unit'}
    out['qc_state']='EVALUATED'
    if mode == 'P0_EVALUATE':
        return stop('EVALUATED_NO_DELIVERY','Evaluation-only comparator has no delivery capability.')
    if f.seller_status == 'UNKNOWN':
        return stop('SELLER_UNKNOWN','Counterparty authority is epistemically unresolved.')
    if f.seller_status == 'ABSENT':
        return stop('NO_SELLER','Structural absence of a recognized seller.')
    if not f.transferable:
        return stop('NONTRANSFERABLE','The stipulated target cannot be transferred/settled.')
    if not f.recipient_authorized or not f.transfer_authorized:
        return stop('UNAUTHORIZED','Required recipient/transfer authorization not present.')
    if f.processed:
        return stop('REPLAY_NO_OP','Run card stipulates request-idempotent delivery; previously processed.')
    if mode == 'P1_TRANSFER':
        if f.a < f.qty:
            return stop('INSUFFICIENT_INVENTORY','Only existing units may be transferred in P1.')
        out['after']={'A':f.a-f.qty,'B':f.b+f.qty,'total':f.a+f.b}
        out['event']='EXISTING_RESOURCE_TRANSFER'; out['settled']=True
        out['qc_state']='SETTLED_RESOURCE_DELIVERY'
        return stop('SETTLED','Conditional delivery and inventory conservation verified.')
    if mode == 'P2_CREATE':
        out['after']={'A':f.a,'B':f.b+f.qty,'total':f.a+f.b+f.qty}
        out['event']='STIPULATED_RESOURCE_CREATION'; out['settled']=True
        out['qc_state']='SETTLED_RESOURCE_DELIVERY'
        return stop('SETTLED','Conditional creation changes the resource total by the amount created.')
    if mode == 'P3_ENACT_UNDERSPECIFIED':
        # Deliberately no hidden postcondition for A or provenance of new units.
        out['after']={'A':None,'B':f.b+f.qty,'total':None}
        out['event']='OUTCOME_POSTCONDITION_ONLY'; out['settled']=None
        out['qc_state']='OUTCOME_ASSERTED_ACCOUNTING_INCOMPLETE'
        return stop('UNDERDETERMINED_ACCOUNTING',
                    'B postcondition can be asserted, but A, conservation and mechanism are unspecified.')
    raise ValueError(mode)

def verify(records):
    assertions=[]
    for r in records:
        f=next(x for x in BASE_CASES if x.case_id==r['case_id'])
        if r['mode']=='P1_TRANSFER' and r['status']=='SETTLED':
            assertions.append((r['case_id'],r['mode'],'conserve_total',r['before']['total']==r['after']['total']))
            assertions.append((r['case_id'],r['mode'],'recipient_delivery',r['after']['B']==f.b+f.qty))
        if r['mode']=='P2_CREATE' and r['status']=='SETTLED':
            assertions.append((r['case_id'],r['mode'],'creation_delta',r['after']['total']-r['before']['total']==f.qty))
            assertions.append((r['case_id'],r['mode'],'original_inventory_preserved',r['after']['A']==f.a))
        if r['status'] in ('UNDEFINED_TARGET','INCOHERENT_TARGET','VALUATION_UNAVAILABLE','UNAUTHORIZED','REPLAY_NO_OP','NO_SELLER','SELLER_UNKNOWN','NONTRANSFERABLE','INSUFFICIENT_INVENTORY','EVALUATED_NO_DELIVERY'):
            assertions.append((r['case_id'],r['mode'],'no_mutation',r['before']==r['after']))
        assertions.append((r['case_id'],r['mode'],'no_automatic_ncoin',not r['ncoin_issued']))
        assertions.append((r['case_id'],r['mode'],'no_premature_1coin',not r['onecoin_issued']))
    return [{'case':a,'mode':b,'rule':c,'pass':d} for a,b,c,d in assertions]

def run():
    records=[execute(f,m) for f in BASE_CASES for m in MODES]
    checks=verify(records)
    counts={}
    for r in records: counts[r['status']]=counts.get(r['status'],0)+1
    result={
      'identity':'OAL-CURR-PILOT-001 / ChatGPT independent simulation v0.1',
      'date':'2026-11-07','status':'OWNER_DIRECTED_INDEPENDENT_EXPLORATION_NOT_CANON',
      'premise':'QC(T)=V(T) is a conceptual stipulation; no physical extraordinary capability is demonstrated',
      'execution_environment':'Python standard library, deterministic discrete state transitions',
      'ncoin_rule':'No NCOIN is auto-issued for any status. Independent consequence models remain unfrozen.',
      'onecoin_rule':'No 1COIN is auto-issued. A separate settlement comparison is described in report.',
      'source_cases':[asdict(f) for f in BASE_CASES], 'modes':list(MODES),
      'records':records,'checks':checks,
      'summary':{'cases':len(BASE_CASES),'modes':len(MODES),'records':len(records),
                 'invariant_checks':len(checks),'check_failures':sum(not c['pass'] for c in checks),
                 'statuses':counts}}
    output=Path(__file__).with_name('OAL_ChatGPT_Pilot_001_Execution_Results_v0.1.json')
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(output),'summary':result['summary']},indent=2))
    assert all(c['pass'] for c in checks)
    return result

if __name__=='__main__':run()
