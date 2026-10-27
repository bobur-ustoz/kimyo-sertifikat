from core import *
from an import stm,combo,COMB
import os, random
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import style
plt.rcParams['font.family']='Arial Unicode MS'
IMG='/Users/macbook/kimyo-sertifikat/kitob/rasmlar/'
OUT='/Users/macbook/kimyo-sertifikat/kitob/rasmlar/gen/'
os.makedirs(OUT,exist_ok=True)
def _save(fig,name):
    style.finalize(fig); fig.tight_layout(); fig.savefig(OUT+name,dpi=200); plt.close(fig); return 'rasmlar/gen/'+name
# ---- graph 1: solubility curve
def g_solub(r,tag):
    S=r.choice([(10,20,30,45,62,80,102),(12,18,26,38,52,70,92),(15,25,35,50,68,88,110)])
    T=[0,10,20,30,40,50,60]
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(T,S,'g-o',ms=3)
    t1,t2=r.sample([20,30,40,50,60],2); t1,t2=max(t1,t2),min(t1,t2)
    for x in (t1,t2):
        y=S[T.index(x)]; ax.plot([x,x],[0,y],'k:',lw=.8); ax.plot([0,x],[y,y],'k:',lw=.8); ax.plot(x,y,'ro',ms=4)
    ax.set_xlabel('harorat, °C'); ax.set_ylabel('eruvchanlik, g/100 g suv'); ax.set_xticks(T); ax.set_yticks(range(0,121,10)); ax.grid(alpha=.3); ax.set_xlim(0,62); ax.set_ylim(0,120)
    name=_save(fig,'sol_%s.png'%tag)
    s1=S[T.index(t1)]; s2=S[T.index(t2)]; m=(100+s1)*r.choice([1,2]); salt=m*s1/(100+s1); water=m-salt; dep=salt-water*s2/100
    ask=r.choice(['cr','om','sol','add']); head="Grafikda tuzning eruvchanligi (g/100 g suv) haroratga bog'liq ko'rsatilgan.\n\n![Grafik: eruvchanlik](%s)\n\n"%name
    if ask=='cr':
        q=numq(head+"%d °C da to'yingan %s g eritma %d °C gacha sovitilganda necha gramm tuz cho'kmaga tushadi?"%(t1,fmt(m),t2),dep,[salt,water*s2/100,dep*2,m-water*s2/100],"Grafikdan S(%d) = %d, S(%d) = %d; %d °C da tuz %s g, suv %s g; %d °C da %s g eriydi → cho'kma %s g"%(t1,s1,t2,s2,t1,fmt(salt),fmt(water),t2,fmt(water*s2/100),fmt(dep)),"Tirkashev III bob (eruvchanlik, grafik)",None)
    elif ask=='om':
        w_=s1/(100+s1)*100
        q=numq(head+"%d °C da tuzning to'yingan eritmasidagi massa ulushini (%%) aniqlang."%t1,w_,[s1,w_/2,s2/(100+s2)*100,w_*1.5],"S(%d) = %d g/100 g suv → ω = %d/(100 + %d)·100 = %s %%"%(t1,s1,s1,s1,fmt(w_,1)),"Tirkashev III bob (eruvchanlik, grafik)",1)
    elif ask=='sol':
        W_=r.choice([50,200,250,400]); a_=s2*W_/100
        q=numq(head+"%d °C da %d g suvda eriydigan tuzning eng ko'p massasini (g) aniqlang."%(t2,W_),a_,[s2,a_*2,a_/2,s1*W_/100],"Grafikdan S(%d) = %d g/100 g; %d g suvda: %d·%d/100 = %s g"%(t2,s2,W_,s2,W_,fmt(a_)),"Tirkashev III bob (eruvchanlik, grafik)",None)
    else:
        m2=(100+s2)*r.choice([1,2]); ad=(s1-s2)*m2/(100+s2)
        q=numq(head+"%d °C da to'yingan %s g eritma %d °C gacha qizdirildi. Eritmani yana to'yingan holatga keltirish uchun necha gramm tuz qo'shish kerak?"%(t2,fmt(m2),t1),ad,[s1-s2,ad*2,ad/2,m2*s1/(100+s1)],"%d °C da suv %s g; %d °C da u %s g tuz eritadi, %d °C da esa %s g → qo'shiladi %s g"%(t2,fmt(m2*100/(100+s2)),t1,fmt(s1*m2/(100+s2)),t2,fmt(s2*m2/(100+s2)),fmt(ad)),"Tirkashev III bob (eruvchanlik, grafik)",None)
    q.kind='graph'; return q
