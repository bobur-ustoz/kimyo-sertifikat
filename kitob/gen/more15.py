import random, math, itertools
from fractions import Fraction
from core import *
from tail import W
from more3 import SC41, f2
# Samarqand darajasi: shartlar BILVOSITA beriladi (nisbat, farq, marta, protonlar yig'indisi, noma'lum element). Mazmun o'zimizniki.
V=22.4; F=96500
AM.setdefault('Sr',88)
ZN={'Pb':82,'S':16,'Cu':29,'Ag':47,'H':1,'C':6,'N':7,'O':8,'Na':11,'Mg':12,'Al':13,'Cl':17,'K':19,'Ca':20,'Fe':26,'Zn':30,'Sr':38,'Ba':56,'Br':35}
def _z(f):
    return sum(ZN[e]*c for e,c in parse(f).items())
def _fm(x,nd=2): return fmt(x,nd)

AM.setdefault('W',184); AM.setdefault('Pb',207)
def _cnt(f): return parse(f)
# oila: subs=[(formula, o'lchov koeffitsiyenti)], meas = (matn shabloni, birlik, koef) ; 'T' – umumiy massa ikkinchi shart sifatida
FAM={
 'carb':dict(subs=[('CaCO3',1),('MgCO3',1),('BaCO3',1),('Na2CO3',1),('K2CO3',1),('SrCO3',1)],meas="Shu aralashma mo'l xlorid kislota bilan ta'sirlashganda %s l (n.sh.) gaz ajraldi",coef=22.4,nd=2,src="8-9-sinf (karbonatlar; kislotalar bilan reaksiya)",extra=lambda a,b,k1,k2:('hcl',"Reaksiyaga sarflangan HCl miqdorini (mol) hisoblang.",2*(a+b))),
 'met':dict(subs=[('Mg',1),('Al',1.5),('Zn',1),('Fe',1)],meas="Shu aralashma mo'l suyultirilgan sulfat kislota bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi",coef=22.4,nd=2,src="9-sinf (metallarning kislotalar bilan reaksiyasi)",extra=lambda a,b,k1,k2:('h2',"Ajralgan vodorod miqdorini (mol) hisoblang.",k1*a+k2*b)),
 'alc':dict(subs=[('CH3OH',0.5),('C2H5OH',0.5),('C3H7OH',0.5),('C4H9OH',0.5)],meas="Shu aralashma natriy bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi",coef=22.4,nd=2,src="10-sinf (spirtlarning natriy bilan reaksiyasi)",extra=None),
 'alk':dict(subs=[('C2H4',1),('C3H6',1),('C4H8',1),('C5H10',1)],meas="Shu aralashma mo'l brom suvi bilan to'liq reaksiyaga kirishganda %s g brom sarflandi",coef=160,nd=1,src="10-sinf (alkenlarning brom bilan birikishi)",extra=None),
 'hc':dict(subs=[('CH4',2),('C2H6',3.5),('C2H4',3),('C2H2',2.5),('C3H8',5)],meas="Shu aralashmani yondirish uchun %s l (n.sh.) kislorod sarflandi",coef=22.4,nd=2,src="10-sinf (uglevodorodlarning yonishi)",extra=None),
 'gas':dict(subs=[('H2',1),('CH4',1),('CO',1),('CO2',1),('N2',1),('NH3',1),('C2H6',1),('O2',1)],meas="Aralashmaning hajmi %s l (n.sh.)",coef=22.4,nd=2,src="8-9-sinf (gaz aralashmalari; Avogadro qonuni)",extra=None),
 'oxr':dict(subs=[('CuO',1),('Fe2O3',3),('PbO',1),('Fe3O4',4)],meas="Shu aralashma vodorod bilan to'liq qaytarilganda %s g suv hosil bo'ldi",coef=18,nd=1,src="9-sinf (metall oksidlarining vodorod bilan qaytarilishi)",extra=None),
 'sulf':dict(subs=[('K2SO4',1),('Na2SO4',1),('MgSO4',1),('Al2(SO4)3',3),('Fe2(SO4)3',3)],meas="Shu aralashma suvda eritilib, mo'l BaCl2 qo'shilganda %s g cho'kma tushdi",coef=233,nd=2,src="9-sinf (sulfatlar; sifat reaksiyasi)",extra=None),
 'chlo':dict(subs=[('NaCl',1),('KCl',1),('MgCl2',2),('CaCl2',2),('AlCl3',3),('FeCl3',3)],meas="Shu aralashma suvda eritilib, mo'l AgNO3 qo'shilganda %s g cho'kma tushdi",coef=143.5,nd=2,src="9-sinf (xloridlar; sifat reaksiyasi)",extra=None),
}
ION={'carb':{'CaCO3':2,'MgCO3':2,'BaCO3':2,'SrCO3':2,'Na2CO3':3,'K2CO3':3},'sulf':{'K2SO4':3,'Na2SO4':3,'MgSO4':2,'Al2(SO4)3':5,'Fe2(SO4)3':5},'chlo':{'NaCl':2,'KCl':2,'MgCl2':3,'CaCl2':3,'AlCl3':4,'FeCl3':4}}
ELN={'C':'uglerod','H':'vodorod','O':'kislorod','N':'azot','Cl':'xlor','Fe':'temir','Cu':'mis','Mg':'magniy','Ca':'kalsiy','Na':'natriy','K':'kaliy','Al':'alyuminiy','S':'oltingugurt','Ba':'bariy'}
def _el(f): return {e:c for e,c in parse(f).items()}
def rel_mix(fam):
    D=FAM[fam]
    def f0(r):
        for _ in range(400):
            (n1,k1),(n2,k2)=r.sample(D['subs'],2)
            M1,M2=M(n1),M(n2); Z1,Z2=_z(n1),_z(n2)
            a=r.choice([0.1,0.2,0.3,0.4,0.5]); b=r.choice([0.1,0.2,0.3,0.4,0.5])
            if a==b: continue
            kind=r.choice(['R','D','Mr','P','At','El','FN','FM','K']+(['Io','Io'] if fam in ION else []))
            e1,e2=_el(n1),_el(n2)
            if kind=='R':
                g=math.gcd(round(a*10),round(b*10)); p,q=round(a*10)//g,round(b*10)//g
                c1=(q,-p,0); txt1="%s va %s ning mol nisbati %d : %d"%(n1,n2,p,q)
            elif kind=='FN':
                fr=Fraction(a/(a+b)).limit_denominator(10)
                if abs(float(fr)-a/(a+b))>1e-9 or fr.denominator>9: continue
                p,q=fr.numerator,fr.denominator
                c1=(q-p,-p,0); txt1="%s ning mol miqdori aralashmadagi umumiy mol miqdorining %d/%d qismini tashkil etadi"%(n1,p,q)
            elif kind=='FM':
                fr=Fraction(M1*a/(M1*a+M2*b)).limit_denominator(12)
                if abs(float(fr)-M1*a/(M1*a+M2*b))>1e-9 or fr.denominator>12: continue
                p,q=fr.numerator,fr.denominator
                c1=((q-p)*M1,-p*M2,0); txt1="%s ning massasi aralashma massasining %d/%d qismini tashkil etadi"%(n1,p,q)
            elif kind=='K':
                fr=Fraction(b/a).limit_denominator(6)
                if abs(float(fr)-b/a)>1e-9 or fr==1: continue
                p,q=fr.numerator,fr.denominator
                c1=(p,-q,0); txt1=("%s ning mol miqdori %s nikidan %d/%d marta ko'p"%(n2,n1,p,q)) if p>q else ("%s ning mol miqdori %s ning mol miqdorining %d/%d qismiga teng"%(n2,n1,p,q))
            elif kind=='D':
                d=abs(M2*b-M1*a)
                if d<1e-9: continue
                sgn=1 if M2*b>M1*a else -1
                c1=(-M1*sgn,M2*sgn,d); big,small=(n2,n1) if sgn>0 else (n1,n2)
                txt1="%s ning massasi %s ning massasidan %s g ga ko'p"%(big,small,_fm(d,1))
            elif kind=='Mr':
                fr=Fraction(M1*a).limit_denominator(1000)/Fraction(M2*b).limit_denominator(1000); p,q=fr.numerator,fr.denominator
                if max(p,q)>40: continue
                c1=(M1*q,-M2*p,0); txt1="%s va %s ning massalari nisbati %d : %d"%(n1,n2,p,q)
            elif kind=='P':
                z=Z1*a+Z2*b; c1=(Z1,Z2,z); txt1="aralashmadagi protonlarning umumiy soni %s·N_A"%_fm(z,2)
            elif kind=='Io':
                i1,i2=ION[fam][n1],ION[fam][n2]; s_=i1*a+i2*b
                if i1==i2: continue
                c1=(i1,i2,s_); txt1="suvdagi eritmasida aralashma dissotsilanganda hosil bo'ladigan ionlarning umumiy soni %s·N_A (to'liq dissotsilanish)"%_fm(s_,2)
            elif kind=='At':
                s_=sum(e1.values())*a+sum(e2.values())*b; c1=(sum(e1.values()),sum(e2.values()),s_); txt1="aralashmadagi atomlarning umumiy soni %s·N_A"%_fm(s_,2)
            else:
                els=sorted(set(e1)|set(e2)); 
                if len(els)<2: continue
                E,X=r.sample(els,2)
                tE=e1.get(E,0)*a+e2.get(E,0)*b; tX=e1.get(X,0)*a+e2.get(X,0)*b
                if tX==0 or tE==0: continue
                fr=Fraction(tE/tX).limit_denominator(8)
                if abs(float(fr)-tE/tX)>1e-9 or fr==1: continue
                p,q=fr.numerator,fr.denominator
                c1=(q*e1.get(E,0)-p*e1.get(X,0),q*e2.get(E,0)-p*e2.get(X,0),0)
                txt1="aralashmadagi %s atomlari sonining %s atomlari soniga nisbati %d : %d"%(ELN.get(E,E),ELN.get(X,X),p,q)
            sec_kind=r.choice(['G','T'])
            if sec_kind=='G':
                G=D['coef']*(k1*a+k2*b); c2=(D['coef']*k1,D['coef']*k2,G); txt2=D['meas']%_fm(G,D['nd'])
            else:
                T=M1*a+M2*b; c2=(M1,M2,T); txt2="Aralashmaning massasi %s g"%_fm(T,1)
            det=c1[0]*c2[1]-c1[1]*c2[0]
            if abs(det)<1e-9: continue
            break
        else: return f0(r)
        mt=M1*a+M2*b
        asks=[("Aralashmadagi %s ning massasini (g) toping."%n1,M1*a,[M2*b,M1*a*2,mt/2,M1*b]),
              ("Aralashmadagi %s ning massa ulushini (%%) aniqlang."%n2,M2*b/mt*100,[M1*a/mt*100,b/(a+b)*100,50,M2*b/mt*50]),
              ("Aralashmadagi %s ning mol ulushini (%%) hisoblang."%n1,a/(a+b)*100,[b/(a+b)*100,M1*a/mt*100,50,a*100])]
        if D.get('extra'):
            _,txt_,val_=D['extra'](a,b,k1,k2); asks.append((txt_,val_,[val_*2,val_/2,a+b,(a+b)*2]))
        if fam=='gas': asks.append(("Aralashmaning vodorodga nisbatan zichligini aniqlang.",mt/(a+b)/2,[mt/(a+b),mt/(a+b)/4,M1/2,M2/2]))
        ask,ans,wr=r.choice(asks)
        t="%s va %s aralashmasi tarkibida %s. %s. %s"%(n1,n2,txt1,txt2,ask)
        sol="x = n(%s), y = n(%s): 1-shart: %s; 2-shart: %s → tizimni yechamiz: x = %s mol, y = %s mol → %s"%(n1,n2,txt1,txt2,_fm(a,3),_fm(b,3),_fm(ans,3))
        return numq(t,ans,wr,sol,D['src'],2)
    def f(r):
        for _ in range(30):
            q=f0(r)
            if q.exact: return q
        return q
    f.__name__='rel_mix_'+fam
    return f
