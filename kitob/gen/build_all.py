import sys, random, re, json, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from core import *
import short2, harder, hardness, um, um2, an, org, pic, pic2, pic3, pic4, pic5, pic6, tail, more, more2, more3, more4, more5, more6, tah
from collections import Counter
K='/Users/macbook/kimyo-sertifikat/kitob/'
exec(open('/tmp/plan.py').read())   # rows (13 umumiy topics per variant), pool
UMG={
'mol/stexiometriya':[um.c_atoms,um.c_Natoms,um.c_gasmix,um.c_gasvol,um.c_excess,um.c_density],
'eritma %/M/eruvchanlik':[um2.c_mix,um2.c_evap,um2.c_molar,um2.c_hyd,um2.c_sol,tail.tbl_mix,um.c_hydrate],
'atom/davriy/izoelektron':[um.t_config,um.t_isoel,um.c_isotope,um.c_ion],
'kvant/yadro':[um.t_qnum,um.t_decay],
'dissotsilanish/pH/gidroliz':[um2.c_alpha,um2.c_ionsum,um2.c_ph,um2.t_hydr],
"bog'lanish/gibridlanish":[um2.t_sigpi,um2.t_hyb,um2.t_bondtype],
'muvozanat':[um2.c_K,um2.c_init,um2.t_lech,um2.c_press,tail.tbl_eq],
'tezlik':[um2.c_vant,um2.c_gamma_table,um2.c_massact,um2.c_rate],
'OQR':[um2.c_oqrsum,um2.c_oqrfrac,um2.t_os,um2.t_onlyox],
'elektroliz':[um2.c_farad,um2.t_elec],
'qonunlar/gaz/ekvivalent':[um.c_pv,um.c_ekv,um.c_vol],
'tushuncha/valentlik':[um.t_jism,um.t_valent,um.c_hydrate],
'oleum/molyal/normal':[um2.c_oleum,um2.c_normal,um2.c_molal],
'kuchlanish qatori':[um2.c_plate,um2.t_act]}
ANOR=['S/SO2/H2SO4','N/NH3/HNO3','P/C/Si','galogenlar','IA metallar','IIA/IIIA metallar (Ca,Mg,Al)','d-metallar (Fe,Cu,Zn,Cr)','suv qattiqligi','oksid/asos/kislota/tuz','genetik zanjir/reaksiya turlari',"mineral o'g'itlar/nodir gazlar",'tuzlarning termik parchalanishi']
ANG={'S/SO2/H2SO4':[an.c_pyrite,an.t_react],'N/NH3/HNO3':[an.c_hno3,an.c_nitr,an.t_nitrate_prod],'P/C/Si':[an.c_p,an.c_co2naoh],'galogenlar':[an.c_halo,an.c_nacl_hcl],'IA metallar':[an.c_iah2,an.c_nahco3,an.t_iaf],'IIA/IIIA metallar (Ca,Mg,Al)':[an.c_almg,an.c_alnaoh,an.c_co2ca],'d-metallar (Fe,Cu,Zn,Cr)':[an.c_cucuo,an.c_feoh,an.c_fecl,an.c_znzno,an.c_dich,an.t_df],'suv qattiqligi':[an.c_boil,an.c_soda],'oksid/asos/kislota/tuz':[an.t_oxcls,an.t_salt,an.t_react],'genetik zanjir/reaksiya turlari':[an.t_genetic,an.t_react],"mineral o'g'itlar/nodir gazlar":[an.t_fert,an.c_fert,an.t_nob],'tuzlarning termik parchalanishi':[an.c_nitr,an.t_nitrate_prod]}
def tf(name,kind): return lambda r:org.t_orgfact(r,kind)
ORG=[[org.c_halogenation,org.c_formula,org.t_isom,org.t_nom,tf('a','alkan')],
[org.c_alkenemix,org.t_nom,tf('a','alken'),org.c_ethanol],
[org.c_benz,tf('a','aren'),org.c_carbide],
[org.c_alcna,tf('a','spirt'),org.t_oprod],
[org.c_ag,org.c_aldid,tf('a','ald')],
[org.c_acid,tf('a','kis'),org.t_isom],
[org.c_ester,org.c_ester_hyd,org.c_fat,tf('a','efir')],
[org.c_carb,tf('a','ugl'),org.t_class],
[org.c_amine,tf('a','amin'),org.t_class],
[org.c_poly,tf('a','pol'),org.t_oprod]]
for _t in ANG: ANG[_t]=ANG[_t]+[more.build_inorg(_t)]
for _t in ANG: ANG[_t]=ANG[_t]+[more.build_inorg(_t)] if False else ANG[_t]
for _i,_k in enumerate(['alkan','alken','aren','spirt','ald','kis','efir','ugl','amin','pol']): ORG[_i]=ORG[_i]+[more.build_org(_k)]
UMG['eritma %/M/eruvchanlik']+= [more2.tbl_mix2,more2.tbl_solub,more2.c_prep2]
UMG['muvozanat']+=[more2.tbl_eq2,more2.tbl_eq2]
UMG['tezlik']+=[more2.tbl_rate]
UMG['atom/davriy/izoelektron']+=[more2.tbl_atoms]
UMG['kvant/yadro']+=[more2.t_qnum2]
RX2={}
for _i,_k in enumerate(['alkan','alken','aren','spirt','ald','kis','efir','ugl','amin','pol']):
    _f=more.rx2_engine(_k,'10-sinf (ikki bosqichli hisob)')
    if _f:
        RX2[_i]=_f
        if _i%2==0: ORG[_i]=ORG[_i]+[_f]
