from core import *
from tail import W as _W
def W(t,text,bands,sol,score):
    c=lambda x:x.replace('%%','%')
    return _W(t,c(text),[c(b) for b in bands],[c(x) for x in sol],score)
import math
SC41=[(6,3),(2,1),(3,3),(2,2),(2,1)]
SC43=[(6,3),(3,2),(3,3),(3,2)]
def f2(x,nd=2): return fmt(x,nd)
# ---------------------------------------------------------------- 41-A: xlorid eritmasi elektrolizi
ELB=[('NaCl',58.5,'NaOH',40,1),('KCl',74.5,'KOH',56,1),('BaCl2',208,'Ba(OH)2',171,2),('CaCl2',111,'Ca(OH)2',74,2)]
def w41_elec(r):
    X,Mx,H,Mh,k=r.choice(ELB)
    for _ in range(100):
        s=r.choice([0.1,0.2,0.25,0.5]); ntot=s*r.choice([2,2.5,3,4]); w=r.choice([200,300,400,500]); Q=k*s*96500
        I=r.choice([5,10,4,2,20,25]);
        if Q%I==0: break
    t=int(Q//I); m=ntot*Mx
    nH=k/2*s; mh2=nH*2; mcl=nH*71; msol=m+w-mh2-mcl
    wH=s*Mh/msol*100; wX=(ntot-s)*Mx/msol*100; mI2=nH*254; mhcl=k*s*36.5/0.10
    text="%s g %s %d g suvda eritildi. Hosil bo'lgan eritma inert elektrodlar yordamida %d A tok kuchi bilan %d s davomida elektroliz qilindi."%(f2(m),X,w,I,t)
    bands=["Elektroliz tenglamasini yozing. Katodda va anodda ajralgan gazlarning hajmini (l, n.sh.) hisoblang (F = 96500 C/mol).","Elektroliz qilingan %s ning massasini (g) toping."%X,"Elektroliz tugagach eritmadagi %s va qolgan %s ning massa ulushlarini (%%) aniqlang."%(H,X),"Anodda ajralgan gaz mo'l KI eritmasidan o'tkazildi. Ajralgan yodning massasini (g) hisoblang (reaksiya tenglamasini yozing).","Elektroliz tugagan eritmani to'liq neytrallash uchun 10 %% li HCl eritmasidan necha gramm kerak?"]
    eq="2%s + 2H2O → 2%s + H2↑ + Cl2↑"%(X,H) if k==1 else "%s + 2H2O → %s + H2↑ + Cl2↑"%(X,H)
    sol=["%s. n(e⁻) = It/F = %d·%d/96500 = %s mol; n(H2) = n(Cl2) = %s mol → V = **%s l** (har biri)"%(eq,I,t,f2(k*s,3),f2(nH,3),f2(nH*22.4)),
     "n(%s) = n(e⁻)/%d = %s mol; m = %s·%s = **%s g**"%(X,k,f2(s,3),f2(s,3),fmt(Mx),f2(s*Mx)),
     "m(eritma) = %s + %d − %s (H2) − %s (Cl2) = %s g; ω(%s) = %s/%s = **%s %%**; ω(%s) = %s/%s = **%s %%**"%(f2(m),w,f2(mh2),f2(mcl),f2(msol),H,f2(s*Mh),f2(msol),f2(wH,2),X,f2((ntot-s)*Mx),f2(msol),f2(wX,2)),
     "Cl2 + 2KI → 2KCl + I2: n(I2) = %s mol → m = **%s g**"%(f2(nH,3),f2(mI2)),
     "%s + %s HCl → ...: n(HCl) = %s mol = %s g; 10 %% li eritma: %s/0,1 = **%s g**"%(H,('' if k==1 else '2 '),f2(k*s,3),f2(k*s*36.5),f2(k*s*36.5),f2(mhcl))]
    _Ms={'NaCl':106,'KCl':138,'BaCl2':197,'CaCl2':100}[X]; _ns=s/2 if k==1 else s
    bands[4]+=" Elektroliz tugagan eritmadan CO2 o'rta tuz (karbonat) hosil bo'lguncha yuttirilsa, hosil bo'ladigan karbonat massasini (g) ham hisoblang."; sol[4]+="; %s: n(karbonat) = %s mol → **%s g**"%(('CO2 + 2%s → M2CO3 + H2O'%H if k==1 else 'CO2 + %s → MCO3↓ + H2O'%H),f2(_ns,3),f2(_ns*_Ms,2))
    bands[1]+=" Elektroliz davomida o'tgan zaryadni (C) ham hisoblang."; sol[1]+="; Q = %d·%d = **%d C**"%(I,t,I*t)
    bands[3]+=" Neytrallash uchun sarflangan HCl miqdorini (mol) ham toping."; sol[3]+="; n(HCl) = %s mol"%f2(k*s,3)
    return W("41",text,bands,sol,SC41)
# ---------------------------------------------------------------- 41-B: qotishma + kislota + ishqor
AL=[('Mg',24,1,'MgSO4',120,'Mg(OH)2',58,'MgO',40,1,False),('Fe',56,1,'FeSO4',152,'Fe(OH)2',90,'Fe2O3',80,1,True)]
DS=[('Al',27,1.5,'Al2(SO4)3'),('Zn',65,1,'ZnSO4')]
def w41_alloy(r):
    R=r.choice(AL); D=r.choice(DS)
    nR=r.choice([0.1,0.2,0.15,0.25]); nD=r.choice([0.1,0.2,0.3,0.15])
    m=nR*R[1]+nD*D[1]; H2=nR*R[2]+nD*D[2]; V=H2*22.4; mac=H2*98/0.2
    hyd=nR*R[6]; ox=nR*R[8]*(0.5 if R[10] else 1)*(2 if R[10] else 1)/ (2 if R[10] else 1)
    if R[10]: ox=nR/2*160
    else: ox=nR*40
    text="%s (%s) va %s (%s) dan iborat %s g qotishma mo'l suyultirilgan sulfat kislotada eritildi, bunda %s l (n.sh.) gaz ajraldi. Hosil bo'lgan eritmaga mo'l NaOH eritmasi qo'shildi, hosil bo'lgan cho'kma ajratib olindi va havoda qizdirib quritildi."%({'Mg':'Magniy','Fe':'Temir'}[R[0]],R[0],{'Al':'alyuminiy','Zn':'rux'}[D[0]],D[0],f2(m),f2(V))
    bands=["Reaksiya tenglamalarini yozing va qotishmadagi har bir metallning massasini (g) aniqlang.","Qotishmadagi %s ning massa ulushini (%%) hisoblang."%R[0],"Eritish uchun sarflangan 20 %% li H2SO4 eritmasining massasini (g) aniqlang.","Mo'l NaOH qo'shilganda hosil bo'lgan cho'kmaning formulasi va massasini (g) toping%s."%(" (reaksiya tenglamalarini yozing)" ),"Cho'kma havoda to'liq qizdirilganda hosil bo'lgan oksidning massasini (g) hisoblang."]
    sol=["x·%s + y·%s = %s; %s x + %s y = %s mol → n(%s) = %s mol (**%s g**), n(%s) = %s mol (**%s g**)"%(fmt(R[1]),fmt(D[1]),f2(m),fmt(R[2]),fmt(D[2]),f2(H2,3),R[0],f2(nR,3),f2(nR*R[1]),D[0],f2(nD,3),f2(nD*D[1])),
     "ω(%s) = %s/%s = **%s %%**"%(R[0],f2(nR*R[1]),f2(m),f2(nR*R[1]/m*100,1)),
     "n(H2SO4) = n(H2) = %s mol = %s g; eritma: %s/0,2 = **%s g**"%(f2(H2,3),f2(H2*98),f2(H2*98),f2(mac)),
     "Mo'l NaOH da %s amfoter bo'lgani uchun eriydi; cho'kma %s: %s mol · %s = **%s g**"%('Al(OH)3' if D[0]=='Al' else 'Zn(OH)2',R[5],f2(nR,3),fmt(R[6]),f2(hyd)),
     ("4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3; 2Fe(OH)3 → Fe2O3 + 3H2O: n(Fe2O3) = %s mol → **%s g**"%(f2(nR/2,3),f2(ox)) if R[10] else "Mg(OH)2 → MgO + H2O: %s mol · 40 = **%s g**"%(f2(nR,3),f2(ox)))]
    return W("41",text,bands,sol,SC41)
# ---------------------------------------------------------------- 41-C: muvozanat (umumiy)
EQ3=[('N2O4 ⇌ 2NO2',[('N2O4',1)],[('NO2',2)]),('H2 + I2 ⇌ 2HI',[('H2',1),('I2',1)],[('HI',2)]),('2SO2 + O2 ⇌ 2SO3',[('SO2',2),('O2',1)],[('SO3',2)]),('N2 + 3H2 ⇌ 2NH3',[('N2',1),('H2',3)],[('NH3',2)]),('PCl5 ⇌ PCl3 + Cl2',[('PCl5',1)],[('PCl3',1),('Cl2',1)]),('CO + Cl2 ⇌ COCl2',[('CO',1),('Cl2',1)],[('COCl2',1)]),('2NO + O2 ⇌ 2NO2',[('NO',2),('O2',1)],[('NO2',2)])]
def w41_eq(r):
    for _ in range(200):
        eq,rs,ps=r.choice(EQ3); V=r.choice([1,2,4,5,10]); x=r.choice([0.5,1,2,0.25])
        init=[r.choice([1,2,3,4,5]) for _ in rs]
        eqm=[a-x*c for a,(n,c) in zip(init,rs)]
        if all(e>0 for e in eqm): break
    pm=[x*c for n,c in ps]
    num=1
    for p,(n,c) in zip(pm,ps): num*=(p/V)**c
    den=1
    for e,(n,c) in zip(eqm,rs): den*=(e/V)**c
    K=num/den
    n0=sum(init); neq=sum(eqm)+sum(pm); dn=sum(c for _,c in ps)-sum(c for _,c in rs)
    alpha=x*rs[0][1]/init[0]*100
    vfac=2**sum(c for _,c in rs)
    state=', '.join('%s – %s mol'%(n,f2(e,3)) for e,(n,c) in zip(eqm,rs))+'; '+', '.join('%s – %s mol'%(n,f2(p,3)) for p,(n,c) in zip(pm,ps))
    text="Hajmi %d l bo'lgan idishda %s sistema muvozanat holatiga keldi. Muvozanat qaror topganda idishdagi moddalar miqdori: %s."%(V,eq,state)
    bands=["Muvozanat konstantasini (K) hisoblang.","Moddalarning boshlang'ich konsentratsiyalarini (mol/l) aniqlang.","%s ning necha foizi reaksiyaga kirishgan?"%rs[0][0],"Idish hajmi izotermik ravishda 2 marta kamaytirilsa, to'g'ri reaksiya tezligi (elementar reaksiya deb hisoblang) necha marta o'zgaradi?","Bosim oshirilganda muvozanat qaysi tomonga siljiydi va K qiymati qanday o'zgaradi? Muvozanatdagi umumiy mol miqdorining boshlang'ich mol miqdoriga nisbatini toping."]
    ini=', '.join('%s %s'%(n,f2(a/V,3)) for a,(n,c) in zip(init,rs))
    ex=lambda L:'·'.join('[%s]%s'%(n,('^%d'%c if c>1 else '')) for n,c in L)
    sol=["K = %s/(%s) = **%s**"%(ex(ps),ex(rs),f2(K,3)),"n(bosh.) = n(muv.) + n(sarflangan): %s mol/l"%ini,"α = %s/%s = **%s %%**"%(f2(x*rs[0][1],3),f2(init[0]),f2(alpha,1)),"v = k·%s; hajm 2 marta kamayganda konsentratsiyalar 2 marta ortadi: 2^%d = **%d marta ortadi**"%('·'.join('[%s]%s'%(n,('^%d'%c if c>1 else '')) for n,c in rs),sum(c for _,c in rs),vfac),
     ("Δn = %+d → muvozanat %s siljiydi; K harorat funksiyasi, o'zgarmaydi. n(muv.)/n(bosh.) = %s/%s = **%s**"%(dn,('chapga' if dn>0 else ('o\'ngga' if dn<0 else 'siljimaydi')),f2(neq,3),f2(n0),f2(neq/n0,3)))]
    _Mav=(sum(e*M(n) for e,(n,c) in zip(eqm,rs))+sum(p*M(n) for p,(n,c) in zip(pm,ps)))/neq
    bands[4]+=" Muvozanat aralashmasining o'rtacha molyar massasini (g/mol) ham hisoblang."; sol[4]+="; M(o'rt.) = Σ(n·M)/Σn = **%s g/mol**"%f2(_Mav,2)
    bands[1]+=" Boshlang'ich moddalarning umumiy miqdorini (mol) ham toping."; sol[1]+="; n(bosh.) = **%s mol**"%f2(n0,2)
    bands[3]+=" Teskari reaksiya uchun K' = 1/K ni ham hisoblang."; sol[3]+="; K' = **%s**"%f2(1/K,3)
    return W("41",text,bands,sol,SC41)
# ---------------------------------------------------------------- 41-D: pH
def w41_ph(r):
    cand=[]
    for c1 in (0.1,0.05,0.02,0.04,0.2,0.01):
        for V1 in (0.1,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.75,0.8,0.9):
            for c2 in (0.1,0.05,0.02,0.01,0.2,0.04):
                V2=1-V1; d=c1*V1-c2*V2
                for k in (1,2,3):
                    if abs(abs(d)-10**-k)<1e-12 and d!=0: cand.append((c1,V1,c2,V2,d,k))
    c1,V1,c2,V2,d,k=r.choice(cand); acid=d>0
    base=r.choice(['NaOH','KOH'])
    pH=k if acid else 14-k
    a_=r.choice([0.01,0.02,0.05]); cw=r.choice([0.1,0.2,0.05]); Ka=cw*a_**2/(1-a_)
    hw=cw*a_; pHw=-math.log10(hw)
    text="Quyidagi eritmalar berilgan: HCl ning %s mol/l li eritmasi va %s ning %s mol/l li eritmasi. Ularni aralashtirib, umumiy hajmi 1 l bo'lgan eritma tayyorlandi (%s l HCl eritmasi va %s l %s eritmasi). Shuningdek, sirka kislotaning %s mol/l li eritmasida dissotsilanish darajasi %s %%."%(f2(c1,3),base,f2(c2,3),f2(V1,2),f2(V2,2),base,f2(cw,3),f2(a_*100,0))
    bands=["Aralashtirilgandan keyingi eritmaning pH ini aniqlang.","Dastlabki HCl eritmasining pH ini hisoblang.","Dastlabki %s eritmasining pH ini hisoblang."%base,"Sirka kislota eritmasidagi H⁺ ionlari konsentratsiyasini (mol/l) va pH ni aniqlang (lg 2 = 0,3, lg 5 = 0,7 ni ishlating).","Sirka kislotaning dissotsilanish konstantasini hisoblang (K = Cα²/(1 − α))."]
    sol=["n(H⁺) = %s mol; n(OH⁻) = %s mol; ortiqcha %s: %s mol / 1 l = 10⁻%d mol/l → **pH = %d**"%(f2(c1*V1,4),f2(c2*V2,4),'H⁺' if acid else 'OH⁻',f2(abs(d),4),k,pH),
     "[H⁺] = %s → **pH = %s**"%(f2(c1,3),f2(-math.log10(c1),2)),
     "[OH⁻] = %s → pOH = %s → **pH = %s**"%(f2(c2,3),f2(-math.log10(c2),2),f2(14+math.log10(c2),2)),
     "[H⁺] = Cα = %s·%s = %s mol/l → **pH = %s**"%(f2(cw,3),f2(a_,3),f2(hw,5),f2(pHw,2)),
     "K = %s·%s²/(1 − %s) = **%s**"%(f2(cw,3),f2(a_,3),f2(a_,3),(lambda e:'%s·10^%d'%(fmt(Ka/10**e,2),e))(math.floor(math.log10(Ka))))]
    bands[4]+=" Shuningdek HCl eritmasi 10 marta suyultirilsa pH necha bo'ladi?"; sol[4]+="; [H⁺] = %s/10 → **pH = %s**"%(f2(c1,3),f2(-math.log10(c1/10),2))
    bands[1]+=" 1 l shu eritmadagi HCl massasini (g) ham hisoblang."; sol[1]+="; m = %s·36,5 = **%s g**"%(f2(c1,3),f2(c1*36.5,2))
    bands[3]+=" Shuningdek %s eritmasi 100 marta suyultirilsa pH qancha bo'ladi?"%base; sol[3]+="; pH = 14 + lg(%s/100) = **%s**"%(f2(c2,3),f2(14+math.log10(c2/100),2))
    return W("41",text,bands,sol,SC41)
# ---------------------------------------------------------------- 41-E: OQR / xlor
OXB=[('2KMnO4 + 16HCl → 2KCl + 2MnCl2 + 5Cl2 + 8H2O','KMnO4',158,2,5,16,10),('MnO2 + 4HCl → MnCl2 + Cl2 + 2H2O','MnO2',87,1,1,4,2),('K2Cr2O7 + 14HCl → 2KCl + 2CrCl3 + 3Cl2 + 7H2O','K2Cr2O7',294,1,3,14,6),('KClO3 + 6HCl → KCl + 3Cl2 + 3H2O','KClO3',122.5,1,3,6,5)]
def w41_redox(r):
    eq,ox,Mo,co,cc,ch,cho=r.choice(OXB); a=r.choice([0.3,0.6,0.5,0.9,1.5]);
    ncl=a; nox=ncl*co/cc; nhcl=ncl*ch/cc; nhox=ncl*cho/cc
    # KI step and KClO3 step
    mI2=ncl/2*254; mKClO3=ncl/2/3*122.5
    coefs={'KMnO4':2+16+2+2+5+8,'MnO2':1+4+1+1+2,'K2Cr2O7':1+14+2+2+3+7,'KClO3':1+6+1+3+3}[ox]
    text="Laboratoriyada xlor olish uchun %s ga konsentrlangan xlorid kislota ta'sir ettirildi: %s. Ajralgan %s l (n.sh.) xlor gazining yarmi mo'l KI eritmasidan o'tkazildi, qolgan yarmi esa issiq mo'l KOH eritmasiga yuttirildi."%(ox,eq,f2(a*22.4))
    bands=["Reaksiyani elektron balans usulida tenglang: oksidlovchi va qaytaruvchini ko'rsating, koeffitsiyentlar yig'indisini toping.","%s ning sarflangan massasini (g) hisoblang."%ox,"Sarflangan HCl miqdorini (mol) va shundan qaytaruvchi sifatida ishtirok etgan qismini (mol) aniqlang.","Xlor mo'l KI eritmasidan o'tkazilganda ajralgan yodning massasini (g) toping (reaksiya tenglamasini yozing).","Issiq KOH eritmasiga yuttirilganda (3Cl2 + 6KOH → KClO3 + 5KCl + 3H2O) hosil bo'lgan KClO3 massasini (g) aniqlang."]
    sol=["Tenglama: %s; oksidlovchi %s, qaytaruvchi Cl⁻ (HCl); koeffitsiyentlar yig'indisi **%d**"%(eq,ox,coefs),"n(Cl2) = %s mol; n(%s) = %s·%d/%d = %s mol → m = **%s g**"%(f2(ncl,3),ox,f2(ncl,3),co,cc,f2(nox,3),f2(nox*Mo)),"n(HCl) = %s mol (**%s mol**); qaytaruvchi: **%s mol**"%(f2(nhcl,3),f2(nhcl,3),f2(nhox,3)),"Cl2 + 2KI → 2KCl + I2: n(Cl2) = %s mol → n(I2) = %s mol → **%s g**"%(f2(ncl/2,3),f2(ncl/2,3),f2(mI2)),"n(Cl2) = %s mol; n(KClO3) = %s/3 = %s mol → **%s g**"%(f2(ncl/2,3),f2(ncl/2,3),f2(ncl/6,3),f2(mKClO3))]
    bands[4]+=" Agar xlor sovuq KOH eritmasiga yuttirilsa (Cl2 + 2KOH → KCl + KClO + H2O), hosil bo'ladigan KClO massasini (g) ham toping."; sol[4]+="; n(KClO) = %s mol → **%s g**"%(f2(ncl/2,3),f2(ncl/2*74.5,2))
    bands[1]+=" Sarflangan oksidlovchining miqdorini (mol) ham toping."; sol[1]+="; n(%s) = **%s mol**"%(ox,f2(nox,3))
    bands[3]+=" Sarflangan KI massasini (g) ham toping."; sol[3]+="; n(KI) = 2·%s = %s mol → **%s g**"%(f2(ncl/2,3),f2(ncl,3),f2(ncl*166,2))
    return W("41",text,bands,sol,SC41)
# ---------------------------------------------------------------- 41-F: kristallogidrat
HYD=[('Na2CO3·10H2O',286,'Na2CO3',106),('FeSO4·7H2O',278,'FeSO4',152),('CuSO4·5H2O',250,'CuSO4',160),('ZnSO4·7H2O',287,'ZnSO4',161),('MgSO4·7H2O',246,'MgSO4',120)]
def w41_hyd2(r):
    H,Mh,A,Ma=r.choice(HYD); n=r.choice([0.1,0.2,0.05,0.25]); w=r.choice([200,300,400,500]); m=n*Mh; msol=m+w; om=n*Ma/msol*100
    nw=round((Mh-Ma)/18); wH2O=(Mh-Ma)/Mh*100
    if A=='Na2CO3':
        b2="Eritmaga mo'l CaCl2 qo'shildi. Hosil bo'lgan cho'kma massasini (g) toping."; v2=n*100; s2="Na2CO3 + CaCl2 → CaCO3↓ + 2NaCl: %s mol · 100 = **%s g**"%(f2(n,3),f2(v2))
        b3="Xuddi shunday eritmaga mo'l HCl qo'shilganda ajralgan gazning hajmini (l, n.sh.) hisoblang."; s3="Na2CO3 + 2HCl → 2NaCl + CO2↑ + H2O: **%s l**"%f2(n*22.4)
        b4="Eritmani to'liq neytrallash (Na2CO3 + 2HCl → 2NaCl + CO2 + H2O) uchun 10 %% li HCl eritmasidan necha gramm kerak?"; s4="n(HCl) = %s mol = %s g; %s/0,1 = **%s g**"%(f2(2*n,3),f2(2*n*36.5),f2(2*n*36.5),f2(2*n*36.5/0.1))
    else:
        b2="Eritmaga mo'l BaCl2 eritmasi qo'shildi. Hosil bo'lgan cho'kma massasini (g) toping."; v2=n*233; s2="%s + BaCl2 → BaSO4↓ + ...: n(BaSO4) = %s mol → **%s g**"%(A,f2(n,3),f2(v2))
        oh={'FeSO4':'Fe(OH)2','CuSO4':'Cu(OH)2','ZnSO4':'Zn(OH)2','MgSO4':'Mg(OH)2'}[A]; Moh=M(oh)
        b3="Xuddi shunday eritmaga ekvivalent miqdorda NaOH qo'shilganda hosil bo'lgan %s cho'kmasining massasini (g) toping."%oh; s3="%s + 2NaOH → %s↓ + Na2SO4: %s mol · %s = **%s g**"%(A,oh,f2(n,3),fmt(Moh),f2(n*Moh))
        if A=='MgSO4': b4="Ushbu eritmadan sulfat ionlarini to'liq cho'ktirish uchun 10 %% li BaCl2 eritmasidan (M = 208) necha gramm kerak?"; s4="n(BaCl2) = %s mol = %s g; %s/0,1 = **%s g**"%(f2(n,3),f2(n*208),f2(n*208),f2(n*2080))
        else:
            met={'FeSO4':('Zn',65,'Fe',56),'CuSO4':('Fe',56,'Cu',64),'ZnSO4':('Mg',24,'Zn',65)}[A]
            b4="Eritmaga %s plastinka tushirildi (%s tuzidagi metall to'liq siqib chiqarildi). Plastinka massasi qanchaga (g) o'zgargan?"%(met[0],A); d=n*(met[3]-met[1]); s4="%s + %s → %s%s...: Δm = %s·(%s − %s) = **%s g** (%s)"%(met[0],A,met[0],'SO4',f2(n,3),fmt(met[3]),fmt(met[1]),f2(abs(d)),'ortadi' if d>0 else 'kamayadi')
    text="%s g %s %d g suvda eritildi."%(f2(m),H,w)
    bands=["Hosil bo'lgan eritmadagi %s ning massa ulushini (%%) toping."%A,b2,b3,b4,"Kristallogidratdagi kristallizatsion suvning massa ulushini (%) va unda suv molekulalari sonini toping."]
    sol=["m(%s) = %s·%s = %s g; m(eritma) = %s + %d = %s g; ω = **%s %%**"%(A,f2(n,3),fmt(Ma),f2(n*Ma),f2(m),w,f2(msol),f2(om,2)),s2,s3,s4,"ω(H2O) = (%s − %s)/%s = **%s %%**; suv molekulalari: **%d** ta"%(fmt(Mh),fmt(Ma),fmt(Mh),f2(wH2O,1),nw)]
    bands[4]+=" Shu miqdor kristallogidrat suvsizlantirilganda massa necha gramm kamayadi?"; sol[4]+="; Δm = %s·(%s − %s) = **%s g**"%(f2(n,3),fmt(Mh),fmt(Ma),f2(n*(Mh-Ma),2))
    bands[1]+=" Eritmadagi kation miqdorini (mol) ham toping."; sol[1]+="; n(kation) = **%s mol**"%f2(n,3)
    bands[3]+=" Dastlabki eritma massasini (g) ham ayting."; sol[3]+="; m(eritma) = %s + %d = **%s g**"%(f2(m,2),w,f2(msol,2))
    return W("41",text,bands,sol,SC41)
W41N=[w41_elec,w41_alloy,w41_eq,w41_ph,w41_redox,w41_hyd2]
# ================================================================ 43
NIT=[('Cu',64,'CuO',80,188,'mis'),('Zn',65,'ZnO',81,189,'rux'),('Pb',207,'PbO',223,331,'qo\'rg\'oshin'),('Mg',24,'MgO',40,148,'magniy')]
def w43_nit2(r):
    Me,Ar,Ox,Mox,Mn,nm=r.choice(NIT); n=r.choice([0.2,0.4,0.1]); frac=r.choice([0.5,0.25]); dec=n*frac; salt=Me+'(NO3)2'
    start=n*Mn; resid=start-dec*(Mn-Mox); gas=dec*2.5*22.4; wat=r.choice([200,300,100]); hno3=dec*2*63; msol=wat+dec*2*46+dec*0.5*32; om=hno3/msol*100
    h2so4=dec*98/0.2; msalt=dec*(Ar+96)
    text="%s g %s qizdirilganda qisman parchalandi va qattiq qoldiq massasi %s g bo'ldi. Ajralgan gazlar aralashmasi %d g suvga to'liq yuttirildi. Qattiq qoldiqdagi %s esa mo'l suyultirilgan H2SO4 bilan reaksiyaga kiritildi."%(f2(start),salt,f2(resid),wat,Ox)
    bands=["Parchalanish reaksiyasi tenglamasini yozing. Parchalangan %s ning ulushini (%%) va ajralgan gazlar umumiy hajmini (l, n.sh.) aniqlang."%salt,"Qattiq qoldiqdagi %s ning massa ulushini (%%) hisoblang."%Ox,"Gazlar suvga yuttirilganda hosil bo'lgan eritmadagi HNO3 ning massa ulushini (%) toping (reaksiya tenglamasini yozing).","Qoldiqdagi %s ni to'liq eritish uchun 20 %% li H2SO4 eritmasidan necha gramm kerak va hosil bo'lgan %sSO4 ning massasi qancha?"%(Ox,Me)]
    sol=["2%s → 2%s + 4NO2 + O2; massa kamayishi %s g; parchalangan %s mol, boshlang'ich %s mol → **%s %%**; gazlar: NO2 %s + O2 %s mol → **%s l**"%(salt,Ox,f2(start-resid),f2(dec,3),f2(n,3),f2(frac*100,0),f2(dec*2,3),f2(dec/2,3),f2(gas)),
     "%s %s mol = %s g; ω = %s/%s = **%s %%**"%(Ox,f2(dec,3),f2(dec*Mox),f2(dec*Mox),f2(resid),f2(dec*Mox/resid*100,1)),
     "4NO2 + O2 + 2H2O → 4HNO3: HNO3 %s mol = %s g; eritma %d + %s + %s = %s g → **%s %%**"%(f2(dec*2,3),f2(hno3),wat,f2(dec*2*46),f2(dec/2*32),f2(msol),f2(om,2)),
     "%s + H2SO4 → %sSO4 + H2O: n(H2SO4) = %s mol = %s g → 20 %% li eritma **%s g**; %sSO4: %s mol · %s = **%s g**"%(Ox,Me,f2(dec,3),f2(dec*98),f2(h2so4),Me,f2(dec,3),fmt(Ar+96),f2(msalt))]
    bands.append("Ajralgan NO2 va O2 gazlari aralashmasining o'rtacha molyar massasini (g/mol) hisoblang."); sol.append("NO2 : O2 = 4 : 1 → M = (4·46 + 32)/5 = **43,2 g/mol**")
    return W("43",text,bands,sol,SC41)
AN=[('Cl⁻','NaCl','AgNO3',('oq cho\'kma (AgCl)','—','—'),143.5,'AgCl'),('SO4²⁻','Na2SO4','BaCl2',('—','oq cho\'kma (BaSO4)','—'),233,'BaSO4'),('CO3²⁻','Na2CO3','HCl',('—','—','gaz (CO2) ajraladi'),44,'CO2'),('PO4³⁻','Na3PO4','AgNO3',('—','—','sariq cho\'kma (Ag3PO4)'),419,'Ag3PO4'),('Br⁻','NaBr','AgNO3',('—','och sariq cho\'kma (AgBr)','—'),188,'AgBr'),('I⁻','KI','AgNO3',('—','—','sariq cho\'kma (AgI)'),235,'AgI')]
def w43_anion(r):
    # 3 ta anion; AgNO3, BaCl2, HCl reagentlari
    pool=[('Cl⁻','NaCl',58.5,{'AgNO3':'oq cho\'kma (AgCl)','BaCl2':'—','HCl':'—'},143.5,'AgCl','AgNO3'),
          ('SO4²⁻','Na2SO4',142,{'AgNO3':"—",'BaCl2':"oq cho'kma (BaSO4)",'HCl':'—'},233,'BaSO4','BaCl2'),
          ('CO3²⁻','Na2CO3',106,{'AgNO3':"oq-sarg'ish cho'kma",'BaCl2':"oq cho'kma (BaCO3)",'HCl':'gaz (CO2) ajraladi'},197,'BaCO3','BaCl2'),
          ('PO4³⁻','Na3PO4',164,{'AgNO3':"sariq cho'kma (Ag3PO4)",'BaCl2':"oq cho'kma",'HCl':'—'},419,'Ag3PO4','AgNO3'),
          ('Br⁻','NaBr',103,{'AgNO3':"och sariq cho'kma (AgBr)",'BaCl2':'—','HCl':'—'},188,'AgBr','AgNO3'),
          ('I⁻','KI',166,{'AgNO3':"sariq cho'kma (AgI)",'BaCl2':'—','HCl':'—'},235,'AgI','AgNO3')]
    pick=r.sample(pool,3)
    # CO3 + PO4 together would be confusing for BaCl2 table; allow anyway
    sal=[p[1] for p in pick]; labels=['X','Y','Z']; perm=list(range(3)); r.shuffle(perm)
    rows=[]
    for reag in ('AgNO3','BaCl2','HCl'):
        rows.append('| %s | %s |'%(reag,' | '.join(pick[perm[i]][3][reag] for i in range(3))))
    tab="| Reagent | X | Y | Z |\n|---|---|---|---|\n"+"\n".join(rows)
    n=r.choice([0.1,0.2,0.05])
    tgt=pick[perm[r.randrange(3)]]; ti=[pick[perm[i]] for i in range(3)].index(tgt)
    text="Uch probirkada (X, Y, Z) natriy yoki kaliy tuzlarining eritmalari bor: %s (tartibsiz). Har bir eritmaga reagentlar ta'sir ettirildi, kuzatuvlar jadvalda:\n\n%s"%(', '.join(sorted(sal)),tab)
    ans=', '.join('%s – %s'%(labels[i],pick[perm[i]][1]) for i in range(3))
    # mass of precipitate for chosen tube
    mp=n*tgt[4]; reag=tgt[6]; prod=tgt[5]
    if prod=='CO2': mp=n*22.4
    bands=["X, Y, Z probirkalardagi moddalarni aniqlang va kuzatilgan reaksiyalarning ionli tenglamalarini yozing.","%s probirkadagi tuz %s mol miqdorda olingan. Unga mo'l %s qo'shilganda %s %s toping."%(labels[ti],f2(n,3),reag,'hosil bo\'lgan cho\'kma' if prod!='CO2' else 'ajralgan gaz','massasini (g)' if prod!='CO2' else 'hajmini (l, n.sh.)'),"Uchala eritmaning har biriga %s mol dan solingan bo'lsa, mo'l AgNO3 qo'shilganda hosil bo'ladigan barcha cho'kmalarning umumiy massasini (g) toping (ularning formulalarini yozing)."%f2(n,3),"Eritmalarda kuzatilgan hodisalarni (cho'kma yoki gaz hosil bo'lishi) tushuntiring: qaysi ion qaysi reagent bilan qanday birikma hosil qiladi? Shu usul bilan ionlarni aniqlash qoidasini yozing."]
    tot=0; forms=[]
    for p in pick:
        pr=p[3]['AgNO3']
        if pr!='—':
            mm={'Cl⁻':143.5,'CO3²⁻':276,'PO4³⁻':419,'Br⁻':188,'I⁻':235}[p[0]]
            coef=1
            tot+=n*mm
            forms.append(pr)
    sol=[ans+". Ionli tenglamalar: "+"; ".join(("Ag⁺ + %s → %s↓"%(p[0],p[5]) if p[6]=='AgNO3' and p[3]['AgNO3']!='—' else ("Ba²⁺ + SO4²⁻ → BaSO4↓" if p[0]=='SO4²⁻' else ("CO3²⁻ + 2H⁺ → CO2↑ + H2O" if p[0]=='CO3²⁻' else '—'))) for p in pick),
         "%s: %s mol → **%s %s**"%(tgt[1],f2(n,3),f2(mp),'g' if prod!='CO2' else 'l'),
         "Cho'kmalar: %s; umumiy massa **%s g**%s"%(', '.join(forms),f2(tot),' (Ag3PO4 uchun n(Ag3PO4) = n(Na3PO4))' if any(p[0].startswith('PO4') for p in pick) else ''),
         "Cl⁻ + Ag⁺ → AgCl (oq), Br⁻ → AgBr (och sariq), I⁻ → AgI (sariq), SO4²⁻ + Ba²⁺ → BaSO4 (oq), CO3²⁻ + H⁺ → CO2 (gaz). Har bir ion o'ziga xos cho'kma yoki gaz hosil qilishi bilan aniqlanadi"]
    nag=sum(n*({'PO4³⁻':3,'CO3²⁻':2}.get(p[0],1)) for p in pick if p[3]['AgNO3']!='—')
    bands.append("Uchala eritmaning har biriga %s mol dan solingan. AgNO3 bilan cho'kadigan ionlarni to'liq cho'ktirish uchun 10 %% li AgNO3 eritmasidan necha gramm kerak?"%fmt(n,2)); sol.append("n(AgNO3) = %s mol → m = %s·170/0,1 = **%s g**"%(fmt(nag,2),fmt(nag,2),fmt(nag*170/0.1,1)))
    return W("43",text,bands,sol,SC41)
TR=[('Al',27,1.5,'Fe',56,'Fe(OH)3',107,'Fe(OH)2'),('Al',27,1.5,'Mg',24,'Mg(OH)2',58,'Mg(OH)2'),('Zn',65,1.0,'Fe',56,'Fe(OH)3',107,'Fe(OH)2'),('Zn',65,1.0,'Mg',24,'Mg(OH)2',58,'Mg(OH)2')]
def w43_alloy3(r):
    A,MA,hA,B,MB,hyd,Mhyd,hyd0=r.choice(TR); a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); c=r.choice([0.1,0.05]); mass=a*MA+b*MB+c*64
    h2_naoh=a*hA*22.4; h2_hcl=(a*hA+b)*22.4; no2=c*2*22.4; ppt=b*Mhyd
    text="%s, %s va misdan iborat %s g aralashma mo'l NaOH eritmasi bilan reaksiyaga kirishganda %s l (n.sh.) vodorod ajraldi. Xuddi shunday tarkibli %s g aralashma mo'l xlorid kislota bilan reaksiyaga kirishganda esa %s l (n.sh.) vodorod ajraldi."%({'Al':'Alyuminiy','Zn':'Rux'}[A],{'Fe':'temir','Mg':'magniy'}[B],f2(mass),f2(h2_naoh),f2(mass),f2(h2_hcl))
    bands=["Aralashmadagi har bir metallning massasini (g) va massa ulushini (%) aniqlang (reaksiya tenglamalarini yozing).","Xlorid kislota bilan reaksiyadan keyin qolgan qoldiq konsentrlangan HNO3 da to'liq eritildi. Ajralgan gazning hajmini (l, n.sh.) hisoblang.","Xlorid kislota bilan olingan eritmaga mo'l NaOH qo'shildi, cho'kma ajratib olinib, %s. Cho'kma massasini (g) toping."%("havoda to'liq oksidlandi" if B=='Fe' else "quritildi"),"Hosil bo'lgan Cu(NO3)2 eritmasi bug'latilib, quruq tuz qizdirilganda hosil bo'ladigan qattiq qoldiq massasini (g) va gazlar aralashmasining hajmini (l, n.sh.) aniqlang."]
    sol=["NaOH bilan faqat %s reaksiyaga kirishadi: n(%s) = %s mol = %s g; HCl bilan: n(%s) = %s mol = %s g; Cu = %s g. ω: %s %s %%, %s %s %%, Cu %s %%"%(A,A,f2(a),f2(a*MA),B,f2(b),f2(b*MB),f2(c*64),A,f2(a*MA/mass*100,1),B,f2(b*MB/mass*100,1),f2(c*64/mass*100,1)),
     "Cu + 4HNO3(kons.) → Cu(NO3)2 + 2NO2 + 2H2O: NO2 %s mol → **%s l**"%(f2(c*2),f2(no2)),
     "%s + 2NaOH → %s↓ + 2NaCl; %s: **%s g**"%(B+'Cl2',hyd0,('4Fe(OH)2 + O2 + 2H2O → 4Fe(OH)3' if B=='Fe' else 'Mg(OH)2 o\'zgarmaydi'),f2(ppt)),
     "2Cu(NO3)2 → 2CuO + 4NO2 + O2: CuO %s mol = **%s g**; gazlar %s mol → **%s l**"%(f2(c),f2(c*80),f2(2.5*c,3),f2(2.5*c*22.4))]
    nhcl=2*(a*hA+b)
    bands.append("Ushbu aralashma (butun massasi) to'liq reaksiyaga kirishishi uchun 20 % li HCl eritmasidan necha gramm kerak (mis reaksiyaga kirishmaydi)?"); sol.append("n(HCl) = 2·(%s + %s) = %s mol → m = %s·36,5/0,2 = **%s g**"%(fmt(a*hA,2),fmt(b,2),fmt(nhcl,2),fmt(nhcl,2),fmt(nhcl*36.5/0.2,1)))
    return W("43",text,bands,sol,SC41)
W43N=[w43_nit2,w43_anion,w43_alloy3]
