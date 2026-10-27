from core import *
from pic import _save
from pic3 import _img,_opts
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch
import numpy as np, math
import re as _re
_SUB=str.maketrans('0123456789','₀₁₂₃₄₅₆₇₈₉')
def subf(t):
    return _re.sub(r'(?<=[A-Za-z\)])(\d+)',lambda m:m.group(1).translate(_SUB),t)
def _fin(q): q.kind='picture'; return q
# ------------------------------------------------------------ davriy jadval parchasi
P2=['Li','Be','B','C','N','O','F','Ne']; P3=['Na','Mg','Al','Si','P','S','Cl','Ar']
EN={'Li':1.0,'Be':1.5,'B':2.0,'C':2.5,'N':3.0,'O':3.5,'F':4.0,'Na':0.9,'Mg':1.2,'Al':1.5,'Si':1.8,'P':2.1,'S':2.5,'Cl':3.0}
def p_pt(r):
    cells=[(p,g) for p in (2,3) for g in range(1,8)]
    for _ in range(100):
        ch=r.sample(cells,3); els=[(P2 if p==2 else P3)[g-1] for p,g in ch]
        if len({EN[e] for e in els})==3: break
    fig,ax=plt.subplots(figsize=(5.6,2.0)); ax.axis('off')
    for p in (2,3):
        for g in range(8):
            el=(P2 if p==2 else P3)[g]; x=g; y=-(p-2)
            lab=el
            for L,(pp,gg) in zip('XYZ',ch):
                if (pp,gg)==(p,g+1): lab=L
            ax.add_patch(Rectangle((x,y),1,1,fc='#eef3fb' if lab in 'XYZ' and len(lab)==1 else 'white',ec='k')); ax.text(x+.5,y+.5,lab,ha='center',va='center',fontsize=13,fontweight='bold' if len(lab)==1 and lab in 'XYZ' else 'normal')
    for g in range(8): ax.text(g+.5,1.15,['IA','IIA','IIIA','IVA','VA','VIA','VIIA','VIIIA'][g],ha='center',fontsize=8)
    ax.text(-.15,.5,'2',ha='right',va='center',fontsize=9); ax.text(-.15,-.5,'3',ha='right',va='center',fontsize=9)
    ax.set_xlim(-.6,8.1); ax.set_ylim(-1.1,1.6); img=_img(_save(fig,'pt_%d.png'%r.randrange(10**6)),'Davriy jadvalning bir qismi')
    head="Rasmda davriy jadvalning bir qismi berilgan (X, Y, Z — noma'lum elementlar).\n\n%s\n\n"%img
    ask=r.choice(['EN','rad','metal'])
    L='XYZ'
    if ask=='EN':
        i=max(range(3),key=lambda k:EN[els[k]]); q=Q(head+"X, Y, Z elementlardan qaysi birining elektrmanfiyligi eng katta?",L[i],[x for x in L if x!=L[i]]+["uchalasiniki teng"],"Elektrmanfiylik: "+', '.join('%s – %s (%s)'%(L[k],els[k],EN[els[k]]) for k in range(3)),"8-sinf (davriy qonun, jadval)",'picture')
    elif ask=='rad':
        rr=lambda k:ch[k][0]*10-ch[k][1]; i=max(range(3),key=rr); q=Q(head+"X, Y, Z elementlardan qaysi birining atom radiusi eng katta?",L[i],[x for x in L if x!=L[i]]+["radiuslari teng"],"Davr raqami katta va guruh raqami kichik bo'lgan element atomining radiusi katta: %s"%els[i],"8-sinf (davriy qonun, jadval)",'picture')
    else:
        m=[k for k in range(3) if ch[k][1]<=3];
        if len(m)==0 or len(m)==3: return p_pt(r)
        ans=''.join(L[k] for k in m); ans=', '.join(L[k] for k in m)
        allc=['X','Y','Z','X, Y','X, Z','Y, Z','X, Y, Z']; ws=[c for c in allc if c!=ans and len(c.split(', '))in(len(m),len(m)+1,len(m)-1)]; r.shuffle(ws)
        q=Q(head+"Qaysi elementlar metallar hisoblanadi?",ans,ws[:3],"Metall: IA–IIIA guruh (B dan tashqari). Elementlar: "+', '.join('%s – %s'%(L[k],els[k]) for k in range(3)),"8-sinf (metallar va metallmaslar, jadval)",'picture')
    return _fin(q)
# ------------------------------------------------------------ orbital diagramma
NAMEZ={5:'bor',6:'uglerod',7:'azot',8:'kislorod',9:'ftor',10:'neon',11:'natriy',12:'magniy',13:'alyuminiy',14:'kremniy',15:'fosfor',16:'oltingugurt',17:'xlor'}
def p_orb(r):
    Z=r.choice(list(NAMEZ)); fig,ax=plt.subplots(figsize=(5.6,2.2)); ax.axis('off')
    subs=[('1s',1,2)]+[('2s',1,2),('2p',3,6)]+([('3s',1,2),('3p',3,6)] if Z>10 else [])
    left=Z; x=0
    for nm,nb,cap in subs:
        e=min(cap,left); left-=e; ups=min(e,nb); downs=e-ups
        for b in range(nb):
            ax.add_patch(Rectangle((x+b*.55,0),.5,.5,fc='white',ec='k'))
            if b<ups: ax.annotate('',xy=(x+b*.55+.15,.45),xytext=(x+b*.55+.15,.05),arrowprops=dict(arrowstyle='->'))
            if b<downs: ax.annotate('',xy=(x+b*.55+.35,.05),xytext=(x+b*.55+.35,.45),arrowprops=dict(arrowstyle='->'))
        ax.text(x+(nb*.55-.05)/2,-.28,nm,ha='center',fontsize=11); x+=nb*.55+.35
    ax.set_xlim(-.1,x); ax.set_ylim(-.5,.7); img=_img(_save(fig,'or_%d.png'%r.randrange(10**6)),'Orbital diagramma')
    head="Rasmda neytral atom elektron qavatlarining orbital diagrammasi (kataklar – orbitallar, o'qlar – elektronlar) berilgan.\n\n%s\n\n"%img
    ask=r.choice(['el','unp'])
    if ask=='el':
        pool=[NAMEZ[z] for z in NAMEZ]; q=Q(head+"Diagramma qaysi element atomiga tegishli?",NAMEZ[Z],_opts(NAMEZ[Z],[NAMEZ[z] for z in NAMEZ if abs(z-Z)<=3],r),"Elektronlar soni %d → Z = %d, %s"%(Z,Z,NAMEZ[Z]),"8-sinf (elektron konfiguratsiya, orbital diagramma)",'picture')
    else:
        un=0; left=Z
        for nm,nb,cap in subs:
            e=min(cap,left); left-=e; un+= e if e<=nb else 2*nb-e
        q=numq(head+"Diagrammadagi atomda nechta juftlashmagan elektron bor?",un,[un+1,un-1 if un>1 else un+3,un+2,Z-un],"Hund qoidasi bo'yicha juftlashmagan elektronlar: %d"%un,"8-sinf (elektron konfiguratsiya, orbital diagramma)",0,'picture')
    return _fin(q)
