from core import *
from pic import _save
from pic3 import _img,_opts
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np, math
def _fin(q): q.kind='picture'; return q
# ---- benzol halqasidagi o'rinbosar
BS=[('CH3','toluol',92,'C7H8'),('OH','fenol',94,'C6H6O'),('NH2','anilin',93,'C6H7N'),('NO2','nitrobenzol',123,'C6H5NO2'),('Cl','xlorbenzol',112.5,'C6H5Cl'),('COOH','benzoy kislota',122,'C7H6O2')]
def p_benzsub(r):
    sub,nm,M,form=r.choice(BS)
    fig,ax=plt.subplots(figsize=(3.0,2.8)); ax.set_aspect('equal'); ax.axis('off')
    pts=[(math.cos(math.pi/2+i*math.pi/3),math.sin(math.pi/2+i*math.pi/3)) for i in range(6)]
    ax.add_patch(Polygon(pts,fill=False,ec='k',lw=2))
    for i in (0,2,4):
        a=(pts[i][0]*.78,pts[i][1]*.78); b2=(pts[i+1][0]*.78,pts[i+1][1]*.78)
        ax.plot([a[0],b2[0]],[a[1],b2[1]],'k',lw=1.6)
    x,y=pts[0]; ax.plot([x,x],[y,y+.55],'k',lw=2); ax.text(x,y+.8,sub.translate(str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')),ha='center',va='center',fontsize=13)
    ax.set_xlim(-1.8,1.8); ax.set_ylim(-1.4,2.0); img=_img(_save(fig,'bs_%d.png'%r.randrange(10**6)),"Benzol hosilasi")
    head="Rasmda benzol hosilasining tuzilish formulasi berilgan.\n\n%s\n\n"%img
    ask=r.choice(['name','formula','M'])
    if ask=='name': q=Q(head+"Birikmaning nomini toping.",nm,_opts(nm,[x[1] for x in BS],r),"Benzol halqasi + %s → %s"%(sub,nm),"10-sinf (aromatik uglevodorodlar)",'picture')
    elif ask=='formula': q=Q(head+"Birikmaning molekulyar formulasini aniqlang.",form,_opts(form,[x[3] for x in BS],r),"Halqa C6H5 + %s → %s"%(sub,form),"10-sinf (aromatik uglevodorodlar)",'picture')
    else: q=numq(head+"Birikmaning molyar massasini (g/mol) hisoblang.",M,[M+16,M-14,M+14,M*2],"%s: %s g/mol"%(form,M),"10-sinf (aromatik uglevodorodlar)",None,'picture')
    return _fin(q)
# ---- aminokislotalar
AA=[('glitsin','H',75,'C2H5NO2'),('alanin','CH3',89,'C3H7NO2'),('valin','CH(CH3)2',117,'C5H11NO2'),('serin','CH2OH',105,'C3H7NO3'),('sistein','CH2SH',121,'C3H7NO2S')]
def p_amino(r):
    nm,R,M,form=r.choice(AA)
    fig,ax=plt.subplots(figsize=(4.2,1.6))
    ax.axis('off'); ax.set_xlim(0,6); ax.set_ylim(0,1.4)
    ax.text(.3,.5,'H₂N – CH – COOH',fontsize=15,ha='left',va='center')
    Rs=R.translate(str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')) if R!='CH(CH3)2' else 'CH(CH₃)₂'
    ax.plot([1.52,1.52],[.72,.92],'k',lw=1.5); ax.text(1.52,1.1,Rs,fontsize=13,ha='center',va='center')
    img=_img(_save(fig,'aa_%d.png'%r.randrange(10**6)),"Aminokislota")
    head="Rasmda α-aminokislotaning tuzilish formulasi berilgan.\n\n%s\n\n"%img
    ask=r.choice(['name','formula','M'])
    if ask=='name': q=Q(head+"Aminokislotaning nomini toping.",nm,_opts(nm,[x[0] for x in AA],r),"Radikal %s → %s"%(R,nm),"10-sinf (aminokislotalar)",'picture')
    elif ask=='formula': q=Q(head+"Aminokislotaning molekulyar formulasini aniqlang.",form,_opts(form,[x[3] for x in AA]+['C4H9NO2'],r),"%s: %s"%(nm,form),"10-sinf (aminokislotalar)",'picture')
    else: q=numq(head+"Aminokislotaning molyar massasini (g/mol) hisoblang.",M,[M+14,M-14,M+18,M*2],"%s: %s g/mol"%(form,M),"10-sinf (aminokislotalar)",None,'picture')
    return _fin(q)
# ---- ion bog' hosil bo'lishi (elektron o'tishi)
IB=[('Na','Cl','NaCl',1,1),('Mg','Cl','MgCl2',2,1),('Ca','O','CaO',2,2),('Al','Cl','AlCl3',3,1),('K','S','K2S',1,2),('Mg','O','MgO',2,2),('Li','F','LiF',1,1)]
def p_ionic(r):
    m,n,form,cm,cn=r.choice(IB)
    fig,ax=plt.subplots(figsize=(5.2,1.8)); ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,3)
    ax.text(1.2,1.2,m,fontsize=18,ha='center',va='center',bbox=dict(boxstyle='circle',fc='#eef3fb'))
    ax.text(5,1.2,n,fontsize=18,ha='center',va='center',bbox=dict(boxstyle='circle',fc='#fbeeee'))
    ax.annotate('',xy=(4.2,2.0),xytext=(1.9,2.0),arrowprops=dict(arrowstyle='->',lw=1.8)); ax.text(3.05,2.4,'e⁻',ha='center',fontsize=12)
    ax.text(7.2,1.2,'→',fontsize=22,ha='center',va='center'); ax.text(8.8,1.2,'ion\nbirikma',fontsize=12,ha='center',va='center')
    img=_img(_save(fig,'ib_%d.png'%r.randrange(10**6)),"Ion bog' hosil bo'lishi")
    head="Rasmda %s va %s atomlari orasida elektron o'tishi sxematik ko'rsatilgan (ion bog' hosil bo'lishi).\n\n%s\n\n"%(m,n,img)
    ask=r.choice(['cat','form','tot'])
    if ask=='cat': q=Q(head+"%s atomi qancha elektron berib, qanday zaryadli ionga aylanadi?"%m,"%d ta, +%d"%(cm,cm),["%d ta, −%d"%(cm,cm),"%d ta, +%d"%(cm+1,cm+1),"%d ta, +%d"%(cm+2,cm+2)],"%s → %s^%d+ (%d e⁻ beradi)"%(m,m,cm,cm),"8-sinf (ion bog')",'picture')
    elif ask=='form': q=Q(head+"Hosil bo'lgan ion birikmaning formulasini toping.",form,_opts(form,[x[2] for x in IB],r),"Zaryadlar: +%d va −%d → %s"%(cm,cn,form),"8-sinf (ion bog')",'picture')
    else:
        a=r.choice([1,2,3])
        q=numq(head+"%d ta %s atomi %s bilan to'liq reaksiyaga kirishganda jami nechta elektron o'tadi?"%(a,m,n),a*cm,[a*cm+cn,a*cm*2,max(a*cm-1,1)+2,a*cn+cm+1],"Har bir %s atomi %d e⁻ beradi → %d·%d = %d"%(m,cm,a,cm,a*cm),"8-sinf (ion bog')",0,'picture')
    return _fin(q)
PICS6=[p_benzsub,p_amino,p_ionic]
PS6={p_benzsub:'O',p_amino:'O',p_ionic:'U'}
