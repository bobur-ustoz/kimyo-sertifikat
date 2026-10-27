from core import *
import re, math
# ---------------- BOG'LANISH ----------------
MOLS=[('CH2=CH2 (etilen)',[2],4,['sp2','sp2']),('HC≡CH (asetilen)',[3],2,['sp','sp']),('C6H6 (benzol)',[2,1,2,1,2,1],6,['sp2']*6),
('CH2=CH–CH=CH2',[2,1,2],6,['sp2']*4),('CH3–CH=CH2',[1,2],6,['sp3','sp2','sp2']),('CH3–C≡CH',[1,3],4,['sp3','sp','sp']),
('CH3COOH',[1,2,1],4,['sp3','sp2']),('HCHO',[2],2,['sp2']),('CH3CHO',[1,2],4,['sp3','sp2']),('CH2=CHCl',[2,1],3,['sp2','sp2']),
('C6H5CH3 (toluol)',[2,1,2,1,2,1,1],8,['sp2']*6+['sp3']),('C2H5OH',[1,1],6,['sp3','sp3']),('C6H5OH (fenol)',[2,1,2,1,2,1,1],6,['sp2']*6),
('HC≡C–CH=CH2',[3,1,2],4,['sp','sp','sp2','sp2']),('H2N–CH2–COOH',[1,1,2,1],5,['sp3','sp2']),('CH3–CH2–CH3',[1,1],8,['sp3']*3)]
def sp_(m): return len(m[1])+m[2], sum(o-1 for o in m[1])
def t_sigpi(r):
    m=pick(r,MOLS); s,p=sp_(m)
    ans='%d va %d'%(s,p); ws=list(dict.fromkeys('%d va %d'%x for x in [(s-1,p),(s,p+1),(s+1,p),(s,max(p-1,0)),(s+2,p+1)] if '%d va %d'%x!=ans))[:3]
    return Q("%s molekulasidagi σ va π bog'lar sonini aniqlang."%m[0].split(' (')[0],ans,ws,"σ: %d (har bir oddiy, ikkilamchi va uchlamchi bog'da 1 ta σ; C–H lar %d); π: %d"%(s,m[2],p),"10-sinf §17 (gibridlanish); Abdusamatov",'theory')
def t_hyb(r):
    m=pick(r,[x for x in MOLS if len(set(x[3]))>1]); h=r.choice(['sp','sp2','sp3']); k=m[3].count(h)
    if k==0: h=m[3][0]; k=m[3].count(h)
    return numq("%s molekulasida %s gibridlangan uglerod atomlari nechta?"%(m[0].split(' (')[0],h),k,[k+1,k+2,max(k-1,0) if k>1 else k+3,len(m[3])],"Gibridlanish: %s"%', '.join('%s'%x for x in m[3]),"10-sinf §17",0,'theory')
BOND=[('NH4Cl',['ion','kovalent qutbli','donor–akseptor']),('NaOH',['ion','kovalent qutbli']),('CO2',['kovalent qutbli']),('N2',['kovalent qutbsiz']),('H2O',['kovalent qutbli']),('KNO3',['ion','kovalent qutbli']),('(NH4)2SO4',['ion','kovalent qutbli','donor–akseptor']),('Cl2',['kovalent qutbsiz']),('NaCl',['ion']),('H3O⁺ (gidroksoniy ioni)',['kovalent qutbli','donor–akseptor'])]
def t_bondtype(r):
    kind=r.choice(['ion','donor–akseptor'])
    items=r.sample(BOND,4); nums=[i+1 for i,x in enumerate(items) if kind in x[1]]
    if not nums: return t_bondtype(r)
    ans=', '.join(map(str,nums)); allc=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4']
    ws=[c for c in allc if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Quyidagi moddalarning qaysilarida %s bog' mavjud? %s"%(kind if kind=='ion' else "donor–akseptor",'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(items))),ans,ws[:3],"; ".join('%s: %s'%(x[0],', '.join(x[1])) for x in items),"8-sinf; Tirkashev II bob (kimyoviy bog'lanish)",'theory')
# ---------------- TEZLIK ----------------
def c_vant(r):
    g=r.choice([2,3,4]); T1=r.choice([20,30,40]); dT=r.choice([20,30,40]); t=r.choice([8,16,27,64,81]); k=dT//10
    if g==2: t=r.choice([8,16,32,64])
    if g==3: t=r.choice([27,81,9])
    if g==4: t=r.choice([16,32,64])
    tt=t*60/g**k
    return numq("Reaksiya tezligining harorat koeffitsiyenti γ = %d. %d °C da reaksiya %d minutda tugasa, %d °C da necha sekundda tugaydi?"%(g,T1,t,T1+dT),tt,[t*60*g**k,t*60/g**(k-1),t/g**k,t*g**k],"%d → %d °C: Δt = %d, tezlik %d^%d = %d marta ortadi; %d·60/%d = %s s"%(T1,T1+dT,dT,g,k,g**k,t,g**k,fmt(tt,1)),"8-sinf; Tirkashev VI bob (Vant-Goff)",None)
