from core import *
import math
def f2(x,nd=2): return fmt(x,nd)
def Nq(text,ans,wr,sol,src,nd=2):
    q=numq(text,ans,wr,sol,src,nd); q.kind='calc'; return q
# ============================================================ 36: murakkab OQR (elektron balans)
OQH=[
('KMnO4 + KI + H2SO4 -> MnSO4 + I2 + K2SO4 + H2O','KMnO4','KI',"Mn⁺⁷ + 5e⁻ → Mn⁺² (2); 2I⁻ − 2e⁻ → I2⁰ (5)"),
('K2Cr2O7 + KI + H2SO4 -> Cr2(SO4)3 + I2 + K2SO4 + H2O','K2Cr2O7','KI',"2Cr⁺⁶ + 6e⁻ → 2Cr⁺³ (1); 2I⁻ − 2e⁻ → I2⁰ (3)"),
('Fe + H2SO4 -> Fe2(SO4)3 + SO2 + H2O','H2SO4','Fe',"S⁺⁶ + 2e⁻ → S⁺⁴ (3); Fe⁰ − 3e⁻ → Fe⁺³ (2)"),
('Zn + HNO3 -> Zn(NO3)2 + N2O + H2O','HNO3','Zn',"2N⁺⁵ + 8e⁻ → 2N⁺¹ (1); Zn⁰ − 2e⁻ → Zn⁺² (4)"),
('C + HNO3 -> CO2 + NO2 + H2O','HNO3','C',"N⁺⁵ + 1e⁻ → N⁺⁴ (4); C⁰ − 4e⁻ → C⁺⁴ (1)"),
('KMnO4 + Na2SO3 + H2O -> MnO2 + Na2SO4 + KOH','KMnO4','Na2SO3',"Mn⁺⁷ + 3e⁻ → Mn⁺⁴ (2); S⁺⁴ − 2e⁻ → S⁺⁶ (3)"),
('H2S + HNO3 -> H2SO4 + NO2 + H2O','HNO3','H2S',"N⁺⁵ + 1e⁻ → N⁺⁴ (8); S⁻² − 8e⁻ → S⁺⁶ (1)"),
('Mg + HNO3 -> Mg(NO3)2 + NH4NO3 + H2O','HNO3','Mg',"N⁺⁵ + 8e⁻ → N⁻³ (1); Mg⁰ − 2e⁻ → Mg⁺² (4)"),
('Al + HNO3 -> Al(NO3)3 + N2O + H2O','HNO3','Al',"2N⁺⁵ + 8e⁻ → 2N⁺¹ (3); Al⁰ − 3e⁻ → Al⁺³ (8)"),
('P + HNO3 + H2O -> H3PO4 + NO','HNO3','P',"N⁺⁵ + 3e⁻ → N⁺² (5); P⁰ − 5e⁻ → P⁺⁵ (3)"),
('FeSO4 + KMnO4 + H2SO4 -> Fe2(SO4)3 + MnSO4 + K2SO4 + H2O','KMnO4','FeSO4',"Mn⁺⁷ + 5e⁻ → Mn⁺² (1); 2Fe⁺² − 2e⁻ → 2Fe⁺³ (5)"),
('Cu + H2SO4 -> CuSO4 + SO2 + H2O','H2SO4','Cu',"S⁺⁶ + 2e⁻ → S⁺⁴ (1); Cu⁰ − 2e⁻ → Cu⁺² (1)")]
def h36(r):
    eq,ox,rd,eb=r.choice(OQH); b=balance(eq); co={s:c for s,c in b}
    nL=len(eq.split('->')[0].split(' + '))
    ask=r.choice(['all','react','oxred'])
    show=eq.replace('->','→')
    if ask=='all': a=sum(c for _,c in b); t="%s reaksiya tenglamasini elektron balans usulida tenglang va barcha koeffitsiyentlar yig'indisini aniqlang."%show
    elif ask=='react': a=sum(c for _,c in b[:nL]); t="%s reaksiya tenglamasini tenglang. Reagentlar (chap qism) koeffitsiyentlari yig'indisini toping."%show
    else: a=co[ox]+co[rd]; t="%s reaksiya tenglamasini tenglang. Oksidlovchi va qaytaruvchi oldidagi koeffitsiyentlar yig'indisini aniqlang."%show
    left=' + '.join('%s%s'%(str(c) if c>1 else '',s) for s,c in b[:nL]); right=' + '.join('%s%s'%(str(c) if c>1 else '',s) for s,c in b[nL:])
    sol="Elektron balans: %s; tenglama: %s → %s; oksidlovchi %s (%d), qaytaruvchi %s (%d) → yig'indi %d"%(eb,left,right,ox,co[ox],rd,co[rd],a)
    return Nq(t,a,[a+1,a-1,a+2,a-2 if a>4 else a+3],sol,"Tirkashev V bob (OQR, murakkab)",0)