# ------------------------------------------------------------ zanjirlar
CHAIN_IN=[(['S','SO2','SO3','H2SO4'],['O2','O2, kat.','H2O']),(['Ca','CaO','Ca(OH)2','CaCO3'],['O2','H2O','CO2']),(['Zn','ZnO','ZnCl2','Zn(OH)2'],['O2','HCl','NaOH']),(['Fe','FeCl2','Fe(OH)2','Fe(OH)3'],['HCl','NaOH','O2, H2O']),(['P','P2O5','H3PO4','Ca3(PO4)2'],['O2','H2O','Ca(OH)2']),(['Na','Na2O','NaOH','Na2CO3'],['O2','H2O','CO2']),(['C','CO2','Na2CO3','CaCO3'],['O2','NaOH','CaCl2']),(['N2','NH3','NO','NO2'],['H2','O2, kat.','O2']),(['Mg','MgO','MgSO4','Mg(OH)2'],['O2','H2SO4','NaOH']),(['Cu','CuCl2','Cu(OH)2','CuO'],['Cl2','NaOH','t°']),(['Si','SiO2','Na2SiO3','H2SiO3'],['O2','NaOH','HCl']),(['Al','Al2O3','AlCl3','Al(OH)3'],['O2','HCl','NaOH (kam)'])]
def draw_chain(labels,reag,fname,vert=False):
    n=len(labels); fig,ax=plt.subplots(figsize=(6.6,1.5)); ax.axis('off')
    for i,l in enumerate(labels):
        ax.text(i*3.3,0,subf(l),ha='center',va='center',fontsize=14,bbox=dict(boxstyle='round,pad=.35',fc='#f3f6fb',ec='k'))
    for i,rg in enumerate(reag):
        ax.annotate('',xy=(i*3.3+3.3-.95,0),xytext=(i*3.3+.95,0),arrowprops=dict(arrowstyle='->',lw=1.4)); ax.text(i*3.3+1.65,.28,subf(rg),ha='center',fontsize=11)
    ax.set_xlim(-.9,(n-1)*3.3+.9); ax.set_ylim(-.6,.7); return _save(fig,fname)
def p_chain_in(r):
    labs,reag=r.choice(CHAIN_IN); labs=list(labs); reag=list(reag)
    mode=r.choice(['cmp','reag'])
    if mode=='cmp':
        i,j=sorted(r.sample([1,2,3],2)) if r.random()<.6 else (r.choice([1,2,3]),None)
        shown=list(labs); mk=[]
        for k,idx in enumerate([x for x in (i,j) if x is not None]): shown[idx]='XY'[k]; mk.append(idx)
        img=_img(draw_chain(shown,reag,'ci_%d.png'%r.randrange(10**6)),'Moddalar zanjiri')
        if len(mk)==1:
            ans=labs[mk[0]]; allc=[l for L,_ in CHAIN_IN for l in L if l!=ans and l not in labs[:1]]
            ws=_opts(ans,[l for l in labs if l!=ans and l!=labs[0]]+r.sample(allc,3),r)
            q=Q("Rasmdagi o'zgarishlar zanjirida X moddaning formulasini aniqlang.\n\n%s"%img,ans,ws,"Zanjir: %s"%' → '.join(labs),"9-sinf (genetik bog'lanish)",'picture')
        else:
            ans="X – %s, Y – %s"%(labs[mk[0]],labs[mk[1]]); ws=[]
            others=[l for l in labs[1:] if l not in (labs[mk[0]],labs[mk[1]])]
            pool=["X – %s, Y – %s"%(b,a) for a,b in [(labs[mk[0]],labs[mk[1]])]]+["X – %s, Y – %s"%(labs[mk[0]],o) for o in others]+["X – %s, Y – %s"%(o,labs[mk[1]]) for o in others]+["X – %s, Y – %s"%(labs[mk[1]],labs[0])]
            q=Q("Rasmdagi o'zgarishlar zanjirida X va Y moddalarni aniqlang.\n\n%s"%img,ans,_opts(ans,pool,r),"Zanjir: %s"%' → '.join(labs),"9-sinf (genetik bog'lanish)",'picture')
    else:
        k=r.randrange(3); shownr=list(reag); ans=reag[k]; shownr[k]='X'
        img=_img(draw_chain(labs,shownr,'ci_%d.png'%r.randrange(10**6)),'Moddalar zanjiri')
        allr=list({rr for _,R in CHAIN_IN for rr in R if rr!=ans})
        q=Q("Rasmdagi zanjirda %s dan %s hosil bo'lishi uchun X reagentni aniqlang.\n\n%s"%(labs[k],labs[k+1],img),ans,_opts(ans,allr,r),"%s + %s → %s"%(labs[k],ans,labs[k+1]),"9-sinf (genetik bog'lanish)",'picture')
    return _fin(q)
