from core import *
from an import combo, stm, COMB
import re
# ---------- theory: nomenclature ----------
NOM=[('CH3–CH(CH3)–CH2–CH3','2-metilbutan',['3-metilbutan','2-etilpropan','metilbutan']),
('CH3–CH(CH3)–CH(C2H5)–CH2–CH3','3-etil-2-metilpentan',['2-metil-3-etilpentan','3-izopropilpentan','2,3-dietilbutan']),
('CH3–C(CH3)2–CH2–CH3','2,2-dimetilbutan',['2-metilpentan','3,3-dimetilbutan','2,2-dimetilpropan']),
('CH3–CH2–CH(CH3)–CH2–CH3','3-metilpentan',['2-etilbutan','2-metilpentan','3-etilbutan']),
('CH2=CH–CH2–CH3','buten-1',['buten-2','1-butin','butan']),
('CH3–CH=C(CH3)–CH3','2-metilbuten-2',['3-metilbuten-2','2-metilbuten-3','2-metilbuten-1']),
('CH3–C≡C–CH2–CH3','pentin-2',['pentin-3','pentin-1','2-pentin-4']),
('CH3–CH(OH)–CH2–CH3','butanol-2',['butanol-1','2-metilpropanol-1','2-metilpropanol-2']),
('CH3–CH(CH3)–CH2–OH','2-metilpropanol-1',['butanol-1','2-metilpropanol-2','butanol-2']),
('CH3–C(CH3)2–OH','2-metilpropanol-2',['butanol-2','2-metilpropanol-1','butanol-1']),
('CH3–CH2–CH(CH3)–CHO','2-metilbutanal',['3-metilbutanal','pentanal','2-metilbutanon']),
('CH3–CO–CH2–CH3','butanon',['butanal','butanol-2','propanon']),
('CH3–CH(CH3)–COOH','2-metilpropan kislota',['butan kislota','3-metilpropan kislota','2-metilbutan kislota']),
('CH3–CH(NH2)–CH2–CH3','butan-2-amin',['butan-1-amin','2-metilpropan-1-amin','2-aminobutanol']),
('CH2=CH–CH=CH2','butadiyen-1,3',['butadiyen-1,2','buten-1','butin-1']),
('CH3–CH2–CH(Cl)–CH3','2-xlorbutan',['1-xlorbutan','2-xlor-2-metilpropan','3-xlorbutan'])]
def t_nom(r):
    f,n,ws=pick(r,NOM)
    return Q("%s birikmaning sistematik nomi qaysi qatorda to'g'ri keltirilgan?"%f,n,ws,"Asosiy zanjir eng uzun va funksional guruh/qo'shbog'ga yaqin uchdan raqamlanadi; o'rinbosarlar alifbo tartibida: %s"%n,"10-sinf (nomenklatura §6, §11, §20, §24–26)",'theory')
ISO=[('C4H10 alkanning izomerlari soni',2),('C5H12 alkanning izomerlari soni',3),('C6H14 alkanning izomerlari soni',5),('C7H16 alkanning izomerlari soni',9),('C3H7OH tarkibli spirtlarning izomerlari soni',2),('C4H9OH tarkibli spirtlarning izomerlari soni',4),('C5H11OH tarkibli spirtlarning izomerlari soni',8),('C4H8 alkenlarning izomerlari soni (sis-trans izomerlar bilan, siklik bo\'lmagan)',4),('C4H6 alkinlarning izomerlari soni',2),('C5H8 alkinlarning izomerlari soni',3),('C4H9Cl galogenli hosilalarning izomerlari soni',4),('C5H10O aldegidlarning izomerlari soni',4),('C5H10O ketonlarning izomerlari soni',3),('C4H8O2 karbon kislotalarning izomerlari soni',2),('C5H10O2 karbon kislotalarning izomerlari soni',4),('C4H8O2 murakkab efirlarning izomerlari soni',4),('C8H10 aromatik uglevodorodlarning izomerlari soni (benzol halqasi saqlagan)',4),('C3H9N aminlarning izomerlari soni',4),('C4H10O oddiy efirlarning izomerlari soni',3)]
def t_isom(r):
    t,k=pick(r,ISO); ws=[k+1,k-1,k+2,k*2]
    return numq(t+" nechta?",k,ws,"Izomerlarni skelet, funksional guruh o'rni va sinflararo/geometrik izomeriya bo'yicha sanaymiz: %d ta"%k,"10-sinf §6, §12, §20, §28 (izomeriya)",0,'theory')