def g_conc(r,tag):
    A0=r.choice([1.0,1.2,1.4]); B0=r.choice([0.8,1.0,1.2]); x=r.choice([0.4,0.5,0.6])
    A=A0-x;B=B0-x;C=x
    if A<=0.05 or B<=0.05: return g_conc(r,tag)
    K=C/(A*B)
    t=np.linspace(0,10,200); f=lambda a,b:(a+(b-a)*np.exp(-0.9*t))
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(t,f(A0,A),'b',label='A'); ax.plot(t,f(B0,B),'g',label='B'); ax.plot(t,C*(1-np.exp(-0.9*t)),'r',label='C'); ax.axvline(6,ls='--',c='gray'); ax.text(6.1,max(A0,B0)*0.95,'muvozanat',fontsize=7)
    ax.set_xlabel('vaqt, min'); ax.set_ylabel('konsentratsiya, mol/l'); ax.set_yticks(sorted({0,A,B,C,A0,B0})); ax.set_ylim(0,max(A0,B0)*1.1); ax.grid(alpha=.3); ax.legend(fontsize=8,loc='center right')
    name=_save(fig,'conc_%s.png'%tag)
    ask=r.choice(['K','conv','krev','ratio']); head="A + B ⇌ C reaksiyada moddalar konsentratsiyalarining vaqt bo'yicha o'zgarishi grafikda ko'rsatilgan.\n\n![Grafik: muvozanat](%s)\n\n"%name
    sol_="Grafikdan muvozanatda: [A] = %s, [B] = %s, [C] = %s mol/l; "%(fmt(A,2),fmt(B,2),fmt(C,2))
    if ask=='K': q=numq(head+"Grafikdan foydalanib, muvozanat konstantasini (K) aniqlang.",K,[K*2,K/2,C/(A+B),A*B/C],sol_+"K = [C]/([A]·[B]) = %s"%fmt(K,2),"Tirkashev VI bob (muvozanat, grafik)",2)
    elif ask=='conv': q=numq(head+"A moddaning necha foizi reaksiyaga kirishgan (muvozanat holatida)?",x/A0*100,[x/B0*100,A/A0*100,x/(A0+B0)*100,C/A*100],sol_+"A0 = %s; kirishgan %s → %s %%"%(fmt(A0,2),fmt(x,2),fmt(x/A0*100,1)),"Tirkashev VI bob (muvozanat, grafik)",1)
    elif ask=='krev': q=numq(head+"Teskari reaksiya (C ⇌ A + B) uchun muvozanat konstantasini aniqlang.",1/K,[K,1/K*2,1/K/2,A*B],sol_+"K(to'g'ri) = %s; K(teskari) = 1/K = %s"%(fmt(K,2),fmt(1/K,3)),"Tirkashev VI bob (muvozanat, grafik)",3)
    else: q=numq(head+"Muvozanat holatida [C] ning [A] ga nisbatini aniqlang.",C/A,[A/C,C/B,C*A,C/(A+B)],sol_+"[C]/[A] = %s/%s = %s"%(fmt(C,2),fmt(A,2),fmt(C/A,2)),"Tirkashev VI bob (muvozanat, grafik)",2)
    q.kind='graph'; return q
