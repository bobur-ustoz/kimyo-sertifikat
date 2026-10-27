from core import *
from pic import _save
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Polygon, FancyArrowPatch
import numpy as np, math, itertools
U=lambda t:t
def _img(name,alt): return "![%s](rasmlar/gen/%s)"%(alt,name.split('/')[-1])
def _rid(r): return r.randrange(10**6)
def _opts(ans,pool,r,n=3):
    ws=[x for x in dict.fromkeys(pool) if x!=ans]; r.shuffle(ws); return ws[:n]
# ===================================================================== GRAFIKLAR
def g_decay(r,tag):
    T=r.choice([2,3,4,5,10]); N0=r.choice([80,160,64,100,200]); tt=np.linspace(0,4*T,200)
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(tt,N0*0.5**(tt/T),'b')
    pts=[(0,N0),(T,N0/2),(2*T,N0/4)]
    for x,y in pts: ax.plot(x,y,'ro',ms=4); ax.plot([x,x],[0,y],'k:',lw=.8); ax.plot([0,x],[y,y],'k:',lw=.8)
    ax.set_xlabel('vaqt, kun'); ax.set_ylabel('radioaktiv yadrolar soni, mln'); ax.set_xticks([0,T,2*T,4*T]); ax.set_yticks([0,N0/4,N0/2,N0]); ax.grid(alpha=.25)
    img=_img(_save(fig,'de_%s.png'%tag),'Grafik: radioaktiv yemirilish')
    ask=r.choice(['T','left','n'])
    head="Radioaktiv izotop yadrolari sonining vaqtga bog'liqligi grafikda berilgan.\n\n%s\n\n"%img
    if ask=='T': q=numq(head+"Izotopning yarim yemirilish davrini (kun) aniqlang.",T,[T*2,T/2 if T>2 else T+1,2*T+T,T+1],"N = N0/2 bo'lgan vaqt: T = %d kun"%T,"11-sinf (yadro, yarim yemirilish)",0)
    elif ask=='left': k=r.choice([3,4]); q=numq(head+"%d·T vaqtdan keyin dastlabki yadrolarning necha foizi qoladi?"%k,100/2**k,[100/k,100/2**(k-1),100/2**(k+1),50],"%d yarim yemirilish: 100/2^%d = %s %%"%(k,k,fmt(100/2**k,2)),"11-sinf (yadro)",2)
    else: q=numq(head+"%d kundan keyin necha mln yadro yemirilgan bo'ladi?"%(2*T),N0-N0/4,[N0/4,N0/2,N0,N0-N0/2],"Qolgan %s mln; yemirilgan %s mln"%(fmt(N0/4),fmt(N0*0.75)),"11-sinf (yadro)",2)
    q.kind='graph'; return q
def g_line(r,tag):
    rx=[('CaCO3',100,'CO2',22.4),('Zn',65,'H2',22.4),('Mg',24,'H2',22.4),('Na2CO3',106,'CO2',22.4),('Al',27,'H2',33.6)]
    a,Ma,g,Vm=r.choice(rx); x1=r.choice([10,20,25,50]);
    vmax=x1*Vm/Ma
    fig,ax=plt.subplots(figsize=(5,3.2)); xs=np.linspace(0,x1*2,10); ax.plot(xs,xs*Vm/Ma,'b'); ax.plot(x1,vmax,'ro'); ax.plot([x1,x1],[0,vmax],'k:',lw=.8); ax.plot([0,x1],[vmax,vmax],'k:',lw=.8)
    ax.set_xlabel('m(%s), g'%a); ax.set_ylabel('V(%s), l (n.sh.)'%g); ax.set_xticks([0,x1,2*x1]); ax.set_yticks([0,round(vmax,2)]); ax.grid(alpha=.25)
    img=_img(_save(fig,'li_%s.png'%tag),'Grafik: gaz hajmi massaga bog\'liq')
    head="Mo'l kislota bilan %s ning turli massalari ta'sirlashganda ajralgan %s hajmi grafikda keltirilgan (n.sh.).\n\n%s\n\n"%(a,g,img)
    ask=r.choice(['M','V3'])
    if ask=='M': q=numq(head+"%s ning molyar massasini (g/mol) grafikdan aniqlang."%a,Ma,[Ma*2,Ma/2,Ma+Vm,Ma*1.5],"Grafikdan %s g → %s l, M = m·Vm/V = %s g/mol"%(x1,fmt(vmax,2),fmt(Ma)),"8-sinf (molyar hajm, grafik)",None)
    else: m3=r.choice([2*x1,x1*3,x1/2]); q=numq(head+"%s g %s dan qancha hajm (l) gaz ajraladi?"%(fmt(m3),a),m3*Vm/Ma,[m3*Vm/Ma*2,m3*Vm/Ma/2,vmax,m3*Vm],"V = %s·%s/%s = %s l"%(fmt(m3),fmt(Vm),fmt(Ma),fmt(m3*Vm/Ma,2)),"8-sinf (molyar hajm, grafik)",2)
    q.kind='graph'; return q