FACT={
'alkan':[("Metan suvda yaxshi eriydi",False),("Alkanlarda faqat σ-bog'lar bor",True),("Alkanlar uchun almashinish reaksiyasi xos",True),("Alkanlar KMnO4 eritmasini rangsizlantiradi",False),("Propan odatiy sharoitda gaz",True),("Alkanlar uchun birikish reaksiyalari xos",False),("Sikloalkanlarning umumiy formulasi CnH2n",True),("Metanning katalitik oksidlanishidan formaldegid olinadi",True),("Alkanlar yonganda CO2 va H2O hosil bo'ladi",True)],
'alken':[("Etilen bromli suvni rangsizlantiradi",True),("Alkenlarda π-bog' yo'q",False),("Propenga HBr birikishi Markovnikov qoidasiga bo'ysunadi",True),("Alkenlar KMnO4 ning suvli eritmasi bilan glikol hosil qiladi",True),("Etilen sanoatda kreking gazlaridan olinadi",True),("Alkinlar uchun umumiy formula CnH2n+2",False),("Asetilen Ag2O ning ammiakli eritmasi bilan cho'kma beradi (butin-2 beradi)",False),("Kauchuk izoprenning polimeri",True),("Asetilenni Kucherov reaksiyasi bilan sirka aldegidiga aylantirish mumkin",True)],
'aren':[("Benzol bromli suvni rangsizlantirmaydi",True),("Benzolda 6 ta sp² gibridlangan uglerod bor",True),("Toluol KMnO4 bilan benzoy kislotagacha oksidlanadi",True),("Benzol uchun birikish reaksiyalari mutlaqo xos emas",False),("Neft fraksiyalaridan gazolin 150 °C gacha haydaladi",True),("Naftalin – bir halqali aren",False),("Benzoldan nitrobenzol nitrolash bilan olinadi",True),("Tabiiy gazning asosiy qismi propan",False)],
'spirt':[("Etanol natriy bilan reaksiyaga kirishadi",True),("Fenol Cu(OH)2 ni eritib ko'k kompleks hosil qiladi",False),("Glitserin Cu(OH)2 bilan ko'k kompleks hosil qiladi",True),("Fenol NaOH bilan reaksiyaga kirishadi",True),("Birlamchi spirt oksidlanganda aldegid hosil bo'ladi",True),("Uchlamchi spirtlar oson oksidlanadi",False),("Fenol FeCl3 bilan binafsha rang beradi",True),("Etilenglikol zaharsiz",False),("Etanolning molekulalar aro vodorod bog'i bor",True)],
'ald':[("Aldegidlar \"kumush ko'zgu\" reaksiyasini beradi",True),("Aseton Cu(OH)2 ni qaytaradi",False),("Formalin — formaldegidning 40 % li eritmasi",True),("Ketonlar kuchsiz oksidlovchilar bilan oksidlanmaydi",True),("Aldegidlar qaytarilganda ikkilamchi spirt hosil bo'ladi",False),("Sirka aldegid Kucherov reaksiyasi bilan olinadi",True),("Aseton suvda erimaydi",False),("Formaldegid gaz holatda, suvda yaxshi eriydi",True)],
'kis':[("Chumoli kislota \"kumush ko'zgu\" reaksiyasini beradi",True),("Sirka kislota karbonatlar bilan CO2 ajratadi",True),("Stearin kislota to'yinmagan kislota",False),("Olein kislota Br2 ni biriktiradi",True),("Benzoy kislota Na2CO3 bilan reaksiyaga kirishmaydi",False),("Karboksil guruh karbonil va gidroksil guruhlardan iborat",True),("Qattiq suvda sovun yaxshi ko'piklanadi",False),("Sirka angidrid ikki molekula sirka kislotadan suv chiqib hosil bo'ladi",True)],
'efir':[("Murakkab efirlarning gidrolizi ishqoriy muhitda qaytmas",True),("Yog'lar glitserin va yuqori yog' kislotalarning murakkab efirlari",True),("Suyuq yog'lar to'yinmagan kislotalardan hosil bo'lgan",True),("Sovun — yuqori yog' kislotalarning natriyli tuzi",True),("Efirlanish reaksiyasi qaytmas",False),("Dietil efir spirtdan yuqori haroratda qaynaydi",False),("Suyuq yog'larni gidrogenlab qattiq yog' olinadi",True),("Etilatsetat efir hidli suyuqlik",True)],
'ugl':[("Glyukoza \"kumush ko'zgu\" reaksiyasini beradi",True),("Saxaroza Feling suyuqligini qaytaradi",False),("Kraxmal yod bilan ko'k rang beradi",True),("Selluloza β-glyukoza qoldiqlaridan iborat",True),("Maltoza gidrolizlanganda ikki molekula glyukoza hosil qiladi",True),("Kraxmal va selluloza bir xil M ga ega",False),("Fruktoza ketospirt",True),("Glyukoza gidrolizlanadi",False)],
'amin':[("Anilin bromli suv bilan oq cho'kma beradi",True),("Aminlar kuchsiz asoslar xossasini namoyon qiladi",True),("Aminokislotalar faqat kislotali xossaga ega",False),("Oqsillar biuret reaksiyasini beradi",True),("Nitrobenzoldan anilin Zinin reaksiyasi bilan olinadi",True),("Glitsin optik faol",False),("Dipeptidda 2 ta peptid bog' bor",False),("Aminokislotalar amfoter birikmalar",True)],
'pol':[("Polietilen polimerlanish reaksiyasi bilan olinadi",True),("Fenolformaldegid smola polikondensatsiya mahsuloti",True),("Kapron poliamid tola",True),("Lavsan poliamid tola",False),("Termoreaktiv polimerlar qizdirilganda qayta yumshaydi",False),("Tabiiy kauchuk – sis-1,4-poliizopren",True),("Polimerning M = zveno M · polimerlanish darajasi",True),("Teflon — polivinilxlorid",False)]}
def t_orgfact(r,topic=None):
    topic=topic or r.choice(list(FACT)); ans,ws,it=stm(r,FACT[topic],want=r.choice([True,False]) if False else True)
    lab={'alkan':'alkanlar va sikloalkanlar','alken':'alken, alkadiyen va alkinlar','aren':'arenlar, neft va tabiiy gaz','spirt':'spirt va fenollar','ald':'aldegid va ketonlar','kis':'karbon kislotalar','efir':'murakkab efirlar va yog\'lar','ugl':'uglevodlar','amin':'aminlar, aminokislotalar va oqsillar','pol':'yuqori molekulyar birikmalar'}[topic]
    return Q("%s haqida qaysi fikrlar to'g'ri? %s"%(lab.capitalize(),'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it))),ans,ws,'; '.join('%d) %s'%(i+1,'to\'g\'ri' if x[1] else 'noto\'g\'ri') for i,x in enumerate(it)),"10-sinf (mavzuga oid paragraflar); Abdusamatov",'theory')
