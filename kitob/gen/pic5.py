from core import *
def _d(ans,pool,r,n=3):
    ws=[x for x in dict.fromkeys(pool) if x!=ans]; r.shuffle(ws); return ws[:n]
def _im(name,alt): return "![%s](rasmlar/darslik/%s.png)"%(alt,name)
def _q(text,ans,pool,sol,src,r):
    q=Q(text,ans,_d(ans,pool,r),sol,src,'picture'); q.kind='picture'; return q
def _n(text,ans,wr,sol,src,nd=2):
    q=numq(text,ans,wr,sol,src,nd); q.kind='picture'; return q
SEP_ALL=['filtrlash','distillash','bug\'latish','dekantatsiya (tindirish)','ajratgich voronka yordamida ajratish','magnit yordamida ajratish']
MIX_ALL=['suv va qum','suv va etanol','osh tuzi eritmasi','suv va kerosin','temir va oltingugurt kukuni','loyqa suv']
def f_spirt(r):
    names={1:'idish',2:'metall disk',3:'pilik',4:'qalpoqcha'}; k=r.choice([1,2,3,4])
    return _q("Rasmda spirt lampasining tuzilishi ko'rsatilgan. %d raqami bilan belgilangan qism nima deb ataladi?\n\n%s"%(k,_im('d_spirt_lampa','Spirt lampasi')),names[k],list(names.values())+['shtativ','tutqich'],"Spirt lampasi: idish (1), metall disk (2), pilik (3), qalpoqcha (4)","7-sinf (laboratoriya jihozlari, 3-rasm)",r)
def f_alanga(r):
    h="\n\n%s"%_im('d_alanga','Alanga zonalari')
    k=r.choice(['hot','cold','mid'])
    if k=='hot': return _q("Rasmda spirt lampasi alangasi ko'rsatilgan. Probirkani qizdirishda alanganing qaysi qismidan foydalaniladi?"+h,"1 – yuqori chetki xira qism",["2 – o'rta ravshan qism","3 – pastki qism, pilikka yaqin","hamma qismidan bir xil"],"Alanganing eng issiq joyi – yuqori chetki xira qismi (1)","7-sinf (spirt lampasi alangasi, 5-rasm)",r)
    if k=='cold': return _q("Rasmda spirt lampasi alangasi tasvirlangan. Alanganing qaysi qismi eng kam issiq va pilikka yaqin?"+h,"3 – pastki qism",["1 – yuqori qism","2 – o'rta qism","hamma qismi bir xil"],"3 – pastki, juda xira, issiq bo'lmagan qism","7-sinf (5-rasm)",r)
    return _q("Rasmda alanganing 2 raqami bilan ko'rsatilgan qismi qanday xususiyatga ega?"+h,"ravshan, issiq qism",["chetlari xira, eng issiq qism","juda xira, issiq bo'lmagan qism","rangsiz va sovuq qism"],"2 – o'rta ravshan, issiq qism","7-sinf (5-rasm)",r)
def f_tind(r):
    h="\n\n%s"%_im('d_tindirish','Aralashmani ajratish')
    if r.random()<.5: return _q("Rasmda aralashmani ajratish usuli ko'rsatilgan. Bu usul qanday ataladi?"+h,SEP_ALL[3],[SEP_ALL[0],SEP_ALL[1],SEP_ALL[2]],"Tindirib, tiniq suyuqlikni sirtidan quyib olish – dekantatsiya","7-sinf (aralashmalarni ajratish, 9-rasm)",r)
    return _q("Rasmda tasvirlangan usul bilan qaysi aralashmani ajratish mumkin?"+h,"loyqa suv (suv va qum zarrachalari)",["osh tuzi eritmasi","suv va etanol","suv va kerosin"],"Zichligi katta zarrachalar cho'kadi, suv sirtidan quyib olinadi","7-sinf (9-rasm)",r)