UMG['mol/stexiometriya']+=[more2.tbl_gas,more2.c_vol2]
UMG['OQR']+=[more2.tbl_oqr]; UMG['kuchlanish qatori']+=[more2.tbl_series]; UMG["bog'lanish/gibridlanish"]+=[more2.tbl_bond]; UMG['kvant/yadro']+=[more2.tbl_nuclide]
UMG['qonunlar/gaz/ekvivalent']+=[more2.c_ekv2,more2.c_pv2]
THEORY={more2.t_qnum2,um.t_jism,um.t_valent,um.t_config,um.t_qnum,um.t_decay,um.t_isoel,um2.t_sigpi,um2.t_hyb,um2.t_bondtype,um2.t_lech,um2.t_hydr,um2.t_os,um2.t_onlyox,um2.t_elec,um2.t_act,an.t_iaf,an.t_df,an.t_oxcls,an.t_salt,an.t_react,an.t_fert,an.t_nob,an.t_nitrate_prod,an.t_genetic,org.t_nom,org.t_isom,org.t_class,org.t_oprod}
def is_theory(f):
    if f in THEORY: return True
    return getattr(f,'__name__','').startswith('<lambda>')
USEDF=set()
GALL=[pic.g_solub,pic.g_conc,pic.g_rate,pic3.g_solub2]+list(pic2.GRAPHS2)+list(pic3.GRAPHS3)
PALL=[pic.p_ester,pic2.p_struct,pic2.p_atom,pic4.p_iso]+list(pic4.PICS4)+list(pic6.PICS6)
TALL=list(pic5.PICT); USEDT=set()
USEDG=set(); USEDP=set(); USEDW=set(); LOG=[]; USEDS=set(); SHP=0.55
E_='eritma %/M/eruvchanlik'; T_='tezlik'; P_='dissotsilanish/pH/gidroliz'; A_='atom/davriy/izoelektron'; M_='mol/stexiometriya'
GTOPIC={pic.g_solub:E_,pic2.g_gasv:T_,pic2.g_titr:P_,pic2.g_ppt:P_,pic2.g_hyd:E_,pic2.g_vant:T_,pic2.g_far:'elektroliz',pic2.g_ie:A_,pic3.g_decay:'kvant/yadro',pic3.g_line:M_,pic3.g_energy:'muvozanat',pic3.g_pie:M_,pic3.g_hydr:"bog'lanish/gibridlanish",pic3.g_radii:A_,pic3.g_phbar:P_,pic3.g_air:'qonunlar/gaz/ekvivalent',pic3.g_massp:A_}
PSEC={**pic6.PS6,pic4.p_iso:'O',pic.p_ester:'O',pic2.p_struct:'O',pic2.p_atom:'U',pic4.p_pt:'U',pic4.p_orb:'U',pic4.p_chain_in:'A',pic4.p_chain_org:'O',pic4.p_benz:'O',pic4.p_model:'U',pic4.p_lattice:'U',pic4.p_ring:'O',pic4.p_fg:'O',pic4.p_series:'A',pic4.p_decay:'U',pic4.p_ind:'U',pic4.p_lewis:'U'}
def choose(r,funcs,want_theory):
    fresh=[f for f in funcs if f not in USEDF] or funcs
    cand=[f for f in fresh if is_theory(f)==want_theory] or fresh
    f=r.choice(cand); USEDF.add(f); return f
