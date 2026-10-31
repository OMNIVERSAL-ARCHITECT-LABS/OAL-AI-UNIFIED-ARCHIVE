import csv
from pathlib import Path
# Source: Perplexity execution, P1 Cairn, finite resources section.
# Selected design targets, not experimental observations.
rows=[]
for mode,power in [("Normal",150.0),("Essential",12.0),("Preservation",0.2)]:
    energy_h=6000.0/power
    heat_h=30000.0*20.0/power/3600.0
    rows.append({"mode":mode,"power_W":power,"energy_only_h":energy_h,
                 "no_export_thermal_h":heat_h,"combined_bound_h":min(energy_h,heat_h)})
assert abs(rows[0]["energy_only_h"]-40.0)<1e-10
assert abs(rows[0]["no_export_thermal_h"]-10/9)<1e-10
assert abs(rows[2]["combined_bound_h"]-2500/3)<1e-10
with Path("cairn_recomputed.csv").open("w",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=rows[0]);writer.writeheader();writer.writerows(rows)
