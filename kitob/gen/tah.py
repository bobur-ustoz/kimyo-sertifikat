from core import *
import itertools
def _cap(s): return s[0].upper()+s[1:]
def _distr(ans,pool,r,n=3):
    ws=[x for x in dict.fromkeys(pool) if x!=ans]; r.shuffle(ws); return ws[:n]
SEP=[('qum va suv aralashmasi','filtrlash'),('temir qipig\'i va oltingugurt kukuni','magnit yordamida ajratish (temir tortiladi)'),('osh tuzi eritmasidan tuz','bug\'latish'),('suv va etanol aralashmasi','distillash (fraksiyalab haydash)'),('suv va benzin aralashmasi','ajratgich voronka'),('yod va qum aralashmasi','sublimatsiya (yod haydaladi)'),('tuz va qum aralashmasi','suvda eritib, filtrlash, so\'ng bug\'latish'),('kerosin va suv aralashmasi','ajratgich voronka'),('mis kukuni va temir qipig\'i','magnit yordamida ajratish (temir tortiladi)'),('suv va sirka kislota aralashmasi','distillash (fraksiyalab haydash)')]
def t_sep(r):
    nm,m=r.choice(SEP); ws=_distr(m,[x[1] for x in SEP],r)
    q=Q("Quyidagi aralashmani ajratish uchun qaysi usul mos: %s?"%nm,m,ws,"%s: %s"%(nm,m),"7-sinf (aralashmalarni ajratish usullari)",'theory'); q.kind='theory'; return q
EQP=[('o\'lchov silindri','suyuqlik hajmini o\'lchash'),('byuretka','titrlashda reagent hajmini aniq o\'lchash'),('chinni kosacha','eritmalarni bug\'latish'),('Bunzen kolbasi bilan voronka','vakuum ostida filtrlash'),('tigel','qattiq moddalarni yuqori haroratda qizdirish'),('ajratgich voronka','aralashmaydigan suyuqliklarni ajratish'),('Kipp apparati','gaz (H₂, CO₂, H₂S) olish'),('spirt lampasi','probirkani qizdirish'),('Liebix sovutgichi','distillashda bug\'ni kondensatsiyalash'),('eksikator','moddalarni namlikdan saqlash'),('pipetka','eritmaning kichik hajmlarini o\'lchab olish')]
def t_equip(r):
    nm,fn=r.choice(EQP)
    if r.random()<0.5:
        q=Q("Kimyoviy laboratoriyada %s nima uchun ishlatiladi?"%nm,fn,_distr(fn,[x[1] for x in EQP],r),"%s – %s"%(nm,fn),"7-sinf (laboratoriya jihozlari)",'theory')
    else:
        q=Q("«%s» vazifasini bajaruvchi laboratoriya jihozini aniqlang."%fn,nm,_distr(nm,[x[0] for x in EQP],r),"%s – %s"%(nm,fn),"7-sinf (laboratoriya jihozlari)",'theory')
    q.kind='theory'; return q
ION=[('Cl⁻','AgNO3','oq cho\'kma (AgCl)'),('SO4²⁻','BaCl2','oq cho\'kma (BaSO4), HCl da erimaydi'),('CO3²⁻','HCl','rangsiz gaz (CO2) ajraladi'),('Fe³⁺','NaOH','qo\'ng\'ir cho\'kma (Fe(OH)3)'),('Cu²⁺','NaOH','havorang cho\'kma (Cu(OH)2)'),('NH4⁺','NaOH (qizdirilganda)','o\'tkir hidli gaz (NH3)'),('Ag⁺','HCl','oq cho\'kma (AgCl)'),('I⁻','AgNO3','sariq cho\'kma (AgI), HNO3 da erimaydi'),('Br⁻','AgNO3','och sariq cho\'kma (AgBr)'),('PO4³⁻','AgNO3','sariq cho\'kma (Ag3PO4), HNO3 da eriydi'),('Fe²⁺','NaOH','oq-yashil cho\'kma (Fe(OH)2)'),('Ba²⁺','H2SO4','oq cho\'kma (BaSO4), HCl da erimaydi')]
def t_ion(r):
    ion,rg,ob=r.choice(ION)
    if r.random()<0.5:
        q=Q("%s ionini aniqlash uchun qaysi reagent mos va qanday belgi kuzatiladi?"%ion,"%s: %s"%(rg,ob),_distr("%s: %s"%(rg,ob),["%s: %s"%(a,b) for _,a,b in ION],r),"%s + %s → %s"%(ion,rg,ob),"9-sinf (sifat reaksiyalar)",'theory')
    else:
        q=Q("Eritmaga %s qo'shilganda %s kuzatildi. Eritmada qaysi ion bor?"%(rg,ob),ion,_distr(ion,[x[0] for x in ION],r),"%s + %s → %s"%(ion,rg,ob),"9-sinf (sifat reaksiyalar)",'theory')
    q.kind='theory'; return q
OBT=[('vodorod','Zn + HCl','suvni siqib chiqarish usulida'),('karbonat angidrid','CaCO3 + HCl','havoni siqib chiqarish (idish og\'zi yuqoriga)'),('kislorod','KMnO4 (qizdirish)','suvni siqib chiqarish usulida'),('ammiak','NH4Cl + Ca(OH)2 (qizdirish)','havoni siqib chiqarish (idish og\'zi pastga)'),('etilen','C2H5OH + H2SO4 (kons.), 170 °C','suvni siqib chiqarish usulida'),('asetilen','CaC2 + H2O','suvni siqib chiqarish usulida'),('xlor','MnO2 + HCl (kons.)','havoni siqib chiqarish (idish og\'zi yuqoriga)'),('metan','CH3COONa + NaOH (qizdirish)','suvni siqib chiqarish usulida'),('vodorod sulfid','FeS + HCl','havoni siqib chiqarish (idish og\'zi yuqoriga)')]
def t_obtain(r):
    g,rx,col=r.choice(OBT)
    if r.random()<0.6:
        q=Q("Laboratoriyada %s olish uchun qaysi moddalar ishlatiladi?"%g,rx,_distr(rx,[x[1] for x in OBT],r),"%s olinadi: %s"%(g,rx),"9–10-sinf (laboratoriya usullari bilan gaz olish)",'theory')
    else:
        q=Q("Laboratoriyada olingan %s qanday usulda yig'iladi?"%g,col,_distr(col,[x[2] for x in OBT]+["gazni suyuqlantirib yig'iladi","ochiq havoda tutib olinadi"],r),"%s: %s"%(g,col),"9–10-sinf (gazlarni yig'ish)",'theory')
    q.kind='theory'; return q
IND=[('lakmus','kislotali','qizil'),('lakmus','ishqoriy','ko\'k'),('metiloranj','kislotali','qizil'),('metiloranj','ishqoriy','sariq'),('fenolftalein','ishqoriy','malina rangga kiradi (pushti)'),('fenolftalein','kislotali','rangsiz'),('lakmus','neytral','binafsha')]
def t_indic(r):
    ind,med,col=r.choice(IND)
    q=Q("%s indikatori %s muhitda qanday rang beradi?"%(_cap(ind),med),col,_distr(col,[x[2] for x in IND],r),"%s: %s muhit → %s"%(ind,med,col),"8-sinf (indikatorlar)",'theory'); q.kind='theory'; return q
TAHLIL=[t_sep,t_equip,t_ion,t_obtain,t_indic]
