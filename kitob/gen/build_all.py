import sys, random, re, json, os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from core import *
import more7, more8, more9, more10, more11, more12, more13, more14, more15, more16, more17, more18, short2, harder, hardness, um, um2, an, org, pic, pic2, pic3, pic4, pic5, pic6, tail, more, more2, more3, more4, more5, more6, tah
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
UMG['dissotsilanish/pH/gidroliz']+=[more7.t_hydr2]
ANG['oksid/asos/kislota/tuz']+=[more7.t_seq,more7.t_sep_in]
ANG['d-metallar (Fe,Cu,Zn,Cr)']+=[more7.t_seq]
ANG['IIA/IIIA metallar (Ca,Mg,Al)']+=[more7.t_seq]
ANG['galogenlar']+=[more7.t_sep_in]
for _i,_fs in more8.HARD_ORG.items(): ORG[_i]=ORG[_i]+_fs
for _t,_fs in more9.HARD_INORG.items(): ANG[_t]=ANG[_t]+_fs
for _t,_fs in more12.HARD_INORG3.items(): ANG[_t]=ANG[_t]+_fs; more9.HARD_INORG.setdefault(_t,[]).extend(_fs)
for _t,_fs in more12.HARD_UM.items(): UMG[_t]=UMG[_t]+_fs
for _t,_fs in more14.HARD_UM14.items():
    UMG[_t]=UMG[_t]+_fs; more12.HARD_UM.setdefault(_t,[]).extend(_fs)
for _t,_fs in more14.HARD_AN14.items():
    if _fs: ANG[_t]=ANG[_t]+_fs; more9.HARD_INORG.setdefault(_t,[]).extend(_fs)
for _fs_ in (more9.c_metal_mix,more9.c_carbonates): UMG['mol/stexiometriya']=UMG['mol/stexiometriya']+[_fs_]
more12.HARD_UM.setdefault('mol/stexiometriya',[]).extend([more9.c_metal_mix,more9.c_carbonates])
UMG['kuchlanish qatori']=UMG['kuchlanish qatori']+[more9.c_plate]; more12.HARD_UM.setdefault('kuchlanish qatori',[]).append(more9.c_plate)
UMG['mol/stexiometriya']=UMG['mol/stexiometriya']+[more15.rel_carb,more15.rel_met]; more12.HARD_UM.setdefault('mol/stexiometriya',[]).extend([more15.rel_carb,more15.rel_met])
ANG['IIA/IIIA metallar (Ca,Mg,Al)']=ANG['IIA/IIIA metallar (Ca,Mg,Al)']+[more15.rel_carb,more15.rel_met]; more9.HARD_INORG.setdefault('IIA/IIIA metallar (Ca,Mg,Al)',[]).extend([more15.rel_carb,more15.rel_met])
more8.HARD_ORG[1].append(more15.rel_alk); more8.HARD_ORG[3].append(more15.rel_alc); ORG[1]=ORG[1]+[more15.rel_alk]; ORG[3]=ORG[3]+[more15.rel_alc]
def _addpool(d_um=None,d_an=None):
    for t_,fs_ in (d_um or {}).items():
        UMG[t_]=UMG[t_]+fs_; more12.HARD_UM.setdefault(t_,[]).extend(fs_)
    for t_,fs_ in (d_an or {}).items():
        ANG[t_]=ANG[t_]+fs_; more9.HARD_INORG.setdefault(t_,[]).extend(fs_)
_addpool({'qonunlar/gaz/ekvivalent':[more15.rel_gas],'atom/davriy/izoelektron':[more15.rel_gas]},
         {'d-metallar (Fe,Cu,Zn,Cr)':[more15.rel_oxr],'S/SO2/H2SO4':[more15.rel_sulf],'galogenlar':[more15.rel_chlo],'oksid/asos/kislota/tuz':[more15.rel_sulf,more15.rel_chlo,more15.rel_oxr]})
