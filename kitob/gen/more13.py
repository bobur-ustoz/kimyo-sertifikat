import itertools, random
from core import *
# Kimyoviy tahlil (30-32) va sifat reaksiyalari: raqamlangan probirkalar, reagent tanlash, aralashmalarni ajratish usullari.

# ---------------- 1) raqamlangan probirkalar: juft kuzatuvlar bo'yicha moslash ----------------
NEU="bir-birini neytrallaydi"
SETS=[
 (['HCl','NaOH','Na2CO3','AgNO3'],{('HCl','NaOH'):NEU,('HCl','Na2CO3'):"rangsiz, hidsiz gaz ajraladi",('HCl','AgNO3'):"oq tvorogsimon cho'kma tushadi",('NaOH','AgNO3'):"to'q qo'ng'ir cho'kma tushadi",('Na2CO3','AgNO3'):"oq-sarg'ish cho'kma tushadi"}),
 (['NH4Cl','NaOH','H2SO4','BaCl2'],{('NH4Cl','NaOH'):"qizdirilganda o'tkir hidli gaz ajraladi",('NaOH','H2SO4'):NEU,('H2SO4','BaCl2'):"kislotada erimaydigan oq cho'kma tushadi"}),
 (['Na2CO3','HCl','BaCl2','NaOH'],{('Na2CO3','HCl'):"rangsiz, hidsiz gaz ajraladi",('Na2CO3','BaCl2'):"oq cho'kma tushadi",('HCl','NaOH'):NEU}),
 (['FeCl3','NaOH','AgNO3','KSCN'],{('FeCl3','NaOH'):"qo'ng'ir-qizil cho'kma tushadi",('FeCl3','AgNO3'):"oq tvorogsimon cho'kma tushadi",('FeCl3','KSCN'):"eritma qon-qizil rangga kiradi",('NaOH','AgNO3'):"to'q qo'ng'ir cho'kma tushadi",('AgNO3','KSCN'):"oq cho'kma tushadi"}),
 (['CuSO4','NaOH','BaCl2','Na2S'],{('CuSO4','NaOH'):"ko'k cho'kma tushadi",('CuSO4','BaCl2'):"oq cho'kma tushadi",('CuSO4','Na2S'):"qora cho'kma tushadi"}),
 (['Na2S','HCl','Pb(NO3)2','NaOH'],{('Na2S','HCl'):"chirigan tuxum hidli gaz ajraladi",('Na2S','Pb(NO3)2'):"qora cho'kma tushadi",('HCl','NaOH'):NEU,('Pb(NO3)2','NaOH'):"oq cho'kma tushadi (mo'l ishqorda eriydi)"}),
]
def t_tubes(r):
    names,out=r.choice(SETS)
    for _ in range(200):
        perm=list(range(4)); r.shuffle(perm)   # tube i -> substance names[perm[i]]
        tube={i:names[perm[i]] for i in range(4)}
        pairs=[(i,j) for i in range(4) for j in range(i+1,4)]
        def lab(i,j):
            a,b=tube[i],tube[j]
            return out.get((a,b)) or out.get((b,a))
        info=[(i,j,lab(i,j)) for i,j in pairs if lab(i,j)]
        r.shuffle(info)
        for k in range(2,len(info)+1):
            sel=info[:k]
            sols=[]
            for p in itertools.permutations(names):
                ok=True
                for i,j,l in sel:
                    a,b=p[i],p[j]
                    if (out.get((a,b)) or out.get((b,a)))!=l: ok=False;break
                if ok: sols.append(p)
            if len(sols)==1: break
        else: continue
        if len(sols)!=1 or len(sel)<3: continue
        break
    else: return t_tubes(r)
    true=tuple(tube[i] for i in range(4))
    fmt_=lambda p:', '.join('%d-%s'%(i+1,x) for i,x in enumerate(p))
    wrongs=[]
    for a_,b_ in itertools.combinations(range(4),2):
        p=list(true); p[a_],p[b_]=p[b_],p[a_]; wrongs.append(tuple(p))
    r.shuffle(wrongs)
    dis=[fmt_(w) for w in wrongs[:3]]
    stm=' '.join("%d- va %d-probirkalardagi eritmalar aralashtirilganda %s."%(i+1,j+1,l) for i,j,l in sel)
    t="Raqamlangan (1–4) probirkalarda %s eritmalari tartibsiz holda berilgan. Quyidagi kuzatuvlar asosida moddalarni probirka raqami bilan moslang. %s"%(', '.join(sorted(names)),stm)
    sol="; ".join("%d- va %d-probirka: %s → %s va %s"%(i+1,j+1,l,tube[i],tube[j]) for i,j,l in sel)+" → "+fmt_(true)
    return Q(t,fmt_(true),dis,sol,"9-sinf; 10-sinf (sifat reaksiyalari, ion almashinish)",'theory')

