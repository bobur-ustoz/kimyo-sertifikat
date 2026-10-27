from core import *
from more3 import W,SC43,SC41,f2
import math
# ===================================================================== 43 — anorganik kimyo (yangi turlar)
def w43_s_chain(r):
    n=r.choice([0.5,1,2]); e1=r.choice([80,90,100]); e2=r.choice([80,90]); m=n*120
    so2=2*n; so2r=so2*e1/100; so3=so2r*e2/100; h2so4=so3; mh=h2so4*98; naoh=2*h2so4*40; ba=h2so4*233
    text="%s g pirit (FeS2) yondirildi: 4FeS2 + 11O2 → 2Fe2O3 + 8SO2 (unum %d %%). Hosil bo'lgan SO2 katalizator ishtirokida SO3 gacha oksidlandi (unum %d %%), SO3 suvda eritildi."%(f2(m,1),e1,e2)
    bands=["Hosil bo'lgan SO2 hajmini (l, n.sh.) va qattiq qoldiq Fe2O3 massasini (g) hisoblang.","SO3 ning massasini (g) toping (2SO2 + O2 ⇄ 2SO3).","Hosil bo'lgan H2SO4 massasini (g) aniqlang.","Shu kislotani to'liq neytrallash uchun zarur NaOH massasini (g) va mo'l BaCl2 bilan hosil bo'ladigan cho'kma massasini (g) toping."]
    fe2o3=n*0.5*160*e1/100
    sol=["n(FeS2) = %s mol; SO2: 2n·η = %s mol → **%s l**; Fe2O3: n/2·η·160 = **%s g**"%(f2(n,2),f2(so2r,3),f2(so2r*22.4,2),f2(fe2o3,2)),"n(SO3) = %s·%s = %s mol → **%s g**"%(f2(so2r,3),f2(e2/100,2),f2(so3,3),f2(so3*80,2)),"SO3 + H2O → H2SO4: **%s g**"%f2(mh,2),"NaOH: 2·%s·40 = **%s g**; BaSO4: %s·233 = **%s g**"%(f2(h2so4,3),f2(naoh,2),f2(h2so4,3),f2(ba,2))]
    bands.append("Shu H2SO4 dan 20 % li eritma tayyorlash uchun qancha suv (g) kerak?"); sol.append("m(eritma) = %s/0,2 = %s g; suv = %s − %s = **%s g**"%(fmt(mh,2),fmt(mh/0.2,2),fmt(mh/0.2,2),fmt(mh,2),fmt(mh/0.2-mh,2)))
    bands[0]+=" Shuningdek SO2 massasini (g) ham toping."; sol[0]+="; m(SO2) = %s·64 = **%s g**"%(f2(so2r,3),f2(so2r*64,2))
    return W("43",text,bands,sol,SC41)
def w43_p_chain(r):
    n=r.choice([0.2,0.4,0.1]); k=r.choice([2,3]); koh='NaOH'
    h3=n; naoh=n*k; 
    prod={2:('Na2HPO4',142),3:('Na3PO4',164)}[k]
    mp=n*prod[1]; ca=n*164/2*0 
    text="%s g qizil fosfor mo'l kislorodda yondirildi, hosil bo'lgan oksid suvda to'liq eritildi (ortofosfat kislota). Eritmaga %s mol NaOH qo'shildi."%(f2(n*31,2),f2(naoh,2))
    bands=["Reaksiya tenglamalarini yozing. Hosil bo'lgan P2O5 massasini (g) hisoblang.","Hosil bo'lgan H3PO4 massasini (g) toping.","Eritmada qanday tuz hosil bo'lganini aniqlang va uning massasini (g) hisoblang.","Hosil bo'lgan tuz eritmasiga mo'l CaCl2 qo'shilganda cho'kadigan Ca3(PO4)2 massasini (g) toping (faqat %s ioni uchun)."%'PO₄³⁻']
    ppt=n/2*310 if k==3 else 0
    if k==2: bands[3]="Hosil bo'lgan eritmani to'liq neytrallash uchun yana qancha NaOH (g) kerak (Na2HPO4 → Na3PO4)?"; ppt=None
    sol=["4P + 5O2 → 2P2O5: n(P2O5) = %s mol → **%s g**"%(f2(n/2,3),f2(n/2*142,2)),"P2O5 + 3H2O → 2H3PO4: n = %s mol → **%s g**"%(f2(n,3),f2(n*98,2)),"H3PO4 : NaOH = 1 : %d → **%s** %s mol = **%s g**"%(k,prod[0],f2(n,3),f2(mp,2)),("2Na3PO4 + 3CaCl2 → Ca3(PO4)2↓ + 6NaCl: %s mol → **%s g**"%(f2(n/2,3),f2(ppt,2)) if k==3 else "Na2HPO4 + NaOH → Na3PO4 + H2O: %s mol · 40 = **%s g**"%(f2(n,3),f2(n*40,2)))]
    bands.append("Hosil bo'lgan tuzning 10 % li eritmasi massasini (g) hisoblang."); sol.append("m(eritma) = %s/0,1 = **%s g**"%(fmt(mp,2),fmt(mp/0.1,2)))
    bands[1]+=" Kislotada fosforning massa ulushini (%) ham hisoblang."; sol[1]+="; ω(P) = 31/98 = **31,6 %**"
    return W("43",text,bands,sol,SC41)