more8.HARD_ORG[0].append(more15.rel_hc); more8.HARD_ORG[1].append(more15.rel_hc); ORG[0]=ORG[0]+[more15.rel_hc]
REL_SH={37:[more15.s_hydrate_conc,more17.g_evap,more17.g_equil_frac],38:[more15.s_unknown_chloride,more17.g_gas_expansion],36:[more17.g_mix_solutions],39:list(more18.SH_ORG),40:list(more18.SH_ORG)}
ORG[3]+=[more7.t_sep_org]; ORG[4]+=[more7.t_sep_org]; ORG[5]+=[more7.t_sep_org]
THEORY={more14.t_hydr_shift,more7.t_seq,more7.t_sep_in,more7.t_sep_org,more7.t_hydr2,more2.t_qnum2,um.t_jism,um.t_valent,um.t_config,um.t_qnum,um.t_decay,um.t_isoel,um2.t_sigpi,um2.t_hyb,um2.t_bondtype,um2.t_lech,um2.t_hydr,um2.t_os,um2.t_onlyox,um2.t_elec,um2.t_act,an.t_iaf,an.t_df,an.t_oxcls,an.t_salt,an.t_react,an.t_fert,an.t_nob,an.t_nitrate_prod,an.t_genetic,org.t_nom,org.t_isom,org.t_class,org.t_oprod}
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
GFP=set(); DUPS=[]; GFPC={}
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
    for _i in range(40 if not force else 400):
        q=f(r)
        if getattr(q,'exact',True) is False and _i<25: continue   # javob tekis bo'linadigan son bo'lsin (cheksiz kasr emas)
        key=q.text[-90:]+'|'+str(q.ans)
        if key in used: continue
        if q.ans in q.dis or len(set(q.dis))!=3 or len(q.dis)!=3: continue
        if q.ans in ('',None): continue
        if q.text and q.text[0].islower() and not q.text.startswith('pH'): q.text=q.text[0].upper()+q.text[1:]
        q.gen=getattr(f,'__name__','?')
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
    # organik 20-29: hisob masalalari kamida 2 bosqichli (4 tasi 2 bosqichli, 3 tasi 3-5 bosqichli), 3 tasi nazariy
    pat3=[True]*3+[False]*7; ro.shuffle(pat3)
    calc_idx=[i for i in range(10) if not pat3[i]]
    chain_slots=set(ro.sample(calc_idx,3))
    for i in range(10):
        if pat3[i]:
            th=[g for g in ORG[i] if is_theory(g)]; thf=[g for g in th if g not in USEDF] or th
            f=ro.choice(thf); USEDF.add(f); qs[20+i]=gen_valid(ro,f,used,[g for g in th if g is not f])
        else:
            pool=more12.ORG34 if (i in chain_slots or i not in more8.HARD_ORG) else more8.HARD_ORG[i]
            f=ro.choice(pool); qs[20+i]=gen_valid(ro,f,used,[g for g in pool if g is not f])
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
    NEWQ=list(more13.NEWQ)+[more7.t_sep_in,more7.t_sep_org,more7.t_seq]
    _q1=rt.choice(NEWQ); _rest=[g for g in NEWQ+tpool if g is not _q1]; _q2=rt.choice(_rest)
    items=[tfig,_q1,_q2]
    rng={'U':[i for i in range(1,14) if i!=gslot+1 and qs[i].kind not in ('graph','table')],'A':list(range(14,20)),'O':list(range(20,30))}[psec]
    sl=rt.choice(rng); qs[sl]=gen_valid(rt,picf,used)
    rt.shuffle(items)
    for i,f in enumerate(items): qs[30+i]=gen_valid(rt,f,used,[g for g in tpool if g not in items])
    # Samarqand darajasiga yaqinlashtirish: "oson" savollar ulushini cheklash (rasm/grafik/jadval o'zgarmaydi)
    r2=random.Random(6000+v)
    def _pool(i):
        if i<=13: return UMG[topics[i-1]]
        if i<=19: return ANG[base[i-14]]
        return ORG[i-20]
    HDQ=set()
    NEWSET={n_ for m_ in (more7,more8,more9,more10,more11,more12,more13,more14) for n_,v_ in vars(m_).items() if callable(v_)}
    def _single(q):
        g=getattr(q,'gen','') or ''
        return (g.startswith('rx_') or g.startswith('c_')) and g not in NEWSET
    for a_,b_,cap in ((1,13,2),(14,19,1)):
        fails=0
        for _g in range(40):
            easy=[i for i in range(a_,b_+1) if _single(qs[i]) and id(qs[i]) not in HDQ]
            cand=[i for i in easy if qs[i].kind not in ('graph','table','picture') and not getattr(qs[i],'tag','')=='pic']
            if len(easy)<=cap or not cand: break
            i=r2.choice(cand); pl=_pool(i); hp=None
            if i>=20: hp=more8.HARD_ORG.get(i-20)
            elif i>=14: hp=more9.HARD_INORG.get(base[i-14])
            else: hp=more12.HARD_UM.get(topics[i-1])
            useH=bool(hp) and r2.random()<0.9
            if useH: pl=hp
            ok=False
            for _t in range(80):
                q=_try(r2,r2.choice(pl),used)
                if q is None: continue
                _k=fp(q.text)
                if _k in GFP and not (useH and GFPC.get(_k,0)<2): continue
                _lv=hardness.level(q.text)
                _g=getattr(q,'gen','') or ''
                acc=(_lv!='qiyin') if useH else (not (_g.startswith('rx_') or _g.startswith('c_')) or _g in NEWSET)
                if acc:
                    GFP.add(_k); used.add(q.text[-90:]+'|'+str(q.ans)); qs[i]=q
                    if useH: HDQ.add(id(q)); GFPC[_k]=GFPC.get(_k,0)+1
                    ok=True; break
            if not ok:
                fails+=1
                if fails>14: break
    # Samarqand kabi bilvosita (nisbat/farq/marta/proton/atomlar) shartli masalalar ulushi ~35-40 %
    _RELRX=re.compile(r"marta|nisbat|farq|yig'indi|teng bo'lsa|teng ikki|qismi|ga kam|ga ko'p|ga ortiq|noma'lum|\bx\b|\by\b|ikki baravar|proton|atomlar|[0-9]/[0-9]")
    def _isrel(q): return bool(_RELRX.search(re.sub(r'\s+',' ',q.text.lower().replace('‘',"'").replace('’',"'"))))
    _RP={(1,13):list(more17.IND_UM),(14,19):list(more17.IND_AN)}
    _OKT={'mol/stexiometriya','qonunlar/gaz/ekvivalent','eritma %/M/eruvchanlik','atom/davriy/izoelektron',"bog'lanish/gibridlanish",'tushuncha/valentlik'}
    for (a_,b_),tgt in (((1,13),3),((14,19),2)):
        for _g in range(30):
            if sum(1 for i in range(a_,b_+1) if _isrel(qs[i]))>=tgt: break
            cand=[i for i in range(a_,b_+1) if qs[i].kind=='calc' and not _isrel(qs[i]) and (a_!=1 or topics[i-1] in _OKT)]
            if not cand: break
            i=r2.choice(cand); okk=False
            for _t in range(60):
                q=_try(r2,r2.choice(_RP[(a_,b_)]),used)
                if q is None: continue
                _k=fp(q.text)
                if _k in GFP and GFPC.get(_k,0)>=2: continue
                GFP.add(_k); GFPC[_k]=GFPC.get(_k,0)+1; used.add(q.text[-90:]+'|'+str(q.ans)); qs[i]=q; HDQ.add(id(q)); okk=True; break
            if not okk: break
    # aralashma (x, y) masalalari ko'p bo'lmasin: 1-32 da eng ko'pi bilan 4 ta
    _MIXP=('rel_mix_','c_metal_mix','c_carbonates','c_metal_inert','c_fe_oxides','c_halide_mix','c_ald_ag','c_acid_mix','c_ester_mix','c_amine_mix','c_alcohol_mix','c_arene_mix','c_alkene_alkane','c_organic_ca','c_alkene_hydration','i_nitrate_mix','i_si_sio2','i_na_na2o','i_amph_mix','i_ca_cac2','c_gasmix')
    def _ismix(q): return (getattr(q,'gen','') or '').startswith(_MIXP)
    NONMIX={'U':[more14.u_dilute_chain,more14.u_alpha_particles,more14.u_isotope_mass,more14.u_decay,more14.u_equilibrium,more14.u_rate_comb,more14.u_titration,more14.u_koh_electrolysis,more14.u_equiv_chain,more14.u_ph_mix,more14.u_oxide_formula,more12.q_nitrate_hno3,more12.q_hydrate_heat,more12.q_nacl_hcl]+list(more17.IND_UM),
            'A':[more14.i_mg_air,more14.i_no_o2,more14.i_ammofos,more14.i_so2_equil,more14.i_pyrite_partial,more14.i_h2s_o2,more14.i_cl2_alkali,more12.q_nh3_water,more12.q_kclo3_so2,more12.q_cu_o2_h2so4,more9.c_hno3_chain,more9.c_plate,more9.c_cu_h2so4,more9.c_co2_naoh,more9.c_h3po4,more9.c_joint_hydrolysis,more9.c_hardness,more9.c_nitrate_loss]+list(more17.IND_AN),
            'O':[more12.c_chain,more12.c_chain,more12.c_glu_ester,more8.c_halo_formula,more8.c_decomp,more8.c_hydrogenation,more8.c_nitro_chain,more8.c_ethanol_parallel,more8.c_starch_chain,more8.c_amine_comb,more8.c_glucose_chain,more8.c_chain_alkyne]}
    r3=random.Random(8000+v)
    _mx=[i for i in range(1,33) if _ismix(qs[i]) and qs[i].kind=='calc']
    if len(_mx)>4:
        r3.shuffle(_mx)
        for i in _mx[4:]:
            _pool=NONMIX['U' if i<=13 else 'A' if i<=19 else 'O']
            for _t in range(120):
                q=_try(r3,r3.choice(_pool),used)
                if q is None or _ismix(q): continue
                _k=fp(q.text)
                if _k in GFP and GFPC.get(_k,0)>=2: continue
                GFP.add(_k); GFPC[_k]=GFPC.get(_k,0)+1; used.add(q.text[-90:]+'|'+str(q.ans)); qs[i]=q; break
    # bir variantda bir xil generator (va bir xil zanjir) takrorlanmasin
    _seen=set()
    for i in range(1,33):
        q0=qs[i]; g0=getattr(q0,'gen','') or ''
        if q0.kind!='calc' or not g0: continue
        key0=(g0,getattr(q0,'ck',None))
        if key0 in _seen:
            _pool=NONMIX['U' if i<=13 else 'A' if i<=19 else 'O']
            for _t in range(150):
                q=_try(r3,r3.choice(_pool),used)
                if q is None: continue
                k1=((getattr(q,'gen','') or ''),getattr(q,'ck',None))
                if k1 in _seen or k1[0]==g0 and k1[1]==key0[1]: continue
                _k=fp(q.text)
                if _k in GFP and GFPC.get(_k,0)>=2: continue
                GFP.add(_k); GFPC[_k]=GFPC.get(_k,0)+1; used.add(q.text[-90:]+'|'+str(q.ans)); qs[i]=q; key0=k1; break
        _seen.add(key0)
    # har bo'lim ichida savollar oson -> qiyin tartibida (boshlanishi yengil, motivatsiya uchun)
    _rk={'oson':0,'o‘rta':1,'qiyin':2}
    for a_,b_ in ((1,13),(14,19),(20,29)):
        _seq=sorted(range(a_,b_+1),key=lambda i:(max(_rk[hardness.level(qs[i].text)],1 if id(qs[i]) in HDQ else 0),i))
        _old={i:qs[i] for i in range(a_,b_+1)}
        for i,j in zip(range(a_,b_+1),_seq): qs[i]=_old[j]
    # key letters
    letters=list('ABCD')*8; r.shuffle(letters)
    return qs,letters,r,used,base

