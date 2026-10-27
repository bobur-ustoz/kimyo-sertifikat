from core import *
import random
GASES={'H2','O2','CO2','SO2','NH3','NO','NO2','Cl2','CH4','C2H2','C2H4','C2H6','C3H8','C4H10','HCl','H2S','CO','N2','CH3Cl','C3H6','HCHO','CH3NH2'}
SKIP={'H2O'}
# ---------- tags: topic -> reactions (inorganic) ----------
INORG={
'S/SO2/H2SO4':['SO3 + H2O -> H2SO4','Cu + 2H2SO4 -> CuSO4 + SO2 + 2H2O','2H2S + 3O2 -> 2SO2 + 2H2O','H2S + CuSO4 -> CuS + H2SO4','Na2SO3 + 2HCl -> 2NaCl + SO2 + H2O','S + O2 -> SO2','Zn + H2SO4 -> ZnSO4 + H2','BaCl2 + H2SO4 -> BaSO4 + 2HCl','4FeS2 + 11O2 -> 2Fe2O3 + 8SO2','2ZnS + 3O2 -> 2ZnO + 2SO2','SO2 + 2NaOH -> Na2SO3 + H2O','FeS + 2HCl -> FeCl2 + H2S'],
'N/NH3/HNO3':['NH4Cl + NaOH -> NaCl + NH3 + H2O','(NH4)2SO4 + 2NaOH -> Na2SO4 + 2NH3 + 2H2O','4NH3 + 5O2 -> 4NO + 6H2O','Cu + 4HNO3 -> Cu(NO3)2 + 2NO2 + 2H2O','3Cu + 8HNO3 -> 3Cu(NO3)2 + 2NO + 4H2O','2NaNO3 -> 2NaNO2 + O2','2Cu(NO3)2 -> 2CuO + 4NO2 + O2','NH3 + HCl -> NH4Cl','NH3 + HNO3 -> NH4NO3','N2 + 3H2 -> 2NH3','2NO + O2 -> 2NO2','Ca(OH)2 + 2NH4Cl -> CaCl2 + 2NH3 + 2H2O','2AgNO3 -> 2Ag + 2NO2 + O2'],
'P/C/Si':['4P + 5O2 -> 2P2O5','P2O5 + 3H2O -> 2H3PO4','Ca3(PO4)2 + 3H2SO4 -> 3CaSO4 + 2H3PO4','SiO2 + 2NaOH -> Na2SiO3 + H2O','SiO2 + 2C -> Si + 2CO','Na2SiO3 + 2HCl -> 2NaCl + H2SiO3','CaCO3 -> CaO + CO2','CO2 + Ca(OH)2 -> CaCO3 + H2O','2Mg + CO2 -> 2MgO + C','2CO + O2 -> 2CO2','Ca3(PO4)2 + 5C + 3SiO2 -> 3CaSiO3 + 2P + 5CO','H3PO4 + 3NaOH -> Na3PO4 + 3H2O'],
'galogenlar':['2NaBr + Cl2 -> 2NaCl + Br2','2KI + Cl2 -> 2KCl + I2','MnO2 + 4HCl -> MnCl2 + Cl2 + 2H2O','2KMnO4 + 16HCl -> 2KCl + 2MnCl2 + 5Cl2 + 8H2O','NaCl + AgNO3 -> AgCl + NaNO3','2NaCl + H2SO4 -> Na2SO4 + 2HCl','Cl2 + 2NaOH -> NaCl + NaClO + H2O','H2 + Cl2 -> 2HCl','NaBr + AgNO3 -> AgBr + NaNO3','2KClO3 -> 2KCl + 3O2','CaF2 + H2SO4 -> CaSO4 + 2HF','2Fe + 3Cl2 -> 2FeCl3'],
'IA metallar':['2Na + 2H2O -> 2NaOH + H2','2K + 2H2O -> 2KOH + H2','2NaHCO3 -> Na2CO3 + CO2 + H2O','Na2CO3 + 2HCl -> 2NaCl + CO2 + H2O','2Na + Cl2 -> 2NaCl','2Na2O2 + 2CO2 -> 2Na2CO3 + O2','4Li + O2 -> 2Li2O','Na2O + H2O -> 2NaOH','2NaOH + CO2 -> Na2CO3 + H2O','NaOH + HCl -> NaCl + H2O','2KOH + H2SO4 -> K2SO4 + 2H2O','2Li + 2H2O -> 2LiOH + H2'],
'IIA/IIIA metallar (Ca,Mg,Al)':['Ca + 2H2O -> Ca(OH)2 + H2','Al2O3 + 6HCl -> 2AlCl3 + 3H2O','Al(OH)3 + 3HCl -> AlCl3 + 3H2O','MgO + 2HCl -> MgCl2 + H2O','Mg + 2HCl -> MgCl2 + H2','CaO + H2O -> Ca(OH)2','2Mg + O2 -> 2MgO','4Al + 3O2 -> 2Al2O3','Al4C3 + 12H2O -> 4Al(OH)3 + 3CH4','Mg3N2 + 6H2O -> 3Mg(OH)2 + 2NH3','2Al + Fe2O3 -> Al2O3 + 2Fe','2Al + 6HCl -> 2AlCl3 + 3H2','CaCO3 -> CaO + CO2','Mg(OH)2 + 2HCl -> MgCl2 + 2H2O'],
'd-metallar (Fe,Cu,Zn,Cr)':['Fe + CuSO4 -> FeSO4 + Cu','Zn + CuSO4 -> ZnSO4 + Cu','Fe2O3 + 3CO -> 2Fe + 3CO2','Fe2O3 + 6HCl -> 2FeCl3 + 3H2O','FeCl3 + 3NaOH -> Fe(OH)3 + 3NaCl','2Fe(OH)3 -> Fe2O3 + 3H2O','CuO + H2 -> Cu + H2O','CuO + H2SO4 -> CuSO4 + H2O','CuSO4 + 2NaOH -> Cu(OH)2 + Na2SO4','Cu(OH)2 -> CuO + H2O','ZnO + 2HCl -> ZnCl2 + H2O','Zn(OH)2 + 2NaOH -> Na2ZnO2 + 2H2O','4Fe(OH)2 + O2 + 2H2O -> 4Fe(OH)3','2Cu + O2 -> 2CuO','3Fe + 2O2 -> Fe3O4','Fe + 2HCl -> FeCl2 + H2','Zn + 2HCl -> ZnCl2 + H2'],
'suv qattiqligi':['Ca(HCO3)2 -> CaCO3 + CO2 + H2O','Ca(HCO3)2 + Ca(OH)2 -> 2CaCO3 + 2H2O','Mg(HCO3)2 + 2Ca(OH)2 -> Mg(OH)2 + 2CaCO3 + 2H2O','CaSO4 + Na2CO3 -> CaCO3 + Na2SO4','MgCl2 + Na2CO3 -> MgCO3 + 2NaCl','3Ca(HCO3)2 + 2Na3PO4 -> Ca3(PO4)2 + 6NaHCO3','CaCl2 + Na2CO3 -> CaCO3 + 2NaCl','Mg(HCO3)2 -> MgCO3 + CO2 + H2O'],
'oksid/asos/kislota/tuz':['CaO + CO2 -> CaCO3','Na2O + H2O -> 2NaOH','SO3 + 2KOH -> K2SO4 + H2O','HCl + KOH -> KCl + H2O','H2SO4 + 2NaOH -> Na2SO4 + 2H2O','Ba(OH)2 + H2SO4 -> BaSO4 + 2H2O','CuO + 2HNO3 -> Cu(NO3)2 + H2O','Fe(OH)3 + 3HNO3 -> Fe(NO3)3 + 3H2O','N2O5 + H2O -> 2HNO3','P2O5 + 6KOH -> 2K3PO4 + 3H2O','CO2 + Ba(OH)2 -> BaCO3 + H2O','Al2O3 + 3H2SO4 -> Al2(SO4)3 + 3H2O'],
'genetik zanjir/reaksiya turlari':['Zn + 2HCl -> ZnCl2 + H2','CaCO3 -> CaO + CO2','2H2O2 -> 2H2O + O2','AgNO3 + NaCl -> AgCl + NaNO3','2KClO3 -> 2KCl + 3O2','Fe + CuCl2 -> FeCl2 + Cu','2H2O -> 2H2 + O2','BaCl2 + Na2SO4 -> BaSO4 + 2NaCl','2Al + 3CuCl2 -> 2AlCl3 + 3Cu','Na2CO3 + CaCl2 -> CaCO3 + 2NaCl'],
"mineral o'g'itlar/nodir gazlar":['2NH3 + H2SO4 -> (NH4)2SO4','NH3 + H3PO4 -> NH4H2PO4','2NH3 + CO2 -> CO(NH2)2 + H2O','Ca3(PO4)2 + 4H3PO4 -> 3Ca(H2PO4)2','CO(NH2)2 + 2H2O -> (NH4)2CO3','Ca3(PO4)2 + 2H2SO4 -> 2CaSO4 + Ca(H2PO4)2','2KCl + H2SO4 -> K2SO4 + 2HCl','KOH + HNO3 -> KNO3 + H2O'],
'tuzlarning termik parchalanishi':['2NaNO3 -> 2NaNO2 + O2','2Cu(NO3)2 -> 2CuO + 4NO2 + O2','NH4Cl -> NH3 + HCl','2AgNO3 -> 2Ag + 2NO2 + O2','CaCO3 -> CaO + CO2','2Mg(NO3)2 -> 2MgO + 4NO2 + O2','(NH4)2CO3 -> 2NH3 + CO2 + H2O','2KNO3 -> 2KNO2 + O2'],
}
ORGR={
'alkan':['CH4 + Cl2 -> CH3Cl + HCl','C3H8 + 5O2 -> 3CO2 + 4H2O','2C4H10 + 13O2 -> 8CO2 + 10H2O','2CH3Cl + 2Na -> C2H6 + 2NaCl','CH3COONa + NaOH -> CH4 + Na2CO3','C2H6 + Cl2 -> C2H5Cl + HCl','CH4 + 2O2 -> CO2 + 2H2O','2C2H6 + 7O2 -> 4CO2 + 6H2O'],
'alken':['C2H4 + Br2 -> C2H4Br2','C2H4 + H2O -> C2H5OH','C2H4 + 3O2 -> 2CO2 + 2H2O','C3H6 + HCl -> C3H7Cl','C2H4 + H2 -> C2H6','C3H6 + Br2 -> C3H6Br2','C2H5OH -> C2H4 + H2O','C2H2 + 2Br2 -> C2H2Br4'],
'aren':['C6H6 + Br2 -> C6H5Br + HBr','C6H6 + HNO3 -> C6H5NO2 + H2O','2C6H6 + 15O2 -> 12CO2 + 6H2O','C6H6 + 3H2 -> C6H12','CaC2 + 2H2O -> C2H2 + Ca(OH)2','C2H2 + H2O -> CH3CHO','C6H5CH3 + HNO3 -> C6H4CH3NO2 + H2O','3C2H2 -> C6H6'],
'spirt':['2C2H5OH + 2Na -> 2C2H5ONa + H2','2CH3OH + 2Na -> 2CH3ONa + H2','C2H5OH + 3O2 -> 2CO2 + 3H2O','C6H5OH + NaOH -> C6H5ONa + H2O','C6H5OH + 3Br2 -> C6H2Br3OH + 3HBr','C2H5Cl + KOH -> C2H5OH + KCl','2C6H5OH + 2Na -> 2C6H5ONa + H2','C6H12O6 -> 2C2H5OH + 2CO2'],
'ald':['CH3CHO + Ag2O -> CH3COOH + 2Ag','CH3CHO + 2Cu(OH)2 -> CH3COOH + Cu2O + 2H2O','CH3CHO + H2 -> C2H5OH','2CH3CHO + 5O2 -> 4CO2 + 4H2O','HCHO + Ag2O -> HCOOH + 2Ag','C2H2 + H2O -> CH3CHO'],
'kis':['CH3COOH + NaHCO3 -> CH3COONa + CO2 + H2O','2CH3COOH + 2Na -> 2CH3COONa + H2','CH3COOH + NaOH -> CH3COONa + H2O','2CH3COOH + Zn -> (CH3COO)2Zn + H2','2HCOOH + Mg -> (HCOO)2Mg + H2','CH3COOH + C2H5OH -> CH3COOC2H5 + H2O','2CH3COOH + CaCO3 -> (CH3COO)2Ca + CO2 + H2O','C2H5COOH + KOH -> C2H5COOK + H2O'],
'efir':['CH3COOC2H5 + NaOH -> CH3COONa + C2H5OH','CH3COOH + C2H5OH -> CH3COOC2H5 + H2O','HCOOCH3 + NaOH -> HCOONa + CH3OH','CH3COOCH3 + NaOH -> CH3COONa + CH3OH','HCOOH + CH3OH -> HCOOCH3 + H2O','CH3COOC2H5 + H2O -> CH3COOH + C2H5OH'],
'ugl':['C6H12O6 -> 2C2H5OH + 2CO2','C12H22O11 + H2O -> 2C6H12O6','C6H12O6 + Ag2O -> C6H12O7 + 2Ag','6CO2 + 6H2O -> C6H12O6 + 6O2','C6H12O6 + 6O2 -> 6CO2 + 6H2O','C6H12O6 -> 2C3H6O3'],
'amin':['C6H5NH2 + HCl -> C6H5NH3Cl','CH3NH2 + HCl -> CH3NH3Cl','NH2CH2COOH + NaOH -> NH2CH2COONa + H2O','NH2CH2COOH + HCl -> ClNH3CH2COOH','C6H5NO2 + 3H2 -> C6H5NH2 + 2H2O','NH2CH2COOH + C2H5OH -> NH2CH2COOC2H5 + H2O','4CH3NH2 + 9O2 -> 4CO2 + 10H2O + 2N2'],
'pol':['nCH2=CH2 -> (-CH2-CH2-)n'],
}
ORGR['pol']=['C2H4 + H2 -> C2H6','C2H2 + HCl -> C2H3Cl','C2H4 + HCl -> C2H5Cl','C3H6 + H2 -> C3H8','C2H2 + H2 -> C2H4','C2H4 + Cl2 -> C2H4Cl2']
def _mols(side):
    out=[]
    for s in side.split(' + '):
        s=s.strip(); import re
        m=re.match(r'(\d*)(.*)',s); out.append(m.group(2))
    return out