CHAIN_ORG=[(['C2H5OH','C2H4','C2H4Br2'],['H2SO4 (kons.), 170 °C','Br2']),(['C2H2','CH3CHO','CH3COOH'],['H2O, Hg²⁺','Ag2O, NH3']),(['CH3COOH','CH3COOC2H5','CH3COONa'],['C2H5OH, H2SO4','NaOH']),(['C6H6','C6H5NO2','C6H5NH2'],['HNO3, H2SO4','H2, kat.']),(['CaC2','C2H2','C6H6'],['H2O','C, 600 °C']),(['C2H4','C2H5OH','C2H5ONa'],['H2O, H⁺','Na']),(['CH4','CH3Cl','C2H6'],['Cl2, hν','Na']),(['C6H12O6','C2H5OH','CH3CHO'],['bijg\'ish','CuO, t°']),(['C2H5Br','C2H4','C2H6'],['KOH (spirtli)','H2, Ni'])]
def p_chain_org(r):
    labs,reag=r.choice(CHAIN_ORG); mode=r.choice(['cmp','reag'])
    if mode=='cmp':
        k=r.choice([1,2]); shown=list(labs); ans=labs[k]; shown[k]='X'
        img=_img(draw_chain(shown,reag,'co_%d.png'%r.randrange(10**6)),'Organik moddalar zanjiri')
        allc=list({l for L,_ in CHAIN_ORG for l in L if l!=ans})
        q=Q("Rasmdagi o'zgarishlar zanjirida X moddaning formulasini aniqlang.\n\n%s"%img,ans,_opts(ans,[l for l in labs if l!=ans]+r.sample(allc,4),r),"Zanjir: %s"%' → '.join(labs),"10-sinf (organik moddalarning o'zaro bog'lanishi)",'picture')
    else:
        k=r.randrange(2); shownr=list(reag); ans=reag[k]; shownr[k]='X'
        img=_img(draw_chain(labs,shownr,'co_%d.png'%r.randrange(10**6)),'Organik moddalar zanjiri')
        allr=list({rr for _,R in CHAIN_ORG for rr in R if rr!=ans})
        q=Q("Rasmdagi zanjirda %s dan %s olish uchun X reagent va sharoitni aniqlang.\n\n%s"%(labs[k],labs[k+1],img),ans,_opts(ans,allr,r),"%s → %s: %s"%(labs[k],labs[k+1],ans),"10-sinf (organik moddalarning o'zaro bog'lanishi)",'picture')
    return _fin(q)
# ------------------------------------------------------------ benzol hosilalari
SUBS=[('CH3','toluol','C7H8',92),('OH','fenol','C6H6O',94),('NO2','nitrobenzol','C6H5NO2',123),('NH2','anilin','C6H7N',93),('Cl','xlorbenzol','C6H5Cl',112.5),('Br','brombenzol','C6H5Br',157),('COOH','benzoy kislota','C7H6O2',122),('C2H5','etilbenzol','C8H10',106)]
def p_benz(r):
    sub,nm,f,M_=r.choice(SUBS); fig,ax=plt.subplots(figsize=(3.2,2.8)); ax.set_aspect('equal'); ax.axis('off')
    ang=[math.pi/2+i*math.pi/3 for i in range(6)]; pts=[(math.cos(a),math.sin(a)) for a in ang]
    ax.add_patch(Polygon(pts,fill=False,ec='k',lw=1.8))
    for i in (0,2,4):
        a=np.array(pts[i])*.8; b=np.array(pts[(i+1)%6])*.8; d=b-a; a2=a+d*.12; b2=b-d*.12
        ax.plot([a2[0],b2[0]],[a2[1],b2[1]],'k',lw=1.4)
    ax.plot([pts[0][0],pts[0][0]],[pts[0][1],pts[0][1]+.55],'k',lw=1.8); ax.text(0,1.0+.8,sub,ha='center',va='center',fontsize=15,bbox=dict(fc='white',ec='none',pad=1))
    ax.set_xlim(-1.6,1.6); ax.set_ylim(-1.3,2.1); img=_img(_save(fig,'bz_%d.png'%r.randrange(10**6)),'Benzol hosilasi')
    head="Rasmda aromatik uglevodorod hosilasining tuzilish formulasi berilgan.\n\n%s\n\n"%img
    ask=r.choice(['name','formula','M','sigma'])
    names=[s[1] for s in SUBS]
    if ask=='name': q=Q(head+"Birikmaning nomini toping.",nm,_opts(nm,names,r),"Benzol halqasida %s o'rinbosar: %s"%(sub,nm),"10-sinf (arenlar)",'picture')
    elif ask=='formula': q=Q(head+"Birikmaning molekulyar formulasini aniqlang.",f,_opts(f,[s[2] for s in SUBS],r),"Halqa C6H5 + %s → %s"%(sub,f),"10-sinf (arenlar)",'picture')
    elif ask=='M': q=numq(head+"Birikmaning molyar massasini (g/mol) hisoblang.",M_,[M_+14,M_-14,M_+2,M_*2],"M(%s) = %s"%(f,fmt(M_)),"10-sinf (arenlar)",None,'picture')
    else:
        from core import parse
        pp=parse(f); c=pp['C']; h=pp['H']; tot=c+h+pp.get('N',0)+pp.get('O',0)+pp.get('Cl',0)+pp.get('Br',0)
        # sigma count: skeleton bonds = atoms-1 + rings(1) ; halqa: 12 sigma (6 C-C + 6) ... generic: sigma = atoms-1+1
        sig=tot; q=numq(head+"Molekuladagi σ-bog'lar sonini aniqlang (π-bog'lar halqada va o'rinbosarda alohida hisoblanadi).",sig,[sig+1,sig-1,sig+2,sig-2],"Atomlar soni %d, halqa bor: σ = %d − 1 + 1 = %d"%(tot,tot,sig),"10-sinf (arenlar)",0,'picture')
    return _fin(q)