GFP=set(); DUPS=[]
def fp(t):
    t=re.sub(r'\d+(?:[.,]\d+)?','#',t.lower()); t=re.sub(r'[^a-z# ]',' ',t); return re.sub(r'\s+',' ',t).strip()
def gen_valid(r,f,used,alts=()):
    for g in (f,)+tuple(alts):
        for _ in range(60):
            q=_try(r,g,used)
            if q is None: continue
            k=fp(q.text)
            if k in GFP: continue
            GFP.add(k); used.add(q.text[-90:]+'|'+str(q.ans)); return q
    q=_try(r,f,used,force=True); DUPS.append((getattr(f,'__name__','?'),q.text[:60])); used.add(q.text[-90:]+'|'+str(q.ans)); return q
def _try(r,f,used,force=False):
    for _ in range(40 if not force else 400):
        q=f(r)
        key=q.text[-90:]+'|'+str(q.ans)
        if key in used: continue
        if q.ans in q.dis or len(set(q.dis))!=3 or len(q.dis)!=3: continue
        if q.ans in ('',None): continue
        if q.text and q.text[0].islower() and not q.text.startswith('pH'): q.text=q.text[0].upper()+q.text[1:]
        return q
    return None
def gen_valid_old(r,f,used):
    for _ in range(40):
        q=f(r)
        key=q.text[-90:]+'|'+str(q.ans)
        if key in used: continue
        if q.ans in q.dis or len(set(q.dis))!=3 or len(q.dis)!=3: continue
        if q.ans in ('',None): continue
        if q.text and q.text[0].islower() and not q.text.startswith('pH'): q.text=q.text[0].upper()+q.text[1:]
        used.add(key); return q
    raise RuntimeError('cannot gen '+getattr(f,'__name__','?'))
