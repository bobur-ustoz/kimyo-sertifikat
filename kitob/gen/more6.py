from core import *
from tail import W
NAMES={'CH4':'metan','CH3Cl':'xlormetan','C2H6':'etan','C2H5Cl':'xloretan','C2H5OH':'etanol','C2H4':'etilen','C2H4Br2':'1,2-dibrometan','C2H2':'asetilen','CH3CHO':'sirka aldegid (etanal)','CH3COOH':'sirka kislota','CH3COOC2H5':'etilatsetat','CH3COONa':'natriy atsetat','ClCH2COOH':'xlorsirka kislota','NH2CH2COOH':'glitsin','C6H6':'benzol','C6H5NO2':'nitrobenzol','C6H5NH2':'anilin','C6H5Cl':'xlorbenzol','C6H5OH':'fenol','C6H2Br3OH':'2,4,6-tribromfenol','C6H5CH3':'toluol','C6H5COOH':'benzoy kislota','(–CH2–CH2–)n':'polietilen','C6H12O6':'glyukoza','C12H22O11':'saxaroza','CaC2':'kalsiy karbid','CH3OH':'metanol','HCHO':'formaldegid (metanal)','HCOOH':'chumoli kislota','HCOOCH3':'metilformiat','C2H5ONa':'natriy etilat','C6H5NH3Cl':'fenilammoniy xlorid','C3H8':'propan','C3H7Cl':'xlorpropan','C3H6':'propen','C3H7OH':'propanol','CH3COCH3':'aseton','CH3CH(OH)CH3':'propanol-2','(C6H10O5)n':'kraxmal'}
E=[('CH4','CH3Cl','Cl2, yorug\'lik'),('CH3Cl','C2H6','Na'),('C2H6','C2H5Cl','Cl2, yorug\'lik'),('C2H5Cl','C2H5OH','KOH (suvli)'),('C2H5Cl','C2H4','KOH (spirtli)'),('C2H5OH','C2H4','H2SO4 (kons.), 170 °C'),('C2H4','C2H5OH','H2O, H⁺'),('C2H4','C2H4Br2','Br2'),('C2H4Br2','C2H2','KOH (spirtli)'),('C2H2','CH3CHO','H2O, Hg²⁺'),('CH3CHO','C2H5OH','H2, Ni'),('CH3CHO','CH3COOH','Ag2O, NH3'),('C2H5OH','CH3CHO','CuO, t°'),('CH3COOH','CH3COOC2H5','C2H5OH, H2SO4'),('CH3COOC2H5','CH3COONa','NaOH'),('CH3COONa','CH4','NaOH (suyuqlanma), t°'),('CH3COOH','ClCH2COOH','Cl2, P'),('ClCH2COOH','NH2CH2COOH','NH3'),('C2H2','C6H6','C (aktiv), 600 °C'),('C6H6','C6H5NO2','HNO3, H2SO4'),('C6H5NO2','C6H5NH2','Fe, HCl'),('C6H6','C6H5Cl','Cl2, FeCl3'),('C6H5Cl','C6H5OH','NaOH, t°, p'),('C6H5OH','C6H2Br3OH','Br2 (suvli)'),('C6H6','C6H5CH3','CH3Cl, AlCl3'),('C6H5CH3','C6H5COOH','KMnO4, H⁺'),('C2H4','(–CH2–CH2–)n','polimerlanish'),('C6H12O6','C2H5OH','bijg\'ish'),('C12H22O11','C6H12O6','H2O, H⁺'),('(C6H10O5)n','C6H12O6','H2O, H⁺'),('CaC2','C2H2','H2O'),('CH3OH','HCHO','CuO, t°'),('HCHO','HCOOH','Ag2O, NH3'),('HCOOH','HCOOCH3','CH3OH, H2SO4'),('C2H5OH','C2H5ONa','Na'),('C6H5NH2','C6H5NH3Cl','HCl'),('C3H8','C3H7Cl','Cl2, yorug\'lik'),('C3H7Cl','C3H6','KOH (spirtli)'),('C3H6','C3H7OH','H2O, H⁺'),('CH3CH(OH)CH3','CH3COCH3','CuO, t°'),('C3H6','CH3CH(OH)CH3','H2O, H⁺ (Markovnikov)')]
OUT={}
for a,b,c in E: OUT.setdefault(a,[]).append((b,c))
def chain(r,L):
    for _ in range(500):
        s=r.choice(list(OUT)); path=[s]; rg=[]
        while len(path)<L:
            opts=[(b,c) for b,c in OUT.get(path[-1],[]) if b not in path]
            if not opts: break
            b,c=r.choice(opts); path.append(b); rg.append(c)
        if len(path)==L: return path,rg
    return None
def w42x(r):
    fmt_=r.choice(['chain4','chain3'])
    if fmt_=='chain3':
        p,rg=chain(r,4); L=3
    elif fmt_=='chain4':
        p,rg=chain(r,5); L=4
    else:
        p,rg=chain(r,6); L=5
    hide=[i for i in range(1,len(p)-1)]
    lab={i:'XYZUV'[k] for k,i in enumerate(hide)}
    parts=[]
    for i,c in enumerate(p):
        parts.append(lab.get(i,c))
        if i<len(rg): parts.append('—%s→'%rg[i])
    text="Quyidagi o'zgarishlar zanjirida X, Y, Z%s noma'lum organik moddalar:\n%s"%(', U' if len(hide)>3 else '',' '.join(parts))
    text=text.replace("Z, noma'lum","Z noma'lum")
    n=len(rg)
    bands=["%s → %s : reaksiya tenglamasini yozing; hosil bo'lgan moddani nomlang."%(lab.get(i,p[i]),lab.get(i+1,p[i+1])) for i in range(n)]
    sol=["%s + %s → %s (%s)"%(p[i],rg[i],p[i+1],NAMES.get(p[i+1],p[i+1])) for i in range(n)]
    scores={3:[(12,0),(9,0),(4,0)],4:[(12,0),(9,0),(2,0),(2,0)]}.get(n)
    if n==5: bands=bands; scores=None
    if scores is None:
        # to spec: 3 or 4 bands -> merge extra into 4 bands
        bands=bands[:4]; sol=sol[:4]; scores=[(12,0),(9,0),(2,0),(2,0)]
        text=text  # chain still shows full; last reaction asked in 4th band merged below
        if n==5:
            bands[3]=bands[3]+" Shuningdek keyingi o'zgarish (%s → %s) tenglamasini ham yozing."%(lab.get(3,p[3]),lab.get(4,p[4]) if 4 in lab else p[4])
            sol[3]=sol[3]+"; "+"%s + %s → %s"%(p[4],rg[4],p[5]) if False else sol[3]+"; %s + %s → %s (%s)"%(p[4],rg[4],p[5],NAMES.get(p[5],p[5]))
    w=W("42",text,bands,sol,scores)
    return w