def rx_engine(bank,src):
    def f(r):
        eq=r.choice(bank); co=dict(balance(eq)); L,R=eq.split('->'); lft=_mols(L); rgt=_mols(R)
        xs=[s for s in lft if s not in SKIP]
        if not xs: return f(r)
        x=r.choice(xs)
        cand=[s for s in lft+rgt if s!=x and s not in SKIP]
        if not cand: return f(r)
        y=r.choice(rgt if (rgt and r.random()<0.75 and [s for s in rgt if s not in SKIP]) else cand)
        if y in SKIP or y==x: y=r.choice(cand)
        gx=x in GASES and r.random()<0.6; gy=y in GASES and r.random()<0.6
        base=r.choice([0.1,0.2,0.25,0.4,0.5,1,2]); n=base*co[x]/co[x]
        mode=r.choice(['pure','purity','yield','plain'])
        if mode=='purity' and x in GASES|{'HNO3','HCl','H2SO4','H3PO4','CH3COOH','C2H5OH','CH3OH','CH3CHO','HCOOH','C6H6','C6H5NH2','CH3NH2','C6H5CH3','Br2','H2O2','C2H5Cl','HCHO'}: mode='plain'
        if mode=='yield' and y not in rgt: mode='plain'
        p=r.choice([80,75,90,60,50]); eta=r.choice([80,75,90,60,50])
        if gx: given='%s l (n.sh.) %s'%(fmt(n*22.4,2),x); nx=n
        else:
            mx=n*M(x)
            if abs(mx*100-round(mx*100))>1e-6: return f(r)
            if mode=='purity':
                ok=[]
                for pp in (80,75,60,90,50,40,20,25):
                    mi=mx*100/pp
                    if abs(mi*100-round(mi*100))<1e-6 and mi<400: ok.append((pp,mi))
                if not ok: return f(r)
                p,mimp=r.choice(ok); nx=n
                given="tarkibida %d %% aralashma bo'lgan %s g namuna (asosiy modda %s)"%(100-p,fmt(mimp,2),x)
            else: given='%s g %s'%(fmt(mx,2),x); nx=n
        ny=nx*co[y]/co[x]*(eta/100 if mode=='yield' else 1)
        if gy: asked="%s hajmini (l, n.sh.)"%y; ans=ny*22.4; unit='l'
        elif r.random()<0.25: asked="%s miqdorini (mol)"%y; ans=ny; unit='mol'
        else: asked="%s massasini (g)"%y; ans=ny*M(y); unit='g'
        if abs(ans*100-round(ans*100))>1e-6 or ans<=0: return f(r)
        fy=ans/ny if ny else 1
        eqs=eq.replace('->','→')
        yl=' (unum %d %%)'%eta if mode=='yield' else ''
        T=r.choice(["%s reaksiyasida %s ishtirok etdi%s. %s toping.","Reaksiya tenglamasi: %s. Reaksiyaga %s kirishdi%s. %s hisoblang.","%s jarayoni uchun %s olingan%s. %s aniqlang."])
        txt=T%(eqs,given,yl,asked)
        W=[nx*co[x]/co[y]*(fy) if unit!='mol' else nx*co[x]/co[y], ans*2, ans/2, nx*fy]
        if ans>0: pass
        sol="n(%s) = %s mol; tenglamaga ko'ra n(%s) = n(%s)·%d/%d = %s mol%s"%(x,fmt(nx,3),y,x,co[y],co[x],fmt(nx*co[y]/co[x],3),(" ; unum %d %% → %s mol"%(eta,fmt(ny,3)) if mode=='yield' else ''))
        q=numq(txt,ans,W,sol+" → javob: %s %s"%(fmt(ans,2),unit),src,2)
        q.tag='rx'
        return q
    f.__name__='rx_'+src[:6]
    return f
