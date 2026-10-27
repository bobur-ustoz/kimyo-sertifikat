# 33–35 masalalarni qiyinlashtirish: Q2 yoki Q3 ga qo'shimcha bosqich (eritma massa ulushi, unum, havo, ortiqcha)
def _rep(q,old,new):
    return q.replace(old,new) if old in q else q.rstrip('.')+new_suffix(new)
def new_suffix(s): return ' '+s
TW={
 'story1':(2,'sirka kislota massasini (g)','20 % li sirka kislota eritmasining massasini (g)',1/0.2,"20 % li eritma: massa = sof modda/0,2"),
 'story2':(1,'zarur kislorod hajmini (l, n.sh.)','zarur havo hajmini (l, n.sh.; havoda 21 % kislorod bor)',1/0.21,"havo hajmi = V(O2)/0,21"),
 'story3':(2,'massasini (g) aniqlang.','massasini (g) aniqlang (reaksiya unumi 80 %).',0.8,"unum 80 %: amaliy massa = nazariy · 0,8"),
 'story4':(2,'massasini (g) aniqlang.','massasini (g) aniqlang (reaksiya unumi 90 %).',0.9,"unum 90 %: amaliy massa = nazariy · 0,9"),
 'st_metals':(1,'sarflangan','sarflangan 20 % li',1/0.2,"20 % li eritma: massa = sof modda/0,2"),
 'st_carb':(1,'sarflangan HCl massasini (g)','sarflangan 10 % li HCl eritmasining massasini (g)',1/0.1,"10 % li eritma: massa = sof modda/0,1"),
 'st_halide':(1,'Sarflangan AgNO3 massasini (g)','Sarflangan 10 % li AgNO3 eritmasining massasini (g)',1/0.1,"10 % li eritma: massa = sof modda/0,1"),
 'st_oxides':(1,'sarflangan','(20 % ortiqcha olingan) sarflangan',1.2,"20 % ortiqcha olingan: hajm · 1,2"),
 'st_alal':(1,'sarflangan HCl massasini (g)','sarflangan 20 % li HCl eritmasining massasini (g)',1/0.2,"20 % li eritma: massa = sof modda/0,2"),
 'st_acidalc':(2,'massasini (g) aniqlang.','massasini (g) aniqlang (reaksiya unumi 80 %).',0.8,"unum 80 %: amaliy massa = nazariy · 0,8"),
 'st_gasbr':(2,'zarur kislorod hajmini (l, n.sh.)','zarur havo hajmini (l, n.sh.; havoda 21 % kislorod bor)',1/0.21,"havo hajmi = V(O2)/0,21"),
}
def apply(fname,qs,vals,sol):
    if fname not in TW: return qs,vals,sol
    i,old,new,fac,note=TW[fname]
    qs=list(qs); vals=list(vals); sol=list(sol)
    q=qs[i]
    if old in q: q=q.replace(old,new)
    else: q=q.rstrip('.')+' ('+note.split(':')[0]+').'
    qs[i]=q; vals[i]=vals[i]*fac; sol[i]=sol[i]+"; "+note+" → "+('%.2f'%vals[i]).replace('.',',')
    return qs,vals,sol
import re
Q1W={'st_metals','story4'}
def apply1(fname,txt,qs,vals,sol):
    if fname not in Q1W: return qs,vals,sol
    m=re.search(r'iborat ([\d]+(?:,\d+)?) g',txt)
    if not m or 'massasini (g)' not in qs[0]: return qs,vals,sol
    mix=float(m.group(1).replace(',','.'))
    qs=list(qs); vals=list(vals); sol=list(sol)
    qs[0]=qs[0].replace('massasini (g)','massa ulushini (%)')
    old=vals[0]; vals[0]=old/mix*100
    sol[0]=sol[0]+"; ω = m(komponent)/m(aralashma)·100 = %s/%s·100 = %s %%"%(('%.2f'%old).replace('.',','),('%g'%mix).replace('.',','),('%.2f'%vals[0]).replace('.',','))
    return qs,vals,sol