# ---------------- 2) ikki modda: qaysi reagent bilan farqlash mumkin ----------------
PAIRS=[
 ("xlorid kislota va fosfat kislota eritmalari","kumush nitrat",["mis","fenolftalein","lakmus"],"HCl + AgNO3 → AgCl↓ (oq cho'kma); H3PO4 kislotali muhitda cho'kma bermaydi"),
 ("chumoli kislota va sirka kislota","ammiakli kumush oksid",["lakmus","fenolftalein","natriy karbonat"],"HCOOH aldegid guruhi tufayli kumush ko'zgu beradi; ikkala kislota ham lakmusni qizartiradi va Na2CO3 dan CO2 siqib chiqaradi"),
 ("glitserin va etanol","mis(II) gidroksid",["natriy metali","lakmus","natriy gidroksid"],"glitserin Cu(OH)2 ni eritib, yorqin ko'k eritma beradi; Na ikkalasi bilan ham H2 ajratadi"),
 ("glukoza va saxaroza","ammiakli kumush oksid (qizdirilganda)",["mis(II) gidroksid (sovuqda)","yod eritmasi","lakmus"],"glukoza kumush ko'zgu beradi, saxaroza bermaydi; Cu(OH)2 sovuqda ikkalasi bilan ham ko'k eritma beradi"),
 ("benzol va toluol","kislotali KMnO4 eritmasi (qizdirilganda)",["brom suvi","FeCl3 eritmasi","natriy gidroksid"],"toluol KMnO4 ni rangsizlantirib, benzoy kislotagacha oksidlanadi; benzol brom suvi bilan ham reaksiyaga kirishmaydi"),
 ("fenol va etanol","temir(III) xlorid",["natriy metali","lakmus","mis(II) gidroksid"],"fenol FeCl3 bilan binafsha rang beradi; Na ikkalasidan ham H2 ajratadi"),
 ("natriy xlorid, natriy bromid va natriy yodid","kumush nitrat",["xlorid kislota","natriy gidroksid","bariy xlorid"],"AgCl – oq, AgBr – och sariq, AgI – sariq cho'kma"),
 ("natriy nitrat va natriy sulfat","bariy xlorid",["xlorid kislota","natriy gidroksid","lakmus"],"SO4²⁻ BaCl2 bilan BaSO4↓ (oq) beradi; boshqa reagentlar ikkalasi bilan ham o'zgarish bermaydi"),
 ("ammoniy karbonat va kaliy gidrokarbonat","natriy gidroksid (qizdirilganda)",["xlorid kislota","sulfat kislota","lakmus"],"(NH4)2CO3 dan NH3 ajraladi; kislotalar ikkalasidan ham CO2 ajratadi"),
 ("etilen va etan","brom suvi",["kaliy gidroksid eritmasi","xlorid kislota","lakmus"],"etilen brom suvini rangsizlantiradi, etan reaksiyaga kirishmaydi"),
 ("natriy karbonat va natriy sulfat","xlorid kislota",["bariy xlorid","kumush nitrat","qo'rg'oshin(II) nitrat"],"Na2CO3 dan gaz ajraladi; BaCl2, AgNO3 va Pb(NO3)2 ikkalasi bilan ham oq cho'kma beradi"),
 ("ammoniy xlorid va natriy xlorid","natriy gidroksid (qizdirilganda)",["kumush nitrat","xlorid kislota","bariy xlorid"],"NH4Cl dan NH3 ajraladi; AgNO3 ikkalasi bilan ham AgCl↓ beradi"),
 ("alyuminiy gidroksid va magniy gidroksid cho'kmalari","mo'l natriy gidroksid eritmasi",["xlorid kislota","nitrat kislota","sulfat kislota"],"Al(OH)3 amfoter: ishqorda eriydi; Mg(OH)2 erimaydi; kislotalarda ikkalasi ham eriydi"),
 ("temir(II) xlorid va temir(III) xlorid","kaliy rodanid (KSCN)",["xlorid kislota","bariy xlorid","kumush nitrat"],"Fe³⁺ + SCN⁻ → qon-qizil rang; boshqa reagentlar ikkalasi bilan ham o'zgarmaydi yoki bir xil cho'kma beradi"),
 ("sirka aldegid va aseton","ammiakli kumush oksid",["lakmus","temir(III) xlorid","natriy metali"],"etanal kumush ko'zgu beradi, aseton bermaydi"),
]
def t_dist_pair(r):
    d,ans,ws,why=r.choice(PAIRS)
    return Q("%s eritmalarini (moddalarini) bir-biridan qaysi reagent yordamida farqlash mumkin?"%(d[0].upper()+d[1:]),ans,list(ws),why+".","9-sinf; 10-sinf (sifat reaksiyalari; moddalarni farqlash)",'theory')