def build(v,seed=None):
    r=random.Random(1000+v); used=set(); USEDF.clear()
    qs={}
    row=rows[v-1]
    # umumiy 1-13
    pat=[True]*7+[False]*6; r.shuffle(pat)
    topics=list(row)
    # graph slot
    availg=[g for g in GALL if g not in USEDG] or GALL
    gf0=r.choice(availg); gtype=GTOPIC.get(gf0)
    gslot=None
    for i,tpc in enumerate(topics):
        if tpc==gtype: gslot=i;break
    if gslot is None: gslot=r.randrange(13)
    order=list(range(13))
    for i,tpc in enumerate(topics):
        if i==gslot:
            gf=gf0
            for _t in range(60):
                q=gf(r,'v%02d_%d'%(v,_t)); k=fp(q.text)
                if k not in GFP or _t==59: break
            USEDG.add(gf); GFP.add(k); used.add(q.text[-90:]+'|'+str(q.ans))
        else:
            fs=UMG[tpc]; f=choose(r,fs,pat[i]); q=gen_valid(r,f,used,[g for g in fs if g is not f])
        qs[i+1]=q
    # ensure >=2 table questions among 1-32
    def ntab(): return sum(1 for q in qs.values() if q.kind=='table')
    guard=0
    while ntab()<2 and guard<6:
        guard+=1
        for i in range(13):
            if i!=gslot and qs[i+1].kind=='calc':
                f=r.choice([more2.tbl_eq2,more2.tbl_rate,more2.tbl_atoms,more2.tbl_gas,more2.tbl_mix2,more2.tbl_solub,tail.tbl_eq,tail.tbl_mix])
                qs[i+1]=gen_valid(r,f,used,[more2.tbl_eq2,more2.tbl_rate,more2.tbl_gas,more2.tbl_mix2,more2.tbl_atoms]); break
    LOG.append((v,[(topics[i],qs[i+1].kind) for i in range(13)]))
    ra=random.Random(2000+v)
    # anorganik 14-19
    base=[ANOR[(v*2+i)%12] for i in range(6)]
    pat2=[True]*3+[False]*3; ra.shuffle(pat2)
    for i,tpc in enumerate(base):
        f=choose(ra,ANG[tpc],pat2[i]); qs[14+i]=gen_valid(ra,f,used,[g for g in ANG[tpc] if g is not f])
    ro=random.Random(3000+v)
    # organik 20-29
    pat3=[True]*5+[False]*5; ro.shuffle(pat3)
    for i in range(10):
        f=choose(ro,ORG[i],pat3[i]); qs[20+i]=gen_valid(ro,f,used,[g for g in ORG[i] if g is not f])
    # aniq 3 ta qiyin savol (30 %)
    def hardn(): return [i for i in range(20,30) if hardness.level(qs[i].text)=='qiyin']
    for _g in range(40):
        h=hardn()
        if len(h)==3: break
        if len(h)<3:
            cand=[i for i in range(20,30) if i not in h and (i-20) in RX2]
            if not cand: break
            i=ro.choice(cand)
            for _t in range(15):
                q=gen_valid(ro,RX2[i-20],used)
                if hardness.level(q.text)=='qiyin': qs[i]=q; break
        else:
            i=ro.choice(h)
            alts=[g for g in ORG[i-20] if g is not RX2.get(i-20)]
            for _t in range(15):
                q=gen_valid(ro,ro.choice(alts),used)
                if hardness.level(q.text)!='qiyin': qs[i]=q; break
    rt=random.Random(4000+v)
    # tahlil 30-32
    avail=[p for p in PALL if p not in USEDP] or PALL
    picf=None
    for _t in range(60):
        pf=rt.choice(avail); q_=pf(rt); k=fp(q_.text)
        if k not in GFP: picf=pf; break
    if picf is None: picf=pf
    USEDP.add(picf)
    psec=PSEC[picf]
    availT=[p for p in TALL if p not in USEDT] or TALL
    tfig=rt.choice(availT); USEDT.add(tfig)
    tpool=[pic.t_qualtab,pic.t_safety,pic.c_prep,more2.c_prep2]+list(tah.TAHLIL)
    items=[tfig]+rt.sample(tpool,2)
    rng={'U':[i for i in range(1,14) if i!=gslot+1 and qs[i].kind not in ('graph','table')],'A':list(range(14,20)),'O':list(range(20,30))}[psec]
    sl=rt.choice(rng); qs[sl]=gen_valid(rt,picf,used)
    rt.shuffle(items)
    for i,f in enumerate(items): qs[30+i]=gen_valid(rt,f,used,[g for g in tpool if g not in items])
    # key letters
    letters=list('ABCD')*8; r.shuffle(letters)
    return qs,letters,r,used,base
def render_q(n,q,L):
    d=q.dis[:]; opts=d[:]
    # random distractor placement was random already; place answer at L
    opts.insert('ABCD'.index(L),q.ans)
    lines='  '.join('%s) %s'%(c,o) for c,o in zip('ABCD',opts))
    if max(len(o) for o in opts)>34: lines='\n'.join('%s) %s'%(c,o) for c,o in zip('ABCD',opts))
    return "**%d.** %s\n%s\n"%(n,q.text,lines)
SHORT_CALC=lambda: None
def make3335_new(r,v):
    import tail
    allst=[('o',f) for f in tail.STORIES]+[('n',f) for f in more.STORIES2]
    for _ in range(60):
        kind,f=r.choice(allst); x=f(r)
        if kind=='o': txt,qs,vals,sid,sol,src=x
        else: txt,qs,vals,sol,src=x
        qs,vals,sol=harder.apply(f.__name__,qs,vals,sol); qs,vals,sol=harder.apply1(f.__name__,txt,qs,vals,sol)
        k=fp(txt)
        if k in GFP and _<59: continue
        opts,key=tail._opts(r,vals,None)
        if len(set(opts))!=6 or len(set(key))!=3: continue
        GFP.add(k); return dict(text=txt,qs=qs,opts=opts,key=key,sol=sol,vals=vals,src=src)
    raise RuntimeError('3335')