# ============================================================ 37: umumiy kimyo (murakkab)
def h37_ser(r):
    n1=r.choice([0.05,0.1,0.2]); ne=2*n1; mAg=ne*108; mCu=n1*64; vO2=ne/4*22.4
    q=Nq("Ketma-ket ulangan ikkita elektrolizyordan (CuSO4 va AgNO3 eritmalari, inert elektrodlar) tok o'tkazildi. Birinchi elektrolizyor katodida %s g mis ajraldi. Ikkala elektrolizyor anodlarida ajralgan kislorodning umumiy hajmini (l, n.sh.) toping (anodda ikkalasida ham O2 ajraladi)."%f2(mCu,2),(ne/4+ne/4)*22.4,[vO2,vO2*4,(ne/2+ne/4)*22.4,ne*22.4],"n(Cu) = %s mol → n(e⁻) = 2·%s = %s mol; har bir elektrolizyorda anodda n(O2) = %s/4 = %s mol; jami = 2·%s = %s mol → %s l"%(f2(n1,3),f2(n1,3),f2(ne,3),f2(ne,3),f2(ne/4,3),f2(ne/4,3),f2(ne/2,3),f2(ne/2*22.4,2)),"Tirkashev V bob (elektroliz, Faradey)",2)
    return q
def h37_eq(r):
    al=r.choice([0.25,0.5,0.2,0.4]); V=r.choice([1,2,4]); n0=r.choice([1,2,4]); M0=92
    Mav=M0/(1+al); D=Mav/2
    K=(2*al*n0/V)**2/((1-al)*n0/V)
    return Nq("%d l hajmli yopiq idishda %d mol N2O4 qizdirilganda N2O4 ⇄ 2NO2 muvozanati qaror topdi. Muvozanat aralashmasining vodorodga nisbatan zichligi %s ga teng. Shu haroratdagi muvozanat konstantasini (K, mol/l) hisoblang."%(V,n0,f2(D,2)),K,[K*2,K/2,K*V,al*100],"M(o'rt.) = 2·%s = %s; M = 92/(1 + α) → α = %s; muvozanat: [N2O4] = %s, [NO2] = %s mol/l; K = [NO2]²/[N2O4] = %s"%(f2(D,2),f2(Mav,2),f2(al,2),f2((1-al)*n0/V,3),f2(2*al*n0/V,3),f2(K,3)),"Tirkashev VI bob (muvozanat, gaz zichligi)",3)
def h37_gascomb(r):
    x=r.choice([10,20,30,40]); y=r.choice([10,20,30,40]); V=x+y
    contr=2*x+1.5*y
    return Nq("CH4 va H2 dan iborat %s ml aralashma mo'l kisloroda yondirildi (suv suyuq holatda; hajmlar bir xil sharoitda o'lchandi). Reaksiyadan so'ng gazlar hajmi %s ml ga kamaydi. Aralashmadagi CH4 hajmini (ml) toping."%(fmt(V,0),fmt(contr,1)),x,[y,x*2,x/2,V-contr],"CH4 + 2O2 → CO2 + 2H2O(s): ΔV = 2x; 2H2 + O2 → 2H2O(s): ΔV = 1,5y; x + y = %s; 2x + 1,5y = %s → x = %s ml"%(fmt(V,0),fmt(contr,1),fmt(x,0)),"11-sinf (gaz qonunlari, Gey-Lyussak)",0)
