import re, random
from core import *
from an import stm, combo, COMB
# Haqiqiy imtihon ruhidagi savollar: kuzatiladigan o'zgarish (rang, cho'kma, gaz), sifat reaksiyalari,
# aralash mavzu (elektrolit + organik, gidroliz + indikator). Hammasi 8-11-sinf darsliklari doirasida.

OBS=[
 ('CuSO4 eritmasiga NaOH eritmasi qo\'shilsa',"ko'k cho'kma tushadi"),
 ('FeCl3 eritmasiga NaOH eritmasi qo\'shilsa',"qo'ng'ir-qizil cho'kma tushadi"),
 ('FeSO4 eritmasiga NaOH eritmasi qo\'shilsa',"oq (havoda tez yashil, so'ng qo'ng'ir tusga kiradigan) cho'kma tushadi"),
 ('AgNO3 eritmasiga NaCl eritmasi qo\'shilsa',"oq tvorogsimon cho'kma tushadi"),
 ('AgNO3 eritmasiga KBr eritmasi qo\'shilsa',"och sariq cho'kma tushadi"),
 ('AgNO3 eritmasiga KI eritmasi qo\'shilsa',"sariq cho'kma tushadi"),
 ('BaCl2 eritmasiga Na2SO4 eritmasi qo\'shilsa',"oq cho'kma tushadi"),
 ('Na2CO3 eritmasiga HCl eritmasi qo\'shilsa',"gaz pufakchalari ajraladi"),
 ('NH4Cl eritmasiga NaOH eritmasi qo\'shib qizdirilsa',"o'tkir hidli gaz ajraladi"),
 ('Pb(NO3)2 eritmasiga KI eritmasi qo\'shilsa',"sariq cho'kma tushadi"),
 ('NaOH eritmasiga fenolftalein tomizilsa',"eritma qip-qizil tusga kiradi"),
 ('HCl eritmasiga lakmus tomizilsa',"eritma qizil tusga kiradi"),
 ('NaOH eritmasiga metiloranj tomizilsa',"eritma sariq tusga kiradi"),
 ('Brom suviga etilen yuborilsa',"brom suvining rangi yo'qoladi"),
 ('Kislotali KMnO4 eritmasiga Na2SO3 eritmasi qo\'shilsa',"binafsha rang yo'qoladi"),
]
def _grp(t):
    for k,g in (("ko'k cho'kma",'blue'),("qo'ng'ir-qizil",'brown'),("oq",'white'),("sariq cho'kma",'yellow'),("och sariq",'yellow'),("gaz",'gas'),("o'tkir",'gas'),("qizil",'red'),("sariq tusga",'yo'),("rangi yo'qoladi",'dec'),("rang yo'qoladi",'dec')):
        if k in t: return g
    return t
def t_obs(r):
    a,ans=r.choice(OBS); g=_grp(ans)
    pool=[x[1] for x in OBS if _grp(x[1])!=g]
    ws=[]
    for w in r.sample(pool,len(pool)):
        if _grp(w) not in [_grp(x) for x in ws]: ws.append(w)
        if len(ws)==3: break
    return Q("%s, qanday o'zgarish kuzatiladi?"%a,ans,ws,"%s – %s."%(a,ans),"9-sinf; Tirkashev (sifat reaksiyalari)",'theory')
def t_obs2(r):
    # qaysi juftlikda ... kuzatiladi
    key=r.choice(["cho'kma tushadi","gaz ajraladi"])
    P=[('CuSO4 va NaOH',"cho'kma tushadi"),('BaCl2 va Na2SO4',"cho'kma tushadi"),('AgNO3 va NaCl',"cho'kma tushadi"),('FeCl3 va NaOH',"cho'kma tushadi"),
       ('Na2CO3 va HCl',"gaz ajraladi"),('NH4Cl va NaOH (qizdirilganda)',"gaz ajraladi"),('Na2S va HCl',"gaz ajraladi"),('K2CO3 va H2SO4',"gaz ajraladi"),
       ('NaOH va HCl',"ko'rinadigan o'zgarish yo'q"),('KCl va NaNO3',"ko'rinadigan o'zgarish yo'q"),('NaCl va KNO3',"ko'rinadigan o'zgarish yo'q"),('Na2SO4 va KCl',"ko'rinadigan o'zgarish yo'q")]
    good=[p for p in P if p[1]==key]; bad=[p for p in P if p[1]!=key]
    k=r.randint(1,2); it=r.sample(good,k)+r.sample(bad,4-k); r.shuffle(it)
    fl=[p[1]==key for p in it]; ans,ws=combo(r,fl,key)
    return Q("Quyidagi juftlik eritmalari aralashtirilganda qaysilarida %s? %s"%(key,'; '.join('%d) %s'%(i+1,p[0]) for i,p in enumerate(it))),ans,ws,'; '.join('%s – %s'%p for p in it),"9-sinf; Tirkashev (ion almashinish reaksiyalari)",'theory')