def _insert_before_ask(text,sentence):
    # oxirgi gapdan (savol) oldin chalg'ituvchi gapni joylaymiz
    i=text.rfind('. ',0,len(text)-1)
    if i<0 or '\n' in text[i:]: return text.rstrip()+' '+sentence
    return text[:i+2]+sentence+' '+text[i+2:]
def make_decoy(text,r):
    """Haqiqiy, lekin masala javobiga ta'sir qilmaydigan ma'lumot. (matn, tur) yoki None."""
    t=text
    if '![' in t or '|---' in t: return None
    m=re.search(r"mo'l (?:konsentrlangan |suyultirilgan )?(xlorid kislota|sulfat kislota|brom suvi|NaOH|KOH|HCl|H2SO4|AgNO3|BaCl2|ammiakli kumush oksid|ohakli suv)",t)
    kinds=[]
    if m: kinds.append(('reagent',"Reagent (%s) eritmasining massa ulushi %d %% va zichligi %s g/ml; u mo'l miqdorda olingan."%(m.group(1),r.choice([10,20,36,50]),fmt(r.choice([1.05,1.12,1.18,1.3,1.4]),2))))
    if re.search(r"aralashma",t) and re.search(r"(CaCO3|MgCO3|BaCO3|Na2CO3|K2CO3|SrCO3|CuO|Fe2O3|PbO|Fe3O4|MgSO4|K2SO4|Na2SO4|Al2\(SO4\)3|Fe2\(SO4\)3|NaCl|KCl|AlCl3|FeCl3|CaCl2|MgCl2|\bMg |\bAl |\bZn |\bFe |Si va SiO2|Na2O)",t) and not re.search(r"\bC\d*H|OH\b|CH3|n\.sh\.\) (gaz|H2)",t.split('aralashma')[0]):
        kinds.append(('zichlik',"Aralashmaning zichligi %s g/sm³ ga teng."%fmt(r.choice([2.3,2.8,3.1,3.9,4.6,5.2]),1)))
    if 'qizdir' in t: kinds.append(('vaqt',"Qizdirish %d daqiqa davom etdi."%r.choice([15,20,30,45,60])))
    if 'elektroliz' in t and 'konsentratsiya' not in t: kinds.append(('hajm',"Elektrolizyorning hajmi %d l."%r.choice([2,3,5])))
    if 'unum' in t: kinds.append(('bosim',"Barcha reaksiyalar %s atm bosimda olib borildi."%r.choice(['1','1,5','2'])))
    if not kinds: return None
    k,s=r.choice(kinds)
    return _insert_before_ask(t,s),k,s