rel_carb=rel_mix('carb'); rel_met=rel_mix('met'); rel_alc=rel_mix('alc'); rel_alk=rel_mix('alk'); rel_hc=rel_mix('hc'); rel_gas=rel_mix('gas'); rel_oxr=rel_mix('oxr'); rel_sulf=rel_mix('sulf'); rel_chlo=rel_mix('chlo')

# ---------------- qisqa javobli (36-40): bilvosita shartli, qo'shimcha bosqichli ----------------
def s_hydrate_conc(r):
    for _ in range(100):
        m=r.choice([25,50,75,100]); m0=r.choice([100,200,250,300]); p0=r.choice([5,8,10,16])
        w2=(m0*p0/100+0.64*m)/(m0+m)*100
        if abs(w2*10-round(w2*10))<1e-9: break
    return numq("%d g %d %% li CuSO4 eritmasida %s g CuSO4·5H2O eritildi. Hosil bo'lgan eritmada tuzning massa ulushi %s %% bo'ldi. Qo'shilgan kristallogidrat massasini (g) toping."%(m0,p0,"noma'lum miqdordagi" if False else "m",_fm(w2,1)) if False else "%d g %d %% li CuSO4 eritmasiga m g CuSO4·5H2O eritildi, natijada tuzning massa ulushi %s %% ga yetdi. m ni (g) toping."%(m0,p0,_fm(w2,1)),m,[m*2,m/2,m+m0*0.1,m*1.5],"(%s + 0,64·m)/(%d + m) = %s → m = %d g"%(_fm(m0*p0/100,1),m0,_fm(w2/100,3),m),"8-9-sinf (kristallogidratlar; eritmalar)",0)