def w43_n_chain(r):
    V=r.choice([44.8,89.6,22.4,67.2]); e1=r.choice([80,90]); e2=r.choice([80,100]); n=V/22.4
    no=n*e1/100; hno3=no*e2/100; mh=hno3*63; nh4=hno3; nh3_need=nh4*17; mnn=nh4*80
    text="%s l (n.sh.) ammiak katalizator ishtirokida kislorodda oksidlandi (4NH3 + 5O2 → 4NO + 6H2O, unum %d %%). Hosil bo'lgan NO ni nitrat kislotagacha qayta ishlash unumi %d %%."%(f2(V,1),e1,e2)
    bands=["Hosil bo'lgan NO hajmini (l, n.sh.) hisoblang.","Nitrat kislota ishlab chiqarishning keyingi bosqichlari tenglamalarini yozing va olingan HNO3 massasini (g) toping.","Hosil bo'lgan HNO3 ni to'liq neytrallash uchun zarur ammiak hajmini (l, n.sh.) aniqlang (NH3 + HNO3 → NH4NO3).","Hosil bo'lgan ammoniy nitrat massasini (g) hisoblang va azotning massa ulushini (%) toping."]
    sol=["n(NH3) = %s mol; n(NO) = %s·%s = %s mol → **%s l**"%(f2(n,2),f2(n,2),f2(e1/100,2),f2(no,3),f2(no*22.4,2)),"2NO + O2 → 2NO2; 4NO2 + O2 + 2H2O → 4HNO3: n(HNO3) = %s mol → **%s g**"%(f2(hno3,3),f2(mh,2)),"NH3 : HNO3 = 1 : 1 → **%s l**"%f2(nh4*22.4,2),"NH4NO3: %s mol · 80 = **%s g**; ω(N) = 28/80 = **35 %%**"%(f2(nh4,3),f2(mnn,2))]
    bands.append("Olingan HNO3 dan 63 % li eritma necha gramm tayyorlanadi?"); sol.append("m(eritma) = %s/0,63 = **%s g**"%(fmt(mh,2),fmt(mh/0.63,2)))
    bands[0]+=" Hosil bo'lgan NO ning massasini (g) ham toping."; sol[0]+="; m(NO) = %s·30 = **%s g**"%(f2(no,3),f2(no*30,2))
    return W("43",text,bands,sol,SC41)
def w43_carb(r):
    a=r.choice([0.1,0.2,0.3]); b=r.choice([0.1,0.2,0.05]); m=a*100+b*84
    co2=a+b; loss=co2*44; res=m-loss; hcl=2*(a+b)
    text="CaCO3 va MgCO3 dan iborat %s g aralashma doimiy massagacha qizdirildi. Ajralgan gaz mo'l Ca(OH)2 eritmasidan o'tkazildi."%f2(m,2)
    bands=["Aralashmadagi har bir tuzning massasini (g) va massa ulushini (%) aniqlang (reaksiya tenglamalarini yozing).","Ajralgan gaz hajmini (l, n.sh.) va qattiq qoldiq massasini (g) toping.","Gaz Ca(OH)2 eritmasidan o'tkazilganda hosil bo'lgan cho'kma massasini (g) hisoblang.","Qattiq qoldiqni to'liq eritish uchun 10 % li HCl eritmasidan necha gramm kerak?"]
    sol=["x·100 + y·84 = %s; x + y = %s → CaCO3 %s g (%s %%), MgCO3 %s g (%s %%)"%(f2(m,2),f2(co2,2),f2(a*100,1),f2(a*100/m*100,1),f2(b*84,2),f2(b*84/m*100,1)),"n(CO2) = %s mol → **%s l**; qoldiq CaO + MgO = **%s g**"%(f2(co2,2),f2(co2*22.4,2),f2(res,2)),"CO2 + Ca(OH)2 → CaCO3↓ + H2O: %s mol → **%s g**"%(f2(co2,2),f2(co2*100,2)),"CaO + 2HCl; MgO + 2HCl: n(HCl) = %s mol = %s g → 10 %% li eritma **%s g**"%(f2(hcl,2),f2(hcl*36.5,2),f2(hcl*36.5/0.1,1))]
    bands.append("Qoldiq oksidlar suvga solinganda hosil bo'ladigan Ca(OH)2 massasini (g) toping (CaO + H2O → Ca(OH)2)."); sol.append("n(CaO) = %s mol → m(Ca(OH)2) = %s·74 = **%s g**"%(fmt(a,2),fmt(a,2),fmt(a*74,2)))
    bands[1]+=" Qoldiqdagi CaO ning massa ulushini (%) ham hisoblang."; sol[1]+="; ω(CaO) = %s/%s = **%s %%**"%(f2(a*56,2),f2(res,2),f2(a*56/res*100,1))
    return W("43",text,bands,sol,SC41)