def g_rate(r,tag):
    a=r.choice([2.0,1.6,2.4]); e=r.choice([1.2,1.0,0.8,1.4])
    k=0.3; t1,t2=r.choice([(0,5),(5,10),(0,10),(2,6)])
    c0=a; cinf=r.choice([0.4,0.2]); k=r.choice([0.3,0.25,0.35])
    c=lambda t:cinf+(c0-cinf)*np.exp(-k*t)
    v1=c(t1); v2=c(t2); v1=round(v1,1); v2=round(v2,1)
    if v1<=v2: return g_rate(r,tag)
    tt=np.linspace(0,10,200)
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(tt,c(tt),'b')
    # adjust curve points to labelled values by marking
    for x,y in ((t1,v1),(t2,v2)):
        ax.plot(x,y,'ro',ms=4); ax.plot([x,x],[0,y],'k:',lw=.8); ax.plot([0,x],[y,y],'k:',lw=.8)
    ax.set_xlabel('vaqt, min'); ax.set_ylabel('[A], mol/l'); ax.set_xticks(sorted({0,t1,t2,10})); ax.set_yticks(sorted({0,v1,v2})); ax.set_xlim(0,10.5); ax.set_ylim(0,c0*1.1); ax.grid(alpha=.25)
    name=_save(fig,'rate_%s.png'%tag)
    v=(v1-v2)/(t2-t1)
    ask=r.choice(['v','pct','mol','half']); head="Grafikda A moddaning (A → mahsulot) konsentratsiyasi vaqt bo'yicha o'zgarishi ko'rsatilgan.\n\n![Grafik: tezlik](%s)\n\n"%name
    sl="Grafikdan: %d min – %s mol/l, %d min – %s mol/l; "%(t1,fmt(v1),t2,fmt(v2))
    if ask=='v': q=numq(head+"Reaksiyaning %d-minutdan %d-minutgacha bo'lgan oraliqdagi o'rtacha tezligini mol/(l·min) hisoblang."%(t1,t2),v,[v*2,v/2,(v1-v2),v1/(t2-t1)],sl+"v = (%s − %s)/%d = %s"%(fmt(v1),fmt(v2),t2-t1,fmt(v,3)),"Tirkashev VI bob (reaksiya tezligi, grafik)",3)
    elif ask=='pct': q=numq(head+"%d-minutdan %d-minutgacha A moddaning konsentratsiyasi necha foizga kamaygan (%d-minutdagiga nisbatan)?"%(t1,t2,t1),(v1-v2)/v1*100,[v2/v1*100,(v1-v2)/v2*100,(v1-v2)*100,v2*100],sl+"Δc/c = (%s − %s)/%s = %s %%"%(fmt(v1),fmt(v2),fmt(v1),fmt((v1-v2)/v1*100,1)),"Tirkashev VI bob (reaksiya tezligi, grafik)",1)
    elif ask=='mol':
        Vb=r.choice([2,5,10]); q=numq(head+"Idish hajmi %d l bo'lsa, %d-minutdan %d-minutgacha A moddadan necha mol sarflangan?"%(Vb,t1,t2),(v1-v2)*Vb,[(v1-v2),v1*Vb,v2*Vb,(v1-v2)*Vb*2],sl+"Δn = Δc·V = (%s − %s)·%d = %s mol"%(fmt(v1),fmt(v2),Vb,fmt((v1-v2)*Vb)),"Tirkashev VI bob (reaksiya tezligi, grafik)",None)
    else: q=numq(head+"%d-minutdagi A konsentratsiyasi %d-minutdagidan necha marta katta?"%(t1,t2),v1/v2,[v2/v1,v1-v2,v1*v2,v1/v2*2],sl+"%s/%s = %s"%(fmt(v1),fmt(v2),fmt(v1/v2,2)),"Tirkashev VI bob (reaksiya tezligi, grafik)",2)
    q.kind='graph'; return q