def s_unknown_chloride(r):
    val=r.choice([2,3]); me=r.choice([('Mg',24,2),('Ca',40,2),('Zn',65,2),('Al',27,3),('Fe',56,3),('Cr',52,3)]);
    while me[2]!=val: me=r.choice([('Mg',24,2),('Ca',40,2),('Zn',65,2),('Al',27,3),('Fe',56,3),('Cr',52,3)])
    n=r.choice([0.1,0.2,0.05]); Mcl=me[1]+35.5*val; m=n*Mcl; ag=n*val*143.5
    return numq("Oksidlanish darajasi +%d bo'lgan noma'lum X metallning xloridi %s g massada mo'l AgNO3 eritmasi bilan ta'sirlashganda %s g cho'kma hosil bo'ldi. X metallning nisbiy atom massasini toping."%(val,_fm(m,2),_fm(ag,2)),me[1],[me[1]+35.5,me[1]*2,Mcl,me[1]-8],"n(Cl⁻) = %s/143,5 = %s mol; n(XCl%d) = %s mol; M = %s/%s = %s; Ar(X) = %s − %s = %d"%(_fm(ag,2),_fm(ag/143.5,2),val,_fm(n,3),_fm(m,2),_fm(n,3),_fm(Mcl,1),_fm(Mcl,1),_fm(35.5*val,1),me[1]),"9-sinf (xloridlar; kumush xlorid cho'kmasi)",0)