CLS=[('C2H5OH','spirt'),('C6H5OH','fenol'),('CH3CHO','aldegid'),('CH3COCH3','keton'),('CH3OCH3','oddiy efir'),('CH3COOH','karbon kislota'),('CH3COOC2H5','murakkab efir'),('C2H5NH2','amin'),('C6H5NH2','aromatik amin'),('C6H12O6','monosaxarid'),('C12H22O11','disaxarid'),('H2NCH2COOH','aminokislota'),('CH3NO2','nitrobirikma')]
def t_class(r):
    kind=pick(r,['aldegid','keton','spirt','karbon kislota','murakkab efir','amin','fenol']);
    conf={'amin':{'aromatik amin','aminokislota'},'fenol':{'spirt'},'spirt':{'fenol'},'karbon kislota':{'aminokislota'}}.get(kind,set())
    good=[x for x in CLS if x[1]==kind]; bad=[x for x in CLS if x[1]!=kind and x[1] not in conf]; lst=r.sample(good,1)+r.sample(bad,3); r.shuffle(lst)
    ans=[x for x in lst if x[1]==kind][0][0]
    return Q("Quyidagi birikmalardan qaysi biri %s sinfiga kiradi?"%kind,ans,[x[0] for x in lst if x[0]!=ans],'; '.join('%s – %s'%x for x in lst),"10-sinf (organik birikmalar sinflari)",'theory')
OPR=[('C2H4 + H2O (H⁺)','etanol','CH2=CH2 + H2O → C2H5OH'),('CH3CHO + H2 (Ni)','etanol','CH3CHO + H2 → C2H5OH'),('C2H5OH (H2SO4, 170 °C)','etilen','C2H5OH → C2H4 + H2O'),('CaC2 + H2O','asetilen','CaC2 + 2H2O → C2H2 + Ca(OH)2'),('C2H2 + H2O (Hg²⁺)','sirka aldegid','Kucherov reaksiyasi'),('CH3CHO + Ag2O (NH3)','sirka kislota','CH3CHO + Ag2O → CH3COOH + 2Ag'),('C6H5NO2 + H2 (kat.)','anilin','C6H5NO2 + 3H2 → C6H5NH2 + 2H2O'),('3C2H2 (C, t)','benzol','Zelinskiy trimerlanishi'),('C2H5Cl + KOH (spirt)','etilen','dehidrogalogenlanish'),('CH3COONa + NaOH (t)','metan','CH3COONa + NaOH → CH4 + Na2CO3'),('CH3COOH + C2H5OH (H⁺)','etilatsetat','efirlanish'),('C6H5CH3 + KMnO4 (H⁺)','benzoy kislota','yon zanjir oksidlanishi'),('C2H5OH + CuO (t)','sirka aldegid','C2H5OH + CuO → CH3CHO + Cu + H2O'),('C6H12O6 (bijg\'ish)','etanol','C6H12O6 → 2C2H5OH + 2CO2')]
def t_oprod(r):
    a,p,e=pick(r,OPR); ws=list(dict.fromkeys(x[1] for x in OPR if x[1]!=p)); r.shuffle(ws)
    return Q("%s reaksiyasi natijasida qaysi organik modda hosil bo'ladi?"%a,p,ws[:3],e,"10-sinf (olinish usullari)",'theory')