def f_ajr(r):
    h="\n\n%s"%_im('d_ajratgich','Ajratish voronkasi')
    if r.random()<.5: return _q("Rasmdagi asbob bilan qaysi aralashmani ajratish mumkin?"+h,"suv va kerosin",["suv va qum","osh tuzi eritmasi","suv va etanol"],"Bir-birida erimaydigan suyuqliklar ajratgich voronka yordamida ajratiladi","7-sinf (10-rasm)",r)
    return _q("Rasmda keltirilgan laboratoriya asbobi qanday ataladi?"+h,"ajratgich voronka",["Kipp apparati","tigel","byuretka"],"Bir-birida erimaydigan suyuqliklarni ajratish voronkasi","7-sinf (10-rasm)",r)
def f_filtr(r):
    h="\n\n%s"%_im('d_filtr','Filtrlash')
    k=r.choice(['mix','name','left'])
    if k=='mix': return _q("Rasmdagi usul bilan qaysi aralashmani ajratish mumkin?"+h,"suv va qum",["suv va etanol","osh tuzi eritmasi","suv va kerosin"],"Erimaydigan qattiq modda filtrda qoladi","7-sinf (11-rasm)",r)
    if k=='name': return _q("Rasmda aralashmani ajratish usuli ko'rsatilgan. Bu usulni toping."+h,SEP_ALL[0],[SEP_ALL[1],SEP_ALL[2],SEP_ALL[5]],"Voronka va filtr qog'ozi – filtrlash","7-sinf (11-rasm)",r)
    return _q("Rasmdagi tajribada loyqa suv filtrdan o'tkazilganda qaysi modda filtr qog'ozida qoladi?"+h,"suvda erimaydigan qattiq zarrachalar",["suvda erigan osh tuzi","suv molekulalari","etanol"],"Filtr erimaydigan zarrachalarni ushlab qoladi","7-sinf (11-rasm)",r)
def f_bugla(r):
    h="\n\n%s"%_im('d_bugla','Bug\'latish')
    if r.random()<.5: return _q("Rasmda aralashmani ajratish usuli ko'rsatilgan. Bu usul nima deb ataladi?"+h,"bug'latish",["filtrlash","distillash","dekantatsiya"],"Chinni kosachada eritma bug'latiladi","7-sinf (12-rasm)",r)
    return _q("Rasmdagi usul bilan qaysi moddani eritmadan ajratib olish mumkin?"+h,"osh tuzini tuz eritmasidan",["suvni osh tuzi eritmasidan (toza holda)","qumni suvdan","kerosinni suvdan"],"Suv bug'lanib ketadi, tuz chinni kosachada qoladi","7-sinf (12-rasm)",r)
def f_dist(r):
    h="\n\n%s"%_im('d_distill','Distillash')
    if r.random()<.5: return _q("Rasmda aralashmani ajratish usuli ko'rsatilgan. Bu usul nima deb ataladi?"+h,"distillash",["filtrlash","bug'latish","dekantatsiya"],"Qaynash haroratlari farqiga asoslangan","7-sinf (13-rasm)",r)
    return _q("Rasmdagi usul bilan qaysi aralashmani ajratish mumkin?"+h,"suv va etanol",["suv va qum","osh tuzi va qum","suv va kerosin"],"Qaynash harorati farqi: etanol avval haydaladi","7-sinf (13-rasm)",r)