def c_gamma_table(r):
    g=r.choice([2,3]); v0=r.choice([0.5,1,2]); T=[20,30,40]
    v=[v0*g**i for i in range(3)]; Tt=r.choice([50,60]); n=(Tt-20)//10; vx=v0*g**n
    tb="| T, °C | %d | %d | %d |\n|---|---|---|---|\n| v, mol/(l·s) | %s | %s | %s |"%(T[0],T[1],T[2],fmt(v[0]),fmt(v[1]),fmt(v[2]))
    q=numq("Reaksiya tezligining haroratga bog'liqligi jadvalda berilgan:\n\n%s\n\nJadvaldan foydalanib, shu reaksiyaning %d °C dagi tezligini (mol/(l·s)) aniqlang."%(tb,Tt),vx,[v0*g**(n-1),v0*g**(n+1),vx*2,v0*n*g],"γ = %s/%s = %d; 20 → %d °C: %d qadam, v = %s·%d^%d = %s"%(fmt(v[1]),fmt(v[0]),g,Tt,n,fmt(v0),g,n,fmt(vx)),"8-sinf; Tirkashev VI bob",None)
    q.kind='table'
    return q
def c_massact(r):
    a=r.choice([1,2]); b=r.choice([1,2]); k=r.choice([2,3]); mode=r.choice(['v','p'])
    if mode=='v':
        f=k**(a+b); return numq("A + B → mahsulot reaksiyada v = k·[A]^%d·[B]^%d. Idish hajmi %d marta kamaytirilsa (T = const), reaksiya tezligi necha marta o'zgaradi?"%(a,b,k),f,[k**a,k**b,k,f*k],"Konsentratsiyalar %d marta ortadi: v₂/v₁ = %d^(%d+%d) = %d"%(k,k,a,b,f),"Tirkashev VI bob (massalar ta'siri qonuni)",None)
    f=k**a*1; return numq("A + B → mahsulot reaksiyada v = k·[A]^%d·[B]^%d. A moddaning konsentratsiyasi %d marta, B niki %d marta oshirilsa, tezlik necha marta ortadi?"%(a,b,k,k+1),k**a*(k+1)**b,[k**a*(k+1),k*(k+1),k**b*(k+1)**a if a!=b else (k+1)**b],"v₂/v₁ = %d^%d · %d^%d = %d"%(k,a,k+1,b,k**a*(k+1)**b),"Tirkashev VI bob",None)
def c_rate(r):
    for _ in range(100):
        V=r.choice([2,5,10]); dn=r.choice([0.4,0.6,1.0,1.2,3,6]); t=r.choice([20,30,40,50,60,100,120,200]); v=dn/V/t
        if abs(round(v,4)-v)<1e-9 and v>=0.001: break
    mm=r.choice(['mol/(l·s)'])
    return numq("Hajmi %d l bo'lgan idishda A modda miqdori %s s davomida %s mol ga kamaydi. Reaksiyaning o'rtacha tezligini (mol/(l·s)) toping."%(V,t,fmt(dn)),v,[dn/t,dn/V,dn*V/t],"v = Δn/(V·Δt) = %s/(%d·%d) = %s"%(fmt(dn),V,t,fmt(v,5)),"8-sinf; Tirkashev VI bob",5)
# ---------------- MUVOZANAT ----------------
EQR=[('N2 + 3H2 ⇌ 2NH3',['N2','H2','NH3'],[1,3,2]),('2SO2 + O2 ⇌ 2SO3',['SO2','O2','SO3'],[2,1,2]),('H2 + I2 ⇌ 2HI',['H2','I2','HI'],[1,1,2]),('2NO + O2 ⇌ 2NO2',['NO','O2','NO2'],[2,1,2])]
def c_K(r):
    eq,sp,co=pick(r,EQR); c=[r.choice([0.5,1,2]) for _ in range(2)]+[r.choice([1,2,4])]
    K=c[2]**co[2]/(c[0]**co[0]*c[1]**co[1])
    t="%s reaksiyada muvozanat holatida [%s] = %s, [%s] = %s, [%s] = %s mol/l. Muvozanat konstantasini (K) hisoblang."%(eq,sp[0],fmt(c[0]),sp[1],fmt(c[1]),sp[2],fmt(c[2]))
    return numq(t,K,[K*2,K/2,c[2]/(c[0]*c[1]),c[2]**co[2]/(c[0]+c[1])],"K = [%s]^%d/([%s]^%d·[%s]^%d) = %s"%(sp[2],co[2],sp[0],co[0],sp[1],co[1],fmt(K,3)),"Tirkashev VI bob (kimyoviy muvozanat)",3)