def g_energy(r,tag):
    Ea=r.choice([80,100,120,60]); dH=r.choice([-40,-60,-90,50,70]); E0=20
    x=np.linspace(0,10,300); top=E0+Ea; end=E0+dH
    y=E0+(end-E0)*(1/(1+np.exp(-(x-5)*1.6)))+Ea*np.exp(-((x-4)**2)/1.2)
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(x,y,'b'); ax.axhline(E0,ls=':',c='gray'); ax.axhline(end,ls=':',c='gray')
    ax.set_xlabel('reaksiya yo\'li'); ax.set_ylabel('energiya, kJ/mol'); ax.set_yticks(sorted({E0,end,round(max(y))})); ax.set_xticks([]); ax.grid(alpha=.2)
    img=_img(_save(fig,'en_%s.png'%tag),'Grafik: energetik diagramma')
    top=round(max(y)); Eaf=top-E0
    head="Reaksiyaning energetik diagrammasi berilgan (boshlang'ich moddalar energiyasi %d, mahsulotlar %d kJ/mol).\n\n%s\n\n"%(E0,end,img)
    ask=r.choice(['dH','Ea','type'])
    if ask=='dH': q=numq(head+"Reaksiyaning issiqlik effektini (|ΔH|, kJ/mol) aniqlang.",abs(dH),[abs(dH)+Eaf,Eaf,abs(dH)*2,abs(dH)/2],"|ΔH| = |%d − %d| = %d"%(end,E0,abs(dH)),"Tirkashev VI bob (issiqlik effekti, grafik)",0)
    elif ask=='Ea': q=numq(head+"To'g'ri reaksiyaning aktivlanish energiyasini (kJ/mol) aniqlang.",Eaf,[Eaf+abs(dH),abs(dH),Eaf*2,top],"Ea = %d − %d = %d"%(top,E0,Eaf),"Tirkashev VI bob (aktivlanish energiyasi, grafik)",0)
    else:
        a='ekzotermik' if dH<0 else 'endotermik'; q=Q(head+"Reaksiya qaysi turga kiradi?",a,[x_ for x_ in ['ekzotermik','endotermik','katalitik','teskarilanmas'] if x_!=a][:3],"Mahsulotlar energiyasi %s → %s"%('past' if dH<0 else 'yuqori',a),"Tirkashev VI bob (termokimyo, grafik)",'graph')
    q.kind='graph'; return q
def g_pie(r,tag):
    parts=r.choice([(('Cu','Zn'),(64,65)),(('Fe','C'),(56,12)),(('Cu','Sn'),(64,119)),(('Al','Mg'),(27,24)),(('Cu','Ni'),(64,59))])
    names,Ms=parts; w=r.choice([60,70,75,80,90]); fig,ax=plt.subplots(figsize=(3.8,3.4)); ax.pie([w,100-w],labels=['%s'%names[0],'%s'%names[1]],autopct='%1.0f%%',colors=['#EE8A3C','#4F86D6'],startangle=90,wedgeprops=dict(edgecolor='white',linewidth=2),textprops=dict(fontsize=11))
    img=_img(_save(fig,'pi_%s.png'%tag),'Doira diagrammasi: qotishma tarkibi')
    m=r.choice([50,100,200,250]); head="Qotishmaning massa bo'yicha tarkibi doira diagrammasida ko'rsatilgan.\n\n%s\n\n"%img
    ask=r.choice(['m','n','ratio'])
    if ask=='m': q=numq(head+"%s g qotishmadagi %s massasini (g) toping."%(fmt(m),names[1]),m*(100-w)/100,[m*w/100,m*(100-w)/100*2,m/2,m*(100-w)],"m = %s·%d/100 = %s g"%(fmt(m),100-w,fmt(m*(100-w)/100,2)),"8-sinf (massa ulushi, diagramma)",2)
    elif ask=='n': q=numq(head+"%s g qotishmadagi %s ning modda miqdorini (mol) hisoblang."%(fmt(m),names[0]),m*w/100/Ms[0],[m*w/100,m*(100-w)/100/Ms[1],m*w/100/Ms[0]*2,m/Ms[0]],"n = %s·%d/(100·%d) = %s mol"%(fmt(m),w,Ms[0],fmt(m*w/100/Ms[0],3)),"8-sinf (mol, diagramma)",2)
    else:
        q=numq(head+"Qotishmadagi %s va %s atomlari sonining nisbati (%s uchun %s ga bo'lingan)ni toping."%(names[0],names[1],names[0],names[1]),(w/Ms[0])/((100-w)/Ms[1]),[w/(100-w),Ms[0]/Ms[1],(100-w)/w,(w/Ms[0])*2],"n(%s)/n(%s) = (%d/%d)/(%d/%d)"%(names[0],names[1],w,Ms[0],100-w,Ms[1]),"8-sinf (mol, diagramma)",2)
    q.kind='graph'; return q
