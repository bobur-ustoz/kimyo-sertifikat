import random, math
from fractions import Fraction
from core import *
# Aralashmasiz (x, y tizimsiz) xilma-xil masalalar: noma'lum modda/element aniqlash, kasr va nisbat shartlari, ketma-ket jarayonlar.
# Shartda qaysi modda reaksiyaga kirishishi yoki kirishmasligi aytilmaydi – o'quvchi o'zi aniqlaydi.
V=22.4; F=96500
def _f(x,nd=2): return fmt(x,nd)
def _frac(p,q): return "%d/%d"%(p,q)

def g_oxide_salt_id(r):
    M_={'Mg':24,'Zn':65,'Cu':64,'Ca':40,'Ni':59}
    me=r.choice(list(M_)); A=M_[me]
    w=(A+96)/(A+996)*100
    others=[k for k in M_ if k!=me]; r.shuffle(others)
    return Q("Oksidlanish darajasi +2 bo'lgan noma'lum X metallning oksidi 10 %% li sulfat kislota eritmasining stexiometrik miqdorida to'liq eritildi. Hosil bo'lgan tuzning massa ulushi %s %% ga teng bo'ldi. X ni aniqlang."%_f(w,2),me,others[:3],"XO + H2SO4 → XSO4 + H2O: 1 mol oksid uchun 98 g H2SO4 → 980 g eritma; ω = (Ar + 96)/(Ar + 16 + 980) = %s → Ar(X) = %d → %s"%(_f(w/100,4),A,me),"9-sinf (oksidlar; eritma massa ulushi)",'calc')
HYD=[('CuSO4',160,5),('FeSO4',152,7),('ZnSO4',161,7),('MgSO4',120,7),('Na2CO3',106,10),('Na2SO4',142,10),('CaCl2',111,6),('CuCl2',135,2),('NiSO4',155,6),('Na2HPO4',142,12)]
def g_hydrate_n(r):
    s,Ms,n=r.choice(HYD); w=18*n/(Ms+18*n)*100
    ws=list(dict.fromkeys(x for x in (n-2,n-1,n+1,n+2,n*2,n+3) if x>0 and x!=n)); r.shuffle(ws)
    return Q("%s tuzining kristallogidratida suvning massa ulushi %s %% ni tashkil etadi. Kristallogidrat formulasidagi suv molekulalari sonini (n) toping."%(s,_f(w,1)),str(n),[str(x) for x in ws[:3]],"18n/(%d + 18n) = %s → n = %d"%(Ms,_f(w/100,4),n),"8-9-sinf (kristallogidratlar)",'calc')
EXP=[('2NH3 → N2 + 3H2',1),('N2O4 ⇌ 2NO2',1),('PCl5 ⇌ PCl3 + Cl2',1),('2SO3 ⇌ 2SO2 + O2',0.5),('C2H6 ⇌ C2H4 + H2',1)]
def g_gas_expansion(r):
    rx,k=r.choice(EXP); al=r.choice([0.2,0.25,0.4,0.5,0.6,0.75])
    fr=Fraction(1+k*al).limit_denominator(20); p,q=fr.numerator,fr.denominator
    ans=al*100
    t="%s reaksiyasi doimiy harorat va bosimda olib borildi; boshlang'ich modda qisman o'zgargach gazlar hajmi %d/%d marta ortdi. Boshlang'ich modda necha foizi o'zgarganini aniqlang."%(rx,p,q)
    return numq(t,ans,[ans/2,ans*2 if ans*2<100 else ans*1.2,100-ans,(fr-1)*100],"1 mol olsak: 1 + %s·α = %s → α = %s = %s %%"%(_f(k),_f(float(fr),3),_f(al,2),_f(ans,0)),"9-11-sinf (gaz hajmi o'zgarishi; parchalanish darajasi)",0)
def g_evap(r):
    for _ in range(100):
        m=r.choice([120,240,300,360,480]); p=r.choice([5,8,10,12,15]); k=r.choice([Fraction(3,2),Fraction(2),Fraction(5,4),Fraction(4,3),Fraction(5,3)])
        ev=m*(1-1/k)
        if p*k<=45 and abs(float(ev)*100-round(float(ev)*100))<1e-9: break
    ev=float(ev)
    t="%d g %d %% li tuz eritmasidan suv bug'latilganda tuzning massa ulushi %d/%d marta ortdi. Bug'latilgan suv massasini (g) toping."%(m,p,k.numerator,k.denominator)
    return numq(t,ev,[m/2,ev*2,m-ev,m*float(k)],"Tuz massasi o'zgarmaydi: %s g; yangi eritma = %s/%s = %s g; bug'langan = %d − %s = %s g"%(_f(m*p/100,1),_f(m*p/100,1),_f(p*float(k)/100,3),_f(m/float(k),2),m,_f(m/float(k),2),_f(ev,2)),"8-9-sinf (eritmalar; bug'latish)",2)