def c_init(r):
    eq,sp,co=pick(r,EQR); x=r.choice([0.5,1,2]); cp=x*co[2]; a=r.choice([0.5,1,1.5]); b=r.choice([1,2,3])
    A0=a+x*co[0]; B0=b+x*co[1]
    which=r.choice([0,1]); ans=[A0,B0][which]
    return numq("%s reaksiyada muvozanat qaror topganda [%s] = %s, [%s] = %s, [%s] = %s mol/l bo'ldi. %s ning boshlang'ich konsentratsiyasini (mol/l) aniqlang."%(eq,sp[0],fmt(a),sp[1],fmt(b),sp[2],fmt(cp),sp[which]),ans,[a if which==0 else b,ans+x,ans-x if ans-x>0 else ans+2*x,ans*2],"%s ning sarfi = %s·%d/%d = %s → boshlang'ich %s"%(sp[which],fmt(cp),co[which],co[2],fmt(x*co[which]),fmt(ans)),"Tirkashev VI bob",None)
LCH=[('N2 + 3H2 ⇌ 2NH3 + Q',{'T↓':'o\'ngga','P↑':'o\'ngga','T↑':'chapga','P↓':'chapga','kat.':'siljimaydi'}),('2SO2 + O2 ⇌ 2SO3 + Q',{'T↓':'o\'ngga','P↑':'o\'ngga','T↑':'chapga','P↓':'chapga','kat.':'siljimaydi'}),('N2 + O2 ⇌ 2NO – Q',{'T↑':'o\'ngga','T↓':'chapga','P↑':'siljimaydi','P↓':'siljimaydi','kat.':'siljimaydi'}),('CaCO3 ⇌ CaO + CO2 – Q',{'T↑':'o\'ngga','P↓':'o\'ngga','T↓':'chapga','P↑':'chapga','kat.':'siljimaydi'}),('2NO + O2 ⇌ 2NO2 + Q',{'T↓':'o\'ngga','P↑':'o\'ngga','T↑':'chapga','P↓':'chapga','kat.':'siljimaydi'})]
CHN={'T↑':'haroratni oshirish','T↓':'haroratni pasaytirish','P↑':'bosimni oshirish','P↓':'bosimni pasaytirish','kat.':'katalizator qo\'shish'}
def t_lech(r):
    eq,d=pick(r,LCH); ks=r.sample(list(CHN),4); nums=[i+1 for i,k in enumerate(ks) if d[k]=="o'ngga"]
    if not nums: return t_lech(r)
    ans=', '.join(map(str,nums)); allc=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4','4']
    ws=[c for c in allc if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("%s muvozanatni o'ngga siljitadigan o'zgarishlarni toping: %s."%(eq,'; '.join('%d) %s'%(i+1,CHN[k]) for i,k in enumerate(ks))),ans,ws[:3],"Le-Shatelye prinsipi: "+'; '.join('%s – %s'%(CHN[k],d[k]) for k in ks),"Tirkashev VI bob (Le-Shatelye)",'theory')
def c_press(r):
    eq=pick(r,[('N2 + 3H2 ⇌ 2NH3',[1,3,2],'N2','H2','NH3'),('2SO2 + O2 ⇌ 2SO3',[2,1,2],'SO2','O2','SO3')])
    s,co,a,b,c=eq; n0=r.choice([8,12,16,20]); pct=r.choice([20,25,10])
    # initial exact stoichiometric ratio
    ta=co[0]; tb=co[1]; sa=n0*ta/(ta+tb); sb=n0*tb/(ta+tb)
    dn=n0*pct/100; # decrease = (sum co reactants - co product)*x
    d=co[0]+co[1]-co[2]; x=dn/d; A=sa-co[0]*x; B=sb-co[1]*x; C=co[2]*x
    return numq("%s reaksiyasida %s va %s stexiometrik nisbatda olingan umumiy %d mol aralashma muvozanat qaror topganda doimiy T va V da bosim %d %% ga kamaydi. Muvozanatdagi %s ning miqdorini (mol) aniqlang."%(s,a,b,n0,pct,c),C,[A,B,x,C*2],"Bosim %d %% ga kamaydi → Δn = %s mol = %d·x → x = %s; n(%s) = %d·x = %s mol"%(pct,fmt(dn),d,fmt(x),c,co[2],fmt(C)),"Tirkashev VI bob; 11-sinf (muvozanat)",None)
# ---------------- ERITMA ----------------
def c_mix(r):
    m1=r.choice([100,200,300]); m2=r.choice([200,300,400]); w1=r.choice([10,15,20]); w2=r.choice([25,30,40]); w=(m1*w1+m2*w2)/(m1+m2)
    return numq("%d g %d %% li va %d g %d %% li tuz eritmalari aralashtirildi. Hosil bo'lgan eritmaning massa ulushini (%%) aniqlang."%(m1,w1,m2,w2),w,[(w1+w2)/2,w1+w2,w*0.9,(m1*w2+m2*w1)/(m1+m2)],"m(tuz) = %d·%s + %d·%s = %s g; ω = %s/%d = %s %%"%(m1,fmt(w1/100),m2,fmt(w2/100),fmt((m1*w1+m2*w2)/100),fmt((m1*w1+m2*w2)/100),m1+m2,fmt(w,2)),"Tirkashev III bob (eritmalar)",2)
def c_evap(r):
    m=r.choice([200,300,400,500]); w=r.choice([10,15,20]); k=r.choice([2,2.5,4,5]);
    mt=m*w/100; mf=m*w*0.01*1/ (w*k/100) if False else None
    w2=w*k;
    if w2>=60: return c_evap(r)
    ev=m-m*w/w2
    return numq("%d g %d %% li tuz eritmasidan suv bug'latilib, massa ulushi %d %% ga yetkazildi. Bug'latilgan suv massasini (g) aniqlang."%(m,w,w2),ev,[m*w/w2,m-ev*2,ev*2,m*w2/w-m],"m(tuz) = %s g; yangi eritma %s g; bug'langan %s g"%(fmt(m*w/100),fmt(m*w/w2),fmt(ev)),"Tirkashev III bob",None)
def c_molar(r):
    D={'H2SO4':{10:1.07,20:1.14,30:1.22,40:1.30},'NaOH':{10:1.11,20:1.22,30:1.33,40:1.43},'HCl':{10:1.05,20:1.10,30:1.15},'HNO3':{10:1.05,20:1.12,30:1.18,40:1.25},'KOH':{10:1.09,20:1.19,30:1.29,40:1.40}}
    f=r.choice([('H2SO4',98),('NaOH',40),('HCl',36.5),('HNO3',63),('KOH',56)]); w=r.choice(list(D[f[0]])); rho=D[f[0]][w]
    C=10*w*rho/f[1]
    return numq("Zichligi %s g/ml bo'lgan %d %% li %s eritmasining molyar konsentratsiyasini (mol/l) aniqlang."%(fmt(rho),w,f[0]),C,[C/10,w*rho/f[1],C*2,10*w/f[1]],"C = 10·ω·ρ/M = 10·%d·%s/%s = %s"%(w,fmt(rho),fmt(f[1]),fmt(C,3)),"11-sinf 4-bob (molyar konsentratsiya)",2)
def c_hyd(r):
    f,mm,mw=r.choice([('CuSO4.5H2O',250,160),('Na2CO3.10H2O',286,106),('FeSO4.7H2O',278,152),('Na2SO4.10H2O',322,142)]); n=r.choice([0.1,0.2,0.05]); water=r.choice([100,200,300]);
    w=n*mw/(n*mm+water)*100
    return numq("%s g %s %s g suvda eritildi. Eritmadagi tuzning massa ulushini (%%) aniqlang."%(fmt(n*mm,2),f.replace('.','·'),water),w,[n*mw/water*100,n*mm/(n*mm+water)*100,w*2,w/2],"m(tuz) = %s g; m(eritma) = %s g; ω = %s %%"%(fmt(n*mw,2),fmt(n*mm+water,2),fmt(w,2)),"Tirkashev III bob (kristallogidrat)",2)
def c_sol(r):
    S1=r.choice([100,120,150]); S2=r.choice([20,25,30,40]); m=(100+S1)*r.choice([1,2]);
    salt=m*S1/(100+S1); water=m-salt; keep=water*S2/100; dep=salt-keep
    return numq("Tuzning eruvchanligi yuqori haroratda %d g, past haroratda %d g (100 g suvda). Yuqori haroratda to'yingan %s g eritma past haroratgacha sovitilsa, necha gramm tuz cho'kmaga tushadi?"%(S1,S2,fmt(m)),dep,[salt,keep,dep*2,m-keep],"Yuqori T: tuz %s g, suv %s g; past T da %s g suvda %s g eriydi; cho'kma %s g"%(fmt(salt),fmt(water),fmt(water),fmt(keep),fmt(dep)),"Tirkashev III bob (eruvchanlik)",None)
def c_oleum(r):
    w=r.choice([10,20,30]); mo=r.choice([100,200]); mw=r.choice([300,400,500]); so3=mo*w/100; h2=mo-so3; add=so3/80*98; tot=h2+add; res=tot/(mo+mw)*100
    return numq("Tarkibida %d %% SO3 bo'lgan %d g oleum %d g suvga qo'shildi. Hosil bo'lgan eritmadagi H2SO4 ning massa ulushini (%%) aniqlang."%(w,mo,mw),res,[h2/(mo+mw)*100,tot/mw*100,res*1.5],"SO3 %s g, H2SO4 %s g; SO3 + H2O → H2SO4: %s g; jami %s g / %d g = %s %%"%(fmt(so3),fmt(h2),fmt(add,2),fmt(tot,2),mo+mw,fmt(res,2)),"Tirkashev III bob (oleum); Tashev",2)
def c_normal(r):
    f=r.choice([('H2SO4',98,2),('H3PO4',98,3),('HCl',36.5,1),('Ca(OH)2',74,2),('Al2(SO4)3',342,6)]); C=r.choice([0.1,0.2,0.5,1])
    N=C*f[2]
    return numq("%s M %s eritmasining normal konsentratsiyasini (n) aniqlang."%(fmt(C),f[0]),N,[C,N*2,C/f[2],N/2],"N = M·z = %s·%d = %s"%(fmt(C),f[2],fmt(N)),"11-sinf 4-bob (normal konsentratsiya)",None)
def c_molal(r):
    f,m=pick(r,[('NaOH',40),('KOH',56),('NaCl',58.5),('HCl',36.5)]); n=r.choice([0.2,0.5,1]); w=r.choice([200,250,500])
    b=n/(w/1000)
    return numq("%s g %s %s g suvda eritildi. Eritmaning molyal konsentratsiyasini (mol/kg) aniqlang."%(fmt(n*m,2),f,w),b,[n/(w+n*m)*1000,n/w,b*2,b/2],"n = %s mol; b = n/m(erituvchi, kg) = %s/%s = %s"%(fmt(n),fmt(n),fmt(w/1000),fmt(b,2)),"11-sinf 4-bob (molyal konsentratsiya)",2)
# ---------------- DISSOTSILANISH ----------------
def c_alpha(r):
    C=r.choice([0.1,0.2,0.5,1]); a=r.choice([1,2,5]); H=C*a/100
    return numq("%s M sirka kislota eritmasida dissotsilanish darajasi %d %% bo'lsa, vodorod ionlari konsentratsiyasini (mol/l) aniqlang."%(fmt(C),a),H,[H*10,H/10,C,C*(1-a/100)],"[H⁺] = α·C = %s·%s = %s"%(fmt(a/100),fmt(C),fmt(H,4)),"9-sinf; Tirkashev IV bob (dissotsilanish darajasi)",4)
def c_ionsum(r):
    salts=[('Na2SO4',3),('AlCl3',4),('K3PO4',4),('CaCl2',3),('NaCl',2),('Al2(SO4)3',5),('Ba(OH)2',3),('HNO3',2)]
    s=r.sample(salts,2); n=[r.choice([1,2,3]) for _ in s]; V=r.choice([2,4,5])
    tot=sum(a*b[1] for a,b in zip(n,s)); C=tot/V
    return numq("%d mol %s va %d mol %s suvda eritilib, eritma hajmi %d l ga yetkazildi. Eritmadagi barcha ionlarning umumiy molyar konsentratsiyasini (mol/l) aniqlang (kuchli elektrolitlar to'liq dissotsilanadi)."%(n[0],s[0][0],n[1],s[1][0],V),C,[sum(n)/V,tot/V*2,tot/V/2,(tot-n[0])/V],"%s → %d ion, %s → %d ion: (%d·%d + %d·%d)/%d = %s"%(s[0][0],s[0][1],s[1][0],s[1][1],n[0],s[0][1],n[1],s[1][1],V,fmt(C)),"Tirkashev IV bob (kuchli elektrolitlar)",None)
def c_ph(r):
    mode=r.choice(['dil','mix','poh'])
    if mode=='dil':
        p=r.choice([1,2,3]); k=r.choice([10,100,1000]); new=p+int(math.log10(k));
        return numq("pH = %d bo'lgan kuchli kislota eritmasi %d marta suyultirildi. Yangi eritmaning pH qiymatini aniqlang."%(p,k),new,[new+1,new-1 if new>1 else new+2,p,7],"[H⁺] %d marta kamayadi → pH = %d + %d = %d"%(k,p,int(math.log10(k)),new),"9-sinf; Tirkashev IV bob (pH)",0)
    if mode=='poh':
        p=r.choice([9,10,11,12,13]);
        return numq("pH = %d bo'lgan eritmada gidroksid ionlari konsentratsiyasi 10^(−x) mol/l ga teng. x ni aniqlang."%p,14-p,[p,14-p+1,p-1,7],"pH + pOH = 14 → pOH = %d"%(14-p),"Tirkashev IV bob (suvning ion ko'paytmasi)",0)
    a=r.choice([2,3]);
    return numq("pH = %d bo'lgan HCl eritmasining 100 ml siga pH = %d bo'lgan NaOH eritmasidan 100 ml qo'shildi. Hosil bo'lgan eritmaning pH qiymatini aniqlang."%(a,14-a),7,[a,14-a,a+1,10],"n(H⁺) = n(OH⁻) = 10^(−%d)·0,1 mol → neytral, pH = 7"%a,"9-sinf (pH)",0)
HYD=[('CuSO4','kislotali'),('Na2CO3','ishqoriy'),('NaCl','neytral'),('Al2(SO4)3','kislotali'),('K2S','ishqoriy'),('KNO3','neytral'),('FeCl3','kislotali'),('CH3COONa','ishqoriy'),('ZnCl2','kislotali'),('K2SO4','neytral'),('NaNO2','ishqoriy'),('Na2SO4','neytral'),('NH4Cl','kislotali'),('K3PO4','ishqoriy')]
def t_hydr(r):
    kind=r.choice(['kislotali','ishqoriy','neytral']); pool=[x for x in HYD]; r.shuffle(pool)
    good=[x for x in pool if x[1]==kind][:r.randint(1,2)]; bad=[x for x in pool if x[1]!=kind][:4-len(good)]; lst=good+bad; r.shuffle(lst)
    nums=[i+1 for i,x in enumerate(lst) if x[1]==kind]; ans=', '.join(map(str,nums))
    allc=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4','1','2','3','4']
    ws=[c for c in allc if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Quyidagi tuzlarning qaysilari suvli eritmasi %s muhitga ega? %s"%(kind,'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(lst))),ans,ws[:3],'; '.join('%s – %s'%x for x in lst),"9-sinf (gidroliz); Tirkashev IV bob",'theory')
# ---------------- OQR ----------------
OQRB=['KMnO4 + HCl -> MnCl2 + Cl2 + KCl + H2O','K2Cr2O7 + HCl -> CrCl3 + Cl2 + KCl + H2O','K2Cr2O7 + FeSO4 + H2SO4 -> Cr2(SO4)3 + Fe2(SO4)3 + K2SO4 + H2O','Cu + HNO3 -> Cu(NO3)2 + NO + H2O','Cu + HNO3 -> Cu(NO3)2 + NO2 + H2O','Zn + HNO3 -> Zn(NO3)2 + NH4NO3 + H2O','Fe + H2SO4 -> Fe2(SO4)3 + SO2 + H2O','KMnO4 + K2SO3 + H2O -> MnO2 + K2SO4 + KOH','Al + HNO3 -> Al(NO3)3 + NO + H2O','KMnO4 + FeSO4 + H2SO4 -> MnSO4 + Fe2(SO4)3 + K2SO4 + H2O','Cl2 + KOH -> KCl + KClO3 + H2O','P + HNO3 + H2O -> H3PO4 + NO','S + HNO3 -> H2SO4 + NO','Mg + H2SO4 -> MgSO4 + H2S + H2O','NaCrO2 + Br2 + NaOH -> Na2CrO4 + NaBr + H2O']
def c_oqrsum(r):
    eq=pick(r,OQRB); b=balance(eq); s=sum(c for _,c in b)
    show=eq.replace('->','→')
    return numq("%s reaksiya tenglamasini tenglang va barcha koeffitsiyentlar yig'indisini aniqlang."%show,s,[s+1,s-1,s+2,s-2 if s>3 else s+3],"Tenglama: %s. Yig'indi %d"%(' + '.join('%s%s'%(str(c) if c>1 else '',x) for x,c in b[:len([1 for _ in eq.split('->')[0].split(' + ')])])+' → '+' + '.join('%s%s'%(str(c) if c>1 else '',x) for x,c in b[len(eq.split('->')[0].split(' + ')):]),s),"Tirkashev V bob; 11-sinf 7-bob (OQR tenglash)",None)
def c_oqrfrac(r):
    # HNO3 oxidizer count from Cu + HNO3
    rx=[('Cu + HNO3 -> Cu(NO3)2 + NO + H2O','Cu','HNO3','NO'),('Zn + HNO3 -> Zn(NO3)2 + NO + H2O','Zn','HNO3','NO'),('Al + HNO3 -> Al(NO3)3 + NO + H2O','Al','HNO3','NO'),('Cu + HNO3 -> Cu(NO3)2 + NO2 + H2O','Cu','HNO3','NO2'),('Cu + H2SO4 -> CuSO4 + SO2 + H2O','Cu','H2SO4','SO2')]
    eq,me,ac,gas=pick(r,rx); co=dict(balance(eq)); n=co[me]*r.choice([1,2])
    ox=n*co[gas]/co[me]; tot=n*co[ac]/co[me]
    return numq("%s reaksiyasida %s mol %s erisa, %s ning necha moli oksidlovchi vazifasini bajaradi?"%(eq.replace('->','→'),n,me,ac),ox,[tot,tot-ox,ox*2,n],"Oksidlovchi %s %s ga qaytariladi: n(%s) = %s mol → n(%s, oksidlovchi) = %s mol"%(ac,gas,gas,fmt(ox),ac,fmt(ox)),"Tirkashev V bob; Tashev (HNO3, H2SO4)",None)
OS=[('Na2S2O3','S',[2,'o\'rtacha'],'+2'),('K2Cr2O7','Cr',None,'+6'),('KMnO4','Mn',None,'+7'),('NH4NO3','N',None,'−3 va +5'),('Na2SO3','S',None,'+4'),('H3PO3','P',None,'+3'),('KClO3','Cl',None,'+5'),('HNO2','N',None,'+3'),('CrO3','Cr',None,'+6'),('K2MnO4','Mn',None,'+6'),('H2O2','O',None,'−1'),('NaH','H',None,'−1')]
def t_os(r):
    f,e,_,ans=pick(r,[x for x in OS if x[0] not in ('Na2S2O3',)])
    pool=['+1','+2','+3','+4','+5','+6','+7','−1','−2','−3','−3 va +5','+3 va +5']
    ws=[x for x in pool if x!=ans]; r.shuffle(ws)
    return Q("%s tarkibida %s ning oksidlanish darajasini aniqlang."%(f,e),ans,ws[:3],"Oksidlanish darajalari yig'indisi 0: %s da %s = %s"%(f,e,ans),"8-sinf; Tirkashev V bob (oksidlanish darajasi)",'theory')
OXI=['Cl⁻','Al³⁺','S²⁻','Fe²⁺','Mn⁷⁺ (MnO4⁻)','Na⁺','I⁻','K⁺','Zn²⁺','Fe³⁺']
ONLYOX={'Al³⁺','Na⁺','K⁺','Zn²⁺','Mn⁷⁺ (MnO4⁻)'}
ONLYRED={'Cl⁻','S²⁻','I⁻'}
def t_onlyox(r):
    kind=r.choice(['oksidlovchi','qaytaruvchi']); S=ONLYOX if kind=='oksidlovchi' else ONLYRED
    good=[x for x in OXI if x in S]; bad=[x for x in OXI if x not in S]; r.shuffle(good); r.shuffle(bad)
    k=1 if kind=='qaytaruvchi' else r.randint(1,2); lst=good[:k]+bad[:4-k]; r.shuffle(lst)
    nums=[i+1 for i,x in enumerate(lst) if x in S]; ans=', '.join(map(str,nums))
    allc=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4','1','2','3','4']
    ws=[c for c in allc if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Faqat %s bo'la oladigan ionlarni aniqlang: %s"%(kind,'; '.join('%d) %s'%(i+1,x) for i,x in enumerate(lst))),ans,ws[:3],"Eng yuqori oksidlanish darajasidagi ionlar faqat oksidlovchi, eng past darajadagilar faqat qaytaruvchi","Tirkashev V bob; 11-sinf 7-bob",'theory')
# ---------------- ELEKTROLIZ ----------------
def c_farad(r):
    case=r.choice([('CuSO4','Cu',2,64,'O2',4,32),('AgNO3','Ag',1,108,'O2',4,32),('NaCl','H2',2,2,'Cl2',2,71),('CuCl2','Cu',2,64,'Cl2',2,71)])
    salt,me,z,Am,gas,zg,Mg=case; I=r.choice([2,4,5,10]); t=r.choice([965,1930,3860,9650]); Q_=I*t; ne=Q_/96500
    what=r.choice(['katod','anod'])
    if what=='katod':
        if me=='H2': m=ne/2*2; lab='H2 massasi (g)'; ans=m
        else: m=ne/z*Am; lab='%s massasi (g)'%me; ans=m
    else:
        if gas=='O2': n=ne/4; vol=n*22.4
        else: n=ne/2; vol=n*22.4
        lab='anodda ajralgan %s hajmi (l, n.sh.)'%gas; ans=vol
    return numq("%s eritmasi inert elektrodlar yordamida %d A tok kuchi bilan %d s elektroliz qilindi. %s ni toping."%(salt,I,t,('Katodda ajralgan '+lab) if what=='katod' else (lab[0].upper()+lab[1:])),ans,[ans*2,ans/2,ans*ne,ans*1.5 if ans*1.5!=ans else ans+1],"Q = I·t = %d C; n(e⁻) = %s mol → %s"%(Q_,fmt(ne,3),fmt(ans,3)),"11-sinf 8-bob (Faradey qonunlari); Tirkashev V bob",3)
ELP=[('KNO3','H2 va O2'),('CuSO4','Cu va O2'),('NaCl','H2, Cl2 va NaOH'),('AgNO3','Ag va O2'),('CuCl2','Cu va Cl2'),('Na2SO4','H2 va O2'),('K2CO3','H2 va O2'),('ZnSO4','Zn, H2 va O2')]
def t_elec(r):
    salt,prod=pick(r,ELP); ws=[p for _,p in ELP if p!=prod]; ws=list(dict.fromkeys(ws)); r.shuffle(ws)
    return Q("%s ning suvli eritmasi inert elektrodlar bilan elektroliz qilinganda qaysi moddalar ajraladi?"%salt,prod,ws[:3],"Katod: aktivlik qatoriga qarab; anod: kislorodli kislota qoldig'i bo'lsa suv oksidlanadi (O2), Cl⁻ bo'lsa Cl2","11-sinf 8-bob; Tirkashev V bob (elektroliz)",'theory')
# ---------------- KUCHLANISH ----------------
def c_plate(r):
    cs=[('Cu','AgNO3','Ag',64,216,170,1),('Fe','CuSO4','Cu',56,64,160,1),('Zn','CuSO4','Cu',65,64,160,1),('Zn','Pb(NO3)2','Pb',65,207,331,1),('Fe','AgNO3','Ag',56,216,170,2)]
    me,salt,pr,M1,M2,Ms,k=pick(r,cs); n=r.choice([0.05,0.1,0.2]);
    if me=='Fe' and salt=='AgNO3': dm=n*(2*108-56)
    else: dm=n*(M2-M1)
    w=r.choice([None])
    msalt=2*n*170 if salt=='AgNO3' else n*Ms
    sg='ortadi' if dm>0 else 'kamayadi'
    return numq("%s plastinka %s g %s ni tutgan eritmaga tushirildi va %s to'liq ajralib chiqquncha ushlab turildi. Plastinka massasi necha gramm %s?"%(me,fmt(msalt,1),salt,pr,sg),abs(dm),[abs(dm)*2,abs(dm)/2,msalt,n*M2],"n(%s) = %s mol; Δm = %s g (%s)"%(salt,fmt(msalt/Ms,3),fmt(abs(dm),2),sg),"Tashev; 9-sinf (metallarning kuchlanish qatori)",2)
ACT=['Mg','Al','Zn','Fe','Pb','Cu','Ag']
def t_act(r):
    ps=[('Zn','CuSO4'),('Cu','ZnSO4'),('Fe','CuCl2'),('Ag','CuSO4'),('Mg','FeSO4'),('Cu','AgNO3'),('Pb','ZnCl2'),('Al','CuSO4'),('Fe','MgCl2')]
    can={('Zn','CuSO4'),('Fe','CuCl2'),('Mg','FeSO4'),('Cu','AgNO3'),('Al','CuSO4')}
    kind=r.choice([True,False]); items=r.sample(ps,4); nums=[i+1 for i,x in enumerate(items) if (x in can)==kind]
    if not nums: return t_act(r)
    ans=', '.join(map(str,nums)); allc=['1, 2','1, 3','2, 3','1, 2, 3','2, 4','1, 4','3, 4','1, 3, 4','2, 3, 4','1, 2, 4','1','2','3','4']
    ws=[c for c in allc if c!=ans and abs(len(c.split(', '))-len(nums))<=1]; r.shuffle(ws)
    return Q("Qaysi juftliklarda reaksiya %s? %s"%('boradi' if kind else 'bormaydi','; '.join('%d) %s va %s'%(i+1,a,b) for i,(a,b) in enumerate(items))),ans,ws[:3],"Metall o'z tuzidan faolligi pastroq metallni siqib chiqaradi (Mg > Al > Zn > Fe > Pb > H > Cu > Ag)","Tashev; 9-sinf (kuchlanish qatori)",'theory')