# ------------------------------------------------------------ sharsimon modellar
MOLS={'H2O':{'at':[('O',0,0,'r'),('H',-.9,-.7,'w'),('H',.9,-.7,'w')],'b':[(0,1,1),(0,2,1)],'form':'H2O','geo':'burchakli','hyb':'sp³','pi':0,'polar':'qutbli'},
'CO2':{'at':[('C',0,0,'k'),('O',-1.2,0,'r'),('O',1.2,0,'r')],'b':[(0,1,2),(0,2,2)],'form':'CO2','geo':'chiziqli','hyb':'sp','pi':2,'polar':"qutbsiz"},
'NH3':{'at':[('N',0,0,'b'),('H',-1,-.7,'w'),('H',1,-.7,'w'),('H',0,.95,'w')],'b':[(0,1,1),(0,2,1),(0,3,1)],'form':'NH3','geo':'uchburchakli piramida','hyb':'sp³','pi':0,'polar':'qutbli'},
'CH4':{'at':[('C',0,0,'k'),('H',-1,.8,'w'),('H',1,.8,'w'),('H',-1,-.8,'w'),('H',1,-.8,'w')],'b':[(0,1,1),(0,2,1),(0,3,1),(0,4,1)],'form':'CH4','geo':'tetraedr','hyb':'sp³','pi':0,'polar':'qutbsiz'},
'C2H4':{'at':[('C',-.7,0,'k'),('C',.7,0,'k'),('H',-1.4,.9,'w'),('H',-1.4,-.9,'w'),('H',1.4,.9,'w'),('H',1.4,-.9,'w')],'b':[(0,1,2),(0,2,1),(0,3,1),(1,4,1),(1,5,1)],'form':'C2H4','geo':'yassi','hyb':'sp²','pi':1,'polar':'qutbsiz'},
'C2H2':{'at':[('C',-.7,0,'k'),('C',.7,0,'k'),('H',-1.9,0,'w'),('H',1.9,0,'w')],'b':[(0,1,3),(0,2,1),(1,3,1)],'form':'C2H2','geo':'chiziqli','hyb':'sp','pi':2,'polar':'qutbsiz'}}
def p_model(r):
    key=r.choice(list(MOLS)); m=MOLS[key]; fig,ax=plt.subplots(figsize=(3.6,2.6)); ax.set_aspect('equal'); ax.axis('off')
    col={'r':'#e03030','w':'#f7d046','k':'#2e9e4f','b':'#2f56d6'}; rad={'r':.38,'w':.24,'k':.36,'b':.36}
    for a,b,o in m['b']:
        (x1,y1),(x2,y2)=m['at'][a][1:3],m['at'][b][1:3]
        for d in {1:[0],2:[-.07,.07],3:[-.12,0,.12]}[o]: ax.plot([x1,x2],[y1+d,y2+d],c='#555',lw=2.6,zorder=1)
    for s,x,y,c in m['at']:
        ax.add_patch(Circle((x,y),rad[c],fc=col[c],ec='#222',lw=1.4,zorder=2)); ax.add_patch(Circle((x-rad[c]*.32,y+rad[c]*.34),rad[c]*.28,fc='white',ec='none',alpha=.55,zorder=3))
    ax.set_xlim(-2.4,2.4); ax.set_ylim(-1.5,1.7); img=_img(_save(fig,'md_%d.png'%r.randrange(10**6)),'Molekula modeli')
    head="Rasmda molekulaning sharsimon modeli tasvirlangan (yashil – C, sariq – H, qizil – O, ko'k – N).\n\n%s\n\n"%img
    ask=r.choice(['form','geo','hyb','pi','polar'])
    ALL=list(MOLS.values())
    if ask=='form': q=Q(head+"Molekulaning formulasini aniqlang.",m['form'],_opts(m['form'],[x['form'] for x in ALL],r),"Modeldagi atomlar: "+''.join(a[0] for a in m['at']),"8–10-sinf (molekulalar tuzilishi)",'picture')
    elif ask=='geo': q=Q(head+"Molekula fazoviy shakli qanday?",m['geo'],_opts(m['geo'],[x['geo'] for x in ALL]+['halqasimon'],r),"%s molekulasi shakli: %s"%(m['form'],m['geo']),"11-sinf (molekulalar geometriyasi)",'picture')
    elif ask=='hyb': q=Q(head+"Markaziy atomning gibridlanish turi qanday?",m['hyb'],_opts(m['hyb'],['sp','sp²','sp³','sp³d'],r),"%s: markaziy atom %s"%(m['form'],m['hyb']),"11-sinf (gibridlanish)",'picture')
    elif ask=='pi': q=numq(head+"Molekuladagi π-bog'lar sonini aniqlang.",m['pi'],[m['pi']+1,m['pi']+2,max(m['pi']-1,0)+3,4],"%s da π-bog'lar: %d"%(m['form'],m['pi']),"11-sinf (kovalent bog' turlari)",0,'picture')
    else: q=Q(head+"Molekula qutbli yoki qutbsizligini aniqlang.",m['polar'],["qutbli" if m['polar']=="qutbsiz" else "qutbsiz","ionli","metall bog'li"],"%s: %s"%(m['form'],m['polar']),"11-sinf (bog' qutbliligi)",'picture')
    return _fin(q)