def build_inorg(topic): return rx_engine(INORG[topic],'9-sinf; Tirkashev (%s, hisob)'%topic)
def build_org(kind): return rx_engine(ORGR[kind],'10-sinf (%s, hisob)'%kind)
# ---------- 33-35 stories ----------
def _o(r,vals):
    from tail import _opts
    return _opts(r,vals,None)
MET=[('Zn',65,1,'ZnCl2','ZnSO4',1),('Mg',24,1,'MgCl2','MgSO4',1),('Fe',56,1,'FeCl2','FeSO4',1),('Al',27,1.5,'AlCl3','Al2(SO4)3',0.5)]
def st_metals(r):
    for _ in range(50):
        pair=r.sample(MET,2); inert=r.random()<0.3
        if inert: A=('Cu',64,0,'','',0); B=pair[0]
        else: A,B=pair
        nA=r.choice([0.1,0.2,0.3,0.15,0.05]); nB=r.choice([0.1,0.2,0.3,0.15,0.05])
        if A[1]*nA+B[1]*nB!=round(A[1]*nA+B[1]*nB,2): continue
        break
    m=A[1]*nA+B[1]*nB; H2=A[2]*nA+B[2]*nB; acid=r.choice(['HCl','H2SO4']); 
    hv=H2*22.4
    mAcid=(2*H2)*36.5 if acid=='HCl' else H2*98
    salts=(nA*A[1+0+0] if False else 0)
    if acid=='HCl': msalt=nB*M(B[3])+(nA*M(A[3]) if A[3] else 0); sn=B[3]
    else: msalt=nB*B[5]*M(B[4])+(nA*A[5]*M(A[4]) if A[4] else 0); sn=B[4]
    nm={'Zn':'rux','Mg':'magniy','Fe':'temir','Al':'alyuminiy','Cu':'mis'}
    names=nm[A[0]]+' va '+nm[B[0]]
    note=" (mis kislota bilan reaksiyaga kirishmaydi)" if inert else ""
    txt="%s (%s va %s) dan iborat %s g qotishma mo'l %s eritmasida eritilganda %s l (n.sh.) gaz ajraldi%s."%(names.capitalize(),A[0],B[0],fmt(m,2),acid,fmt(hv,2),note)
    qs=["Qotishmadagi %s massasini (g) aniqlang."%A[0],"Reaksiya uchun sarflangan %s massasini (g) aniqlang."%acid,"Eritmadagi tuzlarning umumiy massasini (g) aniqlang."]
    vals=[nA*A[1],mAcid,msalt]
    sol=["%s va %s uchun m = %s g, V(H2) = %s l → n(%s) = %s mol, m = %s g"%(A[0],B[0],fmt(m,2),fmt(hv,2),A[0],fmt(nA),fmt(nA*A[1],2)),"n(%s) = %s mol → m = %s g"%(acid,fmt(2*H2 if acid=='HCl' else H2,3),fmt(mAcid,2)),"Tuzlar: %s g"%fmt(msalt,2)]
    opts,key=_o(r,vals)
    return txt,qs,vals,sol,"9-sinf (metallar), Tashev (qotishmalar)"