def w43_halo(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.05,0.15]); m=a*103+b*150
    nacl=(a+b)*58.5; loss=m-nacl; cl2=(a+b)/2*22.4
    text="NaBr va NaI dan iborat %s g aralashma suvda eritilib, mo'l xlor o'tkazildi. Eritma bug'latilib, qoldiq quritilganda uning massasi %s g bo'ldi."%(f2(m,2),f2(nacl,2))
    bands=["Reaksiya tenglamalarini yozing. Aralashmadagi NaBr va NaI massalarini (g) toping.","Sarflangan xlor hajmini (l, n.sh.) hisoblang.","Ajralgan brom va yodning massalarini (g) toping.","Dastlabki aralashma eritmasiga mo'l AgNO3 qo'shilganda hosil bo'ladigan cho'kmalar massasini (g) aniqlang."]
    br2=a/2*160; i2=b/2*254; ppt=a*188+b*235
    sol=["103x + 150y = %s; 58,5(x + y) = %s → n(NaBr) = %s mol (**%s g**), n(NaI) = %s mol (**%s g**)"%(f2(m,2),f2(nacl,2),f2(a,2),f2(a*103,2),f2(b,2),f2(b*150,2)),"2NaBr + Cl2 → 2NaCl + Br2; 2NaI + Cl2 → 2NaCl + I2: n(Cl2) = (x+y)/2 = %s mol → **%s l**"%(f2((a+b)/2,3),f2(cl2,2)),"Br2: **%s g**; I2: **%s g**"%(f2(br2,2),f2(i2,2)),"AgBr: %s·188 = %s g; AgI: %s·235 = %s g; jami **%s g**"%(f2(a,2),f2(a*188,2),f2(b,2),f2(b*235,2),f2(ppt,2))]
    bands.append("Ajralgan brom va yod aralashmasida bromning massa ulushini (%) toping."); sol.append("ω(Br2) = %s/(%s + %s) = **%s %%**"%(fmt(br2,2),fmt(br2,2),fmt(i2,2),fmt(br2/(br2+i2)*100,1)))
    bands[1]+=" Hosil bo'lgan NaCl miqdorini (mol) ham toping."; sol[1]+="; n(NaCl) = %s + %s = **%s mol**"%(f2(a,2),f2(b,2),f2(a+b,2))
    return W("43",text,bands,sol,SC41)