def strip_hint(t):
    out=[];i=0
    while i<len(t):
        if t[i]=='(' and i>0 and t[i-1]==' ':
            d=0;j=i
            while j<len(t):
                d+= (t[j]=='(')-(t[j]==')')
                if d==0: break
                j+=1
            seg=t[i:j+1]
            if d==0 and ('→' in seg or '⇌' in seg):
                if out and out[-1]==' ': out.pop()
                i=j+1; continue
        out.append(t[i]); i+=1
    return ''.join(out)
def decoy_fallback(text,r):
    opts=["Tajriba %d daqiqa davom etdi."%r.choice([10,20,40]),"Tajriba laboratoriyada, %s idishda o'tkazildi."%r.choice(['shisha','chinni','kvars'])]
    if not re.search(r"n\.sh\.|hajm",text): opts+=["Tajriba hajmi %d ml bo'lgan kolbada o'tkazildi."%r.choice([250,500,1000])]
    s=r.choice(opts)
    return _insert_before_ask(text,s),'idish/vaqt',s
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
        kind,f=(('n',r.choice(more18.NEWST2)) if r.random()<0.9 else ('n',r.choice(more17.NEWST))); x=f(r)
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
    rd=random.Random(7000+v); DEC={}
    for n_ in range(1,33):
        q_=qs[n_]
        if q_.kind!='calc' or rd.random()>0.45: continue
        res=make_decoy(q_.text,rd)
        if res:
            q_.text,k_,s_=res; q_.sol=q_.sol+" Eslatma: «%s» – chalg'ituvchi ma'lumot, hisobga olinmaydi."%s_.rstrip('.'); DEC[n_]=k_
    for n_ in range(1,33): qs[n_].text=strip_hint(qs[n_].text)
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
    pools={n:(REL_SH[n] if (n in REL_SH and rs.random()<(0.9 if n in (39,40) else 0.5)) else (new[n] if rs.random()<SHP else old[n])) for n in range(36,41)}
    for n in range(36,41):
        av=[g for g in pools[n] if g not in USEDS] or pools[n]
        f=r.choice(av); USEDS.add(f); q=gen_valid(r,f,used,[g for g in pools[n] if g is not f]); sh.append((n,q))
    def pickw(lst):
        av=[f for f in lst if f not in USEDW] or lst
        for i in range(80):
            f=r.choice(av); w=f(r); k=fp(w.text)
            if k not in GFP or i==79: GFP.add(k); USEDW.add(f); w.gen=getattr(f,'__name__','?'); return w
    W41L=list(tail.W41)+[f for f in more3.W41N if f is not more3.w41_alloy]+list(more4.W41M)
    _weak={more3.w41_molar,more3.w41_gasmix,more3.w41_equiv,more3.w41_isotope,more3.w41_vant} if hasattr(more3,'w41_molar') else set()
    _weak|={getattr(m_,n_) for m_ in (tail,more3,more4) for n_ in ('w41_molar','w41_gasmix','w41_equiv','w41_isotope','w41_vant') if hasattr(m_,n_)}
    W41L=[f for f in W41L if f not in _weak]
    W43L=list(tail.W43)+list(more3.W43N)+[more3.w41_alloy]+list(more5.W43M)
    _weak43={getattr(m_,n_) for m_ in (tail,more3,more4,more5) for n_ in ('w43_al','w43_fe','w43_hard','w43_carb','w43_halo','w43_p_chain') if hasattr(m_,n_)}
    W43L=[f for f in W43L if f not in _weak43]
    _N41=[more10.w41_iron,more10.w41_kmno4,more15.w41_hydrate_id]+list(more12.NEW41B)+list(more16.NEW41C); _N43=list(more12.NEW43)+[more16.w43_thermite,more16.w43_no2o2]+list(more16.NEW43C); _T43=[getattr(m_,n_) for m_ in (tail,more3,more4,more5) for n_ in ('w43_metals','w43_anion','w43_tahlil','w43_gasid') if hasattr(m_,n_)]; w41=pickw([_N41[(v-1)%len(_N41)]]); w42=(more6w42(r) if v%5==1 else more11.w42_complete(r)); w43=pickw([_N43[(v-1)%len(_N43)]]) if v%10 else pickw(_T43); w41.title='41'; w43.title='43'
    for n_,q_ in sh:
        if n_==38 or rd.random()<0.75:
            res=make_decoy(q_.text,rd) or decoy_fallback(q_.text,rd)
            if res: q_.text,k_,s_=res; q_.sol=q_.sol+" Eslatma: «%s» – chalg'ituvchi ma'lumot."%s_.rstrip('.'); DEC[n_]=k_
        q_.text=strip_hint(q_.text)
    for n_ in range(1,33): qs[n_].text=strip_hint(qs[n_].text)
    s['text']=strip_hint(s['text'])
    w41.text=strip_hint(w41.text); w43.text=strip_hint(w43.text)
    for w_ in (w41,w43): w_.bands=[strip_hint(x_) for x_ in w_.bands]
    for w_,nm_ in ((w41,41),(w43,43)):
        if rd.random()<0.6:
            res=make_decoy(w_.text,rd)
            if res: w_.text,k_,s_=res; DEC[nm_]=k_
    return dict(v=v,qs=qs,key=key,tests=tests,s=s,sh=sh,w41=w41,w42=w42,w43=w43,base=base,dec=DEC)
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
    AUD=[]
    for v in which:
        V=make_variant(v)
        AUD.append(dict(v=v,dec={str(k):x for k,x in V['dec'].items()},gens={n:getattr(V['qs'][n],'gen','?') for n in V['qs']},sh={n:getattr(q,'gen','?') for n,q in V['sh']},w41=getattr(V['w41'],'gen','?'),w42=getattr(V['w42'],'gen','chain/complete'),w43=getattr(V['w43'],'gen','?'),b41=len(V['w41'].bands),b42=len(V['w42'].bands),b43=len(V['w43'].bands)))
        md=md_variant(V)
        open(K+'MS_variant_%02d.md'%v if False else K+'gen/out_variant_%02d.md'%v,'w',encoding='utf8').write(md)
        print(v,len(md))
    json.dump(AUD,open(K+'gen/audit.json','w'))
    import collections as _c
    M=_c.defaultdict(_c.Counter)
    for v,l in LOG:
        for t,k in l: M[t][k]+=1
    print('TOPIC x FORM'); 
    for t in UMG: print('%-28s'%t,dict(M[t]))
    print('DUPS',len(DUPS)); import collections; print(collections.Counter(n for n,_ in DUPS).most_common(30))