CARB=[('CaCO3',100,'CaCl2',2),('MgCO3',84,'MgCl2',2),('Na2CO3',106,'NaCl',2),('K2CO3',138,'KCl',2),('BaCO3',197,'BaCl2',2),('NaHCO3',84,'NaCl',1),('KHCO3',100,'KCl',1)]
def st_carb(r):
    for _ in range(80):
        A,B=r.sample(CARB,2); nA=r.choice([0.1,0.2,0.3,0.15]); nB=r.choice([0.1,0.2,0.3,0.05]);
        if abs(A[1]*nA+B[1]*nB-round(A[1]*nA+B[1]*nB,2))<1e-9: break
    m=A[1]*nA+B[1]*nB; co2=nA+nB; hcl=A[3]*nA+B[3]*nB
    t3=r.choice(['ppt','salt'])
    if t3=='ppt':
        q3="Ajralgan gaz mo'l Ca(OH)2 eritmasidan o'tkazilganda hosil bo'lgan cho'kma massasini (g) aniqlang."; v3=co2*100; s3="CO2 + Ca(OH)2 → CaCO3: %s mol · 100 = %s g"%(fmt(co2,3),fmt(v3,2))
    else:
        v3=nA*(M(A[2])*(1 if A[3]==2 else 1)*(1 if A[2]!='NaCl' else 1))
        # salt masses: carbonate-> chloride coefficient 1 (BaCl2 etc) ; bicarbonate -> 1 chloride unit
        def salt(c,n): return n*M(c[2]) if True else 0
        v3=salt(A,nA)+salt(B,nB); q3="Reaksiyadan so'ng eritmadagi tuzlar umumiy massasini (g) aniqlang."; s3="Xloridlar: %s g"%fmt(v3,2)
    txt="%s va %s dan iborat %s g aralashma mo'l xlorid kislota bilan to'liq reaksiyaga kirishdi."%(A[0],B[0],fmt(m,2))
    qs=["Ajralgan gaz hajmini (l, n.sh.) aniqlang.","Aralashmani to'liq eritish uchun sarflangan HCl massasini (g) aniqlang (M(HCl) = 36,5 g/mol).",q3]
    vals=[co2*22.4,hcl*36.5,v3]
    sol=["n(CO2) = %s + %s = %s mol → %s l"%(fmt(nA),fmt(nB),fmt(co2),fmt(co2*22.4,2)),"n(HCl) = %s mol → %s g"%(fmt(hcl),fmt(hcl*36.5,2)),s3]
    return txt,qs,vals,sol,"9-sinf (uglerod, karbonatlar), Tashev"