def w43_al(r):
    n=r.choice([0.1,0.2,0.05]); k=r.choice([3,4])
    naoh1=3*n; naoh2=4*n; ppt1=n*78; co2=n; ppt2=n*78
    text="%s mol AlCl3 saqlagan eritmaga NaOH eritmasi qo'shildi. Avval %s mol NaOH qo'shilganda cho'kma hosil bo'ldi, so'ng yana %s mol NaOH qo'shilganda cho'kma to'liq erib ketdi (Na[Al(OH)4] hosil bo'ldi)."%(f2(n,2),f2(naoh1,2),f2(n,2))
    bands=["Cho'kma hosil bo'lish va erish reaksiyalari tenglamalarini yozing. Cho'kma massasini (g) hisoblang.","Jami sarflangan NaOH massasini (g) aniqlang.","Hosil bo'lgan Na[Al(OH)4] eritmasidan mo'l CO2 o'tkazilganda cho'kadigan Al(OH)3 massasini (g) toping.","Al(OH)3 cho'kmasi qizdirilganda hosil bo'ladigan oksid massasini (g) hisoblang."]
    ox=ppt2/2/78*102 if False else n/2*102
    sol=["AlCl3 + 3NaOH → Al(OH)3↓ + 3NaCl; Al(OH)3 + NaOH → Na[Al(OH)4]; n(Al(OH)3) = %s mol → **%s g**"%(f2(n,2),f2(ppt1,2)),"n(NaOH) = %s + %s = %s mol → **%s g**"%(f2(naoh1,2),f2(n,2),f2(naoh2,2),f2(naoh2*40,2)),"Na[Al(OH)4] + CO2 → Al(OH)3↓ + NaHCO3: **%s g**"%f2(ppt2,2),"2Al(OH)3 → Al2O3 + 3H2O: n(Al2O3) = %s mol → **%s g**"%(f2(n/2,3),f2(ox,2))]
    bands.append("Na[Al(OH)4] eritmasining hajmi 500 ml bo'lsa, tuzning molyar konsentratsiyasini (mol/l) hisoblang."); sol.append("C = %s/0,5 = **%s mol/l**"%(fmt(n,2),fmt(n/0.5,2)))
    return W("43",text,bands,sol,SC41)
def w43_fe(r):
    n=r.choice([0.1,0.2,0.05]); m=n*56
    cl2=n*1.5*22.4; fecl3=n*162.5; fe2o3=n/2*160; i2=n/2*254
    text="%s g temir mo'l xlorda yondirildi. Hosil bo'lgan tuz suvda eritilib, avval ishqor bilan, so'ng boshqa porsiyasi KI eritmasi bilan ta'sirlashtirildi."%f2(m,2)
    bands=["Reaksiya tenglamasini yozing. Sarflangan xlor hajmini (l, n.sh.) va hosil bo'lgan tuz massasini (g) toping.","Tuz eritmasiga mo'l NaOH qo'shilganda hosil bo'lgan cho'kma massasini (g) aniqlang.","Cho'kma qizdirilganda hosil bo'ladigan oksid massasini (g) hisoblang.","Tuzning shunday miqdoriga mo'l KI qo'shilganda ajraladigan yod massasini (g) toping (2FeCl3 + 2KI → 2FeCl2 + 2KCl + I2)."]
    sol=["2Fe + 3Cl2 → 2FeCl3: V(Cl2) = %s·1,5·22,4 = **%s l**; m(FeCl3) = **%s g**"%(f2(n,2),f2(cl2,2),f2(fecl3,2)),"FeCl3 + 3NaOH → Fe(OH)3↓ + 3NaCl: %s·107 = **%s g**"%(f2(n,2),f2(n*107,2)),"2Fe(OH)3 → Fe2O3 + 3H2O: n = %s mol → **%s g**"%(f2(n/2,3),f2(fe2o3,2)),"n(I2) = %s/2 = %s mol → **%s g**"%(f2(n,2),f2(n/2,3),f2(i2,2))]
    bands.append("Hosil bo'lgan FeCl3 eritmasiga temir qo'shilib FeCl2 hosil qilindi (2FeCl3 + Fe → 3FeCl2). Sarflangan temir massasini (g) toping."); sol.append("n(Fe) = %s/2 = %s mol → **%s g**"%(fmt(n,2),fmt(n/2,3),fmt(n/2*56,2)))
    bands[0]+=" Hosil bo'lgan FeCl3 miqdorini (mol) ham toping."; sol[0]+="; n(FeCl3) = n(Fe) = **%s mol**"%f2(n,2)
    return W("43",text,bands,sol,SC41)