def more6w42(r):
    for i in range(80):
        w=more6.w42x(r); k=fp(w.text)
        if k not in GFP: GFP.add(k); return w
    return w
def make_variant(v):
    qs,letters,r,used,base=build(v)
    key={}; tests=[]
    for n in range(1,33):
        q=qs[n]; L=letters[n-1]; key[n]=L; tests.append((n,render_q(n,q,L)))
    # 33-35
    s=make3335_new(r,v)
    # 36-40
    sh=[]
    old={36:[um2.c_oqrsum],37:[um2.c_farad,um2.c_sol,um2.c_mix,um.c_gasvol,um2.c_molar,um2.c_oleum,um2.c_K,um2.c_ph],38:[an.c_almg,an.c_alnaoh,an.c_cucuo,an.c_znzno,an.c_pyrite,an.c_nitr,an.c_co2naoh,an.c_halo],39:[org.c_formula,org.c_alkenemix,org.c_alcna,org.c_ag,org.c_acid,org.c_benz],40:[org.c_ester,org.c_fat,org.c_carb,org.c_amine,org.c_poly,org.c_aldid,org.c_ester_hyd,org.c_carbide]}
    new={36:list(short2.H36),37:list(short2.H37),38:list(short2.H38),39:list(short2.H39),40:list(short2.H40)}
    rs=random.Random(5000+v)
    pools={n:(new[n] if rs.random()<SHP else old[n]) for n in range(36,41)}
    for n in range(36,41):
        av=[g for g in pools[n] if g not in USEDS] or pools[n]
        f=r.choice(av); USEDS.add(f); q=gen_valid(r,f,used,[g for g in pools[n] if g is not f]); sh.append((n,q))
    def pickw(lst):
        av=[f for f in lst if f not in USEDW] or lst
        for i in range(80):
            f=r.choice(av); w=f(r); k=fp(w.text)
            if k not in GFP or i==79: GFP.add(k); USEDW.add(f); return w
    W41L=list(tail.W41)+[f for f in more3.W41N if f is not more3.w41_alloy]+list(more4.W41M)
    W43L=list(tail.W43)+list(more3.W43N)+[more3.w41_alloy]+list(more5.W43M)
    w41=pickw(W41L); w42=(tail.w42(r,v) if v%6==0 else more6w42(r)); w43=pickw(W43L); w41.title='41'; w43.title='43'
    return dict(v=v,qs=qs,key=key,tests=tests,s=s,sh=sh,w41=w41,w42=w42,w43=w43,base=base)
def short_text(q):
    t=q.text
    return t