HAL=[('NaCl','AgCl',143.5,'NaNO3'),('NaBr','AgBr',188,'NaNO3'),('KCl','AgCl',143.5,'KNO3'),('KBr','AgBr',188,'KNO3'),('KI','AgI',235,'KNO3'),('NaI','AgI',235,'NaNO3')]
def st_halide(r):
    for _ in range(80):
        A,B=r.sample(HAL,2)
        if A[1]==B[1]: continue
        nA=r.choice([0.1,0.2,0.05,0.15]); nB=r.choice([0.1,0.2,0.05,0.15])
        m=nA*M(A[0])+nB*M(B[0])
        if abs(m-round(m,2))<1e-9: break
    P=nA*A[2]+nB*B[2]
    txt="%s va %s dan iborat %s g aralashma suvda eritilib, mo'l AgNO3 eritmasi qo'shildi; hosil bo'lgan cho'kmalarning umumiy massasi %s g."%(A[0],B[0],fmt(m,2),fmt(P,2))
    qs=["Aralashmadagi %s massasini (g) aniqlang."%A[0],"Sarflangan AgNO3 massasini (g) aniqlang (M(AgNO3) = 170 g/mol).","Eritmada hosil bo'lgan nitratlarning umumiy massasini (g) aniqlang."]
    nit=nA*M(A[3])+nB*M(B[3])
    vals=[nA*M(A[0]),(nA+nB)*170,nit]
    sol=["x·M(%s) + y·M(%s) = %s; x·%s + y·%s = %s → x = %s mol"%(A[0],B[0],fmt(m,2),fmt(A[2]),fmt(B[2]),fmt(P,2),fmt(nA)),"n(AgNO3) = %s mol → %s g"%(fmt(nA+nB),fmt((nA+nB)*170,2)),"Nitratlar: %s g"%fmt(nit,2)]
    return txt,qs,vals,sol,"9-sinf (galogenidlar), Tashev"