def f_vod(r):
    h="\n\n%s"%_im('d_vodorod','Vodorod olish')
    k=r.choice(['coll','num'])
    if k=='coll': return _q("Rasmdagi tajribada Zn ga HCl ta'sir ettirib olingan vodorod qanday usulda yig'iladi?"+h,"suvni siqib chiqarish usulida",["havoni siqib chiqarish (idish og'zi pastga)","havoni siqib chiqarish (idish og'zi yuqoriga)","gazni yig'ib bo'lmaydi"],"Vodorod suvda erimaydi, shuning uchun suv ustida yig'iladi","7-sinf (28-rasm)",r)
    m=r.choice([3.25,6.5,13,1.3]); V=m/65*22.4
    return _n("Rasmdagi asbobda %s g rux mo'l xlorid kislota bilan reaksiyaga kirishdi (Zn + 2HCl → ZnCl2 + H2). Ajralgan vodorodning hajmini (l, n.sh.) aniqlang.%s"%(fmt(m,2),h),V,[V*2,V/2,m/65,m/65*44.8],"n(Zn) = %s/65 = %s mol; V(H2) = %s l"%(fmt(m,2),fmt(m/65,3),fmt(V,2)),"7-sinf (28-rasm); 8-sinf (stexiometriya)")
def f_xlor(r):
    h="\n\n%s"%_im('d_xlor','Xlor olish')
    k=r.choice(['reag','num','naoh'])
    if k=='reag': return _q("Rasmda laboratoriyada gaz olish asbobi ko'rsatilgan. Qaysi moddalar o'zaro ta'sirlashadi?"+h,"MnO2 va konsentrlangan HCl",["Zn va HCl","CaCO3 va HCl","NH4Cl va Ca(OH)2"],"MnO2 + 4HCl → MnCl2 + Cl2↑ + 2H2O","8-sinf (xlor olinishi, 15-rasm)",r)
    if k=='naoh': return _q("Rasmdagi asbobda oxirgi idishga NaOH eritmasi solingan. Uning vazifasi nima?"+h,"ortiqcha xlorni yutib, atrof-muhitni zaharlanishdan saqlash",["xlorni quritish","xlorni suvda eritish","reaksiyani tezlashtirish"],"Cl2 + 2NaOH → NaCl + NaClO + H2O","8-sinf (xlor olinishi, 15-rasm)",r)
    m=r.choice([8.7,17.4,4.35,26.1]); V=m/87*22.4
    return _n("Rasmdagi asbobda %s g MnO2 ga mo'l konsentrlangan HCl ta'sir ettirildi (MnO2 + 4HCl → MnCl2 + Cl2 + 2H2O). Ajralgan xlor hajmini (l, n.sh.) aniqlang.%s"%(fmt(m,2),h),V,[V*2,V/2,m/87*71,m/87],"n(MnO2) = %s/87 = %s mol; V(Cl2) = %s l"%(fmt(m,2),fmt(m/87,3),fmt(V,2)),"8-sinf (xlor olinishi, 15-rasm)")
def f_hcl(r):
    h="\n\n%s"%_im('d_hcl_lab','HCl olish')
    if r.random()<.5:
        m=r.choice([5.85,11.7,23.4,58.5]); V=m/58.5*22.4
        return _n("Rasmdagi asbobda %s g NaCl ga konsentrlangan H2SO4 ta'sir ettirib qizdirildi (NaCl + H2SO4 → NaHSO4 + HCl). Ajralgan HCl hajmini (l, n.sh.) aniqlang.%s"%(fmt(m,2),h),V,[V*2,V/2,m/36.5,m/58.5],"n(NaCl) = %s mol; V(HCl) = %s l"%(fmt(m/58.5,3),fmt(V,2)),"8-sinf (vodorod xlorid olinishi, 17-rasm)")
    return _q("Rasmdagi asbobda NaCl ga konsentrlangan H2SO4 ta'sir ettirilmoqda. Sulfat kislota bu yerda qanday vazifani bajaradi?"+h,"uchuvchan bo'lmagan kuchli kislota sifatida HCl ni siqib chiqaradi",["tuzni oksidlaydi","faqat erituvchi vazifasini bajaradi","reaksiyada ishtirok etmaydi"],"NaCl + H2SO4 → NaHSO4 + HCl↑","8-sinf (17-rasm)",r)