GRAPHS=[g_solub,g_conc,g_rate]
# ---- picture questions
def p_etilen(r):
    kind=r.choice(['vol','obs','role','gas'])
    img='rasmlar/lab_etilen.png'
    if kind=='vol':
        n=r.choice([0.1,0.2,0.5]); y=r.choice([75,80,90]); ans=n*22.4*y/100
        q=numq("Rasmdagi asbobda %s g etil spirti konsentrlangan H2SO4 bilan 170 °C da qizdirildi va %d %% unum bilan etilen olindi. Hosil bo'lgan gazning hajmini (l, n.sh.) aniqlang.\n\n![Etilen olish asbobi](%s)"%(fmt(n*46,2),y,img),ans,[n*22.4,ans*2,n*46*y/100,n*22.4*y/50],"C2H5OH → C2H4 + H2O: n = %s mol → %s l"%(fmt(n),fmt(ans,2)),"10-sinf lab. № 1; Abdusamatov (etilen olinishi)",2)
    elif kind=='obs':
        q=Q("Rasmda etilen olish tajribasi tasvirlangan. Ajralgan gaz bromli suvga va KMnO4 eritmasiga yuttirildi hamda yondirildi. Qaysi kuzatuvlar to'g'ri? 1) bromli suv rangsizlanadi; 2) KMnO4 eritmasi rangsizlanadi; 3) gaz havorang alanga bilan yonadi; 4) gaz qurumli, tutaydigan alanga bilan yonadi\n\n![Etilen olish asbobi](%s)"%img,'1, 2, 3',['1, 2, 4','2, 3, 4','1, 3, 4'],"Etilen (π-bog') Br2 suvini va KMnO4 ni rangsizlantiradi, havorang alanga bilan yonadi; qurumli alanga asetilenga xos","10-sinf lab. № 1",'theory')
    elif kind=='role':
        q=Q("Rasmdagi tajribada C2H5OH va H2SO4 (kons.) aralashmasi (1 : 3) qizdirildi. Quyidagilardan qaysi biri to'g'ri? ![Etilen olish asbobi](%s)"%img,"H2SO4 suv tortuvchi va katalizator vazifasini bajaradi",["H2SO4 oksidlovchi, etilen oksidlanish mahsuloti","H2SO4 reaksiyada ishtirok etmaydi va faqat erituvchi","Hosil bo'lgan gaz havodan og'ir, shuning uchun idish teskari tutiladi"],"Kons. H2SO4 suvni tortib oladi va reaksiyani yo'naltiradi (C2H5OSO3H oraliq mahsulot)","10-sinf lab. № 1",'theory')
        q.text=q.text.replace(" ![Etilen olish asbobi](%s)"%img,"\n\n![Etilen olish asbobi](%s)"%img)
    else:
        q=Q("Rasmdagi tajribada hosil bo'ladigan C2H4 gazining xossalari haqida qaysi fikrlar to'g'ri? 1) suvdan yengil; 2) bromli suvni rangsizlantiradi; 3) polimerlanishi mumkin; 4) alkanlarga xos almashinish reaksiyalariga kirishadi\n\n![Etilen olish asbobi](%s)"%img,'2, 3',['1, 2','2, 4','1, 3, 4'],"Etilen havodan yengil (M = 28 < 29), π-bog' hisobiga birikadi va polimerlanadi; almashinish asosiy emas","10-sinf §13",'theory')
    q.kind='picture'; return q
SEP=[('qum va suv aralashmasi',2),('suv va etanol aralashmasi',1),('suv va kerosin aralashmasi',4),('osh tuzi eritmasidan tuzni ajratib olish',3)]
def p_sep(r):
    img='rasmlar/lab_ajratish.png'
    if r.random()<0.5:
        nm,k=pick(r,SEP); ws=[str(x) for x in (1,2,3,4) if x!=k]
        q=Q("2-rasmda laboratoriyada aralashmalarni ajratish usullari tasvirlangan: 1 — distillash, 2 — filtrlash, 3 — bug'latish, 4 — bo'lgich voronka. %s qaysi rasmdagi usul bilan ajratiladi?\n\n![Ajratish usullari](%s)"%(nm.capitalize(),img),str(k),ws,"%s uchun %s"%(nm,{1:"distillash (qaynash harorati farqi)",2:"filtrlash",3:"bug'latish",4:"bo'lgich voronka (aralashmaydigan suyuqliklar)"}[k]),"7-sinf (aralashmalarni ajratish, 9–13-rasmlar)",'theory')
    else:
        items=r.sample(SEP,3); letters='abc'; txt=['%s) %s'%(letters[i],x[0]) for i,x in enumerate(items)]
        ans=', '.join('%s-%d'%(letters[i],x[1]) for i,x in enumerate(items))
        perms=set([ans])
        import itertools
        ws=[]
        for p in itertools.permutations([x[1] for x in items]):
            c=', '.join('%s-%d'%(letters[i],p[i]) for i in range(3))
            if c!=ans: ws.append(c)
        r.shuffle(ws)
        q=Q("2-rasmda aralashmalarni ajratish usullari tasvirlangan: 1 — distillash, 2 — filtrlash, 3 — bug'latish, 4 — bo'lgich voronka. Aralashmalarni mos rasm raqami bilan moslang: %s.\n\n![Ajratish usullari](%s)"%('; '.join(txt),img),ans,ws[:3],"; ".join('%s → %d'%(x[0],x[1]) for x in items),"7-sinf (aralashmalarni ajratish)",'theory')
    q.kind='picture'; return q