def h37_ph(r):
    cand=[]
    for ca in (0.05,0.1,0.02,0.01,0.025):
        for Va in (0.1,0.2,0.25,0.3,0.4,0.5,0.6,0.7,0.75,0.8):
            for cb in (0.05,0.1,0.02,0.01,0.025):
                Vb=1-Va; d=2*ca*Va-2*cb*Vb
                for k in (1,2,3):
                    if abs(abs(d)-10**-k)<1e-12: cand.append((ca,Va,cb,Vb,d,k))
    ca,Va,cb,Vb,d,k=r.choice(cand); pH=k if d>0 else 14-k
    return Nq("H2SO4 ning %s mol/l li eritmasidan %s l va Ba(OH)2 ning %s mol/l li eritmasidan %s l aralashtirildi (umumiy hajm 1 l, ikkala modda to'liq dissotsilanadi, BaSO4 cho'kmasi e'tiborga olinmasin). Hosil bo'lgan eritmaning pH ini aniqlang."%(f2(ca,3),f2(Va,2),f2(cb,3),f2(Vb,2)),pH,[pH+1,pH-1 if pH>2 else pH+3,14-pH,pH+2],"n(H⁺) = 2·%s·%s = %s mol; n(OH⁻) = 2·%s·%s = %s mol; ortiqcha %s: %s mol/1 l = 10⁻%d → pH = %d"%(f2(ca,3),f2(Va,2),f2(2*ca*Va,4),f2(cb,3),f2(Vb,2),f2(2*cb*Vb,4),'H⁺' if d>0 else 'OH⁻',f2(abs(d),4),k,pH),"Tirkashev V bob (pH, neytrallash)",0)
def h37_vant(r):
    g=r.choice([2,3]); t1=r.choice([24,72,48]); dT=r.choice([20,30]); k=dT//10; fac=2**r.choice([1,2])
    t2=t1/(g**k*fac*1.0)
    if abs(t2-round(t2,1))>1e-9: return h37_vant(r)
    return Nq("Reaksiya 30 °C da %d minutda tugaydi. γ = %d. Harorat %d °C ga oshirilib, reagentlardan birining konsentratsiyasi %d marta oshirildi (reaksiya shu modda bo'yicha 1-tartibli). Reaksiya necha minutda tugaydi?"%(t1,g,dT,fac),t2,[t1/g**k,t1/fac,t2*2,t2/2],"v₂/v₁ = %d^%d · %d = %d; t₂ = %d/%d = %s min"%(g,k,fac,g**k*fac,t1,g**k*fac,f2(t2,2)),"Tirkashev VI bob (Vant-Goff, tartib)",2)
# ============================================================ 38: anorganik (murakkab)
def h38_alloy(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); c=r.choice([0.1,0.05]); m=a*27+b*56+c*64
    vn=a*1.5*22.4; vh=(a*1.5+b)*22.4
    return Nq("Al, Fe va Cu dan iborat aralashma mo'l NaOH eritmasi bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi; xuddi shunday massadagi aralashma mo'l HCl bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi, erimagan qoldiq 6,4 g Cu bo'lsa... Aralashmaning dastlabki massasini (g) toping."%(f2(vn,2),f2(vh,2)) if False else "Al, Fe va Cu dan iborat aralashma mo'l NaOH eritmasi bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi; xuddi shunday massadagi aralashma mo'l HCl bilan ta'sirlashganda %s l (n.sh.) vodorod ajraldi, erimay qolgan qoldiq (mis) massasi %s g. Aralashmaning dastlabki massasini (g) toping."%(f2(vn,2),f2(vh,2),f2(c*64,2)),m,[a*27+b*56,m*2,m/2,m-c*64],"NaOH bilan faqat Al: n(Al) = %s/1,5/22,4 = %s mol (%s g); HCl bilan Al va Fe: n(Fe) = %s/22,4 − 1,5·%s = %s mol (%s g); Cu = %s g; jami = %s g"%(f2(vn,2),f2(a,2),f2(a*27,2),f2(vh,2),f2(a,2),f2(b,2),f2(b*56,2),f2(c*64,2),f2(m,2)),"9-sinf (Al, Fe, Cu)",2)
def h38_carb(r):
    a=r.choice([0.1,0.2,0.3]); b=r.choice([0.1,0.2]); m=a*100+b*84; res=m-(a+b)*44
    return Nq("CaCO3 va MgCO3 dan iborat %s g aralashma doimiy massagacha qizdirilganda qoldiq massasi %s g bo'ldi. Aralashmadagi CaCO3 ning massasini (g) toping."%(f2(m,2),f2(res,2)),a*100,[b*84,a*100*2,a*100/2,m-res],"Ajralgan CO2 = %s − %s = %s g = %s mol; x + y = %s; 100x + 84y = %s → x = %s mol → %s g"%(f2(m,2),f2(res,2),f2(m-res,2),f2((m-res)/44,3),f2((m-res)/44,3),f2(m,2),f2(a,2),f2(a*100,2)),"9-sinf (karbonatlar, termik parchalanish)",2)