def g_hydr(r,tag):
    grp=r.choice([('VIA',['H2O','H2S','H2Se'],[100,-60,-41],'H2O'),('VIIA',['HF','HCl','HBr','HI'],[20,-85,-67,-35],'HF'),('VA',['NH3','PH3','AsH3'],[-33,-88,-62],'NH3')])
    n,names,bp,hb=grp; fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(names,bp,'o-b'); ax.set_ylabel('qaynash harorati, °C'); ax.grid(alpha=.25); ax.set_xlabel('%s guruh elementlarining vodorodli birikmalari'%n)
    img=_img(_save(fig,'hy2_%s.png'%tag),'Grafik: vodorodli birikmalarning qaynash harorati')
    head="%s guruh elementlarining vodorodli birikmalari qaynash haroratlari grafikda berilgan.\n\n%s\n\n"%(n,img)
    ask=r.choice(['anom','why'])
    if ask=='anom': q=Q(head+"Qaysi birikmaning qaynash harorati qonuniyatdan keskin farq qiladi?",hb,[x for x in names if x!=hb][:3],"Molekulalar orasida vodorod bog'lanish %s da"%hb,"8-sinf (vodorod bog'lanish, grafik)",'graph')
    else: q=Q(head+"%s ning qaynash harorati yuqoriligining sababi nima?"%hb,"Molekulalararo vodorod bog'lanish borligi",["Molekula massasi kattaligi","Ion bog'lanish mavjudligi","Kovalent bog' mustahkamligi"],"%s molekulalari orasida H-bog' hosil bo'ladi"%hb,"8-sinf (vodorod bog'lanish, grafik)",'graph')
    q.kind='graph'; return q
def g_radii(r,tag):
    per=r.choice([('Li','Be','B','C','N','O','F'),('Na','Mg','Al','Si','P','S','Cl')]); rad=[152,112,85,77,75,73,71] if per[0]=='Li' else [186,160,143,118,110,103,99]
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.bar(per,rad,color='#6fa86f'); ax.set_ylabel('atom radiusi, pm'); ax.grid(axis='y',alpha=.25)
    img=_img(_save(fig,'ra_%s.png'%tag),'Diagramma: atom radiuslari')
    head="%d-davr elementlari atom radiuslarining o'zgarishi diagrammada ko'rsatilgan.\n\n%s\n\n"%(2 if per[0]=='Li' else 3,img)
    ask=r.choice(['big','trend','Cl'])
    if ask=='big': q=Q(head+"Qaysi elementning atom radiusi eng katta?",per[0],[per[3],per[5],per[6]],"Davrda chapdan o'ngga radius kamayadi: eng katta %s"%per[0],"8-sinf (davriy qonun, diagramma)",'graph')
    elif ask=='trend': q=Q(head+"Davr bo'yicha chapdan o'ngga atom radiusi qanday o'zgaradi va sababi nima?","Kamayadi, yadro zaryadi ortishi tufayli",["Ortadi, qavatlar soni ko'payishi tufayli","Kamayadi, qavatlar soni kamayishi tufayli","O'zgarmaydi"],"Qavatlar soni bir xil, Z ortadi → tortishuv kuchayadi","8-sinf (davriy qonun, diagramma)",'graph')
    else: i=r.choice([2,3,5]); q=numq(head+"%s atomi radiusi %s atomi radiusidan necha pm katta?"%(per[i],per[6]),rad[i]-rad[6],[rad[i]+rad[6],rad[i],rad[i]-rad[6]+10,rad[6]],"%d − %d = %d pm"%(rad[i],rad[6],rad[i]-rad[6]),"8-sinf (davriy qonun, diagramma)",0)
    q.kind='graph'; return q