def w43_hard(r):
    ca=r.choice([0.01,0.02,0.04]); mg=r.choice([0.01,0.02]); V=r.choice([10,50,100])
    ncc=ca*V; nmg=mg*V
    boil=ncc*100; mgco3=nmg*84; soda=(ncc+nmg)*106
    text="%d m³ qattiq suvda Ca(HCO3)2 ning konsentratsiyasi %s mol/m³, Mg(HCO3)2 niki %s mol/m³ ga teng (1 m³ = 1000 l)."%(V,f2(ca*1000,0),f2(mg*1000,0))
    bands=["Suv qaynatilganda qanday reaksiyalar sodir bo'lishini yozing.","Qaynatish natijasida hosil bo'ladigan CaCO3 cho'kmasi massasini (kg) hisoblang.","Mg(HCO3)2 dan hosil bo'ladigan MgCO3 massasini (kg) toping.","Suvni yumshatish uchun sodadan (Na2CO3) necha kilogramm kerakligini hisoblang (Ca²⁺ va Mg²⁺ ni to'liq cho'ktirish uchun)."]
    ncc2=ca*1000*V/1000; nmg2=mg*1000*V/1000
    sol=["Ca(HCO3)2 → CaCO3↓ + CO2↑ + H2O; Mg(HCO3)2 → MgCO3↓ + CO2↑ + H2O","n(Ca(HCO3)2) = %s mol → m(CaCO3) = **%s kg**"%(f2(ca*1000*V,0),f2(ca*1000*V*100/1000,2)),"n(Mg(HCO3)2) = %s mol → m(MgCO3) = **%s kg**"%(f2(mg*1000*V,0),f2(mg*1000*V*84/1000,2)),"Ca²⁺ + CO3²⁻ → CaCO3; Mg²⁺ + CO3²⁻ → MgCO3: n(Na2CO3) = %s mol → **%s kg**"%(f2((ca+mg)*1000*V,0),f2((ca+mg)*1000*V*106/1000,2))]
    bands.append("Suvni ohak sutini (Ca(OH)2) bilan yumshatishda zarur Ca(OH)2 massasini (kg) hisoblang (Ca(HCO3)2 + Ca(OH)2 → 2CaCO3 + 2H2O; Mg(HCO3)2 + 2Ca(OH)2 → Mg(OH)2 + 2CaCO3 + 2H2O)."); sol.append("n(Ca(OH)2) = %s + 2·%s = %s mol → **%s kg**"%(fmt(ca*1000*V,0),fmt(mg*1000*V,0),fmt((ca+2*mg)*1000*V,0),fmt((ca+2*mg)*1000*V*74/1000,2)))
    bands[1]+=" Qaynatish bilan ajralgan CO2 hajmini (m³, n.sh.) ham hisoblang."; sol[1]+="; n(CO2) = n(Ca(HCO3)2) + n(Mg(HCO3)2) = %s mol → **%s m³**"%(f2((ca+mg)*1000*V,0),f2((ca+mg)*1000*V*22.4/1000,2))
    return W("43",text,bands,sol,SC41)
def w43_gasid(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2,0.05]); V=(a+b)*22.4
    text="SO2 va CO2 dan iborat %s l (n.sh.) gazlar aralashmasi avval mo'l bromli suvdan, so'ngra mo'l Ba(OH)2 eritmasidan o'tkazildi. Bromli suvdan o'tgandan keyin SO2 to'liq yutildi."%f2(V,2)
    bands=["Bromli suv bilan SO2 reaksiyasi tenglamasini yozing (SO2 + Br2 + 2H2O → H2SO4 + 2HBr). Hosil bo'lgan H2SO4 massasini (g) toping.","Mo'l BaCl2 qo'shilganda bromli suvli eritmada hosil bo'lgan cho'kma massasini (g) aniqlang.","Ba(OH)2 eritmasida hosil bo'lgan cho'kma massasini (g) hisoblang.","Dastlabki aralashmaning o'rtacha molyar massasini (g/mol) va havoga nisbatan zichligini toping."]
    M_=(a*64+b*44)/(a+b)
    sol=["n(SO2) = %s mol → n(H2SO4) = %s mol → **%s g**"%(f2(a,2),f2(a,2),f2(a*98,2)),"H2SO4 + BaCl2 → BaSO4↓ + 2HCl: **%s g**"%f2(a*233,2),"CO2 + Ba(OH)2 → BaCO3↓ + H2O: %s mol·197 = **%s g**"%(f2(b,2),f2(b*197,2)),"M = (%s·64 + %s·44)/%s = **%s g/mol**; D(havo) = %s/29 = **%s**"%(f2(a,2),f2(b,2),f2(a+b,2),f2(M_,2),f2(M_,2),f2(M_/29,2))]
    bands.append("Bromli suvli eritmada hosil bo'lgan HBr massasini (g) hisoblang."); sol.append("SO2 + Br2 + 2H2O → H2SO4 + 2HBr: n(HBr) = 2·%s = %s mol → **%s g**"%(fmt(a,2),fmt(2*a,2),fmt(2*a*81,2)))
    bands[0]+=" SO2 hajmini (l, n.sh.) ham hisoblang."; sol[0]+="; V(SO2) = %s·22,4 = **%s l**"%(f2(a,2),f2(a*22.4,2))
    return W("43",text,bands,sol,SC41)
W43M=[w43_s_chain,w43_p_chain,w43_n_chain,w43_carb,w43_halo,w43_al,w43_fe,w43_hard,w43_gasid]