# ---------- calc ----------
HC=[('CH4',1,4),('C2H6',2,6),('C3H8',3,8),('C4H10',4,10),('C2H4',2,4),('C3H6',3,6),('C2H2',2,2),('C6H6',6,6),('C7H8',7,8),('C4H8',4,8)]
def c_formula(r):
    f,c,h=pick(r,[x for x in HC if x[0] not in ('CH4',)]); n=r.choice([0.1,0.2]); co2=n*c*44; h2o=n*h/2*18; m=n*(12*c+h)
    ask=r.choice(['M','f'])
    if ask=='M': return numq("Uglevodorodning %s g massasi yondirilganda %s g CO2 va %s g H2O hosil bo'ldi. Uglevodorodning molyar massasini (g/mol) aniqlang."%(fmt(m,2),fmt(co2,2),fmt(h2o,2)),12*c+h,[(12*c+h)*2,(12*c+h)/2,c*12,(12*c+h)+2],"n(C) = %s, n(H) = %s mol → C%dH%d, M = %d"%(fmt(n*c),fmt(n*h),c,h,12*c+h),"10-sinf (yonish; formulani aniqlash)",None)
    nC=co2/44; nH=h2o/9
    return numq("Uglevodorodning %s g massasi yondirilganda %s g CO2 va %s g H2O hosil bo'ldi. Uglevodorod molekulasidagi uglerod atomlari sonini toping (M = %d g/mol)."%(fmt(m,2),fmt(co2,2),fmt(h2o,2),12*c+h),c,[c+1,c-1 if c>1 else c+2,h,c+2],"n(C) = %s mol, n(uglevodorod) = %s mol → %d"%(fmt(nC),fmt(n),c),"10-sinf (formulani aniqlash)",0)