def g_phbar(r,tag):
    items=[('HCl',1),('CH3COOH',3),('H2O',7),('NH3 (suvli)',11),('Na2CO3',12),('NaOH',13),('H2CO3',4)]
    sel=r.sample(items,5); fig,ax=plt.subplots(figsize=(5,3.2)); ax.bar([s[0] for s in sel],[s[1] for s in sel],color='#8a7fc1'); ax.set_ylabel('pH (0,1 mol/l eritma)'); ax.set_yticks(range(0,15,2)); ax.grid(axis='y',alpha=.25); plt.setp(ax.get_xticklabels(),fontsize=7)
    img=_img(_save(fig,'pb_%s.png'%tag),'Diagramma: eritmalar pH i')
    head="Konsentratsiyasi bir xil (0,1 mol/l) eritmalarning pH qiymatlari diagrammada berilgan.\n\n%s\n\n"%img
    acid=[s[0] for s in sel if s[1]<7]; base=[s[0] for s in sel if s[1]>7]; neu=[s[0] for s in sel if s[1]==7]
    ask=r.choice(['acid','base','strong'])
    pool=[s[0] for s in sel]
    if ask=='acid' and acid: a=min(sel,key=lambda s:s[1])[0]; q=Q(head+"Qaysi eritmada [H⁺] eng katta?",a,_opts(a,pool,r),"pH eng kichik → [H⁺] eng katta: %s"%a,"Tirkashev V bob (pH, diagramma)",'graph')
    elif ask=='base' and base: a=max(sel,key=lambda s:s[1])[0]; q=Q(head+"Qaysi eritmada [OH⁻] eng katta?",a,_opts(a,pool,r),"pH eng katta → [OH⁻] eng katta: %s"%a,"Tirkashev V bob (pH, diagramma)",'graph')
    else:
        s=r.choice(sel); k=s[1]; q=numq(head+"%s eritmasidagi H⁺ konsentratsiyasi qancha marta (10 ning darajasi sifatida) neytral eritmadagidan katta? (neytral pH = 7)"%s[0] if k<7 else head+"%s eritmasining pH i neytraldan necha birlikka farq qiladi?"%s[0],10**(7-k) if k<7 else abs(k-7),[10**(7-k)*10 if k<7 else abs(k-7)+1,abs(k-7),10**(abs(k-7)+1),abs(k-7)*10],"|pH − 7| = %d"%abs(k-7),"Tirkashev V bob (pH, diagramma)",0)
        if k==7: return g_phbar(r,tag)
    q.kind='graph'; return q
def g_air(r,tag):
    fig,ax=plt.subplots(figsize=(4.6,3.2)); gs=['N₂','O₂','Ar','CO₂ va boshq.']; v=[78,21,0.9,0.1]; ax.bar(gs,v,color='#6aa0d8'); ax.set_ylabel('hajmiy ulush, %'); ax.set_yticks([0,21,78,100]); ax.grid(axis='y',alpha=.25)
    img=_img(_save(fig,'ai_%s.png'%tag),'Diagramma: havo tarkibi')
    V=r.choice([50,100,200,250,500]); head="Quruq havo tarkibi diagrammada keltirilgan.\n\n%s\n\n"%img
    ask=r.choice(['O2','mass','D'])
    if ask=='O2': q=numq(head+"%s l (n.sh.) havo tarkibidagi kislorod hajmini (l) toping."%fmt(V),V*0.21,[V*0.78,V*0.21*2,V*0.21/2,V*0.1],"V(O2) = %s·0,21 = %s l"%(fmt(V),fmt(V*.21,2)),"8-sinf (havo tarkibi, diagramma)",2)
    elif ask=='mass': q=numq(head+"%s l (n.sh.) havodagi kislorodning massasini (g) hisoblang."%fmt(V),V*0.21/22.4*32,[V*0.78/22.4*28,V*0.21/22.4*16,V*0.21*32,V*0.21/22.4*64],"n(O2) = %s/22,4 mol; m = ·32 = %s g"%(fmt(V*.21,2),fmt(V*.21/22.4*32,2)),"8-sinf (havo tarkibi, diagramma)",2)
    else:
        Mav=0.78*28+0.21*32+0.009*40+0.001*44; q=numq(head+"Havoning o'rtacha molyar massasini (g/mol) taxminan hisoblang (N2, O2, Ar, CO2 hisobga olinsin).",Mav,[Mav+3,Mav-3,Mav*2,(28+32)/2],"M = 0,78·28 + 0,21·32 + 0,009·40 + 0,001·44 ≈ %s"%fmt(Mav,1),"8-sinf (havo tarkibi, diagramma)",1)
    q.kind='graph'; return q