GASQ=[('H2','faqat suvni siqib chiqarish'),('CH4','faqat suvni siqib chiqarish'),('O2','ikkala usul'),('NO2','faqat havoni siqib chiqarish'),('NH3','hech qaysi'),('CO2','faqat havoni siqib chiqarish')]
def p_gas(r):
    img='rasmlar/m_gaz.png'
    kind=r.choice(['both','none','water','air'])
    names={'both':'ikkala usulda ham','none':"rasmdagi usullarning hech birida",'water':"faqat 1-usul (suvni siqib chiqarish) bilan",'air':"faqat 2-usul (havoni siqib chiqarish, idish og'zi yuqoriga) bilan"}
    truth={'H2':'water','CH4':'water','O2':'both','NO2':'air','NH3':'none','CO2':'air'}
    good=[g for g,v in truth.items() if v==kind]; bad=[g for g,v in truth.items() if v!=kind]
    if kind=='air' and 'CO2' in good: good.remove('CO2')  # CO2 water-soluble ambiguity: use NO2 only
    if not good: return p_gas(r)
    a=r.choice(good); ws=r.sample(bad,3)
    q=Q("Rasmda gazlarni to'plashning ikki usuli ko'rsatilgan: 1 — suvni siqib chiqarish, 2 — havoni siqib chiqarish.\n\n![Gaz yig'ish usullari](%s)\n\nQaysi gazni %s to'plash mumkin?"%(img,names[kind]) if kind in('both','water','air') else "Rasmda gazlarni to'plashning ikki usuli ko'rsatilgan: 1 — suvni siqib chiqarish, 2 — havoni siqib chiqarish.\n\n![Gaz yig'ish usullari](%s)\n\nQaysi gazni rasmdagi usullarning hech birida to'plab bo'lmaydi?"%img,a,ws,"%s: suvda %s, havoga nisbatan %s"%(a,{'H2':"erimaydi",'CH4':"erimaydi",'O2':"kam eriydi",'NO2':"suv bilan reaksiyaga kirishadi",'NH3':"yaxshi eriydi"}.get(a,'-'),{'H2':'yengil','CH4':'yengil','O2':'og\'ir','NO2':'og\'ir','NH3':'yengil'}.get(a,'-')),"7-sinf; 9-sinf (gazlarni olish va yig'ish)",'theory')
    q.kind='picture'; return q
def p_ester(r):
    img='rasmlar/m_efir.png'; kind=r.choice(['ratio','sigma','name'])
    if kind=='ratio':
        q=Q("Rasmda ko'rsatilgan molekulalar o'zaro ta'sirlashganda (H2SO4 ishtirokida) hosil bo'lgan murakkab efir molekulasidagi uglerod atomlarining sp³ gibrid orbitallari sonini sp² gibrid orbitallari soniga nisbatini aniqlang.\n\n![Molekulalar](%s)"%img,'4',['3','5','2,5'],"CH3COOC2H5: 3 sp³ uglerod → 12 orbital; 1 sp² uglerod (C=O) → 3 orbital; 12/3 = 4","10-sinf §17, §28",'theory')
    elif kind=='sigma':
        q=Q("Rasmda ko'rsatilgan molekulalar o'zaro ta'sirlashganda hosil bo'lgan murakkab efir molekulasidagi σ-bog'lar sonini aniqlang.\n\n![Molekulalar](%s)"%img,'13',['12','14','11'],"CH3COOC2H5: 8 ta C–H + 2 ta C–C + 1 ta C=O (σ) + 2 ta C–O = 13 σ","10-sinf §17, §28",'theory')
    else:
        q=Q("Rasmda ko'rsatilgan molekulalar H2SO4 ishtirokida o'zaro reaksiyaga kirishdi. Hosil bo'lgan organik moddaning nomini toping.\n\n![Molekulalar](%s)"%img,'etilatsetat',['metilatsetat','etilformiat','propil spirti'],"Sirka kislota + etanol → etilatsetat + H2O (efirlanish)","10-sinf §28",'theory')
    q.kind='picture'; return q