def md_variant(V):
    v=V['v']; qs=V['qs']; key=V['key']; T=dict(V['tests'])
    def sec(a,b): return ''.join(T[i]+'\n' for i in range(a,b+1))
    s=V['s']
    opts_txt='  '.join('%s) %s'%(c,o) for c,o in zip('ABCDEF',s['opts']))
    md=f"""# KIMYO — Milliy sertifikat NAMUNA VARIANT № {v} (1–43)

---

## I QISM. YOPIQ TESTLAR (1–32, har biri bitta to'g'ri javob)

### UMUMIY KIMYO (1–13)

{sec(1,13)}
### ANORGANIK KIMYO (14–19)

{sec(14,19)}
### ORGANIK KIMYO (20–29)

{sec(20,29)}
### KIMYOVIY TAHLIL (30–32)

{sec(30,32)}
---

## II QISM. MOSLASHTIRISH (33–35)

**33–35.** Topshiriqlarga mos javoblarni A–F variantlaridan tanlang.
{s['text']}

**33.** {s['qs'][0]}
**34.** {s['qs'][1]}
**35.** {s['qs'][2]}

{opts_txt}

---

## III QISM. QISQA JAVOBLI (36–40) — javobni son bilan yozing

"""
    for n,q in V['sh']:
        t=q.text
        md+=f"**{n}.** {t}\n\n"
    md+="---\n\n## IV QISM. YOZMA ISH (41–43) — to'liq yechim ko'rsatiladi\n\n"
    def wtext(w,title):
        out=f"### {w.title}-topshiriq ({title})\n"+w.text+"\n"
        for i,b in enumerate(w.bands,1): out+=f"{i}) {b}\n"
        return out+"\n"
    md+=wtext(V['w41'],"umumiy kimyo; 5 band, 25 ball")
    md+="### 42-topshiriq (organik kimyo; %d band, 25 ball; hisob-kitob yo'q)\n"%len(V['w42'].bands)+V['w42'].text+"\n"
    for i,b in enumerate(V['w42'].bands,1): md+=f"{i}) {b}\n"
    md+="\n"
    md+=wtext(V['w43'],"anorganik kimyo yoki kimyoviy tahlil; %d band, 25 ball"%len(V['w43'].bands))
    # answers
    md+="\n---\n---\n\n# JAVOBLAR VA YECHIMLAR\n\n## Javoblar kaliti\n"
    md+="| "+" | ".join(str(i) for i in range(1,17))+" |\n|"+"---|"*16+"\n| "+" | ".join(key[i] for i in range(1,17))+" |\n\n"
    md+="| "+" | ".join(str(i) for i in range(17,33))+" |\n|"+"---|"*16+"\n| "+" | ".join(key[i] for i in range(17,33))+" |\n\n"
    md+="33 → **%s** (%s); 34 → **%s** (%s); 35 → **%s** (%s).\n"%(s['key'][0],fmt(s['vals'][0],2),s['key'][1],fmt(s['vals'][1],2),s['key'][2],fmt(s['vals'][2],2))
    md+="36 → **%s**; 37 → **%s**; 38 → **%s**; 39 → **%s**; 40 → **%s**.\n\n"%tuple(q.ans for _,q in V['sh'])
    md+="## 1–32 qisqa yechimlar\n| № | Tur | Javob | Yechim | Manba |\n|---|---|---|---|---|\n"
    kindmap={'calc':'hisob','theory':'nazariy','graph':'grafik','table':'jadval','picture':'rasm'}
    for n in range(1,33):
        q=qs[n]; md+="| %d | %s | %s | %s | %s |\n"%(n,kindmap.get(q.kind,q.kind),key[n],q.sol.replace('|','/').replace('\n',' '),q.src)
    md+="\n## 33–35\n"
    for i,t in enumerate(s['sol']): md+="**%d.** %s → **%s**\n"%(33+i,t,s['key'][i])
    md+="\n## 36–40\n"
    for n,q in V['sh']: md+="**%d.** %s → **%s**\n"%(n,q.sol,q.ans)
    for w in (V['w41'],V['w42'],V['w43']):
        md+="\n---\n\n## %s-topshiriq — yechim va baholash (M — usul, A — hisob)\n"%w.title
        tm=ta=0
        for i,(sol_,sc) in enumerate(zip(w.sol,w.score),1):
            if w.title=='42': md+="%d) %s\n"%(i,sol_); tm+=sc[0]
            else:
                M_,A_=sc; tm+=M_; ta+=A_
                md+="**%d-band (M %d + A %d = %d ball).** %s\n"%(i,M_,A_,M_+A_,sol_)
        if w.title=='42': md+="Jami %d ball.\n"%tm
        else: md+="Jami: M %d + A %d = %d ball.\n"%(tm,ta,tm+ta)
    return md
if __name__=='__main__':
    which=[int(x) for x in sys.argv[1:]] or list(range(1,21))
    for v in which:
        V=make_variant(v)
        md=md_variant(V)
        open(K+'MS_variant_%02d.md'%v if False else K+'gen/out_variant_%02d.md'%v,'w',encoding='utf8').write(md)
        print(v,len(md))
    import collections as _c
    M=_c.defaultdict(_c.Counter)
    for v,l in LOG:
        for t,k in l: M[t][k]+=1
    print('TOPIC x FORM'); 
    for t in UMG: print('%-28s'%t,dict(M[t]))
    print('DUPS',len(DUPS)); import collections; print(collections.Counter(n for n,_ in DUPS).most_common(30))