def f_hclerish(r):
    h="\n\n%s"%_im('d_hcl_erish','HCl ning suvda erishi')
    if r.random()<.5: return _q("Rasmda to'ntarilgan silindrdagi vodorod xlorid gazi suvga tushirilganda suv silindrni to'ldirmoqda. Bu nimani ko'rsatadi?"+h,"HCl gazi suvda juda yaxshi eriydi",["HCl suvda erimaydi","HCl havodan yengil","HCl suv bilan reaksiyaga kirishmaydi"],"1 hajm suvda ~500 hajm HCl eriydi","8-sinf (19-rasm)",r)
    k=r.choice([1,2,5]); V=22.4*k; w=36.5*k/(36.5*k+1000)*100
    return _n("Rasmda HCl ning suvda erishi ko'rsatilgan. %s l (n.sh.) HCl 1000 g suvda eritilsa, hosil bo'lgan eritmadagi HCl ning massa ulushi necha foiz?%s"%(fmt(V,1),h),w,[36.5*k/1000*100,w/2,w*2,36.5*k],"m(HCl) = %s g; ω = %s/(%s + 1000) = %s %%"%(fmt(36.5*k,1),fmt(36.5*k,1),fmt(36.5*k,1),fmt(w,2)),"8-sinf (19-rasm; eritmalar)",2)
def f_nh3(r):
    h="\n\n%s"%_im('d_nh3_lab','Ammiak olish')
    k=r.choice(['num','coll','reag'])
    if k=='num':
        m=r.choice([5.35,10.7,21.4,26.75]); V=m/53.5*22.4
        return _n("Rasmdagi asbobda %s g NH4Cl ga Ca(OH)2 ta'sir ettirib qizdirildi (2NH4Cl + Ca(OH)2 → CaCl2 + 2NH3 + 2H2O). Ajralgan ammiak hajmini (l, n.sh.) aniqlang.%s"%(fmt(m,2),h),V,[V*2,V/2,m/17,m/53.5],"n(NH4Cl) = %s mol; V(NH3) = %s l"%(fmt(m/53.5,3),fmt(V,2)),"8-sinf (ammiak olinishi, 23-rasm)")
    if k=='coll': return _q("Rasmdagi asbobda olingan ammiak qanday yig'iladi?"+h,"og'zi pastga qaratilgan probirkada, havoni siqib chiqarish usulida",["suvni siqib chiqarish usulida","og'zi yuqoriga qaratilgan idishda","yig'ib bo'lmaydi"],"NH3 havodan yengil (M = 17 < 29) va suvda yaxshi eriydi","8-sinf (23-rasm)",r)
    return _q("Rasmda ammiak olish tajribasi ko'rsatilgan. Qaysi moddalar aralashmasi qizdirilmoqda?"+h,"NH4Cl va Ca(OH)2",["NaCl va H2SO4","Zn va HCl","CaCO3 va HCl"],"2NH4Cl + Ca(OH)2 → CaCl2 + 2NH3↑ + 2H2O","8-sinf (23-rasm)",r)
def f_fontan(r):
    h="\n\n%s"%_im('d_nh3_fontan','Ammiak fontani')
    if r.random()<.5: return _q("Rasmdagi tajribada fenolftalein qo'shilgan suvga ammiak yuttirildi, eritma pushti rangga kirdi. Bu nimani ko'rsatadi?"+h,"NH3 suvda yaxshi eriydi va eritma ishqoriy xossaga ega",["NH3 suvda erimaydi, eritma kislotali","NH3 suvda erimaydi, eritma neytral","NH3 havodan og'ir"],"NH3 + H2O ⇄ NH4⁺ + OH⁻","8-sinf (24-rasm)",r)
    k=r.choice([1,2,4]); V=22.4*k; w=17*k/(17*k+1000)*100
    return _n("Rasmda ammiakning suvda erishi ko'rsatilgan. %s l (n.sh.) NH3 1000 g suvda eritilsa, eritmadagi ammiakning massa ulushi necha foiz?%s"%(fmt(V,1),h),w,[17*k/1000*100,w*2,w/2,17*k],"m(NH3) = %s g; ω = %s %%"%(fmt(17*k,1),fmt(w,2)),"8-sinf (24-rasm; eritmalar)",2)