def st_oxides(r):
    for _ in range(60):
        x=r.choice([0.1,0.2,0.05,0.15]); y=r.choice([0.1,0.05,0.2])
        break
    m=80*x+160*y; res=64*x+112*y; h2=x+3*y
    red=r.choice(['H2','CO'])
    txt="CuO va Fe2O3 dan iborat %s g aralashma qizdirilib, %s oqimida to'liq qaytarildi; qoldiq (metallar) massasi %s g."%(fmt(m,2),red,fmt(res,2))
    qs=["Aralashmadagi CuO massasini (g) aniqlang.","Qaytarish uchun sarflangan %s hajmini (l, n.sh.) aniqlang."%red,"Qaytarish natijasida hosil bo'lgan %s massasini (g) aniqlang."%('suv' if red=='H2' else 'CO2')]
    prod=h2*(18 if red=='H2' else 44)
    vals=[80*x,h2*22.4,prod]
    sol=["80x + 160y = %s; 64x + 112y = %s → x = %s mol; m(CuO) = %s g"%(fmt(m,2),fmt(res,2),fmt(x),fmt(80*x,2)),"n(%s) = x + 3y = %s mol → %s l"%(red,fmt(h2,3),fmt(h2*22.4,2)),"n(%s) = %s mol → %s g"%('H2O' if red=='H2' else 'CO2',fmt(h2,3),fmt(prod,2))]
    return txt,qs,vals,sol,"9-sinf (metallar oksidlari), Tashev"