def c_alkenemix(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); ask=r.choice(['br','h2'])
    # ethene + propyne
    m=a*28+b*26
    import math as _m; _g=_m.gcd(round(a*10),round(b*10)); rat=" Aralashmadagi etilen va asetilenning mol nisbati %d : %d."%(round(a*10)//_g,round(b*10)//_g)
    if ask=='br': ans=(a+2*b)*160; txt="Etilen va asetilendan iborat %s g aralashma mo'l bromli suv bilan to'liq reaksiyaga kirishdi. Sarflangan brom massasini (g) aniqlang."%fmt(m,2)+rat
    else: ans=(a+2*b)*22.4; txt="Etilen va asetilendan iborat %s g aralashmani to'liq gidrogenlash uchun sarflanadigan vodorod hajmini (l, n.sh.) aniqlang."%fmt(m,2)+rat
    return numq(txt,ans,[ans*2,ans/2,(a+b)*(160 if ask=='br' else 22.4),a*(160 if ask=='br' else 22.4)+b*(160 if ask=='br' else 22.4)*1],"28x + 26y = %s; x = %s, y = %s mol; etilen 1 mol, asetilen 2 mol birikma → %s"%(fmt(m,2),fmt(a),fmt(b),fmt(ans,2)),"10-sinf §13, §15 (alken va alkin birikish reaksiyalari)",2)
def c_benz(r):
    cs=[('benzoldan nitrobenzol',78,123,'C6H6 + HNO3 → C6H5NO2 + H2O'),('toluoldan benzoy kislota',92,122,'C6H5CH3 → C6H5COOH'),('nitrobenzoldan anilin',123,93,'C6H5NO2 + 3H2 → C6H5NH2 + 2H2O'),('fenoldan 2,4,6-tribromfenol',94,331,'C6H5OH + 3Br2 → C6H2Br3OH + 3HBr')]
    name,m1,m2,eq=pick(r,cs); n=r.choice([0.1,0.2,0.5]); y=r.choice([60,75,80,90])
    return numq("%s g %s olishda unum %d %% bo'lsa, mahsulot massasini (g) aniqlang."%(fmt(n*m1,2),name,y),n*m2*y/100,[n*m2,n*m2*2*y/100,n*m1*y/100,n*m2/ (y/100)],"%s: n = %s mol → %s g nazariy → %d %% = %s g"%(eq,fmt(n),fmt(n*m2,2),y,fmt(n*m2*y/100,2)),"10-sinf §16, §23, §33",2)
def c_alcna(r):
    a=r.choice([0.1,0.2]); b=r.choice([0.1,0.2]); sp=[('CH3OH',32),('C2H5OH',46),('C3H7OH',60)]; s1,s2=r.sample(sp,2); mix=a*s1[1]+b*s2[1]; V=(a+b)/2*22.4
    if r.random()<0.5: return numq("%s va %s dan iborat %s g aralashma natriy bilan to'liq reaksiyaga kirishganda ajraladigan vodorod hajmini (l, n.sh.) toping."%(s1[0],s2[0],fmt(mix,2)),V,[V*2,V/2,(a+b)*22.4,mix/ (s1[1]+s2[1])*11.2],"2ROH + 2Na → 2RONa + H2: n(spirt) = %s mol → n(H2) = %s mol → %s l"%(fmt(a+b),fmt((a+b)/2),fmt(V,2)),"10-sinf §21 (spirtlar)",2)
    return numq("%s va %s dan iborat %s g aralashma natriy bilan to'liq reaksiyaga kirishganda %s l (n.sh.) vodorod ajraldi. Aralashmadagi %s massasini (g) toping."%(s1[0],s2[0],fmt(mix,2),fmt(V,2),s1[0]),a*s1[1],[b*s2[1],a*s2[1],mix,a*s1[1]*2],"x + y = %s; %d x + %d y = %s → x = %s mol %s = %s g"%(fmt(a+b),s1[1],s2[1],fmt(mix,2),fmt(a),s1[0],fmt(a*s1[1],2)),"10-sinf §21",2)
def c_ag(r):
    f,m,k=pick(r,[('HCHO',30,4),('CH3CHO',44,2),('C2H5CHO',58,2),('HCOOH',46,2),('C6H12O6',180,2)]); n=r.choice([0.1,0.2,0.05]);
    nm={'HCHO':'metanal','CH3CHO':'etanal','C2H5CHO':'propanal','HCOOH':'chumoli kislota','C6H12O6':'glyukoza'}[f]
    return numq("%s g %s Ag2O ning ammiakli eritmasi bilan to'liq oksidlanganda hosil bo'lgan kumush massasini (g) aniqlang."%(fmt(n*m,2),nm),n*k*108,[n*108,n*k*108*2,n*k*108/2,n*m],"%s → %d Ag: %s mol → %s g"%(nm,k,fmt(n*k),fmt(n*k*108,2)),"10-sinf §24; §26; §30 (kumush ko'zgu)",2)
def c_aldid(r):
    f,m,k,nm=pick(r,[('HCHO',30,4,'to\'yingan aldegid'),('CH3CHO',44,2,''),('C2H5CHO',58,2,''),('C3H7CHO',72,2,'')]); n=r.choice([0.1,0.2]);
    return numq("To'yingan bir atomli aldegidning %s g massasi Ag2O ning ammiakli eritmasi bilan oksidlanganda %s g kumush ajraldi. Aldegidning molyar massasini (g/mol) toping."%(fmt(n*m,2),fmt(n*k*108,2)),m,[m*2,m/2,m+14,m-14 if m>30 else m+28],"n(Ag) = %s mol → n(aldegid) = %s mol (RCHO → 2Ag; HCHO → 4Ag) → M = %s"%(fmt(n*k),fmt(n),fmt(m)),"10-sinf §24",None)
def c_acid(r):
    f,m=pick(r,[('HCOOH',46),('CH3COOH',60),('C2H5COOH',74),('C3H7COOH',88)]); n=r.choice([0.1,0.2]); sub=r.choice(['NaHCO3','Na2CO3','NaOH'])
    if sub=='NaHCO3': return numq("To'yingan bir atomli karbon kislotaning %s g massasi mo'l NaHCO3 eritmasi bilan reaksiyaga kirishganda %s l (n.sh.) CO2 ajraldi. Kislotaning molyar massasini (g/mol) aniqlang."%(fmt(n*m,2),fmt(n*22.4,2)),m,[m*2,m/2,m+14,m-14],"RCOOH + NaHCO3 → RCOONa + H2O + CO2: n = %s mol → M = %s"%(fmt(n),fmt(m)),"10-sinf §26",None)
    return numq("%s g %s neytrallash uchun 10 %% li NaOH eritmasidan necha gramm kerak?"%(fmt(n*m,2),{'HCOOH':'chumoli kislotani','CH3COOH':'sirka kislotani','C2H5COOH':'propion kislotani','C3H7COOH':'moy kislotani'}[f]),n*40*10,[n*40,n*40*5,n*m*10,n*40*20],"n(NaOH) = %s mol = %s g; eritma %s g"%(fmt(n),fmt(n*40,2),fmt(n*400,2)),"10-sinf §26",2)
def c_ester(r):
    ac,ma=pick(r,[('sirka kislota',60),('propion kislota',74)]); al,mb=pick(r,[('etanol',46),('metanol',32)]); n1=r.choice([0.2,0.3]); n2=r.choice([0.2,0.3]); y=r.choice([75,80,60])
    lim=min(n1,n2); me={('sirka kislota','etanol'):88,('sirka kislota','metanol'):74,('propion kislota','etanol'):102,('propion kislota','metanol'):88}[(ac,al)]
    return numq("%s g %s va %s g %s dan %d %% unum bilan murakkab efir olindi. Efir massasini (g) toping."%(fmt(n1*ma,2),ac,fmt(n2*mb,2),al,y),lim*me*y/100,[lim*me,n1*me*y/100 if n1!=lim else n2*me*y/100*2,lim*me*y/50,(n1+n2)*me*y/200],"Kam miqdordagi modda: %s mol; nazariy %s g; %d %% → %s g"%(fmt(lim),fmt(lim*me,2),y,fmt(lim*me*y/100,2)),"10-sinf §28 (efirlanish)",2)
def c_ester_hyd(r):
    f,m,salt,ms,alc=pick(r,[('CH3COOC2H5',88,'CH3COONa',82,'etanol'),('CH3COOCH3',74,'CH3COONa',82,'metanol'),('HCOOC2H5',74,'HCOONa',68,'etanol'),('C2H5COOCH3',88,'C2H5COONa',96,'metanol')]); n=r.choice([0.1,0.2,0.25]); what=r.choice(['tuz','spirt'])
    if what=='tuz': return numq("%s g %s mo'l NaOH bilan to'liq gidrolizlandi. Hosil bo'lgan tuz massasini (g) aniqlang."%(fmt(n*m,2),f),n*ms,[n*m,n*ms*2,n*ms/2,n*40],"Efir + NaOH → tuz + spirt: n = %s mol → %s g"%(fmt(n),fmt(n*ms,2)),"10-sinf §28 (efirlar gidrolizi)",2)
    ma_={'etanol':46,'metanol':32}[alc]
    return numq("%s g %s mo'l NaOH bilan to'liq gidrolizlandi. Hosil bo'lgan spirt massasini (g) aniqlang."%(fmt(n*m,2),f),n*ma_,[n*m,n*ma_*2,n*ms,n*ma_/2],"n = %s mol → %s %s g"%(fmt(n),alc,fmt(n*ma_,2)),"10-sinf §28",2)
def c_fat(r):
    cs=[('tristearin',890,'C17H35COONa',306),('tripalmitin',806,'C15H31COONa',278)]
    nm,m,soap,ms=pick(r,cs); n=r.choice([0.1,0.2,0.5]); mode=r.choice(['soap','glyc','h2'])
    if mode=='soap': return numq("%s g %s natriy ishqori bilan to'liq gidrolizlanganda necha gramm sovun hosil bo'ladi?"%(fmt(n*m,2),nm),3*n*ms,[n*ms,3*n*ms*2/3,n*m,3*n*ms/2],"(RCOO)3C3H5 + 3NaOH → 3RCOONa + C3H5(OH)3: %s mol → %s g sovun"%(fmt(n),fmt(3*n*ms,2)),"10-sinf §29 (yog'lar, sovunlanish)",2)
    if mode=='glyc': return numq("%s g %s gidrolizlanganda necha gramm glitserin hosil bo'ladi?"%(fmt(n*m,2),nm),n*92,[n*3*92,n*92/2,n*m,n*46],"1 mol yog'dan 1 mol glitserin: %s mol → %s g"%(fmt(n),fmt(n*92,2)),"10-sinf §29",2)
    return numq("%s g triolein (M = 884) nikel katalizatori ishtirokida to'liq gidrogenlandi. Sarflangan vodorod hajmini (l, n.sh.) aniqlang."%fmt(n*884,2),3*n*22.4,[n*22.4,6*n*22.4,3*n*22.4/2,n*884/22.4],"Triolein molekulasida 3 ta C=C: n(H2) = 3·%s = %s mol → %s l"%(fmt(n),fmt(3*n),fmt(3*n*22.4,2)),"10-sinf §29 (yog'larni gidrogenlash)",2)
def c_carb(r):
    mode=r.choice(['maltose','starch','sucrose','ferm'])
    if mode=='maltose':
        n=r.choice([0.1,0.2,0.05]); return numq("%s g maltoza to'liq gidrolizlanib, hosil bo'lgan mahsulot Ag2O ning ammiakli eritmasi bilan oksidlandi. Ajralgan kumush massasini (g) aniqlang."%fmt(n*342,2),n*2*2*108,[n*2*108,n*4*108*2,n*108,n*342],"Maltoza → 2 glyukoza → 4 Ag: %s mol → %s g"%(fmt(n),fmt(n*4*108,2)),"10-sinf §31 (maltoza)",2)
    if mode=='starch':
        n=r.choice([1,2,0.5]); y=r.choice([100,80,90]); return numq("%s g kraxmal to'liq gidrolizlanib (unum %d %%), hosil bo'lgan glyukoza massasini (g) aniqlang."%(fmt(n*162,2),y),n*180*y/100,[n*162,n*180,n*180*y/50,n*342*y/100],"(C6H10O5)n → n C6H12O6: %s mol zveno → %s g (%d %%)"%(fmt(n),fmt(n*180*y/100,2),y),"10-sinf §31 (kraxmal)",2)
    if mode=='sucrose':
        n=r.choice([0.1,0.2,0.5]); return numq("%s g saxaroza gidrolizlanganda necha gramm glyukoza hosil bo'ladi?"%fmt(n*342,2),n*180,[n*342,n*360,n*90,n*180*2],"C12H22O11 + H2O → C6H12O6 + C6H12O6: %s mol → glyukoza %s g"%(fmt(n),fmt(n*180,2)),"10-sinf §31",2)
    n=r.choice([0.5,1,2]); return numq("%s mol glyukoza spirtli bijg'itilganda hosil bo'lgan etanol massasini (g) aniqlang."%fmt(n),n*2*46,[n*46,n*4*46,n*180,n*2*46/2],"C6H12O6 → 2C2H5OH + 2CO2: etanol %s mol = %s g"%(fmt(2*n),fmt(2*n*46,2)),"10-sinf §30–31 (bijg'ish)",2)
def c_amine(r):
    mode=r.choice(['burn','salt','aa','aavar'])
    if mode=='burn':
        n=r.choice([0.2,0.4]); return numq("%s mol CH3NH2 to'liq yondirilganda hosil bo'lgan CO2 va N2 hajmlari yig'indisini (l, n.sh.) aniqlang (4CH3NH2 + 9O2 → 4CO2 + 10H2O + 2N2)."%fmt(n),(n+n/2)*22.4,[n*22.4,n*2*22.4,(n+n)*22.4,n*22.4*0.5],"%s mol → CO2 %s mol + N2 %s mol = %s l"%(fmt(n),fmt(n),fmt(n/2),fmt((n+n/2)*22.4,2)),"10-sinf §33",2)
    if mode=='salt':
        n=r.choice([0.1,0.2,0.25]); return numq("%s g anilin mo'l xlorid kislota bilan reaksiyaga kirishganda hosil bo'lgan tuz massasini (g) aniqlang."%fmt(n*93,2),n*129.5,[n*93,n*129.5*2,n*36.5,n*166],"C6H5NH2 + HCl → C6H5NH3Cl: n = %s mol → %s g"%(fmt(n),fmt(n*129.5,2)),"10-sinf §33",2)
    cs=[('glitsin',75,'H2NCH2COOH'),('alanin',89,'CH3CH(NH2)COOH'),('valin',117,'(CH3)2CHCH(NH2)COOH')]
    nm,m,f=pick(r,cs); n=r.choice([0.1,0.2,0.3])
    if mode=='aa': return numq("Noma'lum α-aminokislotaning %s g massasi NaOH bilan reaksiyaga kirishganda %s g suv hosil bo'ldi. Aminokislotaning molyar massasini (g/mol) aniqlang."%(fmt(n*m,2),fmt(n*18,2)),m,[m*2,m/2,m+14,m-14],"RCH(NH2)COOH + NaOH → RCH(NH2)COONa + H2O: n(H2O) = n(kislota) = %s mol → M = %s"%(fmt(n),fmt(m)),"10-sinf §34 (aminokislotalar)",None)
    return numq("%s g %s HCl bilan reaksiyaga kirishganda hosil bo'lgan tuz massasini (g) aniqlang."%(fmt(n*m,2),nm),n*(m+36.5),[n*m,n*36.5,n*(m+36.5)*2,n*(m-36.5)],"%s + HCl → [H3N⁺–R–COOH]Cl⁻: n = %s mol → %s g"%(nm,fmt(n),fmt(n*(m+36.5),2)),"10-sinf §34",2)
def c_poly(r):
    mon,m=pick(r,[('etilen',28),('propilen',42),('vinilxlorid',62.5),('stirol',104),('izobutilen',56),('butadiyen-1,3',54),('izopren',68)]); n=r.choice([100,500,1000,2000,2500]); mode=r.choice(['M','n'])
    if mode=='M': return numq("%s monomeridan olingan polimerning polimerlanish darajasi %d bo'lsa, uning molyar massasini (g/mol) aniqlang."%(mon,n),m*n,[m*n/2,m*n*2,m+n,m*n/10],"M = %s · %d = %s"%(fmt(m),n,fmt(m*n)),"10-sinf §35 (YuMB)",None)
    return numq("%s monomeridan olingan polimerning molyar massasi %s g/mol. Polimerlanish darajasini aniqlang."%(mon,fmt(m*n)),n,[n*2,n/2,n+10,n*m],"n = M(polimer)/M(monomer) = %s/%s = %d"%(fmt(m*n),fmt(m),n),"10-sinf §35",0)
def c_ethanol(r):
    n=r.choice([0.2,0.5,1]); y=r.choice([75,80,90]); mode=r.choice(['eten','but'])
    if mode=='eten': return numq("%s g etil spirtidan %d %% unum bilan etilen olindi. Etilen hajmini (l, n.sh.) aniqlang."%(fmt(n*46,2),y),n*22.4*y/100,[n*22.4,n*22.4*y/50,n*46*y/100,n*22.4/ (y/100)],"C2H5OH → C2H4 + H2O: n = %s mol → %s l (%d %%)"%(fmt(n),fmt(n*22.4*y/100,2),y),"10-sinf §21 (etilen olinishi)",2)
    return numq("%s g etil spirtidan Lebedev usuli bilan (%d %% unum) butadiyen-1,3 olindi (2C2H5OH → C4H6 + H2 + 2H2O). Butadiyen massasini (g) aniqlang."%(fmt(n*46,2),y),n/2*54*y/100,[n*54*y/100,n/2*54,n*46,n/2*54*y/50],"2 mol spirtdan 1 mol butadiyen: %s mol → %s g (%d %%)"%(fmt(n/2),fmt(n/2*54*y/100,2),y),"10-sinf §14; Abdusamatov (Lebedev)",2)
def c_carbide(r):
    n=r.choice([0.2,0.5,1]); y=r.choice([80,90,100]); mode=r.choice(['ac','benz','ald'])
    if mode=='ac': return numq("%s g CaC2 suv bilan reaksiyaga kirishganda ajraladigan asetilen hajmini (l, n.sh.) aniqlang (unum %d %%)."%(fmt(n*64,2),y),n*22.4*y/100,[n*22.4,n*64*y/100,n*22.4*2,n*22.4*y/200],"CaC2 + 2H2O → C2H2 + Ca(OH)2: %s mol → %s l"%(fmt(n),fmt(n*22.4*y/100,2)),"10-sinf §15 (asetilen olinishi)",2)
    if mode=='benz': return numq("%s mol asetilendan Zelinskiy usuli bilan (%d %% unum) benzol olindi. Benzol massasini (g) aniqlang."%(fmt(n*3),y),n*78*y/100,[n*3*78*y/100,n*78,n*26,n*78*y/50],"3C2H2 → C6H6: %s mol → %s mol benzol → %s g"%(fmt(n*3),fmt(n),fmt(n*78*y/100,2)),"10-sinf §15; Abdusamatov",2)
    return numq("%s g asetilendan Kucherov reaksiyasi bilan (%d %% unum) sirka aldegid olindi. Aldegid massasini (g) aniqlang."%(fmt(n*26,2),y),n*44*y/100,[n*44,n*26*y/100,n*44*y/50,n*88*y/100],"C2H2 + H2O → CH3CHO: %s mol → %s g"%(fmt(n),fmt(n*44*y/100,2)),"10-sinf §15 (Kucherov)",2)
def c_halogenation(r):
    n=r.choice([0.1,0.2,0.5]); mode=r.choice(['cl','toluene'])
    return numq("%s mol metan xlor bilan to'liq xlorlanib, CCl4 olindi. Sarflangan xlor hajmini (l, n.sh.) aniqlang."%fmt(n),n*4*22.4,[n*22.4,n*2*22.4,n*3*22.4,n*8*22.4],"CH4 + 4Cl2 → CCl4 + 4HCl: Cl2 %s mol → %s l"%(fmt(4*n),fmt(4*n*22.4,2)),"10-sinf §8 (alkanlar galogenlanishi)",2)