def h38_halide(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.05,0.1]); m=a*103+b*150; res=(a+b)*58.5
    return Nq("NaBr va NaI dan iborat %s g aralashma eritilib, mo'l xlor o'tkazildi, eritma bug'latilib quruq qoldiq %s g chiqdi. Aralashmadagi NaI ning massasini (g) toping."%(f2(m,2),f2(res,2)),b*150,[a*103,b*150*2,b*150/2,(a+b)*58.5],"x + y = %s/58,5 = %s mol; 103x + 150y = %s → y = %s mol → %s g"%(f2(res,2),f2(a+b,3),f2(m,2),f2(b,3),f2(b*150,2)),"9-sinf (galogenlar)",2)
def h38_nitr(r):
    n=r.choice([0.2,0.4]); fr=r.choice([0.25,0.5]); dec=n*fr; res=n*188-dec*108
    return Nq("%s g Cu(NO3)2 qizdirilganda qisman parchalandi, qattiq qoldiq massasi %s g bo'ldi. Ajralgan gazlar (n.sh.) hajmini (l) hisoblang."%(f2(n*188,2),f2(res,2)),dec*2.5*22.4,[dec*22.4,dec*4*22.4,dec*2.5,n*2.5*22.4],"Massa kamayishi = %s − %s = %s g; 2Cu(NO3)2 → 2CuO + 4NO2 + O2: 108 g kamayish ⇔ 2 mol parchalanish → %s mol; gazlar 2,5·%s = %s mol → %s l"%(f2(n*188,2),f2(res,2),f2(dec*108,2),f2(dec,3),f2(dec,3),f2(dec*2.5,3),f2(dec*2.5*22.4,2)),"9-sinf (nitratlar termik parchalanishi)",2)
def h38_p(r):
    n=r.choice([0.2,0.4]); k=r.choice([1.5,2.5]);
    x=n*k-n if k==1.5 else None
    if k==1.5: m_=n*0.5*120+n*0.5*142; txt="NaOH : H3PO4 = 1,5 : 1"; sol="NaH2PO4 va Na2HPO4: x + y = %s; x + 2y = %s → x = y = %s mol; m = %s·120 + %s·142 = %s g"%(f2(n,2),f2(n*1.5,2),f2(n/2,3),f2(n/2,3),f2(n/2,3),f2(m_,2))
    else:
        m_=n*0.5*142+n*0.5*164; txt="NaOH : H3PO4 = 2,5 : 1"; sol="Na2HPO4 va Na3PO4: x + y = %s; 2x + 3y = %s → x = y = %s mol; m = %s·142 + %s·164 = %s g"%(f2(n,2),f2(n*2.5,2),f2(n/2,3),f2(n/2,3),f2(n/2,3),f2(m_,2))
    return Nq("%s g fosfor yondirib hosil bo'lgan oksid suvda eritildi, so'ng eritmaga %s mol NaOH qo'shildi (%s). Hosil bo'lgan tuzlar umumiy massasini (g) toping."%(f2(n*31,2),f2(n*k,2),txt),m_,[m_*2,m_/2,n*142,n*164],sol,"9-sinf (fosfor va uning birikmalari)",2)
def h38_hard(r):
    ca=r.choice([0.01,0.02,0.04]); mg=r.choice([0.01,0.02]); V=r.choice([10,50,100])
    return Nq("%d m³ suvda Ca(HCO3)2 konsentratsiyasi %s mol/m³, Mg(HCO3)2 niki %s mol/m³. Suvni Ca(OH)2 bilan to'liq yumshatish uchun Ca(OH)2 ning massasini (kg) hisoblang."%(V,f2(ca*1000,0),f2(mg*1000,0)),(ca+2*mg)*1000*V*74/1000,[(ca+mg)*1000*V*74/1000,(ca+2*mg)*1000*V*100/1000,(ca+2*mg)*1000*V*37/1000,(2*ca+mg)*1000*V*74/1000],"Ca(HCO3)2 + Ca(OH)2 → 2CaCO3 + 2H2O (1:1); Mg(HCO3)2 + 2Ca(OH)2 → Mg(OH)2 + 2CaCO3 + 2H2O (1:2): n = %s + 2·%s = %s mol → %s kg"%(f2(ca*1000*V,0),f2(mg*1000*V,0),f2((ca+2*mg)*1000*V,0),f2((ca+2*mg)*1000*V*74/1000,2)),"9-sinf (suv qattiqligi)",2)
