"""Barcha matplotlib grafiklari uchun yagona uslub (kitob dizayniga mos: ko'k palitra, yengil to'r, ochiq spayn)."""
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mc
from matplotlib.patches import Rectangle
PAL={'blue':'#4F86D6','dark':'#2F4F7F','orange':'#EE8A3C','green':'#3FA34D','red':'#D9534F','gray':'#6B7785','light':'#DCEBFA'}
# bir harfli ranglarni palitraga moslash
_m={'b':PAL['blue'],'g':PAL['green'],'r':PAL['red'],'k':'#222222','m':'#8E6BBF','c':'#2BA5B5','y':'#E9B83A'}
for k,v in _m.items():
    rgb=mc.to_rgb(v); mc.BASE_COLORS[k]=rgb; mc._colors_full_map[k]=rgb
plt.rcParams.update({'font.family':'Arial Unicode MS','font.size':10,'axes.spines.top':False,'axes.spines.right':False,
 'axes.edgecolor':'#555555','axes.linewidth':1.0,'axes.grid':True,'axes.axisbelow':True,'grid.color':'#C9D1DB','grid.alpha':.6,'grid.linewidth':.7,
 'axes.labelcolor':'#222222','xtick.color':'#333333','ytick.color':'#333333','lines.linewidth':2.0,'lines.markersize':5,
 'figure.facecolor':'white','axes.facecolor':'white','savefig.facecolor':'white','legend.frameon':False})
RECOL={k:PAL['blue'] for k in ('#c1704a','#c15a5a','#8a7fc1','#6fa86f','#6aa0d8','#4a7fc1')}
def finalize(fig):
    for ax in fig.axes:
        if not ax.axison: continue
        ax.grid(axis='x',visible=False) if ax.get_xscale()=='linear' and any(isinstance(p,Rectangle) for p in ax.patches) else None
        for p in ax.patches:
            if isinstance(p,Rectangle) and p.get_width()>0 and p.get_height()>0:
                fc=mc.to_hex(p.get_facecolor())
                p.set_facecolor(RECOL.get(fc.lower(),PAL['blue'] if fc.lower()=='#1f77b4' else fc))
                p.set_edgecolor(PAL['dark']); p.set_linewidth(.9)
