"""
일로온나 (Job-On-Na) - 부울경 청년 맞춤형 직업·기업 추천 플랫폼
"""

import streamlit as st
import pandas as pd
import numpy as np
import re
import plotly.graph_objects as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────────────────────────
# 페이지 기본 설정
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="일로온나 | Job-On-Na",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────────────────────────────────────
# 전역 CSS
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&family=Bebas+Neue&display=swap');

html, body, [class*="css"] { font-family: 'Noto Sans KR', sans-serif !important; }
.main .block-container { padding: 0 2rem 3rem 2rem; max-width: 1200px; margin: 0 auto; }
.stApp { background: #F0F4F8; }

.hero {
    background: linear-gradient(135deg, #0D2137 0%, #1B4F72 55%, #1A8CA3 100%);
    border-radius: 0 0 32px 32px;
    padding: 2.8rem 3rem 3rem;
    margin: -0.5rem -2rem 2.5rem -2rem;
    position: relative; overflow: hidden;
    box-shadow: 0 8px 40px rgba(13,33,55,0.35);
}
.hero::before {
    content:''; position:absolute; top:-80px; right:-60px;
    width:340px; height:340px; border-radius:50%;
    background:rgba(255,255,255,0.04);
}
.hero-badge {
    display:inline-block; background:#F39C12; color:#fff;
    padding:4px 16px; border-radius:20px; font-size:0.72rem;
    font-weight:700; letter-spacing:1.5px; margin-bottom:0.9rem;
}
.hero-title {
    font-family:'Bebas Neue',sans-serif; font-size:3.8rem;
    color:#fff; letter-spacing:5px; margin:0; line-height:1;
    text-shadow:0 2px 12px rgba(0,0,0,0.25);
}
.hero-sub {
    color:rgba(255,255,255,0.75); font-size:0.95rem;
    margin-top:0.6rem; font-weight:300; letter-spacing:0.5px;
}
.hero-stats { display:flex; gap:2.5rem; margin-top:1.8rem; }
.hero-stat-num { font-size:1.6rem; font-weight:900; color:#F39C12; line-height:1; }
.hero-stat-label { font-size:0.7rem; color:rgba(255,255,255,0.6); margin-top:2px; }

.section-head { display:flex; align-items:center; gap:10px; margin:2rem 0 1rem; }
.section-icon {
    width:36px; height:36px; border-radius:10px;
    background:linear-gradient(135deg,#1B4F72,#1A8CA3);
    display:flex; align-items:center; justify-content:center;
    font-size:1rem; flex-shrink:0;
    box-shadow:0 3px 10px rgba(27,79,114,0.3);
}
.section-title { font-size:1.15rem; font-weight:700; color:#0D2137; }
.section-desc { font-size:0.82rem; color:#5D6D7E; margin-top:1px; }

.input-card {
    background:#fff; border-radius:18px; padding:1.5rem 1.8rem;
    border:1px solid #DDE3EA; margin-bottom:1.2rem;
    box-shadow:0 2px 12px rgba(0,0,0,0.05);
}
.input-card-title {
    font-size:0.85rem; font-weight:700; color:#1B4F72;
    text-transform:uppercase; letter-spacing:1px;
    border-bottom:2px solid #EBF5FB; padding-bottom:0.6rem;
    margin-bottom:1rem;
}

.step-wrap {
    background:#fff; border-radius:14px; padding:1rem 1.5rem;
    display:flex; align-items:center; gap:0;
    box-shadow:0 2px 8px rgba(0,0,0,0.05);
    margin-bottom:1.8rem; border:1px solid #DDE3EA; overflow:hidden;
}
.step-item { display:flex; align-items:center; gap:8px; flex:1; padding:0 8px; }
.step-dot {
    width:30px; height:30px; border-radius:50%;
    display:flex; align-items:center; justify-content:center;
    font-size:0.8rem; font-weight:700; flex-shrink:0;
    background:#E8EDF2; color:#8FA0B0;
}
.step-dot.active {
    background:linear-gradient(135deg,#1B4F72,#1A8CA3);
    color:#fff; box-shadow:0 3px 10px rgba(27,79,114,0.35);
}
.step-dot.done { background:#27AE60; color:#fff; }
.step-label { font-size:0.75rem; color:#8FA0B0; font-weight:500; }
.step-label.active { color:#1B4F72; font-weight:700; }
.step-line { width:32px; height:2px; background:#E8EDF2; flex-shrink:0; }
.step-line.done { background:#27AE60; }

.stButton > button {
    background:linear-gradient(135deg,#1B4F72 0%,#1A8CA3 100%) !important;
    color:#fff !important; border:none !important;
    border-radius:14px !important; padding:0.75rem 2rem !important;
    font-size:1rem !important; font-weight:700 !important;
    box-shadow:0 4px 18px rgba(27,79,114,0.35) !important;
    transition:all 0.3s !important; width:100%;
}
.stButton > button:hover {
    transform:translateY(-2px) !important;
    box-shadow:0 8px 24px rgba(27,79,114,0.45) !important;
}

.result-banner {
    background:linear-gradient(135deg,#0D2137 0%,#1B4F72 60%,#1A8CA3 100%);
    border-radius:18px; padding:1.8rem 2rem; margin-bottom:2rem;
    color:#fff; position:relative; overflow:hidden;
    box-shadow:0 8px 32px rgba(13,33,55,0.3);
}
.result-banner-title { font-size:1.4rem; font-weight:900; margin-bottom:0.3rem; }
.result-banner-sub { font-size:0.85rem; opacity:0.75; }
.result-chips { display:flex; flex-wrap:wrap; gap:8px; margin-top:1rem; }
.result-chip {
    background:rgba(255,255,255,0.15); border:1px solid rgba(255,255,255,0.25);
    padding:4px 14px; border-radius:20px; font-size:0.78rem; font-weight:500;
}

.job-card {
    background:#fff; border-radius:20px; padding:1.8rem 2rem;
    border:1.5px solid #DDE3EA; margin-bottom:1.5rem;
    position:relative; overflow:hidden;
    box-shadow:0 4px 20px rgba(0,0,0,0.07); transition:all 0.3s;
}
.job-card:hover {
    box-shadow:0 8px 32px rgba(27,79,114,0.15);
    border-color:#AED6F1; transform:translateY(-2px);
}
.job-card-accent {
    position:absolute; top:0; left:0; width:5px; height:100%;
    background:linear-gradient(180deg,#1B4F72,#1A8CA3);
}
.job-rank-badge {
    position:absolute; top:1.5rem; right:1.5rem;
    background:linear-gradient(135deg,#1B4F72,#1A8CA3);
    color:#fff; border-radius:50%; width:46px; height:46px;
    display:flex; align-items:center; justify-content:center;
    font-size:1.2rem; font-weight:900;
    box-shadow:0 4px 12px rgba(27,79,114,0.35);
}
.job-title { font-size:1.35rem; font-weight:800; color:#0D2137; margin-bottom:3px; }
.job-cat { font-size:0.78rem; color:#8FA0B0; margin-bottom:1rem; }
.score-grid { display:grid; grid-template-columns:1fr 1fr; gap:0.6rem; margin:1rem 0; }
.score-label { font-size:0.72rem; color:#8FA0B0; margin-bottom:3px; font-weight:600; }
.score-bar-bg { background:#EBF5FB; border-radius:8px; height:7px; overflow:hidden; }
.score-bar-fill { height:100%; border-radius:8px; background:linear-gradient(90deg,#1B4F72,#1A8CA3); }
.score-val { font-size:0.75rem; color:#1B4F72; font-weight:700; margin-top:2px; }
.tags-wrap { display:flex; flex-wrap:wrap; gap:6px; margin-top:0.8rem; }
.tag {
    background:#EBF5FB; color:#1B4F72; border:1px solid #AED6F1;
    padding:3px 11px; border-radius:20px; font-size:0.73rem; font-weight:500;
}
.tag-warn { background:#FEF9E7; color:#B7770D; border-color:#F9E79F; }
.job-meta { display:flex; gap:1.5rem; margin-top:1rem; padding-top:1rem; border-top:1px solid #F0F4F8; }
.job-meta-val { font-size:1rem; font-weight:800; color:#1B4F72; }
.job-meta-key { font-size:0.68rem; color:#8FA0B0; }
.total-score-row {
    background:linear-gradient(135deg,#EBF5FB,#E8F8F5);
    border-radius:12px; padding:0.8rem 1rem; margin-top:1rem;
    display:flex; align-items:center; justify-content:space-between;
    border:1px solid #AED6F1;
}
.total-score-label { font-size:0.82rem; color:#1B4F72; font-weight:600; }
.total-score-val { font-size:1.4rem; font-weight:900; color:#1B4F72; }

.company-card {
    background:#fff; border-radius:14px; padding:1.2rem 1.4rem;
    border:1px solid #DDE3EA; margin-bottom:0.8rem;
    transition:all 0.25s; position:relative;
    box-shadow:0 2px 8px rgba(0,0,0,0.04);
}
.company-card:hover { border-color:#AED6F1; box-shadow:0 4px 16px rgba(27,79,114,0.12); }
.company-name { font-size:0.98rem; font-weight:700; color:#0D2137; }
.company-brand {
    display:inline-block;
    background:linear-gradient(135deg,#1B4F72,#1A8CA3);
    color:#fff; padding:2px 10px; border-radius:12px;
    font-size:0.67rem; font-weight:700; margin:4px 3px 4px 0;
}
.company-info { font-size:0.78rem; color:#8FA0B0; margin-top:4px; }
.company-score-badge {
    position:absolute; top:1rem; right:1rem;
    background:#F39C12; color:#fff;
    border-radius:20px; padding:2px 12px;
    font-size:0.72rem; font-weight:700;
}

.alt-card {
    background:#FDFEFE; border-radius:14px; padding:1.2rem 1.5rem;
    border:1px dashed #D5D8DC; margin-bottom:0.7rem; opacity:0.85;
}
.alt-card-title { font-size:0.95rem; font-weight:700; color:#5D6D7E; }
.alt-card-reason { font-size:0.75rem; color:#AEB6BF; margin-top:3px; }

.stSelectbox label, .stRadio label, .stSlider label,
.stNumberInput label { font-weight:600 !important; color:#1B4F72 !important; font-size:0.85rem !important; }
.divider { border:none; border-top:1px solid #DDE3EA; margin:1.5rem 0; }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# 데이터 로드 (캐싱)
# ─────────────────────────────────────────────────────────────────────────────
@st.cache_data(show_spinner=False)
def load_data():
    # ── 직업 데이터 ──────────────────────────────────────────────
    job_df = pd.read_csv(
        "final_merged_updated.csv",
        encoding="utf-8-sig",
        dtype=str
    )

    def parse_wage(s):
        if pd.isna(s):
            return np.nan
        nums = re.findall(r"[\d,]+", str(s))
        return float(nums[0].replace(",", "")) if nums else np.nan

    job_df["임금_만원"] = job_df["평균임금"].apply(parse_wage)

    edu_cols = {
        "중졸이하": "학력분포(%) : 중졸이하",
        "고졸": "학력분포(%) : 고졸",
        "전문대졸": "학력분포(%) : 전문대졸",
        "대졸": "학력분포(%) : 대졸",
        "대학원졸": "학력분포(%) : 대학원졸",
        "박사졸": "학력분포(%) : 박사졸",
    }
    for key, col in edu_cols.items():
        job_df[key + "_pct"] = pd.to_numeric(job_df[col], errors="coerce").fillna(0) if col in job_df.columns else 0.0

    major_cols = {
        "인문": "전공학과분포(%) : 인문계열",
        "사회": "전공학과분포(%) : 사회계열",
        "교육": "전공학과분포(%) : 교육계열",
        "공학": "전공학과분포(%) : 공학계열",
        "자연": "전공학과분포(%) : 자연계열",
        "의학": "전공학과분포(%) : 의학계열",
        "예체능": "전공학과분포(%) : 예체능계열",
    }
    for key, col in major_cols.items():
        job_df[key + "_major_pct"] = pd.to_numeric(job_df[col], errors="coerce").fillna(0) if col in job_df.columns else 0.0

    job_df["만족도_num"] = pd.to_numeric(job_df.get("직업만족도(%)", pd.Series(dtype=float)), errors="coerce").fillna(70)

    prospect_map = {"다소 증가": 2, "유지": 1, "다소 감소": -1, "감소": -2}
    job_df["전망_num"] = job_df.get("일자리전망률", pd.Series(dtype=str)).map(prospect_map).fillna(0)
    job_df["업무환경_텍스트"] = job_df.get("직업 내 비교업무환경 : 업무수행능력", pd.Series(dtype=str)).fillna("")

    # ── 기업 데이터 ──────────────────────────────────────────────
    # busansimple.py 273라인 수정
    comp_df = pd.read_csv(
        "worknet_smlgnt_master.csv",
        encoding="utf-8-sig",
        dtype=str
    )
    # 💥 이 코드를 추가하세요! 모든 컬럼명의 앞뒤 공백을 제거합니다.
    comp_df.columns = comp_df.columns.str.strip() 
    
    comp_df["상시근로자_num"] = pd.to_numeric(comp_df.get("상시근로자 수", pd.Series(dtype=float)), errors="coerce").fillna(0)

    # 이제 '지역명'을 안전하게 찾을 수 있습니다.
    mask_buk = comp_df["지역명"].str.contains("부산|울산|경남", na=False)
    buk_df = comp_df[mask_buk].copy().reset_index(drop=True)
    
    comp_df.columns = comp_df.columns.str.strip()
    comp_df["상시근로자_num"] = pd.to_numeric(comp_df.get("상시근로자 수", pd.Series(dtype=float)), errors="coerce").fillna(0)

    mask_buk = comp_df["지역명"].str.contains("부산|울산|경남", na=False)
    buk_df = comp_df[mask_buk].copy().reset_index(drop=True)

    return job_df, comp_df, buk_df


@st.cache_data(show_spinner=False)
def get_all_departments(job_df):
    dept_set = set()
    col = "관련학과"
    if col not in job_df.columns:
        return []
    for val in job_df[col].dropna():
        for dep in str(val).split(","):
            dep = dep.strip()
            if dep and len(dep) > 1:
                dept_set.add(dep)
    return sorted(dept_set)


# ─────────────────────────────────────────────────────────────────────────────
# 스코어링 엔진
# ─────────────────────────────────────────────────────────────────────────────

def compute_major_score(job_df, user_major, user_dept):
    """전공 매칭 점수 (30점 만점): 학과 직접매칭(20) + 계열비율(10)"""
    scores = pd.Series(0.0, index=job_df.index)

    if user_dept:
        dept_kw = user_dept.replace(" ", "")
        for idx, row in job_df.iterrows():
            related = str(row.get("관련학과", "")).replace(" ", "")
            if dept_kw in related:
                scores[idx] += 20.0
            elif len(dept_kw) >= 2 and dept_kw[:2] in related:
                scores[idx] += 8.0

    major_col_map = {
        "인문계열": "인문_major_pct", "사회계열": "사회_major_pct",
        "교육계열": "교육_major_pct", "공학계열": "공학_major_pct",
        "자연계열": "자연_major_pct", "의학계열": "의학_major_pct",
        "예체능계열": "예체능_major_pct",
    }
    col_key = major_col_map.get(user_major)
    if col_key and col_key in job_df.columns:
        pct = job_df[col_key].astype(float)
        max_p = pct.max()
        if max_p > 0:
            scores += (pct / max_p) * 10.0

    return scores.clip(0, 30)


def compute_burnout_score(job_df, burnout_level):
    """번아웃/스트레스 매칭 점수 (30점 만점)"""
    env_col = "업무환경_텍스트"
    scores = pd.Series(0.0, index=job_df.index)

    stress_kw = ["주말 및 공휴일 출근", "위험한 장비 노출", "신체적 강인성",
                 "오염물질 노출", "매우 춥거나 더운 기온", "고지대 작업", "위험한 상태 노출"]
    low_kw = ["실내 근무", "앉아서 근무", "이메일 이용하기", "재택근무"]

    for idx, row in job_df.iterrows():
        txt = str(row.get(env_col, ""))
        s_cnt = sum(1 for k in stress_kw if k in txt)
        l_cnt = sum(1 for k in low_kw if k in txt)

        if burnout_level == "고위험":
            scores[idx] = (max(0, len(stress_kw) - s_cnt) / len(stress_kw)) * 20 + (l_cnt / len(low_kw)) * 10
        elif burnout_level == "중간":
            balance = (max(0, len(stress_kw) - s_cnt) / len(stress_kw)) * 15
            sat = float(row.get("만족도_num", 70)) / 100 * 15
            scores[idx] = balance + sat
        else:
            sat = float(row.get("만족도_num", 70)) / 100 * 15
            w = row.get("임금_만원", 0)
            try:
                w_score = min(15, float(w) / 1000 * 5) if w and not np.isnan(float(w)) else 0
            except:
                w_score = 0
            scores[idx] = sat + w_score

    return scores.clip(0, 30)


def compute_env_score(job_df, env_pref):
    """근무환경 부합도 (20점 만점)"""
    env_col = "업무환경_텍스트"
    scores = pd.Series(0.0, index=job_df.index)
    indoor_kw = ["실내 근무", "앉아서 근무", "이메일 이용하기"]
    outdoor_kw = ["실외 근무", "걷거나 뛰기", "위험한 장비 노출"]

    for idx, row in job_df.iterrows():
        txt = str(row.get(env_col, ""))
        in_cnt = sum(1 for k in indoor_kw if k in txt)
        out_cnt = sum(1 for k in outdoor_kw if k in txt)
        total = max(1, in_cnt + out_cnt)
        if env_pref == "실내 선호":
            scores[idx] = (in_cnt / total) * 20
        elif env_pref == "실외 선호":
            scores[idx] = (out_cnt / total) * 20
        else:
            scores[idx] = 14.0

    return scores.clip(0, 20)


def compute_value_score(job_df, core_value):
    """가치관 가중치 (20점 만점)"""
    wage_vals = pd.to_numeric(job_df.get("임금_만원", pd.Series(0)), errors="coerce").fillna(0)
    wage_norm = (wage_vals - wage_vals.min()) / (wage_vals.max() - wage_vals.min() + 1e-6)

    prospect = job_df.get("전망_num", pd.Series(0)).astype(float)
    prospect_norm = (prospect + 2) / 4

    sat = job_df.get("만족도_num", pd.Series(70)).astype(float)
    sat_norm = (sat - sat.min()) / (sat.max() - sat.min() + 1e-6)

    env_col = "업무환경_텍스트"
    stress_kw = ["주말 및 공휴일 출근", "위험한 장비 노출", "신체적 강인성", "오염물질 노출"]
    low_kw = ["재택근무", "실내 근무", "앉아서 근무"]
    wlb = pd.Series(0.0, index=job_df.index)
    for idx, row in job_df.iterrows():
        txt = str(row.get(env_col, ""))
        s = sum(1 for k in stress_kw if k in txt)
        l = sum(1 for k in low_kw if k in txt)
        wlb[idx] = (max(0, len(stress_kw) - s) + l) / (len(stress_kw) + len(low_kw))

    val_map = {
        "높은 임금": wage_norm * 20,
        "직업 안정성": prospect_norm * 20,
        "성취·보람": sat_norm * 20,
        "워라밸": wlb * 20,
    }
    return val_map.get(core_value, (wage_norm * 0.3 + prospect_norm * 0.3 + sat_norm * 0.4) * 20).clip(0, 20)


def hard_filter_jobs(job_df, edu_level, min_wage):
    edu_map = {
        "고졸": ["고졸_pct"],
        "전문대졸": ["고졸_pct", "전문대졸_pct"],
        "대졸": ["고졸_pct", "전문대졸_pct", "대졸_pct"],
        "대학원졸": ["고졸_pct", "전문대졸_pct", "대졸_pct", "대학원졸_pct"],
        "박사졸": ["고졸_pct", "전문대졸_pct", "대졸_pct", "대학원졸_pct", "박사졸_pct"],
    }
    relevant = edu_map.get(edu_level, ["대졸_pct"])
    job_df = job_df.copy()
    job_df["사용자학력_누적비율"] = job_df[[c for c in relevant if c in job_df.columns]].astype(float).sum(axis=1)

    edu_mask = job_df["사용자학력_누적비율"] >= 10
    wage_threshold = min_wage * 0.8
    wage_mask = pd.to_numeric(job_df["임금_만원"], errors="coerce").fillna(0) >= wage_threshold

    pass_mask = edu_mask & wage_mask
    filtered_df = job_df[pass_mask].copy().reset_index(drop=True)
    excluded_df = job_df[~edu_mask].copy().reset_index(drop=True)
    return filtered_df, excluded_df


def score_jobs(job_df, user_major, user_dept, burnout_level, env_pref, core_value):
    s_major = compute_major_score(job_df, user_major, user_dept)
    s_burn = compute_burnout_score(job_df, burnout_level)
    s_env = compute_env_score(job_df, env_pref)
    s_val = compute_value_score(job_df, core_value)
    total = s_major + s_burn + s_env + s_val

    job_df = job_df.copy()
    job_df["_s_major"] = s_major.values
    job_df["_s_burn"] = s_burn.values
    job_df["_s_env"] = s_env.values
    job_df["_s_val"] = s_val.values
    job_df["_total"] = total.values
    return job_df.sort_values("_total", ascending=False)


def extract_job_keywords(job_row):
    kws = []
    for col in ["직업 중분류명", "직업소분류명", "직업 대분류명"]:
        val = str(job_row.get(col, ""))
        if val and val != "nan":
            kws += re.split(r"[·/]", val)
            kws.append(val)

    rel = str(job_row.get("관련직업명목록", ""))
    if rel and rel != "nan":
        kws += re.split(r"[,#\s]+", rel)[:5]

    skill_text = str(job_row.get("필수 기술 및 지식", ""))
    kws += re.findall(r"[가-힣]{2,5}", skill_text)[:10]

    kws = [k.strip() for k in kws if k.strip() and len(k.strip()) >= 2]
    return list(dict.fromkeys(kws))[:20]


def score_companies(candidates, burnout_level, culture_pref, size_pref):
    candidates = candidates.copy()
    candidates["_comp_score"] = 0.0

    burnout_culture_kw = {
        "고위험": ["노사문화우수기업", "경남형 청년친화기업", "여가친화기업", "근무혁신 우수기업",
                   "좋은일터조성사업", "남녀고용평등우수기업", "고용친화대표기업"],
        "중간": ["인재육성형중소기업", "대한민국일자리으뜸기업", "근무혁신 우수기업",
                 "노사문화우수기업", "최고일자리 기업"],
        "저위험": ["월드클래스300", "기술혁신형 중소기업(이노비즈)", "세계일류상품생산기업",
                   "글로벌 강소기업", "한국형 히든챔피언 육성프로그램"],
    }
    pref_brands = (culture_pref or []) + burnout_culture_kw.get(burnout_level, [])

    brand_col = "강소기업브랜드명"
    if brand_col in candidates.columns:
        for i, row in candidates.iterrows():
            brand = str(row.get(brand_col, ""))
            bonus = 15 if any(pb in brand for pb in pref_brands) else 0
            candidates.at[i, "_comp_score"] += bonus

    size_ranges = {
        "스타트업/소기업 (1~30명)": (1, 30),
        "중소기업 (31~100명)": (31, 100),
        "중견기업 (101~300명)": (101, 300),
        "대기업 (300명 이상)": (300, 99999),
        "상관없음": (0, 99999),
    }
    lo, hi = size_ranges.get(size_pref, (0, 99999))
    for i, row in candidates.iterrows():
        workers = float(row.get("상시근로자_num", 0))
        if lo <= workers <= hi:
            candidates.at[i, "_comp_score"] += 20
        elif abs(workers - (lo + hi) / 2) < 50:
            candidates.at[i, "_comp_score"] += 8

    return candidates.sort_values("_comp_score", ascending=False)


def match_companies(buk_df, job_row, region_filter, burnout_level, culture_pref, size_pref, top_n=5):
    keywords = extract_job_keywords(job_row)

    if region_filter and "전체" not in region_filter:
        region_mask = buk_df["지역명"].apply(lambda x: any(r in str(x) for r in region_filter))
        pool = buk_df[region_mask].copy()
        if len(pool) < 5:
            pool = buk_df.copy()
    else:
        pool = buk_df.copy()

    search_text = (
        pool.get("업종명(상)", pd.Series("", index=pool.index)).fillna("") + " " +
        pool.get("업종명(중)", pd.Series("", index=pool.index)).fillna("") + " " +
        pool.get("주요생산품목", pd.Series("", index=pool.index)).fillna("")
    )

    sector_kw_map = {
        "경영·사무·금융·보험직": ["금융", "보험", "경영", "컨설팅", "전문 서비스"],
        "연구직 및 공학 기술직": ["제조", "전기", "전자", "건설", "정보통신"],
        "교육·법률·사회복지·경찰·소방직 및 군인": ["교육", "사회복지"],
        "보건·의료직": ["의료", "보건", "제약"],
        "예술·디자인·방송·스포츠직": ["예술", "디자인", "방송"],
        "영업·판매·운전·운송직": ["도매", "소매", "운송", "물류"],
        "건설·채굴직": ["건설", "토목", "건축"],
        "설치·정비·생산직": ["제조", "생산", "기계", "설비"],
    }
    job_sector = str(job_row.get("직업 대분류명", ""))
    industry_hints = sector_kw_map.get(job_sector, ["제조"])

    pool = pool.copy()
    match_scores = pd.Series(0.0, index=pool.index)
    for idx in pool.index:
        txt = str(search_text.get(idx, ""))
        score = sum(3 for kw in keywords if kw in txt)
        score += sum(2 for ih in industry_hints if ih in txt)
        match_scores[idx] = score

    pool["_match_score"] = match_scores.values
    candidates = pool[pool["_match_score"] > 0].copy()
    if len(candidates) < 3:
        candidates = pool.copy()

    candidates = score_companies(candidates, burnout_level, culture_pref, size_pref)
    candidates["_final_comp_score"] = candidates["_match_score"] * 2 + candidates["_comp_score"]
    return candidates.sort_values("_final_comp_score", ascending=False).head(top_n)


# ─────────────────────────────────────────────────────────────────────────────
# UI 컴포넌트
# ─────────────────────────────────────────────────────────────────────────────

def render_hero():
    st.markdown("""
    <div class="hero">
        <div class="hero-badge">🧭 부울경 청년 취업 나침반</div>
        <div class="hero-title">JOB-ON-NA</div>
        <div style="font-family:'Noto Sans KR',sans-serif;font-size:1.5rem;font-weight:900;
                    color:rgba(255,255,255,0.9);margin-top:-4px;letter-spacing:2px;">
            일로온나
        </div>
        <div class="hero-sub">나의 성향·전공·가치관을 분석해 딱 맞는 직업과 부울경 우수기업을 연결합니다</div>
        <div class="hero-stats">
            <div class="hero-stat">
                <div class="hero-stat-num">537+</div>
                <div class="hero-stat-label">분석 직업 수</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-num">2,000+</div>
                <div class="hero-stat-label">부울경 강소기업</div>
            </div>
            <div class="hero-stat">
                <div class="hero-stat-num">100점</div>
                <div class="hero-stat-label">맞춤 스코어링</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def render_step_indicator(current):
    steps = ["기본 정보", "성향·가치관", "기업 선호", "결과 확인"]
    html = ""
    for i, label in enumerate(steps):
        n = i + 1
        cls = "done" if n < current else ("active" if n == current else "")
        icon = "✓" if n < current else str(n)
        lbl_cls = "active" if n == current else ""
        html += f'<div class="step-item"><div class="step-dot {cls}">{icon}</div><div class="step-label {lbl_cls}">{label}</div></div>'
        if i < len(steps) - 1:
            line_cls = "done" if n < current else ""
            html += f'<div class="step-line {line_cls}"></div>'
    st.markdown(f'<div class="step-wrap">{html}</div>', unsafe_allow_html=True)


def render_job_card(rank, job_row, score_detail):
    job_name = str(job_row.get("직업소분류명", "직업명 없음"))
    job_mid  = str(job_row.get("직업 중분류명", ""))
    job_big  = str(job_row.get("직업 대분류명", ""))
    wage     = str(job_row.get("평균임금", "-"))
    sat      = job_row.get("만족도_num", 70)
    prospect = str(job_row.get("일자리전망률", "-"))

    raw_summary = str(job_row.get("직업요약", ""))
    summary = raw_summary[:130] + "..." if len(raw_summary) > 130 else raw_summary

    skills_raw = str(job_row.get("필수 기술 및 지식", ""))
    skill_tags = [s.strip() for s in skills_raw.split(",")[:3] if len(s.strip()) < 15]
    cert_raw = str(job_row.get("관련자격명", ""))
    cert_tags = [c.strip() for c in cert_raw.split(",")[:2] if c.strip() and c.strip() != "nan"]

    total  = score_detail.get("total", 0)
    sm     = score_detail.get("major", 0)
    sb     = score_detail.get("burnout", 0)
    se     = score_detail.get("env", 0)
    sv     = score_detail.get("value", 0)

    prospect_icon = {"다소 증가": "📈", "유지": "➡️", "다소 감소": "📉", "감소": "🔻"}.get(prospect, "➡️")
    tags_html  = "".join(f'<span class="tag">{t}</span>' for t in skill_tags)
    cert_html  = "".join(f'<span class="tag tag-warn">{c}</span>' for c in cert_tags)

    # 💥 수정된 부분: HTML 코드를 왼쪽으로 바짝 붙여서 마크다운 코드 블록 인식을 방지합니다.
    html_content = f"""
<div class="job-card">
<div class="job-card-accent"></div>
<div class="job-rank-badge">#{rank}</div>
<div class="job-title" style="padding-right:60px">{job_name}</div>
<div class="job-cat">{job_big} &gt; {job_mid}</div>
<p style="font-size:0.82rem;color:#5D6D7E;margin:0 0 0.8rem;">{summary}</p>
<div class="score-grid">
<div>
<div class="score-label">📚 전공 매칭 (30점)</div>
<div class="score-bar-bg"><div class="score-bar-fill" style="width:{sm/30*100:.0f}%"></div></div>
<div class="score-val">{sm:.1f}점</div>
</div>
<div>
<div class="score-label">🧠 번아웃 부합도 (30점)</div>
<div class="score-bar-bg"><div class="score-bar-fill" style="width:{sb/30*100:.0f}%"></div></div>
<div class="score-val">{sb:.1f}점</div>
</div>
<div>
<div class="score-label">🏢 근무환경 (20점)</div>
<div class="score-bar-bg"><div class="score-bar-fill" style="width:{se/20*100:.0f}%"></div></div>
<div class="score-val">{se:.1f}점</div>
</div>
<div>
<div class="score-label">💡 가치관 가중치 (20점)</div>
<div class="score-bar-bg"><div class="score-bar-fill" style="width:{sv/20*100:.0f}%"></div></div>
<div class="score-val">{sv:.1f}점</div>
</div>
</div>
<div class="total-score-row">
<span class="total-score-label">🎯 종합 추천 점수</span>
<span class="total-score-val">{total:.1f}<span style="font-size:0.8rem;font-weight:400;color:#8FA0B0"> / 100</span></span>
</div>
<div class="job-meta">
<div class="job-meta-item">
<div class="job-meta-val">{wage}</div>
<div class="job-meta-key">평균 임금</div>
</div>
<div class="job-meta-item">
<div class="job-meta-val">{float(sat):.0f}%</div>
<div class="job-meta-key">직업만족도</div>
</div>
<div class="job-meta-item">
<div class="job-meta-val">{prospect_icon} {prospect}</div>
<div class="job-meta-key">일자리 전망</div>
</div>
</div>
<div class="tags-wrap">{tags_html}{cert_html}</div>
</div>
"""
    st.markdown(html_content, unsafe_allow_html=True)

def render_company_card(rank, comp_row):
    name     = str(comp_row.get("기업명", "-"))
    brand    = str(comp_row.get("강소기업브랜드명", "-"))
    region   = str(comp_row.get("지역명", "-"))
    industry = str(comp_row.get("업종명(상)", "-"))
    product  = str(comp_row.get("주요생산품목", "-"))[:50]
    workers  = comp_row.get("상시근로자_num", 0)
    comp_score = comp_row.get("_final_comp_score", 0)
    homepage = str(comp_row.get("회사홈페이지", ""))
    hp_html = f'<a href="http://{homepage}" target="_blank" style="font-size:0.73rem;color:#1A8CA3;">🌐 홈페이지</a>' if homepage and homepage not in ["nan", ""] else ""
    workers_str = f"{int(float(workers))}명" if workers and float(workers) > 0 else "-"

    st.markdown(f"""
    <div class="company-card">
        <div class="company-score-badge">🏆 매칭 {min(99,int(float(comp_score)))}점</div>
        <div style="display:flex;align-items:center;gap:6px;margin-bottom:4px">
            <span style="font-size:0.8rem;color:#8FA0B0;font-weight:700">#{rank}</span>
            <div class="company-name">{name}</div>
        </div>
        <div><span class="company-brand">{brand}</span></div>
        <div class="company-info">📍 {region} &nbsp;|&nbsp; 🏭 {industry} &nbsp;|&nbsp; 👥 {workers_str}</div>
        <div class="company-info" style="margin-top:4px">📦 {product} &nbsp; {hp_html}</div>
    </div>
    """, unsafe_allow_html=True)


def render_radar_chart(score_detail, job_name):
    cats = ["전공 매칭\n(30점)", "번아웃 부합도\n(30점)", "근무환경\n(20점)", "가치관\n(20점)"]
    vals = [
        score_detail.get("major", 0) / 30 * 100,
        score_detail.get("burnout", 0) / 30 * 100,
        score_detail.get("env", 0) / 20 * 100,
        score_detail.get("value", 0) / 20 * 100,
    ]
    fig = go.Figure(go.Scatterpolar(
        r=vals + [vals[0]], theta=cats + [cats[0]],
        fill="toself", fillcolor="rgba(27,79,114,0.18)",
        line=dict(color="#1B4F72", width=2.5),
        mode="lines+markers", marker=dict(size=7, color="#F39C12"),
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100], tickfont=dict(size=9))),
        showlegend=False,
        margin=dict(l=40, r=40, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=300,
    )
    st.plotly_chart(fig, use_container_width=True)


def render_wage_bar(top3_jobs):
    names, wages = [], []
    for row in top3_jobs:
        names.append(str(row.get("직업소분류명", ""))[:12])
        try:
            w = float(row.get("임금_만원", 0))
            wages.append(w if not np.isnan(w) else 0)
        except:
            wages.append(0)

    fig = px.bar(
        x=wages, y=names, orientation="h",
        color=wages, color_continuous_scale=["#AED6F1", "#1B4F72"],
        text=[f"{w:,.0f}만원" for w in wages],
    )
    fig.update_traces(textposition="outside", textfont_size=12)
    fig.update_layout(
        showlegend=False, coloraxis_showscale=False,
        margin=dict(l=10, r=80, t=10, b=10),
        paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        height=200, xaxis=dict(title="평균 임금 (만원/년)", tickfont=dict(size=10)),
        yaxis=dict(tickfont=dict(size=12)),
    )
    st.plotly_chart(fig, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# 세션 초기화
# ─────────────────────────────────────────────────────────────────────────────
if "results_ready" not in st.session_state:
    st.session_state.results_ready = False

# ─────────────────────────────────────────────────────────────────────────────
# 데이터 로드
# ─────────────────────────────────────────────────────────────────────────────
with st.spinner("📊 데이터를 불러오는 중..."):
    job_df, comp_df, buk_df = load_data()
    all_depts = get_all_departments(job_df)

# ─────────────────────────────────────────────────────────────────────────────
# HERO + STEP
# ─────────────────────────────────────────────────────────────────────────────
render_hero()
render_step_indicator(4 if st.session_state.results_ready else 1)


# ─────────────────────────────────────────────────────────────────────────────
# 입력 폼
# ─────────────────────────────────────────────────────────────────────────────
if not st.session_state.results_ready:

    with st.form("main_form"):

        # ── STEP 1 기본스펙 ─────────────────────────────────────────────────
        st.markdown("""
        <div class="section-head">
            <div class="section-icon">🎓</div>
            <div>
                <div class="section-title">STEP 1 · 기본 스펙</div>
                <div class="section-desc">학과, 최종학력, 희망 임금을 알려주세요</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<div class="input-card-title">🏫 학과 & 학력 정보</div>', unsafe_allow_html=True)

        c1, c2 = st.columns([3, 1])
        with c1:
            dept_search = st.text_input(
                "전공 학과명 입력 (글자 입력 → 자동완성)",
                placeholder="예: 경영학과, 컴퓨터공학과, 간호학과 ...",
            )
            # 자동완성
            if dept_search and len(dept_search) >= 1:
                suggestions = [d for d in all_depts if dept_search in d][:8]
                if suggestions:
                    chosen = st.selectbox(
                        "👇 목록에서 선택하거나 직접 입력을 유지하세요",
                        options=["직접 입력: " + dept_search] + suggestions,
                    )
                    final_dept = dept_search if chosen.startswith("직접 입력:") else chosen
                else:
                    final_dept = dept_search
                    st.caption("💡 DB에 없는 학과명입니다. 계열만 선택해도 분석됩니다.")
            else:
                final_dept = dept_search
                st.caption("💡 학과명을 입력하면 자동완성 목록이 표시됩니다.")

        with c2:
            user_major = st.selectbox("전공 계열",
                ["공학계열", "사회계열", "인문계열", "자연계열",
                 "교육계열", "의학계열", "예체능계열"])

        c3, c4 = st.columns(2)
        with c3:
            edu_level = st.selectbox("최종학력", ["고졸", "전문대졸", "대졸", "대학원졸", "박사졸"], index=2)
        with c4:
            min_wage = st.number_input(
                "최소 희망 임금 (만원/년)",
                min_value=0, max_value=20000, value=3000, step=100,
                help="이 금액의 80% 미만인 직업은 1차 제외됩니다."
            )
        st.markdown('</div>', unsafe_allow_html=True)

        # ── STEP 2 성향·가치관 ─────────────────────────────────────────────
        st.markdown("""
        <div class="section-head">
            <div class="section-icon">🧠</div>
            <div>
                <div class="section-title">STEP 2 · 성향 &amp; 가치관</div>
                <div class="section-desc">번아웃 상태, 근무환경 선호도, 직업 가치관 순위를 알려주세요</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<div class="input-card-title">🔥 번아웃 &amp; 근무 성향</div>', unsafe_allow_html=True)

        burnout_raw = st.radio(
            "현재 나의 번아웃 / 스트레스 수준",
            options=[
                "고위험 — 번아웃 심각, 워라밸 최우선",
                "중간 — 약간 지쳐있지만 균형 추구",
                "저위험 — 열정적, 도전적 환경 선호",
            ],
            index=1,
            help="고위험: 주말출근·위험환경 낮은 직업 우선 / 저위험: 성과·임금 높은 직업 우선"
        )
        burnout_level = burnout_raw.split(" — ")[0]

        c5, c6 = st.columns(2)
        with c5:
            env_pref = st.radio("근무환경 선호", ["실내 선호", "실외 선호", "혼합 무관"])
        with c6:
            core_value = st.radio("직업 가치관 1순위", ["높은 임금", "직업 안정성", "성취·보람", "워라밸"])
        st.markdown('</div>', unsafe_allow_html=True)

        # ── STEP 3 기업 선호 ───────────────────────────────────────────────
        st.markdown("""
        <div class="section-head">
            <div class="section-icon">🏙️</div>
            <div>
                <div class="section-title">STEP 3 · 기업 선호</div>
                <div class="section-desc">희망 지역, 기업 규모, 조직문화를 알려주세요</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        st.markdown('<div class="input-card-title">📍 부울경 지역 &amp; 기업 설정</div>', unsafe_allow_html=True)

        c7, c8 = st.columns(2)
        with c7:
            region_options = ["전체 부울경", "부산", "울산", "경남 창원",
                              "경남 김해", "경남 진주", "경남 양산", "경남 거제"]
            region_raw = st.multiselect(
                "희망 근무 지역 (복수 선택)",
                options=region_options, default=["전체 부울경"],
                help="'전체 부울경' 선택 시 전체 검색"
            )
            region_filter = ["전체"] if "전체 부울경" in region_raw else \
                [r.replace("경남 ", "") for r in region_raw]

        with c8:
            size_pref = st.selectbox("선호 기업 규모", [
                "스타트업/소기업 (1~30명)", "중소기업 (31~100명)",
                "중견기업 (101~300명)", "대기업 (300명 이상)", "상관없음"
            ], index=4)

        culture_pref = st.multiselect(
            "원하는 조직문화 / 기업 브랜드 (복수 선택)",
            options=["노사문화우수기업", "인재육성형중소기업", "근무혁신 우수기업",
                     "경남형 청년친화기업", "여가친화기업", "남녀고용평등우수기업",
                     "대한민국일자리으뜸기업", "최고일자리 기업", "좋은일터조성사업",
                     "월드클래스300", "기술혁신형 중소기업(이노비즈)", "글로벌 강소기업"],
            help="선택한 브랜드 인증 보유 기업에 가산점 부여"
        )
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("🚀 나만의 직업 · 기업 추천 받기")

    # ── 폼 제출 처리 ────────────────────────────────────────────────────────
    if submitted:
        with st.spinner("🔍 데이터를 분석 중입니다... (수십만 건 처리 중)"):

            filtered_df, excluded_df = hard_filter_jobs(job_df, edu_level, min_wage)

            if len(filtered_df) == 0:
                st.error("❌ 조건에 맞는 직업이 없습니다. 학력 또는 희망임금 조건을 완화해 보세요.")
                st.stop()

            scored_df = score_jobs(filtered_df, user_major, final_dept, burnout_level, env_pref, core_value)
            top3 = scored_df.head(3)

            alt_jobs = []
            if len(excluded_df) > 0:
                alt_scored = score_jobs(excluded_df, user_major, final_dept, burnout_level, env_pref, core_value)
                alt_jobs = [alt_scored.iloc[i] for i in range(min(2, len(alt_scored)))]

            company_results = []
            for _, job_row in top3.iterrows():
                matched = match_companies(buk_df, job_row, region_filter, burnout_level, culture_pref, size_pref, top_n=5)
                company_results.append(matched)

            st.session_state.top3_jobs = [top3.iloc[i] for i in range(len(top3))]
            st.session_state.company_results = company_results
            st.session_state.alt_jobs = alt_jobs
            st.session_state.user_input = dict(
                dept=final_dept, major=user_major, edu=edu_level, wage=min_wage,
                burnout=burnout_level, env=env_pref, value=core_value,
                region=region_raw, size=size_pref,
            )
            st.session_state.results_ready = True
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# 결과 화면
# ─────────────────────────────────────────────────────────────────────────────
else:
    top3_jobs      = st.session_state.top3_jobs
    company_results = st.session_state.company_results
    alt_jobs       = st.session_state.alt_jobs
    ui             = st.session_state.user_input

    chips = [
        f"🎓 {ui.get('dept') or ui.get('major', '')}",
        f"📚 {ui.get('edu', '')}",
        f"💰 {ui.get('wage', 0):,}만원 이상",
        f"🔥 번아웃: {ui.get('burnout', '')}",
        f"🏢 {ui.get('env', '')}",
        f"💡 {ui.get('value', '')} 우선",
    ]
    chips_html = "".join(f'<span class="result-chip">{c}</span>' for c in chips)
    st.markdown(f"""
    <div class="result-banner">
        <div class="result-banner-title">🎯 맞춤 분석 완료!</div>
        <div class="result-banner-sub">아래 조건을 기반으로 최적의 직업 3개와 부울경 강소기업을 추천합니다</div>
        <div class="result-chips">{chips_html}</div>
    </div>
    """, unsafe_allow_html=True)

    # 임금 차트
    st.markdown("""
    <div class="section-head">
        <div class="section-icon">📊</div>
        <div><div class="section-title">추천 직업 임금 비교</div>
        <div class="section-desc">Top 3 직업 평균 임금 (만원/년)</div></div>
    </div>
    """, unsafe_allow_html=True)
    render_wage_bar(top3_jobs)
    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # Top 3 직업 + 기업
    st.markdown("""
    <div class="section-head">
        <div class="section-icon">🏆</div>
        <div><div class="section-title">추천 직업 Top 3 + 부울경 매칭 기업</div>
        <div class="section-desc">100점 스코어링 결과 · 각 직업별 맞춤 강소기업</div></div>
    </div>
    """, unsafe_allow_html=True)

    for rank_idx, job_row in enumerate(top3_jobs):
        rank = rank_idx + 1
        score_detail = {
            "major":   float(job_row.get("_s_major", 0)),
            "burnout": float(job_row.get("_s_burn", 0)),
            "env":     float(job_row.get("_s_env", 0)),
            "value":   float(job_row.get("_s_val", 0)),
            "total":   float(job_row.get("_total", 0)),
        }

        col_job, col_radar = st.columns([3, 2])
        with col_job:
            render_job_card(rank, job_row, score_detail)
        with col_radar:
            job_short = str(job_row.get("직업소분류명", ""))[:10]
            st.markdown(f"<div style='font-size:0.8rem;font-weight:700;color:#1B4F72;margin-bottom:4px'>📡 스코어 방사형 분석 — {job_short}</div>", unsafe_allow_html=True)
            render_radar_chart(score_detail, job_short)

        # 기업 카드
        if rank_idx < len(company_results):
            comp_result = company_results[rank_idx]
            job_name = str(job_row.get("직업소분류명", ""))
            st.markdown(f"""
            <div style="background:#F0F4F8;border-radius:12px;padding:0.8rem 1rem;margin-bottom:0.7rem;">
                <span style="font-size:0.82rem;font-weight:700;color:#1B4F72;">
                    🏙️ '{job_name}' 맞춤 부울경 강소기업 Top {min(5, len(comp_result))}
                </span>
            </div>
            """, unsafe_allow_html=True)
            for cr, (_, crow) in enumerate(comp_result.iterrows(), 1):
                render_company_card(cr, crow)

        if rank_idx < 2:
            st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # 대안 직업
    if alt_jobs:
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown("""
        <div class="section-head">
            <div class="section-icon">💡</div>
            <div><div class="section-title">학력 조건 완화 시 고려 가능한 대안 직업</div>
            <div class="section-desc">현 학력 기준 진입 비중이 낮지만 성향 매칭도가 높습니다</div></div>
        </div>
        """, unsafe_allow_html=True)
        for alt_row in alt_jobs:
            alt_name = str(alt_row.get("직업소분류명", ""))
            alt_big  = str(alt_row.get("직업 대분류명", ""))
            alt_edu  = str(alt_row.get("대표학력", ""))
            alt_wage = str(alt_row.get("평균임금", "-"))
            st.markdown(f"""
            <div class="alt-card">
                <div class="alt-card-title">💼 {alt_name}</div>
                <div class="alt-card-reason">
                    {alt_big} · 주요 종사 학력: {alt_edu} · 평균임금: {alt_wage}
                    — 추가 학력을 갖추면 진입 가능성 ↑
                </div>
            </div>
            """, unsafe_allow_html=True)

    # 다시 시작 버튼
    st.markdown("<br><br>", unsafe_allow_html=True)
    col_r, _ = st.columns([1, 3])
    with col_r:
        if st.button("🔄 처음부터 다시 분석하기"):
            for k in ["results_ready", "top3_jobs", "company_results", "alt_jobs", "user_input"]:
                st.session_state.pop(k, None)
            st.rerun()

    # 푸터
    st.markdown("""
    <div style="text-align:center;padding:2.5rem 0 1rem;color:#AEB6BF;font-size:0.75rem;">
        <strong style="color:#5D6D7E;">일로온나 (Job-On-Na)</strong> · 부울경 청년 맞춤형 직업·기업 추천 플랫폼<br>
        데이터 출처: 워크넷 직업정보 DB · 강소기업 마스터 DB<br>
        © 2025 Job-On-Na · Built with ❤️ for 부울경 청년
    </div>
    """, unsafe_allow_html=True)