def f_hno3(r):
    h="\n\n%s"%_im('d_hno3_yogoch','HNO3 va cho\'g\'langan yog\'och')
    if r.random()<.5: return _q("Rasmdagi tajribada qizdirilgan konsentrlangan HNO3 ga tushirilgan cho'g'langan yog'och yonib ketdi. Bu nimani isbotlaydi?"+h,"HNO3 kuchli oksidlovchi",["HNO3 kuchli qaytaruvchi","HNO3 yonuvchi modda","HNO3 inert modda"],"HNO3 → NO2 + O2 ajraladi, oksidlovchilik namoyon bo'ladi","8-sinf (28-rasm)",r)
    return _q("Rasmdagi tajribada cho'g'langan yog'och konsentrlangan HNO3 bug'lari ichida yonmoqda. Bu jarayonda HNO3 qanday vazifani bajaradi?"+h,"oksidlovchi",["qaytaruvchi","katalizator","erituvchi"],"HNO3 yog'ochni (uglerodni) oksidlaydi: C + 4HNO3 → CO2 + 4NO2 + 2H2O","8-sinf (nitrat kislota, 28-rasm)",r)
def f_co2(r):
    h="\n\n%s"%_im('d_co2','CO2 olish')
    k=r.choice(['num','coll','reag'])
    if k=='num':
        m=r.choice([5,10,20,25]); V=m/100*22.4
        return _n("Rasmdagi asbobda %s g CaCO3 ga HCl ta'sir ettirildi (CaCO3 + 2HCl → CaCl2 + CO2 + H2O). Ajralgan CO2 hajmini (l, n.sh.) aniqlang.%s"%(fmt(m,2),h),V,[V*2,V/2,m/44,m/100],"n(CaCO3) = %s mol; V(CO2) = %s l"%(fmt(m/100,3),fmt(V,2)),"9-sinf (CO2 olinishi, 11-rasm)")
    if k=='coll': return _q("Rasmdagi asbobda olingan karbonat angidrid qanday yig'iladi?"+h,"idishning og'zi yuqoriga, havoni siqib chiqarish usulida",["og'zi pastga qaratilgan idishda","suvni siqib chiqarish usulida (CO2 suvda erimaydi)","yig'ib bo'lmaydi"],"CO2 havodan og'ir (M = 44 > 29)","9-sinf (11-rasm)",r)
    return _q("Rasmdagi asbobda CO2 olish uchun qaysi moddalar ishlatilgan?"+h,"CaCO3 va HCl",["Zn va HCl","NaCl va H2SO4","NH4Cl va Ca(OH)2"],"CaCO3 + 2HCl → CaCl2 + CO2↑ + H2O","9-sinf (11-rasm)",r)
def f_elek(r):
    h="\n\n%s"%_im('d_elektr_asbob','Elektr o\'tkazuvchanlik asbobi')
    k=r.choice(['why','which'])
    if k=='why': return _q("Rasmdagi asbobda osh tuzining quruq kristallari lampochkani yondirmaydi, eritmasi esa yondiradi. Sababi nima?"+h,"eritmada erkin harakatlanuvchi ionlar hosil bo'ladi",["eritmada erkin elektronlar bor","tuz suvda molekulalarga parchalanadi","suv metall o'tkazgich"],"NaCl → Na⁺ + Cl⁻ (elektrolitik dissotsilanish)","9-sinf (elektrolitlar, 1-rasm)",r)
    ok=r.choice(['osh tuzi eritmasi','sulfat kislota eritmasi','natriy gidroksid eritmasi','mis sulfat eritmasi'])
    return _q("Rasmdagi asbobning elektrodlari quyidagi eritmalardan qaysi biriga tushirilganda lampochka yonadi?"+h,ok,['shakar eritmasi','etanol','distillangan suv','glyukoza eritmasi'],"Elektrolit eritmalari ionlar hosil qiladi","9-sinf (elektrolitlar, 1-rasm)",r)