PICS=[p_etilen,p_sep,p_gas,p_ester,p_etilen,p_sep]
# ---- tahlil
QTAB=[
 (['Mg(NO3)2','Zn(NO3)2','NaNO3'],'NaOH',[('oq cho\'kma','cho\'kma erimaydi'),('oq cho\'kma','cho\'kma eriydi'),('o\'zgarish yo\'q','—')],['oz miqdor NaOH','mo\'l miqdor NaOH']),
 (['NaCl','Na2SO4','Na2CO3'],'BaCl2 va HCl',[('o\'zgarish yo\'q','—'),('oq cho\'kma','cho\'kma erimaydi'),('oq cho\'kma','cho\'kma gaz chiqarib eriydi')],['BaCl2 qo\'shilganda','cho\'kmaga HCl qo\'shilganda']),
 (['glitserin','etanol','formalin'],'Cu(OH)2',[('tiniq ko\'k eritma','o\'zgarish yo\'q'),('o\'zgarish yo\'q','o\'zgarish yo\'q'),('o\'zgarish yo\'q','qizil cho\'kma')],['Cu(OH)2 (sovuqda)','Cu(OH)2 (qizdirilganda)']),
 (['glyukoza','saxaroza','kraxmal'],'yod va Cu(OH)2',[('o\'zgarish yo\'q','qizdirilganda qizil cho\'kma'),('o\'zgarish yo\'q','o\'zgarish yo\'q'),('ko\'k rang','o\'zgarish yo\'q')],['I2 eritmasi','Cu(OH)2 (qizdirilganda)']),
 (['AlCl3','MgCl2','KCl'],'NaOH',[('oq cho\'kma','cho\'kma mo\'l ishqorda eriydi'),('oq cho\'kma','cho\'kma erimaydi'),('o\'zgarish yo\'q','—')],['oz miqdor NaOH','mo\'l miqdor NaOH']),
 (['FeCl3','CuSO4','ZnCl2'],'NaOH',[('qo\'ng\'ir cho\'kma','—'),('havorang cho\'kma','—'),('oq cho\'kma','mo\'l ishqorda eriydi')],['NaOH (oz miqdor)','NaOH (mo\'l)']),
 (['fenol','glitserin','formalin'],'FeCl3 va Cu(OH)2',[('binafsha rang','—'),('o\'zgarish yo\'q','tiniq ko\'k eritma'),('o\'zgarish yo\'q','qizdirilganda qizil cho\'kma')],['FeCl3','Cu(OH)2']),
 (['NaCl','NaBr','NaI'],'AgNO3',[('oq cho\'kma','—'),('och sariq cho\'kma','—'),('sariq cho\'kma','—')],['AgNO3 qo\'shilganda','—']),
 (['Na2SO4','K2CO3','NH4Cl'],'HCl va NaOH',[('o\'zgarish yo\'q','o\'zgarish yo\'q'),('gaz ajraladi','o\'zgarish yo\'q'),('o\'zgarish yo\'q','o\'tkir hidli gaz ajraladi')],['HCl qo\'shilganda','NaOH qo\'shib qizdirilganda']),
]
import itertools
def t_qualtab(r):
    names,rg,obs,heads=pick(r,QTAB)
    order=list(range(3)); r.shuffle(order); lab='XYZ'
    two=obs[0][1]!='—' or any(o[1]!='—' for o in obs)
    cols=heads if any(o[1]!='—' for o in obs) else heads[:1]
    rows=''.join('| %s | %s |\n'%(lab[i],' | '.join(obs[order[i]][:len(cols)] if len(cols)==2 else obs[order[i]][:1])) for i in range(3))
    tb='| Probirka | %s |\n|---|%s\n%s'%(' | '.join(cols),'---|'*len(cols),rows.rstrip('\n'))
    ans=', '.join('%s – %s'%(lab[i],names[order[i]]) for i in range(3))
    ws=[]
    for p in itertools.permutations(range(3)):
        c=', '.join('%s – %s'%(lab[i],names[p[i]]) for i in range(3))
        if c!=ans: ws.append(c)
    r.shuffle(ws)
    q=Q("Uch probirkada (X, Y, Z) %s eritmalari bor (tartibsiz). Ularga %s ta'sir ettirildi. Kuzatuvlar jadvalda:\n\n%s\n\nX, Y, Z probirkalardagi moddalarni aniqlang."%(', '.join(names),rg,tb),ans,ws[:3],"Sifat reaksiyalar: "+'; '.join('%s: %s'%(names[i],' / '.join(o for o in obs[i] if o!='—')) for i in range(3)),"7–10-sinf va Tashev (laboratoriya ishlari, sifat reaksiyalar)",'theory'); q.kind='table'; return q