def g_massp(r,tag):
    iso=r.choice([(('³⁵Cl','³⁷Cl'),(35,37)),(('⁶³Cu','⁶⁵Cu'),(63,65)),(('¹⁰B','¹¹B'),(10,11)),(('⁷⁹Br','⁸¹Br'),(79,81)),(('²⁴Mg','²⁶Mg'),(24,26))])
    nm,ms=iso; p=r.choice([75,70,80,50,60]); fig,ax=plt.subplots(figsize=(4.8,3.2)); ax.bar([str(ms[0]),str(ms[1])],[p,100-p],width=0.25,color='#c15a5a'); ax.set_xlabel('massa soni (m/z)'); ax.set_ylabel('nisbiy miqdor, %'); ax.set_yticks([0,p,100-p,100]); ax.grid(axis='y',alpha=.25)
    img=_img(_save(fig,'ms_%s.png'%tag),'Massa-spektr')
    head="Elementning massa-spektri (izotoplar tarqalganligi) berilgan.\n\n%s\n\n"%img
    avg=(ms[0]*p+ms[1]*(100-p))/100
    ask=r.choice(['avg','per'])
    if ask=='avg': q=numq(head+"Elementning o'rtacha nisbiy atom massasini aniqlang.",avg,[(ms[0]+ms[1])/2,ms[0]*(100-p)/100+ms[1]*p/100,ms[0],ms[1]],"Ar = (%d·%d + %d·%d)/100 = %s"%(ms[0],p,ms[1],100-p,fmt(avg,2)),"8-sinf (izotoplar, massa-spektr)",2)
    else: q=numq(head+"1000 ta atomning nechtasi og'irroq izotopga tegishli?",(100-p)*10,[p*10,(100-p)*100,(100-p),500],"1000·%d/100 = %d"%(100-p,(100-p)*10),"8-sinf (izotoplar, massa-spektr)",0)
    q.kind='graph'; return q
GRAPHS3=[g_decay,g_line,g_energy,g_pie,g_hydr,g_radii,g_phbar,g_air,g_massp]
def g_solub2(r,tag):
    S={'KNO3':[13,32,64,110,169],'NaCl':[35.7,35.9,36.4,37.1,38.0],'KCl':[28,34,40,45.5,51],'NH4Cl':[29,37,46,55,66]}
    a,b=r.sample(list(S),2); T=[0,20,40,60,80]
    fig,ax=plt.subplots(figsize=(5,3.2)); ax.plot(T,S[a],'o-b',label=a); ax.plot(T,S[b],'s-r',label=b); ax.legend(); ax.set_xlabel('harorat, °C'); ax.set_ylabel('eruvchanlik, g/100 g suv'); ax.set_xticks(T); ax.grid(alpha=.25)
    img=_img(_save(fig,'s2_%s.png'%tag),'Grafik: ikki tuz eruvchanligi')
    t=r.choice([40,60,80]); i=T.index(t); head="%s va %s eruvchanligining haroratga bog'liqligi grafikda berilgan.\n\n%s\n\n"%(a,b,img)
    big=a if S[a][i]>S[b][i] else b
    q=Q(head+"%d °C da qaysi tuzning eruvchanligi katta?"%t,big,[x for x in S if x!=big][:3],"%d °C: %s – %s, %s – %s g/100 g"%(t,a,S[a][i],b,S[b][i]),"Tirkashev III bob (eruvchanlik, grafik)",'graph'); q.kind='graph'; return q