# ============================================================ 39–40: organik (murakkab)
def h39_two(r):
    n=r.choice([0.1,0.2,0.5]); y1=r.choice([80,75,90]); y2=r.choice([80,75,60])
    m=n*46; a=n*y1/100*y2/100*88
    return Nq("%s g etanol avval sirka aldegidgacha (unum %d %%), so'ng sirka kislotagacha (unum %d %%) oksidlandi; hosil bo'lgan kislota mo'l etanol bilan efirlandi (unum 100 %%). Etilatsetat massasini (g) toping."%(f2(m,2),y1,y2),a,[n*88,a*2,a/2,n*y1/100*88],"n(C2H5OH) = %s mol → CH3CHO: %s·%s = %s mol → CH3COOH: ·%s = %s mol → CH3COOC2H5: %s·88 = %s g"%(f2(n,2),f2(n,2),f2(y1/100,2),f2(n*y1/100,3),f2(y2/100,2),f2(n*y1/100*y2/100,3),f2(n*y1/100*y2/100,3),f2(a,2)),"10-sinf (spirt, aldegid, kislota, efir)",2)
def h39_alk(r):
    a=r.choice([0.1,0.05,0.15]); b=r.choice([0.1,0.05]); V=(a+b)*22.4; mBr=a*160+b*320
    return Nq("Etilen va asetilendan iborat %s l (n.sh.) aralashma bromli suvdan o'tkazilganda %s g brom yutildi. Aralashmadagi asetilenning hajmini (l, n.sh.) toping."%(f2(V,2),f2(mBr,2)),b*22.4,[a*22.4,b*22.4*2,b*22.4/2,mBr/160*22.4],"x + y = %s mol; C2H4 + Br2: x; C2H2 + 2Br2: 2y → 160x + 320y = %s → y = %s mol → %s l"%(f2(a+b,3),f2(mBr,2),f2(b,3),f2(b*22.4,2)),"10-sinf (alkenlar va alkinlar)",2)
def h39_glu(r):
    n=r.choice([0.5,1]); y1=r.choice([80,90]); y2=r.choice([80,75]);
    nac=2*n*y1/100*y2/100; naoh=nac*40
    return Nq("%s g glyukoza spirtli bijg'ish natijasida etanolga (unum %d %%), hosil bo'lgan etanol esa sirka kislotagacha (unum %d %%) aylantirildi. Olingan kislotani to'liq neytrallash uchun NaOH ning massasini (g) toping."%(f2(n*180,1),y1,y2),naoh,[nac*98,naoh*2,naoh/2,n*2*40],"n(glyukoza) = %s mol → C2H5OH: 2·%s·%s = %s mol → CH3COOH: ·%s = %s mol → NaOH %s·40 = %s g"%(f2(n,2),f2(n,2),f2(y1/100,2),f2(2*n*y1/100,3),f2(y2/100,2),f2(nac,3),f2(nac,3),f2(naoh,2)),"10-sinf (uglevodlar, spirt, kislota)",2)
def h39_ph(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); m=a*46+b*94
    return Nq("Etanol va fenoldan iborat %s g aralashma natriy bilan to'liq reaksiyaga kirishganda %s l (n.sh.) vodorod ajraldi. Shu aralashmaga mo'l bromli suv ta'sir ettirilganda hosil bo'ladigan cho'kma massasini (g) toping."%(f2(m,2),f2((a+b)/2*22.4,2)),b*331,[a*331,b*331*2,b*331/2,b*94],"x + y = 2·%s/22,4 = %s; 46x + 94y = %s → fenol y = %s mol; C6H5OH + 3Br2 → C6H2Br3OH↓: %s·331 = %s g"%(f2((a+b)/2*22.4,2),f2(a+b,2),f2(m,2),f2(b,2),f2(b,2),f2(b*331,2)),"10-sinf (spirt va fenol)",2)
def h39_est(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2])
    m=a*88+b*74
    return Nq("Etilatsetat va metilatsetat dan iborat %s g aralashma mo'l NaOH eritmasi bilan to'liq gidrolizlandi. Hosil bo'lgan spirtlar umumiy massasini (g) toping."%f2(m,2),a*46+b*32,[a*32+b*46,(a+b)*46,(a*46+b*32)*2,m/2],"CH3COOC2H5 (88) + NaOH → C2H5OH (46); CH3COOCH3 (74) → CH3OH (32); x = %s, y = %s mol (M ga ko'ra: 88x + 74y = %s); spirt: %s·46 + %s·32 = %s g"%(f2(a,2),f2(b,2),f2(m,2),f2(a,2),f2(b,2),f2(a*46+b*32,2)),"10-sinf (murakkab efirlar gidrolizi)",2)
