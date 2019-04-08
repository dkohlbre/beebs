#!/usr/bin/python3
# libraries
import numpy as np
import matplotlib.pyplot as plt
from brokenaxes import brokenaxes
# set width of bar
barWidth = 0.5
colors=["#FF800E","#006BA4","#ABABAB","#595959","#5F9ED1","#C85200"] #tableau colorblind10

dirname="/home/dkohlbre/keystone/processing/keystone-bench/hifive_logs/"

def read_file(fname, typ=float):
    arr = []
    try:
        with open(fname) as f:
            for l in f.readlines():
                v = l.strip()
                if(v[-1] == 'l'):
                    v = v[0:-1]
                arr.append(typ(v))
        return arr
    except(Exception):
        return [0]

def read_beebs():
    # beebs
    beebs_testnames = read_file(dirname+"beebs/TESTLIST", str)
    beebs_results_b = {}
    beebs_results_k = {}
    for test in beebs_testnames:
        beebs_results_b[test] = read_file(dirname+"beebs/BASE_"+test+".log", int)
        beebs_results_k[test] = read_file(dirname+"beebs/KEYSTONE_"+test+".log", int)

    return beebs_results_b, beebs_results_k

def read_coremark():
    coremark_results_b = {}
    coremark_results_k = {}
    coremark_results_b["coremark"] = read_file(dirname+"coremark/BASE_coremark.log")
    coremark_results_k["coremark"] = read_file(dirname+"coremark/KEYSTONE_coremark.log")
    return coremark_results_b, coremark_results_k


plt.figure(figsize=(16,12))

cm_baseline, cm_keystone = read_coremark()
beebs_baseline, beebs_keystone = read_beebs()

keys = beebs_baseline.keys()
bar_k = []
bar_b = []
for t in keys:
    if(len(beebs_keystone[t]) < 10 or len(beebs_baseline[t]) < 10):
        print("ERR on beebs "+t)
        bar_k.append(0)
        bar_b.append(0)
        continue
    bar_k.append(sum(beebs_keystone[t])/len(beebs_keystone[t]))
    bar_b.append(sum(beebs_baseline[t])/len(beebs_baseline[t]))
#    print("Test: "+t+"\n"+"k: "+str(bar_k[-1])+"\nb: "+str(bar_b[-1]))
# Set position of bar on X axis
r1 = np.arange(len(bar_k))
r2 = [x + barWidth for x in r1]

bax = brokenaxes(ylims=((0, 0.2*1e9), (2.0*1e9, 4.5*1e9)),hspace=.05)


# Make the plot
bax.bar(r1, bar_k, color=colors[0], width=barWidth, edgecolor='white', label='Keystone')
bax.bar(r2, bar_b, color=colors[1], width=barWidth, edgecolor='white', label='Baseline')

# Add xticks on the middle of the group bars
plt.xlabel('Test', fontweight='bold')
plt.xticks([r + barWidth/2 for r in range(len(bar_k))], keys, rotation=45)
# Create legend & Show graphic
plt.tight_layout()

plt.legend(loc="best",fancybox=True, framealpha=0.5)

plt.savefig("foo.png",dpi=100)