# ------------------------------------------------------------ kristall panjara
def p_lattice(r):
    kind=r.choice(['ion','atom','mol']); fig,ax=plt.subplots(figsize=(3.4,3.0)); ax.set_aspect('equal'); ax.axis('off')
    if kind=='ion':
        for i in range(4):
            for j in range(4):
                c=(i+j)%2==0; ax.add_patch(Circle((i,j),.38,fc='#e8b04a' if c else '#6aa0d8',ec='k')); ax.text(i,j,'+' if c else '−',ha='center',va='center',fontsize=12)
    elif kind=='atom':
        for i in range(4):
            for j in range(4):
                if i<3: ax.plot([i,i+1],[j,j],'k',lw=2)
                if j<3: ax.plot([i,i],[j,j+1],'k',lw=2)
        for i in range(4):
            for j in range(4): ax.add_patch(Circle((i,j),.22,fc='#555',ec='k',zorder=3))
    else:
        for i in range(3):
            for j in range(3):
                x=i*1.6; y=j*1.6; ax.plot([x,x+.7],[y,y],'k',lw=2); ax.add_patch(Circle((x,y),.25,fc='#d94b4b',ec='k',zorder=3)); ax.add_patch(Circle((x+.7,y),.25,fc='#d94b4b',ec='k',zorder=3))
    ax.set_xlim(-.7,4.3 if kind!='mol' else 5); ax.set_ylim(-.7,4.0); img=_img(_save(fig,'la_%d.png'%r.randrange(10**6)),'Kristall panjara')
    head="Rasmda kristall panjara tuzilishi tasvirlangan.\n\n%s\n\n"%img
    nm={'ion':'ion','atom':'atom','mol':'molekulyar'}[kind]
    prop={'ion':"Yuqori suyuqlanish harorati, suyuqlanmasi elektr tokini o'tkazadi",'atom':"Juda qattiq, suyuqlanish harorati juda yuqori",'mol':"Past suyuqlanish harorati, uchuvchan"}
    ask=r.choice(['type','prop'])
    if ask=='type': q=Q(head+"Bu panjara qaysi turga kiradi?",nm+" kristall panjara",[x+" kristall panjara" for x in ('ion','atom','molekulyar','metall') if x!=nm][:3],"Panjara tugunlarida: %s"%{'ion':'ionlar','atom':'atomlar','mol':'molekulalar'}[kind],"8-sinf (kristall panjaralar)",'picture')
    else: q=Q(head+"Shunday panjarali moddalar uchun qaysi xususiyat xos?",prop[kind],[v for k,v in prop.items() if k!=kind]+["Elektr tokini yaxshi o'tkazadi, plastik"],"Panjara turi bo'yicha: %s"%prop[kind],"8-sinf (kristall panjaralar)",'picture')
    return _fin(q)
# ------------------------------------------------------------ siklik uglevodorodlar
RN={3:'siklopropan',4:'siklobutan',5:'siklopentan',6:'siklogeksan'}
def p_ring(r):
    n=r.choice([3,4,5,6]); k=r.choice([1,1,2]) if n>=5 else 1
    pos=[0] if k==1 else [0,r.choice([1,2])] if n>=5 else [0]
    fig,ax=plt.subplots(figsize=(3.0,2.8)); ax.set_aspect('equal'); ax.axis('off')
    pts=[(math.cos(math.pi/2+i*2*math.pi/n),math.sin(math.pi/2+i*2*math.pi/n)) for i in range(n)]
    ax.add_patch(Polygon(pts,fill=False,ec='k',lw=2))
    for p in pos:
        x,y=pts[p]; ax.plot([x,x*1.55],[y,y*1.55],'k',lw=2); ax.text(x*1.8,y*1.8,'CH₃',ha='center',va='center',fontsize=12)
    ax.set_xlim(-2.3,2.3); ax.set_ylim(-2.2,2.4); img=_img(_save(fig,'rn_%d.png'%r.randrange(10**6)),'Siklik uglevodorod')
    c=n+len(pos); h=2*c
    if len(pos)==1: nm='metil'+RN[n]
    else:
        d=pos[1]; loc='1,2' if d==1 else '1,3'; nm='%s-dimetil%s'%(loc,RN[n])
    ask=r.choice(['name','formula','M'])
    head="Rasmda siklik uglevodorodning tuzilish formulasi berilgan.\n\n%s\n\n"%img
    if ask=='name':
        pool=['metil'+RN[x] for x in RN]+['1,2-dimetil'+RN[x] for x in (5,6)]+['1,3-dimetil'+RN[x] for x in (5,6)]
        q=Q(head+"Birikmaning nomini toping.",nm,_opts(nm,pool,r),"Halqa: %s, o'rinbosarlar %d ta CH3"%(RN[n],len(pos)),"10-sinf (sikloalkanlar)",'picture')
    elif ask=='formula': q=Q(head+"Birikmaning molekulyar formulasini aniqlang.","C%dH%d"%(c,h),["C%dH%d"%(c,h+2),"C%dH%d"%(c+1,h),"C%dH%d"%(c,h-2)],"C%d: CnH2n"%c,"10-sinf (sikloalkanlar)",'picture')
    else: q=numq(head+"Birikmaning molyar massasini (g/mol) hisoblang.",12*c+h,[12*c+h+2,12*c+h-2,12*c+h+14,(12*c+h)*2],"C%dH%d: %d"%(c,h,12*c+h),"10-sinf (sikloalkanlar)",None,'picture')
    return _fin(q)