EQ=[('H2 + I2 ⇌ 2HI',lambda f:4*f*f/(1-f)**2),('CO + H2O ⇌ CO2 + H2',lambda f:f*f/(1-f)**2),('N2 + O2 ⇌ 2NO',lambda f:4*f*f/(1-f)**2)]
def g_equil_frac(r):
    for _ in range(100):
        rx,fn=r.choice(EQ); f=r.choice([Fraction(1,2),Fraction(2,3),Fraction(3,5),Fraction(1,3),Fraction(2,5),Fraction(3,4)]); n=r.choice([1,2,4]); Vv=r.choice([1,2,5])
        K=fn(float(f))
        if abs(K*100-round(K*100))<1e-9: break
    t="%s sistemasida boshlang'ich moddalarning har biridan %d mol dan %d l hajmli idishga solindi. Muvozanat qaror topganda reagentlarning har birining %d/%d qismi sarflangan bo'ldi. Muvozanat konstantasini hisoblang."%(rx,n,Vv,f.numerator,f.denominator)
    return numq(t,K,[K*2,K/2,K+1,math.sqrt(K)],"Sarflangan: %s·%d mol; qoldi (1 − %s)·%d; K = %s (hajm K ni o'zgartirmaydi, Δn = 0)"%(_frac(f.numerator,f.denominator),n,_frac(f.numerator,f.denominator),n,_f(K,3)),"9-11-sinf (kimyoviy muvozanat)",2)
def g_decay_frac(r):
    n=r.choice([2,3,4,5]); T=r.choice([5,8,12,20]); m=r.choice([32,64,80,160]); rem=Fraction(1,2**n)
    ask=r.choice(['n','m'])
    if ask=='n':
        t="Radioaktiv izotopning boshlang'ich miqdorining %d/%d qismi parchalandi. Necha yarim yemirilish davri o'tgan?"%(rem.denominator-1,rem.denominator)
        return numq(t,n,[n+1,n-1 if n>1 else n+2,n*2,rem.denominator/2],"Qolgan qism = 1/%d = (1/2)^%d → %d yarim yemirilish"%(rem.denominator,n,n),"11-sinf (radioaktivlik; yarim yemirilish davri)",0)
    t="Yarim yemirilish davri %d kun bo'lgan izotopning %d g namunasidan %d kun o'tdi. Qolgan izotop massasini (g) toping."%(T,m,n*T)
    return numq(t,m/2**n,[m/2,m/n,m/2**(n+1),m*(1-1/2**n)],"%d kun = %d yarim yemirilish davri; m = %d/2^%d = %s g"%(n*T,n,m,n,_f(m/2**n,3)),"11-sinf (radioaktivlik; yarim yemirilish davri)",3)
def g_mix_solutions(r):
    for _ in range(100):
        p1,p2=r.sample([5,10,15,20,25,30,40],2); a,b=r.choice([(1,2),(2,3),(1,3),(3,2),(1,1),(2,1)])
        w=(a*p1+b*p2)/(a+b)
        if abs(w*10-round(w*10))<1e-9: break
    t="%d %% li va %d %% li tuz eritmalari massalar nisbati %d : %d bo'lgan holda aralashtirildi. Hosil bo'lgan eritmaning massa ulushini (%%) hisoblang."%(p1,p2,a,b)
    return numq(t,w,[(p1+p2)/2,(a*p1+b*p2)/(a+b)*0.8,p1*b/(a+b)+p2*a/(a+b),w*1.2],"m1 = %d·u, m2 = %d·u: ω = (%d·%d + %d·%d)/(%d + %d) = %s %%"%(a,b,a,p1,b,p2,a,b,_f(w,2)),"8-sinf (eritmalarni aralashtirish)",1)

IND_UM=[g_hydrate_n,g_gas_expansion,g_evap,g_equil_frac,g_decay_frac,g_mix_solutions]
IND_AN=[g_oxide_salt_id,g_hydrate_n,g_gas_expansion,g_evap]