def st_alal(r):
    a=r.choice([0.1,0.2,0.3]); b=r.choice([0.05,0.1,0.2])
    m=27*a+102*b; V=1.5*a*22.4; hcl=3*a+6*b; sl=(a+2*b)*133.5
    txt="Al va Al2O3 dan iborat %s g aralashma mo'l xlorid kislotada eritilganda %s l (n.sh.) vodorod ajraldi."%(fmt(m,2),fmt(V,2))
    qs=["Aralashmadagi Al2O3 massasini (g) aniqlang.","Aralashmani eritish uchun sarflangan HCl massasini (g) aniqlang (M(HCl) = 36,5 g/mol).","Hosil bo'lgan AlCl3 massasini (g) aniqlang."]
    vals=[102*b,hcl*36.5,sl]
    sol=["n(H2) = %s → n(Al) = %s mol; m(Al2O3) = %s − %s = %s g"%(fmt(V/22.4,3),fmt(a),fmt(m,2),fmt(27*a,2),fmt(102*b,2)),"n(HCl) = 3·%s + 6·%s = %s mol → %s g"%(fmt(a),fmt(b),fmt(hcl),fmt(hcl*36.5,2)),"n(AlCl3) = %s + 2·%s = %s mol → %s g"%(fmt(a),fmt(b),fmt(a+2*b),fmt(sl,2))]
    return txt,qs,vals,sol,"9-sinf (alyuminiy va uning birikmalari)"
def st_acidalc(r):
    a=r.choice([0.1,0.2,0.3]); b=r.choice([0.1,0.2,0.3])
    m=60*a+46*b; co2=a/1.0*22.4; h2=(a+b)/2*22.4
    txt="Sirka kislota va etanoldan iborat %s g aralashmaga mo'l NaHCO3 eritmasi qo'shilganda %s l (n.sh.) gaz ajraldi. Xuddi shunday massadagi aralashma natriy bilan ta'sirlashganda esa %s l (n.sh.) vodorod ajraldi."%(fmt(m,2),fmt(co2,2),fmt(h2,2))
    qs=["Aralashmadagi sirka kislota massasini (g) aniqlang.","Aralashmadagi etanol massasini (g) aniqlang.","Aralashma to'liq neytrallanganda (faqat kislota) hosil bo'lgan natriy atsetat massasini (g) aniqlang."]
    vals=[60*a,46*b,82*a]
    sol=["CH3COOH + NaHCO3: n(CO2) = n(kislota) = %s mol → %s g"%(fmt(a),fmt(60*a,2)),"m(etanol) = %s − %s = %s g"%(fmt(m,2),fmt(60*a,2),fmt(46*b,2)),"CH3COONa: %s mol · 82 = %s g"%(fmt(a),fmt(82*a,2))]
    return txt,qs,vals,sol,"10-sinf (spirtlar, karbon kislotalar)"