# ------------------------------------------------------------ funksional guruhlar
FG=[('OH','spirtlar','O',1),('CHO','aldegidlar','O',1),('COOH','karbon kislotalar','O2',1),('NH2','aminlar','N',1),('Cl','galogenalkanlar','Cl',1),('COOCH3','murakkab efirlar','O2',1)]
def p_fg(r):
    g,cls,_,__=r.choice(FG); n=r.choice([1,2,3,4])
    chain='CH₃'+'–CH₂'*(n-1)+'–'+g
    fig,ax=plt.subplots(figsize=(5.6,1.0)); ax.axis('off'); ax.text(.5,.5,chain,ha='center',va='center',fontsize=18,transform=ax.transAxes)
    img=_img(_save(fig,'fg_%d.png'%r.randrange(10**6)),'Tuzilish formulasi')
    classes=[x[1] for x in FG]
    head="Rasmda organik birikmaning tuzilish formulasi keltirilgan.\n\n%s\n\n"%img
    c={'OH':n,'CHO':n+1,'COOH':n+1,'NH2':n,'Cl':n,'COOCH3':n+2}[g]
    ask=r.choice(['class','c'])
    if ask=='class': q=Q(head+"Birikma qaysi sinfga mansub?",cls,_opts(cls,classes,r),"%s guruh %s sinfiga xos"%(g,cls),"10-sinf (funksional guruhlar)",'picture')
    else: q=numq(head+"Molekuladagi uglerod atomlari sonini aniqlang.",c,[c+1,c-1 if c>1 else c+3,c+2,c*2],"Uglerod atomlari: %d"%c,"10-sinf (organik birikmalar)",0,'picture')
    return _fin(q)
# ------------------------------------------------------------ kuchlanish qatori
SER=['Li','K','Ca','Na','Mg','Al','Zn','Fe','Ni','Sn','Pb','H','Cu','Hg','Ag','Pt','Au']
def p_series(r):
    ms=[m for m in SER if m!='H']; ch=sorted(r.sample(range(len(ms)),3)); pos={m:i for i,m in enumerate(SER)}
    sel=[ms[i] for i in ch]; mk=dict(zip('XYZ',sel)); perm=list('XYZ'); r.shuffle(perm); mk=dict(zip(perm,sel))
    fig,ax=plt.subplots(figsize=(6.0,1.1)); ax.axis('off')
    for i,m in enumerate(SER):
        lab=m; c='white'
        for L,mm in mk.items():
            if mm==m: lab=L; c='#f7e3c8'
        if m=='H': c='#dfeaf7'
        ax.add_patch(Rectangle((i,0),.95,.9,fc=c,ec='k')); ax.text(i+.47,.45,lab,ha='center',va='center',fontsize=11,fontweight='bold' if lab in 'XYZ' else 'normal')
    ax.text(0,1.1,'Metallarning aktivlik (kuchlanish) qatori — kuchayish → kamayish',fontsize=9); ax.set_xlim(-.1,17.2); ax.set_ylim(-.1,1.5)
    img=_img(_save(fig,'se_%d.png'%r.randrange(10**6)),'Metallar aktivlik qatori')
    head="Rasmda metallarning kuchlanish qatori ko'rsatilgan (X, Y, Z — noma'lum metallar).\n\n%s\n\n"%img
    ask=r.choice(['hcl','displ'])
    if ask=='hcl':
        a=[L for L in 'XYZ' if pos[mk[L]]<pos['H']]; ans=', '.join(a) if a else "hech biri"
        allc=['X','Y','Z','X, Y','X, Z','Y, Z','X, Y, Z','hech biri']; ws=[c for c in allc if c!=ans]; r.shuffle(ws)
        q=Q(head+"Qaysi metallar suyultirilgan HCl dan vodorodni siqib chiqaradi?",ans,ws[:3],"Vodorodgacha turgan metallar: "+', '.join('%s – %s'%(L,mk[L]) for L in 'XYZ'),"9-sinf (metallar aktivligi)",'picture')
    else:
        a,b=r.sample('XYZ',2); can=pos[mk[a]]<pos[mk[b]]
        q=Q(head+"%s metali tuzining eritmasiga %s metall plastinka tushirilsa, reaksiya boradimi?"%(b,a),"Boradi, %s faolroq"%a if can else "Bormaydi, %s kamroq faol"%a,["Boradi, %s faolroq"%a if not can else "Bormaydi, %s kamroq faol"%a,"Faqat qizdirilganda boradi","Faqat konsentrlangan eritmada boradi"],"%s = %s, %s = %s: %s"%(a,mk[a],b,mk[b],'faolroq metall kam faolini siqib chiqaradi' if can else 'kam faol metall faolini siqib chiqarmaydi'),"9-sinf (metallar aktivligi)",'picture')
    return _fin(q)