# ---------------- 33-35: aralashmasiz hikoyalar ----------------
def st_nitrate(r):
    a=r.choice([0.1,0.2,0.4]); Wt=r.choice([100,200,300]); m=a*188
    gas=2*a*46+a/2*32; sol=Wt+gas
    txt="%s g Cu(NO3)2 doimiy massagacha qizdirildi, ajralgan gazlar aralashmasi %d g suvga yuborildi."%(_f(m,1),Wt)
    qs=["Qattiq qoldiq massasini (g) aniqlang.","Hosil bo'lgan nitrat kislota massasini (g) toping.","Olingan eritmada nitrat kislotaning massa ulushini (%) hisoblang."]
    vals=[a*80,2*a*63,2*a*63/sol*100]
    s=["CuO: %s mol → %s g"%(_f(a,3),_f(a*80,2)),"NO2 %s mol, O2 %s mol → 4NO2 + O2 + 2H2O → 4HNO3: %s mol = %s g"%(_f(2*a),_f(a/2,3),_f(2*a),_f(2*a*63,2)),"Eritma = %d + %s = %s g; ω = %s %%"%(Wt,_f(gas,1),_f(sol,1),_f(vals[2],2))]
    return txt,qs,vals,s,"9-sinf (nitratlarning parchalanishi; NO2 ning yutilishi)"
def st_nacl_elec(r):
    I,t_=r.choice([(5,1930),(10,1930),(5,3860),(10,965)]); Wt=r.choice([200,300]); n=I*t_/F; m=n*2*58.5*r.choice([1.5,2])
    qs=["Anodda ajralgan gaz hajmini (l, n.sh.) aniqlang.","Katodda hosil bo'lgan gazning massasini (g) toping.","Elektrolizdan keyingi eritmada NaOH ning massa ulushini (%) hisoblang."]
    sol0=Wt+m; solf=sol0-n/2*71-n/2*2
    vals=[n/2*V,n/2*2,n*40/solf*100]
    txt="%s g NaCl %d g suvda eritildi va eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi."%(_f(m,2),Wt,I,t_)
    s=["n(e⁻) = %d·%d/96500 = %s mol → Cl2 = %s mol = %s l"%(I,t_,_f(n,3),_f(n/2,3),_f(vals[0],2)),"H2 = %s mol → %s g"%(_f(n/2,3),_f(vals[1],3)),"NaOH = %s mol = %s g; eritma = %s − %s − %s = %s g → %s %%"%(_f(n,3),_f(n*40,2),_f(sol0,1),_f(n/2*71,2),_f(n,3),_f(solf,2),_f(vals[2],2))]
    return txt,qs,vals,s,"11-sinf (elektroliz; Faradey qonuni)"
def st_hydrate_base(r):
    a=r.choice([0.1,0.2,0.4]); m=a*250
    txt="%s g CuSO4·5H2O suvda eritilib, eritmaga mo'l NaOH eritmasi qo'shildi, hosil bo'lgan cho'kma ajratilib, doimiy massagacha qizdirildi."%_f(m,1)
    qs=["Cho'kmaning massasini (g) aniqlang.","Qizdirishdan so'ng qolgan qattiq moddaning massasini (g) toping.","Cho'kma hosil bo'lgandan keyin eritmada qolgan natriy sulfat massasini (g) hisoblang."]
    vals=[a*98,a*80,a*142]
    s=["Cu(OH)2: %s mol → %s g"%(_f(a,3),_f(a*98,2)),"CuO: %s mol → %s g"%(_f(a,3),_f(a*80,2)),"Na2SO4: %s mol → %s g"%(_f(a,3),_f(a*142,2))]
    return txt,qs,vals,s,"9-sinf (mis birikmalari; kristallogidratlar)"
def st_nh3_chain(r):
    a=r.choice([2,4,5]); e=r.choice([0.8,0.75,0.9]);
    txt="%d mol ammiakning %s nitrat kislotagacha qayta ishlandi (jami unum 100 %%), qolgan ammiak hosil bo'lgan kislota bilan neytrallandi."%(a,"3/4" if False else "yarmi")
    hn=a/2; nh3=a/2; salt=min(hn,nh3)
    qs=["Hosil bo'lgan nitrat kislota massasini (g) aniqlang.","Neytrallanishda hosil bo'lgan ammoniy nitrat massasini (g) toping.","Qolgan ammiakning n.sh. dagi hajmini (l) hisoblang (neytrallashgacha)."]
    vals=[hn*63,salt*80,nh3*V]
    s=["n(HNO3) = %s mol → %s g"%(_f(hn,2),_f(hn*63,2)),"NH3 + HNO3 → NH4NO3: %s mol → %s g"%(_f(salt,2),_f(salt*80,2)),"V = %s·22,4 = %s l"%(_f(nh3,2),_f(nh3*V,2))]
    return txt,qs,vals,s,"9-sinf (ammiak; nitrat kislota; ammoniy nitrat)"
NEWST=[st_nitrate,st_nacl_elec,st_hydrate_base,st_nh3_chain]