def h40_pol(r):
    mon,Mm,nm=r.choice([('C2H4',28,'polietilen'),('C3H6',42,'polipropilen'),('C8H8',104,'polistirol'),('C2H3Cl',62.5,'polivinilxlorid')]); D=r.choice([500,1000,2000]); y=r.choice([80,90,50]);
    mp=D*Mm*1000/ (1000) # g/mol * ... use 1 mol polymer
    n=r.choice([0.001,0.002,0.005]); mpoly=n*D*Mm; mmon=mpoly/(y/100)
    return Nq("%s polimerining (polimerlanish darajasi %d) %s g namunasini olish uchun polimerlanish unumi %d %% bo'lganda qancha monomer (%s) kerak (g)?"%(nm.capitalize(),D,f2(mpoly,2),y,mon),mmon,[mpoly,mmon*2,mmon/2,mpoly*y/100],"M(polimer) = %d·%s = %s g/mol; n(polimer) = %s/%s = %s mol → monomer: %s·%d = %s mol (nazariy); amaliy: /%s → %s g"%(D,fmt(Mm),f2(D*Mm,1),f2(mpoly,2),f2(D*Mm,1),f2(n,4),f2(n,4),D,f2(n*D,2),f2(y/100,2),f2(mmon,2)),"10-sinf (YuMB, polimerlanish)",2)
def h40_ani(r):
    n=r.choice([0.1,0.2,0.5]); y1=r.choice([80,90]); y2=r.choice([80,75,100])
    nan=n*y1/100; mbr=nan*y2/100*330
    return Nq("%s g nitrobenzol anilinga qaytarildi (unum %d %%), hosil bo'lgan anilin mo'l bromli suv bilan reaksiyaga kirishdi (unum %d %%). Hosil bo'lgan 2,4,6-tribromanilin (M = 330 g/mol) massasini (g) toping."%(f2(n*123,2),y1,y2),mbr,[n*330,mbr*2,mbr/2,nan*330],"n(C6H5NO2) = %s mol → C6H5NH2: %s·%s = %s mol → C6H2Br3NH2: ·%s = %s mol → %s·330 = %s g"%(f2(n,2),f2(n,2),f2(y1/100,2),f2(nan,3),f2(y2/100,2),f2(nan*y2/100,3),f2(nan*y2/100,3),f2(mbr,2)),"10-sinf (aminlar, anilin)",2)
def h40_form(r):
    pick=r.choice([('C4H10',58,82.76,4,10),('C5H12',72,83.33,5,12),('C3H8',44,81.82,3,8),('C6H14',86,83.72,6,14)])
    f,M_,w,c,h=pick; sig=c-1+h
    return Nq("Alkanning vodorodga nisbatan zichligi %s, uglerodning massa ulushi %s %%. Shu alkan molekulasidagi σ-bog'lar umumiy sonini toping."%(f2(M_/2,1),f2(w,2)),sig,[sig+1,sig-1,c+h,sig+2],"M = 2·%s = %s; n(C) = %s·%s/12 = %d; CnH2n+2 → %s; σ = (n − 1) + (2n + 2) = %d"%(f2(M_/2,1),fmt(M_),fmt(M_),f2(w/100,4),c,f,sig),"10-sinf (alkanlar, kovalent bog'lar)",0)
def h40_fat(r):
    n=r.choice([0.01,0.02,0.05]); y=r.choice([80,90])
    mfat=n*890; msoap=3*n*306*y/100
    return Nq("%s g tristearin mo'l NaOH eritmasi bilan to'liq gidrolizlandi (sovun unumi %d %%). Hosil bo'lgan natriy stearat (M = 306 g/mol) massasini (g) toping."%(f2(mfat,2),y),msoap,[3*n*306,msoap*2,msoap/2,n*306*y/100],"n(yog') = %s/890 = %s mol; (C17H35COO)3C3H5 + 3NaOH → 3C17H35COONa + C3H5(OH)3: %s·3·306 = %s g; unum %d %% → %s g"%(f2(mfat,2),f2(n,3),f2(n,3),f2(3*n*306,2),y,f2(msoap,2)),"10-sinf (yog'lar, sovun)",2)
H36=[h36]; H37=[h37_ser,h37_eq,h37_gascomb,h37_ph,h37_vant]; H38=[h38_alloy,h38_carb,h38_halide,h38_nitr,h38_p,h38_hard]; H39=[h39_two,h39_alk,h39_glu,h39_ph,h39_est]; H40=[h40_pol,h40_ani,h40_form,h40_fat]