# ------------------------------------------------------------ yemirilish zanjiri
def p_decay(r):
    seq=r.choice([(('²³⁸U',92),['α','β','β','α']),(('²³²Th',90),['α','α','β','α']),(('²²⁶Ra',88),['α','α','β'])])
    (nm,Z),steps=seq; A=int(''.join(c for c in nm.translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789')) if c.isdigit()))
    fig,ax=plt.subplots(figsize=(6,1.4)); ax.axis('off'); x=0
    cur=(A,Z); labs=[]
    for s in steps:
        labs.append('%d/%d'%cur); cur=(cur[0]-4,cur[1]-2) if s=='α' else (cur[0],cur[1]+1)
    labs.append('%d/%d'%cur)
    a=steps.count('α'); b=steps.count('β')
    for i,l in enumerate(labs):
        ax.text(i*1.9,0,l if i in(0,len(labs)-1) else '?',ha='center',va='center',fontsize=13,bbox=dict(boxstyle='round,pad=.3',fc='#f3f6fb',ec='k'))
        if i<len(steps): ax.annotate('',xy=(i*1.9+1.35,0),xytext=(i*1.9+.55,0),arrowprops=dict(arrowstyle='->')); ax.text(i*1.9+.95,.3,steps[i],ha='center',fontsize=11)
    ax.set_xlim(-.8,(len(labs)-1)*1.9+.8); ax.set_ylim(-.6,.7); img=_img(_save(fig,'dc_%d.png'%r.randrange(10**6)),'Yemirilish zanjiri')
    head="Rasmda radioaktiv yemirilish zanjiri berilgan (massa soni/zaryad; «?» – oraliq yadrolar).\n\n%s\n\n"%img
    ask=r.choice(['a','b','final'])
    if ask=='a': q=numq(head+"Zanjirda nechta α-zarra chiqarilgan?",a,[a+1,a+2,max(a-1,1)+4,b],"α-yemirilish: ΔA/4 = %d"%a,"11-sinf (yadro reaksiyalari)",0,'picture')
    elif ask=='b': q=numq(head+"Zanjirda nechta β-zarra chiqarilgan?",b,[b+1,b+2,a,b+3],"Zaryad balansi: β = %d"%b,"11-sinf (yadro reaksiyalari)",0,'picture')
    else: q=numq(head+"Oxirgi yadroning massa sonini aniqlang.",cur[0],[cur[0]+4,cur[0]-4,cur[0]+1,A],"A = %d − 4·%d = %d"%(A,a,cur[0]),"11-sinf (yadro reaksiyalari)",0,'picture')
    return _fin(q)
# ------------------------------------------------------------ indikator ranglari
IND=[('Lakmus',[(0,5,'#e05050','qizil'),(5,8,'#a070c0','binafsha'),(8,14,'#4a6fd0','ko\'k')]),('Metiloranj',[(0,3.1,'#e05050','qizil'),(3.1,4.4,'#e8a050','zarg\'aldoq'),(4.4,14,'#f0d040','sariq')]),('Fenolftalein',[(0,8.2,'#f4f4f4','rangsiz'),(8.2,10,'#e8a0c0','och pushti'),(10,14,'#d02070','malina rang')])]
def p_ind(r):
    fig,ax=plt.subplots(figsize=(5.6,2.4))
    for i,(nm,ss) in enumerate(IND):
        for a,b,c,_ in ss: ax.add_patch(Rectangle((a,2-i),b-a,.8,fc=c,ec='k',lw=.5))
        ax.text(-.2,2-i+.4,nm,ha='right',va='center',fontsize=10)
    ax.set_xlim(-3,14.2); ax.set_ylim(-.2,3); ax.set_xticks(range(0,15,2)); ax.set_yticks([]); ax.set_xlabel('pH')
    img=_img(_save(fig,'in_%d.png'%r.randrange(10**6)),'Indikatorlar rangi')
    nm,ss=r.choice(IND); pH=r.choice([2,4,6,7,9,11,12,13]); col=[c for a,b,_,c in ss if a<=pH<b][0]
    allc=list({c for _,L in IND for *_,c in L if c!=col})
    head="Rasmda indikatorlarning pH ga bog'liq rangi ko'rsatilgan.\n\n%s\n\n"%img
    ask=r.choice(['col','conc'])
    if ask=='col': q=Q(head+"pH = %d bo'lgan eritmada %s qanday rangga kiradi?"%(pH,nm.lower()),col,_opts(col,allc,r),"Rasmdan: pH = %d → %s"%(pH,col),"8-sinf (indikatorlar)",'picture')
    else:
        c_=r.choice([0.1,0.01,0.001]); ph=int(round(-math.log10(c_))); ind,ss2=IND[1]; col2=[c for a,b,_,c in ss2 if a<=ph<b][0]
        q=Q(head+"%s mol/l HCl eritmasiga metiloranj tomizildi. Eritma qanday rangga kiradi?"%fmt(c_),col2,_opts(col2,allc+['sariq','zarg\'aldoq','qizil'],r),"pH = %d → %s"%(ph,col2),"8-sinf (indikatorlar)",'picture')
    return _fin(q)
# ------------------------------------------------------------ Lyuis formulalari
LW={'H2O':('H:O:H',2),'NH3':('H:N:H',3),'HCl':('H:Cl',1),'Cl2':('Cl:Cl',1),'N2':('N≡N',3),'CO2':('O=C=O',4)}
def p_lewis(r):
    key=r.choice(['HCl','Cl2','H2O','N2','NH3','CO2']); fig,ax=plt.subplots(figsize=(4.4,1.8)); ax.axis('off')
    def dots(x,y,dirs,s=.28):
        for dx,dy in dirs:
            for off in (-.07,.07):
                px=x+dx*s+(0 if dx else off); py=y+dy*s+(0 if dy else off); ax.plot(px,py,'o',ms=3.2,c='k')
    D={'u':[(0,1)],'d':[(0,-1)],'l':[(-1,0)],'r':[(1,0)]}
    if key=='HCl':
        ax.text(0,0,'H',fontsize=18,ha='center',va='center'); ax.text(1.2,0,'Cl',fontsize=18,ha='center',va='center');
        for off in (-.07,.07): ax.plot(.6,off,'o',ms=3.2,c='k')
        dots(1.2,0,D['u']+D['d']+D['r'],.42)
    elif key=='Cl2':
        ax.text(0,0,'Cl',fontsize=18,ha='center',va='center'); ax.text(1.4,0,'Cl',fontsize=18,ha='center',va='center')
        for off in (-.07,.07): ax.plot(.7,off,'o',ms=3.2,c='k')
        dots(0,0,D['u']+D['d']+D['l'],.42); dots(1.4,0,D['u']+D['d']+D['r'],.42)
    elif key=='H2O':
        ax.text(0,0,'O',fontsize=18,ha='center',va='center'); ax.text(-1.0,0,'H',fontsize=18,ha='center',va='center'); ax.text(1.0,0,'H',fontsize=18,ha='center',va='center')
        for xx in (-.5,.5):
            for off in (-.07,.07): ax.plot(xx,off,'o',ms=3.2,c='k')
        dots(0,0,D['u']+D['d'],.4)
    elif key=='NH3':
        ax.text(0,0,'N',fontsize=18,ha='center',va='center'); ax.text(-1.0,0,'H',fontsize=18,ha='center',va='center'); ax.text(1.0,0,'H',fontsize=18,ha='center',va='center'); ax.text(0,-.9,'H',fontsize=18,ha='center',va='center')
        for xx in (-.5,.5):
            for off in (-.07,.07): ax.plot(xx,off,'o',ms=3.2,c='k')
        for off in (-.07,.07): ax.plot(off,-.45,'o',ms=3.2,c='k')
        dots(0,0,D['u'],.4)
    elif key=='N2':
        ax.text(0,0,'N',fontsize=18,ha='center',va='center'); ax.text(1.5,0,'N',fontsize=18,ha='center',va='center')
        for yy in (-.1,0,.1)[:3]:
            for off in (-.04,.04): pass
        for off in (-.08,0,.08): ax.plot(.6+off*0,0,'o',ms=0)
        for yy in (-.14,0,.14):
            ax.plot([.55,.95],[yy,yy],'k',lw=1.2)
        dots(0,0,D['l'],.42); dots(1.5,0,D['r'],.42)
    else:
        ax.text(0,0,'C',fontsize=18,ha='center',va='center'); ax.text(-1.3,0,'O',fontsize=18,ha='center',va='center'); ax.text(1.3,0,'O',fontsize=18,ha='center',va='center')
        for xx in (-.65,.65):
            for yy in (-.07,.07): ax.plot([xx-.2,xx+.2],[yy,yy],'k',lw=1.2)
        dots(-1.3,0,D['u']+D['d'],.42); dots(1.3,0,D['u']+D['d'],.42)
    ax.set_xlim(-2.2,2.6); ax.set_ylim(-1.4,1.0); img=_img(_save(fig,'lw_%d.png'%r.randrange(10**6)),'Elektron formula')
    head="Rasmda molekulaning elektron (Lyuis) formulasi berilgan.\n\n%s\n\n"%img
    ask=r.choice(['form','lone','bond'])
    lone={'HCl':3,'Cl2':6,'H2O':2,'NH3':1,'N2':2,'CO2':4}[key]; bond={'HCl':1,'Cl2':1,'H2O':2,'NH3':3,'N2':3,'CO2':4}[key]
    if ask=='form': q=Q(head+"Molekulaning formulasini aniqlang.",key,_opts(key,list(LW),r),"Elektron formula %s ga mos"%key,"8-sinf (kovalent bog')",'picture')
    elif ask=='lone': q=numq(head+"Molekuladagi bog'lanmagan (taqsimlanmagan) elektron juftlari sonini aniqlang.",lone,[lone+1,max(lone-1,0)+3,lone+2,bond],"Bog'lanmagan juftlar: %d"%lone,"8-sinf (kovalent bog')",0,'picture')
    else: q=numq(head+"Molekuladagi umumiy bog'lovchi elektron juftlari sonini aniqlang.",bond,[bond+1,bond+2,max(bond-1,0)+4,lone],"Bog'lovchi juftlar: %d"%bond,"8-sinf (kovalent bog')",0,'picture')
    return _fin(q)
PICS4=[p_pt,p_orb,p_chain_in,p_chain_org,p_benz,p_model,p_lattice,p_ring,p_fg,p_series,p_decay,p_ind,p_lewis]
def p_iso(r):
    import pic2
    for _ in range(300):
        ms=[]
        for k in range(3):
            n,b,s,kind=pic2.make_mol(r)
            if kind!='alkan': continue
            ms.append((n,b,s,kind))
        if len(ms)<3: continue
        fs=[pic2.mol_formula(*m) for m in ms]; nm=[pic2.name_of(*m) for m in ms]
        pairs=[(i,j) for i in range(3) for j in range(i+1,3) if fs[i]==fs[j] and nm[i]!=nm[j]]
        if len(pairs)==1: break
    else: return p_iso(r)
    fig,axs=plt.subplots(3,1,figsize=(5.4,5.2))
    import pic2 as P
    tag=r.randrange(10**6); 
    for k,(m,ax) in enumerate(zip(ms,axs)):
        n,b,s,kind=m; ax.axis('off')
        pos={};deg={}
        for i in range(n):
            deg[('c',i)]=4-((b[i-1] if i>0 else 0)+(b[i] if i<n-1 else 0))-len(s.get(i+1,[])); pos[('c',i)]=(i*1.7,0)
        side=1
        for p,ls in sorted(s.items()):
            for L in ls:
                pv=('c',p-1)
                for kk in range(L):
                    key=('s',p,kk); pos[key]=((p-1)*1.7,side*1.25*(kk+1)); deg[key]=3 if kk==L-1 else 2
                    ax.plot([pos[pv][0],pos[key][0]],[pos[pv][1],pos[key][1]],'k',lw=1.2,zorder=1); pv=key
            side=-side
        for i in range(n-1): ax.plot([i*1.7,(i+1)*1.7],[0,0],'k',lw=1.2,zorder=1)
        for key,(x,y) in pos.items():
            h=deg[key]; ax.text(x,y,'C' if h==0 else ('CH' if h==1 else 'CH'+('₂' if h==2 else '₃')),ha='center',va='center',fontsize=12,zorder=3,bbox=dict(fc='white',ec='none',pad=1.5))
        ax.set_xlim(-.7,(n-1)*1.7+.7); ax.set_ylim(-3.2,3.2); ax.set_title('ABC'[k],fontsize=15,fontweight='bold',loc='left')
    img=_img(_save(fig,'is_%d.png'%tag),'Izomerlar')
    i,j=pairs[0]; ans='%s va %s'%('ABC'[i],'ABC'[j])
    head="Rasmda uchta uglevodorodning tuzilish formulasi berilgan.\n\n%s\n\n"%img
    allp=['A va B','A va C','B va C','A, B va C']; ws=[x for x in allp if x!=ans]
    q=Q(head+"Qaysi juftlik o'zaro izomerlar hisoblanadi?",ans,ws,"Molekulyar formulalar: "+', '.join('%s – C%dH%d'%('ABC'[k],fs[k][0],fs[k][1]) for k in range(3))+"; tuzilishi har xil → izomerlar %s"%ans,"10-sinf (izomeriya)",'picture')
    return _fin(q)