def f_etilen(r):
    h="\n\n%s"%_im('d_etilen','Etilen olish')
    k=r.choice(['num','br','role'])
    if k=='num':
        m=r.choice([4.6,9.2,23]); y=r.choice([75,80,90]); V=m/46*22.4*y/100
        return _n("Rasmdagi asbobda %s g etanol konsentrlangan H2SO4 bilan 170 °C da qizdirilib, %d %% unum bilan etilen olindi. Hosil bo'lgan etilen hajmini (l, n.sh.) aniqlang.%s"%(fmt(m,2),y,h),V,[m/46*22.4,V*2,V/2,m/46*y],"n(C2H5OH) = %s mol; V = %s·22,4·%s = %s l"%(fmt(m/46,3),fmt(m/46,3),fmt(y/100,2),fmt(V,2)),"10-sinf (etilen olinishi, 6-rasm)")
    if k=='br': return _q("Rasmdagi tajribada hosil bo'lgan gaz bromli suvdan o'tkazilganda nima kuzatiladi?"+h,"bromli suv rangsizlanadi",["bromli suv ko'k rangga kiradi","cho'kma hosil bo'ladi","o'zgarish bo'lmaydi"],"CH2=CH2 + Br2 → CH2Br–CH2Br","10-sinf (etilen olinishi, 6-rasm)",r)
    return _q("Rasmdagi tajribada etanolga konsentrlangan H2SO4 ning vazifasi nima?"+h,"suv tortuvchi va katalizator",["oksidlovchi, etilenni oksidlaydi","faqat erituvchi","reaksiyada ishtirok etmaydi"],"C2H5OH → C2H4 + H2O (H2SO4 suvni tortib oladi)","10-sinf (6-rasm)",r)
def f_efir(r):
    h="\n\n%s"%_im('d_efir','Murakkab efir olish')
    k=r.choice(['what','num','role'])
    if k=='what': return _q("Rasmdagi asbobda sirka kislota va izoamil spirti konsentrlangan H2SO4 ishtirokida qizdirilmoqda. Qanday modda hosil bo'ladi?"+h,"murakkab efir (izoamilasetat)",["oddiy efir","aldegid","uglevod"],"CH3COOH + C5H11OH ⇄ CH3COOC5H11 + H2O","10-sinf (efirlanish, 8-rasm)",r)
    if k=='role': return _q("Rasmdagi tajribada efirlanish reaksiyasida konsentrlangan H2SO4 qanday vazifani bajaradi?"+h,"katalizator va suv tortuvchi",["oksidlovchi","faqat erituvchi","reaksiya mahsuloti"],"H2SO4 muvozanatni efir hosil bo'lish tomoniga siljitadi","10-sinf (efirlanish, 8-rasm)",r)
    m=r.choice([6,12,3]); y=r.choice([80,75,90]); a=m/60*130*y/100
    return _n("Rasmdagi asbobda %s g sirka kislota mo'l izoamil spirti bilan reaksiyaga kirishdi va %d %% unum bilan izoamilasetat (M = 130 g/mol) olindi. Efir massasini (g) aniqlang.%s"%(fmt(m,2),y,h),a,[m/60*130,a*2,a/2,m/130*60],"n(CH3COOH) = %s mol; m = %s·130·%s = %s g"%(fmt(m/60,3),fmt(m/60,3),fmt(y/100,2),fmt(a,2)),"10-sinf (murakkab efirlar, 8-rasm)")
PICT=[f_spirt,f_alanga,f_tind,f_ajr,f_filtr,f_bugla,f_dist,f_vod,f_xlor,f_hcl,f_hclerish,f_nh3,f_fontan,f_hno3,f_co2,f_elek,f_etilen,f_efir]