def s_ratio_burn(r):
    a,b=r.choice([(1,2),(2,1),(1,3),(3,1),(2,3),(3,2)]); u=r.choice([0.05,0.1,0.2])
    A,B=a*u,b*u; co2=A+2*B; h2o=2*A+B
    k=r.choice(['V','m'])
    t="CH4 va C2H2 aralashmasi yondirilganda hosil bo'lgan CO2 va H2O mol miqdorlarining nisbati %d : %d bo'ldi. Aralashmadagi CH4 ning mol ulushi %% da qancha? (Javob butun songa yaxlitlanadi)"%(round(co2/u),round(h2o/u)) if False else "CH4 va C2H2 aralashmasi yondirilganda %s mol CO2 va %s mol suv hosil bo'ldi. Aralashmadagi CH4 ning mol ulushini (%%) toping."%(_fm(co2,2),_fm(h2o,2))
    ans=A/(A+B)*100
    return numq(t,ans,[B/(A+B)*100,50,A*100,ans/2],"CH4: x, C2H2: y; CO2: x + 2y = %s; H2O: 2x + y = %s → x = %s, y = %s; φ = %s %%"%(_fm(co2,2),_fm(h2o,2),_fm(A,2),_fm(B,2),_fm(ans,1)),"10-sinf (yonish; aralashma tarkibi)",1)