BR=[('etilen',True),('atsetilen',True),('propen',True),('butadiyen-1,3',True),('stirol',True),('etan',False),('metan',False),('benzol',False),('geksan',False),('toluol',False),('siklogeksan',False)]
def t_brom(r):
    want=r.choice([True,False]); it=r.sample(BR,4)
    fl=[t==want for _,t in it]
    if not any(fl): return t_brom(r)
    ans,ws=combo(r,fl,want)
    return Q("Quyidagi moddalardan qaysilari %s? %s"%("brom suvini rangsizlantiradi" if want else "brom suvini rangsizlantirmaydi",'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it))),ans,ws,'; '.join('%s – %s'%(x[0],"rangsizlantiradi (qo'sh yoki uch bog')" if x[1] else "rangsizlantirmaydi") for x in it),"10-sinf (to'yinmagan uglevodorodlar sifat reaksiyasi)",'theory')

QUAL=[('glitserin','cu',"Cu(OH)2 bilan yorqin ko'k (ko'k-binafsha) eritma hosil qiladi"),
      ('etanal','ag',"ammiakli kumush oksid eritmasi bilan kumush ko'zgu hosil qiladi"),
      ('anilin','br',"brom suvi bilan oq cho'kma beradi"),
      ('kraxmal','i2',"yod eritmasi bilan ko'k rang beradi"),
      ('oqsil','bi',"kuchli ishqor va CuSO4 bilan binafsha rang beradi (biuret reaksiyasi)")]
def t_qual(r):
    a,g,ans=r.choice(QUAL)
    ws=[x[2] for x in QUAL if x[1]!=g]; r.shuffle(ws)
    return Q("%s uchun xos sifat reaksiyasini ko'rsating."%(a[0].upper()+a[1:]),ans,ws[:3],"%s: %s."%(a,ans),"10-sinf; 11-sinf (sifat reaksiyalari)",'theory')

ELEC=[('NaCl eritmasi',True),('KOH eritmasi',True),('HCl eritmasi',True),('CH3COONa eritmasi',True),('CH3COOH eritmasi (kuchsiz elektrolit)',True),
      ('glukoza eritmasi',False),('etanol eritmasi',False),('saxaroza eritmasi',False),('glitserin eritmasi',False),('distillangan suv (sof)',False),('karbamid eritmasi',False)]
def t_elec_org(r):
    want=r.choice([True,False]); it=r.sample(ELEC,4); fl=[t==want for _,t in it]
    if not any(fl) or all(fl): return t_elec_org(r)
    if want and any(('kuchsiz' in x[0]) for x in it) and sum(fl)==1: pass
    ans,ws=combo(r,fl,want)
    return Q("Quyidagilardan qaysilari elektr tokini %s? %s"%("o'tkazadi" if want else "o'tkazmaydi",'; '.join('%d) %s'%(i+1,x[0].replace(' (kuchsiz elektrolit)','')) for i,x in enumerate(it))),ans,ws,'; '.join('%s – %s'%(x[0],"o'tkazadi (ionlar bor)" if x[1] else "o'tkazmaydi (molekulalar holida)") for x in it),"9-sinf (elektrolitlar) va 10-sinf (organik moddalar)",'theory')

SALT=[('NaCl',"neytral"),('KNO3',"neytral"),('Na2SO4',"neytral"),('Na2CO3',"ishqoriy"),('K2S',"ishqoriy"),('CH3COONa',"ishqoriy"),('NH4Cl',"nordon"),('CuSO4',"nordon"),('ZnCl2',"nordon"),('FeCl3',"nordon"),('Al2(SO4)3',"nordon")]
IND={"neytral":{'fenolftalein':"rangsiz",'lakmus':"binafsha",'metiloranj':"sariq-to'q sariq"},
     "ishqoriy":{'fenolftalein':"qizil (malina)",'lakmus':"ko'k",'metiloranj':"sariq"},
     "nordon":{'fenolftalein':"rangsiz",'lakmus':"qizil",'metiloranj':"qizil (pushti)"}}
def t_salt_ind(r):
    for _ in range(40):
        s,m=r.choice(SALT); ind=r.choice(['lakmus','fenolftalein'])
        ans=IND[m][ind]
        pool=[v[ind] for v in IND.values()]+["sariq","qizil"]
        ws=[]
        for w in pool+["ko'k","pushti"]:
            if w!=ans and w not in ws and not (w.startswith(ans.split()[0]) and w!=ans): ws.append(w)
        r.shuffle(ws)
        if ind=='lakmus':
            ws=[w for w in ["qizil","ko'k","binafsha","sariq"] if w!=ans]
        else:
            ws=[w for w in ["qizil (malina)","rangsiz","sariq","ko'k"] if w!=ans]
        return Q("%s tuzining suvdagi eritmasiga %s tomizilsa, eritma qanday rangga kiradi?"%(s,ind),ans,ws[:3],"%s – %s muhit (gidroliz) → %s %s."%(s,m,ind,ans),"9-sinf; 10-sinf (tuzlar gidrolizi, indikatorlar)",'theory')

ORGONE=[('etanol',"etilen"),('1,2-dibrometan',"etilen"),]
def t_org_inorg_mix(r):
    # aralash: ionlar bo'yicha elektrolitik dissotsilanish + organik kislota
    sub=[('CH3COOH',"CH3COO⁻ va H⁺"),('HCOOH',"HCOO⁻ va H⁺"),('CH3COONa',"CH3COO⁻ va Na⁺"),('C6H5ONa',"C6H5O⁻ va Na⁺"),('CH3NH3Cl',"CH3NH3⁺ va Cl⁻")]
    s,ans=r.choice(sub)
    ws=[x[1] for x in sub if x[1]!=ans]; r.shuffle(ws)
    return Q("%s suvli eritmada dissotsilanganda qaysi ionlar hosil bo'ladi?"%s,ans,ws[:3],"%s → %s."%(s,ans),"9-sinf (dissotsilanish); 10-sinf (organik kislotalar, tuzlar)",'theory')

G7=[t_obs,t_obs2,t_salt_ind,t_org_inorg_mix]
O7=[t_brom,t_qual,t_elec_org]

# ================= QIYINLASHTIRILGAN VERSIYALAR (mantiqiy fikrlash, ko'p bosqichli) =================
SEQ=[
 ("AlCl3 eritmasiga avval oz, so'ng mo'l NaOH eritmasi qo'shilganda","oq cho'kma tushadi","cho'kma erib ketadi","cho'kma erimasdan qoladi","Al(OH)3 amfoter: mo'l ishqorda Na[Al(OH)4] hosil qilib eriydi"),
 ("ZnSO4 eritmasiga avval oz, so'ng mo'l NaOH eritmasi qo'shilganda","oq cho'kma tushadi","cho'kma erib ketadi","cho'kma erimasdan qoladi","Zn(OH)2 amfoter: mo'l ishqorda Na2[Zn(OH)4] hosil qilib eriydi"),
 ("CuSO4 eritmasiga avval NaOH, so'ng mo'l ammiak eritmasi qo'shilganda","ko'k cho'kma tushadi","cho'kma erib, to'q ko'k eritma hosil bo'ladi","cho'kma qo'ng'ir tusga kiradi","Cu(OH)2 mo'l NH3 da kompleks [Cu(NH3)4](OH)2 hosil qilib eriydi"),
 ("AgNO3 eritmasiga avval NaCl, so'ng mo'l ammiak eritmasi qo'shilganda","oq tvorogsimon cho'kma tushadi","cho'kma erib ketadi","cho'kma sariq tusga kiradi","AgCl mo'l NH3 da [Ag(NH3)2]Cl kompleksi sifatida eriydi"),
 ("FeCl3 eritmasiga avval NaOH, so'ng mo'l HCl eritmasi qo'shilganda","qo'ng'ir-qizil cho'kma tushadi","cho'kma erib, sariq eritma hosil bo'ladi","cho'kma erimasdan qoladi","Fe(OH)3 asos: kislotada eriydi (FeCl3 hosil bo'ladi)"),
 ("ohakli suvga avval oz, so'ng mo'l CO2 yuborilganda","eritma loyqalanadi","loyqa yo'qolib, eritma tiniqlashadi","loyqa yanada quyuqlashadi","CaCO3 + CO2 + H2O → Ca(HCO3)2 (eriydi)"),
 ("Na2CO3 eritmasiga HCl eritmasi tomchilab (kislota yetishmaganda) qo'shilganda","gaz ajralmaydi (NaHCO3 hosil bo'ladi)","kislota ko'paytirilsa, gaz ajrala boshlaydi","kislota ko'paytirilsa ham gaz ajralmaydi","Na2CO3 + HCl → NaHCO3 + NaCl, so'ng NaHCO3 + HCl → NaCl + H2O + CO2↑"),
 ("NaOH eritmasiga CuSO4 eritmasi tomchilab qo'shilganda (ishqor mo'l)","ko'k cho'kma tushadi","ko'k cho'kma hosil bo'ladi va erimaydi","cho'kma erib to'q ko'k eritma hosil bo'ladi","Cu(OH)2 mo'l ishqorda erimaydi (amfoterligi juda kuchsiz)"),
]
def t_seq(r):
    for _ in range(50):
        it=r.sample(SEQ,4); fl=[r.random()<0.5 for _ in it]
        if any(fl) and not all(fl): break
    ans,ws=combo(r,fl,True)
    st=[]
    for i,(s,sc,t,f,why) in enumerate(zip(it,[x for x in it],[0]*4,[0]*4,[0]*4)): pass
    lines=[]
    for (setup,o1,o2t,o2f,why),tf in zip(it,fl):
        lines.append("%s: %s, keyin %s"%(setup,o1,o2t if tf else o2f))
    sol='; '.join("%d) %s – %s (%s)"%(i+1,it[i][0].split(' eritmasi')[0].split(' suvga')[0],"to'g'ri" if fl[i] else "noto'g'ri",it[i][4]) for i in range(4))
    return Q("Quyidagi jarayonlar qanday kuzatuvlar bilan boradi? To'g'ri ta'riflangan jarayonlarni belgilang. "+'; '.join("%d) %s"%(i+1,l) for i,l in enumerate(lines)),ans,ws,sol,"9-sinf; 11-sinf (amfoter birikmalar, kompleks hosil bo'lishi)",'theory')

# ajratish mantig'i: reagentlar javob matritsasi (g=gaz, w=oq cho'kma, ...), vektorlar farqlansa ajratadi
SEP_IN={
 'subs':{'NaCl':{'HCl':'-','BaCl2':'-','lakmus':'-','fenolftalein':'-'},
         'Na2SO4':{'HCl':'-','BaCl2':'w','lakmus':'-','fenolftalein':'-'},
         'Na2CO3':{'HCl':'g','BaCl2':'w','lakmus':'k','fenolftalein':'q'},
         'KNO3':{'HCl':'-','BaCl2':'-','lakmus':'-','fenolftalein':'-'}},
 'rea':['HCl','BaCl2','lakmus','fenolftalein'],
 'triples':[('NaCl','Na2SO4','Na2CO3')]}
SEP_ORG={
 'subs':{'etanol':{'Cu(OH)2 (sovuqda)':'-','Cu(OH)2 (qizdirilganda)':'-','[Ag(NH3)2]OH':'-','Na metali':'g','FeCl3':'-'},
         'glitserin':{'Cu(OH)2 (sovuqda)':'k','Cu(OH)2 (qizdirilganda)':'k','[Ag(NH3)2]OH':'-','Na metali':'g','FeCl3':'-'},
         'etanal':{'Cu(OH)2 (sovuqda)':'-','Cu(OH)2 (qizdirilganda)':'r','[Ag(NH3)2]OH':'m','Na metali':'-','FeCl3':'-'},
         'fenol':{'Cu(OH)2 (sovuqda)':'-','Cu(OH)2 (qizdirilganda)':'-','[Ag(NH3)2]OH':'-','Na metali':'g','FeCl3':'b'}},
 'rea':['Cu(OH)2 (sovuqda)','Cu(OH)2 (qizdirilganda)','[Ag(NH3)2]OH','Na metali','FeCl3'],
 'triples':[('etanol','glitserin','etanal'),('etanol','glitserin','fenol'),('etanol','etanal','fenol'),('glitserin','etanal','fenol')]}
def _sep(r,D,intro,src):
    for _ in range(80):
        tr=r.choice(D['triples']); r.shuffle(list(tr)); tr=list(tr); r.shuffle(tr)
        pairs=[]
        for k in (1,2):
            import itertools
            for c in itertools.combinations(D['rea'],k):
                if sum(x.startswith('Cu(OH)2') for x in c)>1: continue
                pairs.append(c)
        cand=r.sample(pairs,4)
        def ok(c): 
            vs=[tuple(D['subs'][s][x] for x in c) for s in tr]; return len(set(vs))==3
        fl=[ok(c) for c in cand]
        if any(fl) and not all(fl): break
    else: return _sep(r,D,intro,src)
    ans,ws=combo(r,fl,True)
    lab=lambda c:' va '.join(c)
    sol='; '.join("%s – %s"%(lab(c),"uchalasini ajratadi" if f else "yetarli emas") for c,f in zip(cand,fl))
    return Q("%s %s ni alohida probirkalarda ajratish uchun qaysi reagent(lar) yetarli? %s"%(intro,', '.join(tr),'; '.join('%d) %s'%(i+1,lab(c)) for i,c in enumerate(cand))),ans,ws,sol,src,'theory')
def t_sep_in(r): return _sep(r,SEP_IN,"Probirkalardagi eritmalar:","9-sinf (ion reaksiyalar, anionlarni aniqlash)")
def t_sep_org(r): return _sep(r,SEP_ORG,"Probirkalardagi organik moddalar:","10-sinf (spirt, aldegid, fenol sifat reaksiyalari)")

HY=[('FeCl3 va Na2CO3',"qo'ng'ir cho'kma va gaz",'Fe(OH)3↓ + CO2↑ (qo\'shma gidroliz)'),
    ('Al2(SO4)3 va Na2CO3',"oq cho'kma va gaz",'Al(OH)3↓ + CO2↑ (qo\'shma gidroliz)'),
    ('Al2(SO4)3 va Na2S',"oq cho'kma va gaz (H2S)",'Al(OH)3↓ + H2S↑ (qo\'shma gidroliz)'),
    ('BaCl2 va Na2CO3',"faqat cho'kma",'BaCO3↓ (almashinish)'),
    ('CaCl2 va Na2CO3',"faqat cho'kma",'CaCO3↓ (almashinish)'),
    ('Na2CO3 va HCl',"faqat gaz",'CO2↑'),
    ('NaCl va Na2CO3',"o'zgarish yo'q",'reaksiya bormaydi'),
    ('K2SO4 va NaNO3',"o'zgarish yo'q",'reaksiya bormaydi')]
def t_hydr2(r):
    mode=r.choice([("ham cho'kma, ham gaz","cho'kma va gaz"),("faqat cho'kma","faqat cho'kma"),("faqat gaz","faqat gaz")])
    key=mode[1]
    for _ in range(50):
        it=r.sample(HY,4); fl=[key in x[1] for x in it]
        if key=="faqat gaz": fl=[x[1]=="faqat gaz" for x in it]
        elif key=="faqat cho'kma": fl=[x[1]=="faqat cho'kma" for x in it]
        else: fl=[("cho'kma" in x[1] and "gaz" in x[1]) for x in it]
        if any(fl) and not all(fl): break
    ans,ws=combo(r,fl,True)
    return Q("Quyidagi tuz eritmalari aralashtirilganda qaysilarida %s hosil bo'ladi? %s"%(mode[0],'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it))),ans,ws,'; '.join('%s – %s (%s)'%x for x in it),"9-sinf; 10-sinf (tuzlar gidrolizi, ion almashinish reaksiyalari)",'theory')
G7H=[t_seq,t_sep_in,t_hydr2]; O7H=[t_sep_org]