SAFE=[("Konsentrlangan kislotani suvga ohista, aralashtirib quyiladi",True),("Suvni konsentrlangan kislotaga tez quyish mumkin",False),("Probirka qizdirilganda og'zi odamga qaratilmaydi",True),("Reaktivlarni tatib ko'rish mumkin",False),("Kimyoviy moddalar hidini bevosita nafas olib aniqlash kerak",False),("Kuygan joy ko'p suv bilan yuviladi",True),("Ortiqcha reaktiv idishga qaytariladi",False),("Spirt lampa boshqa lampadan yoqilmaydi",True),("Zaharli gaz ajraladigan tajriba mo'rili shkafda o'tkaziladi",True),("Ishqor teriga tushsa, qo'l suv bilan yuviladi",True)]
def t_safety(r):
    ans,ws,it=stm(r,SAFE)
    return Q("Kimyo laboratoriyasida ishlash qoidalari haqida qaysi fikrlar to'g'ri? "+'; '.join('%d) %s'%(i+1,x[0]) for i,x in enumerate(it)),ans,ws,'; '.join('%d) %s'%(i+1,'to\'g\'ri' if x[1] else 'noto\'g\'ri') for i,x in enumerate(it)),"7-sinf (xavfsizlik qoidalari); 10-sinf lab.",'theory')
def c_prep(r):
    kind=r.choice(['dil','diag','hyd'])
    if kind=='dil':
        m=r.choice([200,300,500]); w1=r.choice([5,10,20]); w0=r.choice([40,50,80]); x=m*w1/w0
        return numq("%d g %d %% li eritma tayyorlash uchun %d %% li eritmadan necha gramm olish kerak (qolgani suv)?"%(m,w1,w0),x,[m-x,m*w1/100,x*2,m*w0/w1],"m(modda) = %d·%s = %s g; %s/%s = %s g eritma"%(m,fmt(w1/100),fmt(m*w1/100),fmt(m*w1/100),fmt(w0/100),fmt(x,2)),"Tirkashev III bob (eritma tayyorlash)",2)
    if kind=='diag':
        m=r.choice([200,300,600]); a=r.choice([20,30,40]); b=r.choice([5,10]); c=(a+b)//2 if (a+b)%2==0 else a-5
        if not (b<c<a): c=(a+b)/2
        x=m*(c-b)/(a-b)
        return numq("%s %% li va %s %% li eritmalardan %d g %s %% li eritma tayyorlash uchun %s %% li eritmadan necha gramm olish kerak?"%(a,b,m,fmt(c),a),x,[m-x,m*c/a,x*2,m/2],"Diagonal qoida: (c − %s):(%s − c) = %s : %s → %s g"%(fmt(b),fmt(a),fmt(c-b),fmt(a-c),fmt(x,2)),"Tirkashev III bob",2)
    f,mm,mw=pick(r,[('CuSO4.5H2O',250,160),('Na2CO3.10H2O',286,106)]); m=r.choice([100,200,400]); w=r.choice([4,5,8,10]); x=m*w/100/mw*mm
    return numq("%d g %d %% li %s eritmasini %s dan tayyorlash uchun necha gramm kristallogidrat kerak?"%(m,w,f.split('.')[0],f.replace('.','·')),x,[m*w/100,x*2,m*w/100*mm/mw*0.5,m-x],"m(tuz) = %s g; kristallogidrat: %s·%d/%d = %s g"%(fmt(m*w/100),fmt(m*w/100),mm,mw,fmt(x,2)),"Tirkashev III bob; 7-sinf (eritma tayyorlash)",2)