def s_plate_ratio(r):
    a,b=r.choice([(0.1,0.1),(0.2,0.1),(0.1,0.2)]);
    # Fe plastinka AgNO3 va Cu(NO3)2 aralashmasiga; erigan temir massasi va plastinka massasi o'zgarishi berilgan
    mFe=56*(a/2+b); dm=80*a+8*b
    return numq("Temir plastinka AgNO3 va Cu(NO3)2 aralashmasi eritmasiga tushirildi (ikkala tuz to'liq reaksiyaga kirishdi). Plastinkadan %s g temir eridi, plastinka massasi esa %s g ga ortdi. Eritmadagi AgNO3 massasini (g) toping."%(_fm(mFe,1),_fm(dm,1)),170*a,[170*b,170*a*2,64*b,108*a],"Fe + 2AgNO3 → Fe(NO3)2 + 2Ag (Δm = +160 g/mol Fe); Fe + Cu(NO3)2 → Fe(NO3)2 + Cu (Δm = +8): n(Fe) = %s/56 = %s = a/2 + b; 80a + 8b = %s → a = %s mol → m = %s g"%(_fm(mFe,1),_fm(mFe/56,3),_fm(dm,1),_fm(a,2),_fm(170*a,1)),"9-sinf (metallar kuchlanish qatori; plastinka massasi)",1)
SHORT_REL=[s_hydrate_conc,s_unknown_chloride,s_ratio_burn,s_plate_ratio]

# ---------------- 41: noma'lum kristallogidratni aniqlash (bilvosita ma'lumotlar) ----------------
HY=[('Cu',64,'CuSO4',5,'Cu(OH)2','CuO',80),('Zn',65,'ZnSO4',7,'Zn(OH)2','ZnO',81),('Mg',24,'MgSO4',7,'Mg(OH)2','MgO',40),('Ni',59,'NiSO4',6,'Ni(OH)2','NiO',75)]
def w41_hydrate_id(r):
    X,Ax,salt,n,hyd,ox,Mo=r.choice(HY); u=r.choice([0.05,0.1,0.2])
    Ms=Ax+96; Mh=Ms+18*n; m=u*Mh; wH=18*n/Mh*100; ba=u*233
    text=("Tarkibi XSO4·nH2O bo'lgan (X – oksidlanish darajasi +2 bo'lgan metall) kristallogidratning %s g namunasida suvning massa ulushi %s %% ni tashkil etadi. Namuna suvda eritilib, mo'l BaCl2 eritmasi qo'shilganda %s g cho'kma tushdi. "
          "Cho'kma ajratilgach, filtratga mo'l NaOH eritmasi qo'shilib, hosil bo'lgan gidroksid doimiy massagacha kuydirildi.")%(f2(m,2),f2(wH,1),f2(ba,2))
    bands=["Barcha reaksiyalarning tenglamalarini yozing; kristallogidratning molyar massasini va tuzdagi (suvsiz) qismining molyar massasini hisoblang.",
           "X metallni aniqlang va n ning qiymatini toping.",
           "Namunadagi XSO4 ning (suvsiz) massasini va kristallizatsion suv massasini (g) hisoblang.",
           "Filtratga sarflangan NaOH ning minimal miqdorini (mol) toping.",
           "Kuydirishdan hosil bo'lgan oksid massasini (g) aniqlang va u namuna massasining necha foizini tashkil etishini toping."]
    sol=["XSO4·nH2O + BaCl2 → BaSO4↓ + XCl2 + nH2O; XCl2 + 2NaOH → X(OH)2↓ + 2NaCl; X(OH)2 → XO + H2O (t). n(BaSO4) = %s/233 = %s mol = n(XSO4·nH2O); M(kristallogidrat) = %s/%s = **%s g/mol**; M(XSO4) = %s·(1 − %s) = **%s g/mol**"%(f2(ba,2),f2(u,3),f2(m,2),f2(u,3),f2(Mh,1),f2(Mh,1),f2(wH/100,3),f2(Ms,1)),
         "Ar(X) = %s − 96 = %s → **%s**; n = (%s − %s)/18 = **%d**; formula: %s·%dH2O"%(f2(Ms,1),f2(Ax,0),X,f2(Mh,1),f2(Ms,1),n,salt,n),
         "m(XSO4) = %s·%s = **%s g**; m(H2O) = %s − %s = **%s g**"%(f2(u,3),f2(Ms,1),f2(u*Ms,2),f2(m,2),f2(u*Ms,2),f2(m-u*Ms,2)),
         "XCl2 + 2NaOH → X(OH)2: n(NaOH) = 2·%s = **%s mol**"%(f2(u,3),f2(2*u,3)),
         "n(%s) = %s mol → m = %s·%s = **%s g**; ω = %s/%s = **%s %%**"%(ox,f2(u,3),f2(u,3),f2(Mo,1),f2(u*Mo,2),f2(u*Mo,2),f2(m,2),f2(u*Mo/m*100,1))]
    return W("41",text,bands,sol,SC41)