# ---------------- 3) aralashmalarni ajratish usullari ----------------
MIX=[("temir va oltingugurt kukunlari","magnit yordamida"),("osh tuzi va qum","suvda eritish, filtrlash, bug'latish"),("suv va o'simlik moyi","ajratgich voronka yordamida"),("etanol va suv","fraksiyalab haydash"),
     ("yod va osh tuzi","sublimatsiya (qizdirib, bug'ini sovitish)"),("loyqa suv (suv va gil)","tindirish va filtrlash"),("temir va mis kukunlari","magnit yordamida"),("suv va benzin","ajratgich voronka yordamida"),
     ("dengiz suvidan toza suv olish","distillash (haydash)"),("shakar va qum","suvda eritish, filtrlash, bug'latish")]
def t_sep_method(r):
    for _ in range(50):
        it=r.sample(MIX,3)
        meths=[m for _,m in it]
        if len(set(meths))==3: break
    letters='abc'; order=list(range(3)); r.shuffle(order)   # usullar tartibi aralashtiriladi
    ml=[it[i][1] for i in order]
    extra=r.choice([m for _,m in MIX if m not in meths])
    ml.append(extra); idx=list(range(4)); r.shuffle(idx); ml=[ml[i] for i in idx]
    L='abcd'
    ans_map=[L[ml.index(m)] for _,m in it]
    ans=', '.join('%d-%s'%(i+1,a) for i,a in enumerate(ans_map))
    dis=set()
    for _ in range(100):
        p=r.sample(L,3)
        s=', '.join('%d-%s'%(i+1,a) for i,a in enumerate(p))
        if s!=ans: dis.add(s)
        if len(dis)>=3: break
    t="Quyidagi aralashmalarni ajratish usullarini mos qatorda ko'rsating. Aralashmalar: %s. Usullar: %s."%('; '.join('%d) %s'%(i+1,n) for i,(n,_) in enumerate(it)),'; '.join('%s) %s'%(L[i],m) for i,m in enumerate(ml)))
    return Q(t,ans,list(dis)[:3],'; '.join('%s → %s'%(n,m) for n,m in it),"7-sinf (aralashmalarni ajratish); kimyoviy tahlil",'theory')

NEWQ=[t_tubes,t_dist_pair,t_sep_method]