GP=[('C2H6',30,'C2H4',1,'etan','eten'),('CH4',16,'C2H4',1,'metan','eten'),('C3H8',44,'C2H4',1,'propan','eten'),('CH4',16,'C3H6',1,'metan','propen'),('C2H6',30,'C2H2',2,'etan','etin'),('CH4',16,'C2H2',2,'metan','etin')]
def st_gasbr(r):
    A,mA,B,k,nA_,nB_=r.choice(GP); vA=r.choice([2.24,4.48,6.72]); vB=r.choice([1.12,2.24,3.36]); n=vA/22.4; nb=vB/22.4
    mBr=nb*k*160; tot=vA+vB
    comb={'C2H6':3.5,'CH4':2,'C3H8':5,'C2H4':3,'C3H6':4.5,'C2H2':2.5}
    o2=(n*comb[A]+nb*comb[B])*22.4
    phi=vB/tot*100
    txt="%s (%s) va %s (%s) dan iborat %s l (n.sh.) aralashma bromli suvdan o'tkazilganda %s g brom yutildi."%(nA_.capitalize(),A,nB_,B,fmt(tot,2),fmt(mBr,2))
    qs=["Aralashmadagi %s (%s) hajmini (l, n.sh.) aniqlang."%(nB_,B),"Aralashmadagi %s (%s) hajmiy ulushini (%%) aniqlang."%(nB_,B),"Aralashmani to'liq yoqish uchun zarur kislorod hajmini (l, n.sh.) aniqlang."]
    vals=[vB,phi,o2]
    sol=["n(Br2) = %s mol; n(%s) = %s mol → %s l"%(fmt(mBr/160,3),nB_,fmt(nb,3),fmt(vB,2)),"φ = %s/%s = %s %%"%(fmt(vB,2),fmt(tot,2),fmt(phi,2)),"O2 sarfi %s mol → %s l"%(fmt(o2/22.4,3),fmt(o2,2))]
    return txt,qs,vals,sol,"10-sinf (alkenlar, yonish), Tashev"
STORIES2=[st_metals,st_carb,st_halide,st_oxides,st_alal,st_acidalc,st_gasbr]
# ---------- ikki bosqichli (qiyinroq) organik hisob
def _split(eq):
    L,R=eq.split('->'); return _mols(L),_mols(R)
def rx2_engine(kind,src):
    own=ORGR[kind]; allr=[e for k in ORGR for e in ORGR[k]]
    pairs=[]
    for e1 in own:
        l1,r1=_split(e1)
        for e2 in allr:
            if e2==e1: continue
            l2,r2=_split(e2)
            for p in r1:
                if l2[0]==p and 'C' in p and p not in ('CO2','CO') and p!=l1[0] and p not in GASES-{'C2H4','C2H2','CH4','C3H6'} or (l2[0]==p and p in ('C2H4','C2H2','CH4','C3H6','C2H6') and p!=l1[0]):
                    pairs.append((e1,e2,p))
    def f(r):
        e1,e2,p=r.choice(pairs); c1=dict(balance(e1)); c2=dict(balance(e2)); l1,r1=_split(e1); l2,r2=_split(e2)
        a=l1[0]; ys=[x for x in r2 if x not in SKIP and x!=p and 'C' in x and x not in ('CO2','CO') and x!=a and x not in l1]
        if not ys: return f(r)
        b=r.choice(ys); n=r.choice([0.1,0.2,0.25,0.5,1]); e1y=r.choice([80,75,90,60,50]); e2y=r.choice([80,75,90,50])
        mA=n*M(a)
        if abs(mA*100-round(mA*100))>1e-6: return f(r)
        n1=n*c1[p]/c1[a]*e1y/100; n2=n1*c2[b]/c2[p]*e2y/100
        gas=b in GASES
        ans=n2*(22.4 if gas else M(b)); unit='l (n.sh.)' if gas else 'g'
        if abs(ans*100-round(ans*100))>1e-6 or ans<=0.3: return f(r)
        t="%s g %s dan quyidagi ikki bosqichda %s olinadi:\n1) %s (unum %d %%);\n2) %s (unum %d %%).\nOxirgi mahsulot %s ning %s toping."%(fmt(mA,2),a,b,e1.replace('->','→'),e1y,e2.replace('->','→'),e2y,b,'hajmini (l, n.sh.)' if gas else 'massasini (g)')
        wr=[ans/(e1y/100),ans/(e2y/100),n*c1[p]/c1[a]*c2[b]/c2[p]*(22.4 if gas else M(b)),ans*2]
        return numq(t,ans,wr,"n(%s) = %s mol; n(%s) = %s·%d/%d·%s = %s mol; n(%s) = %s·%d/%d·%s = %s mol → %s %s"%(a,fmt(n),p,fmt(n),c1[p],c1[a],fmt(e1y/100,2),fmt(n1,3),b,fmt(n1,3),c2[b],c2[p],fmt(e2y/100,2),fmt(n2,3),fmt(ans,2),unit),src,2)
    f.__name__='rx2_'+kind
    return f if pairs else None
