import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 기본 설정
st.set_page_config(page_title="일로온나 Job-On-Na", page_icon="🌊", layout="wide")

# 타이틀 및 소개
st.title("🌊 일로온나 Job-On-Na 🌊")
st.markdown(" *•*¨*•.¸¸여러분의 전공, 성향에 맞춘 기업을 알려주고 취준 로드맵을 제공합니다¸¸.•*¨*•* ")

# 사이드바 메뉴 구성
st.sidebar.header("ʕ •̀ᴥ•́ ʔ  메뉴 ")
menu = st.sidebar.radio("이동할 페이지를 선택하세요:", 
                        ("1. 프로필 & 번아웃 진단", "2. 부울경 맞춤 일자리 매칭", "3. To-Do & 지원 정책"))

# --------------------------------------------------------------------------------
# 1. 프로필 & 번아웃 진단 페이지
# --------------------------------------------------------------------------------
if menu == "1. 프로필 & 번아웃 진단":
    st.header("✧ 나의 상태와 목표 설정하기 ✧")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🧾기본 스펙 입력")
        major = st.text_input("전공을 입력해주세요 (예: 컴퓨터공학, 경영학)")
        skills = st.text_input("보유 기술 및 자격증 (쉼표로 구분)")
        lifestyle = st.selectbox("가장 중요하게 생각하는 가치는?", ["워라밸(저녁이 있는 삶)", "높은 연봉", "직무 전문성 성장", "안정성"])
    
    with col2:
        st.subheader("🔥번아웃 자가 진단🔥")
        st.markdown("최근 1주일간의 상태를 체크해주세요.")
        q1 = st.slider("아침에 일어날 때 출근/취업준비 할 생각에 피곤함을 느낀다.", 1, 5, 3)
        q2 = st.slider("하루 일과가 끝나면 완전히 지쳐버린다.", 1, 5, 3)
        q3 = st.slider("취업에 대한 자신감이 떨어지고 우울감이 든다.", 1, 5, 3)
        
        burnout_score = q1 + q2 + q3
    
    if st.button("진단 및 프로필 저장"):
        st.success("데이터가 저장되었습니다! 다음 탭으로 이동해보세요.")
        
        # 번아웃 시각화 (Plotly 게이지 차트)
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = burnout_score,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "나의 번아웃 지수"},
            gauge = {'axis': {'range': [None, 15]},
                     'bar': {'color': "darkblue"},
                     'steps' : [
                         {'range': [0, 5], 'color': "lightgreen"},
                         {'range': [5, 10], 'color': "yellow"},
                         {'range': [10, 15], 'color': "red"}]}
        ))
        st.plotly_chart(fig, use_container_width=True)
        
        if burnout_score >= 10:
            st.error("🚨 번아웃 위험 단계입니다! 무리한 취업 준비보다 잠시 휴식이 필요합니다.")
            st.info("💡 추천 케어 방안: 부산시 청년 마음건강 지원사업 신청하기, 동네 산책하기")

# --------------------------------------------------------------------------------
# 2. 부울경 맞춤 일자리 매칭 페이지
# --------------------------------------------------------------------------------
elif menu == "2. 부울경 맞춤 일자리 매칭":
    st.header("⚡내 스펙에 딱 맞는 부울경 유망 기업⚡")
    st.markdown("고용24 API(채용정보, 기업정보)를 연동하여 결과가 표시되는 영역")
    
    # 예시용 가짜 데이터 (실제로는 API에서 json을 받아와서 pandas DataFrame으로 변환)
    dummy_jobs = pd.DataFrame({
        "기업명": ["(주)부산데이터테크", "울산스마트에너지", "경남AI솔루션즈"],
        "직무": ["데이터 분석가", "시스템 엔지니어", "AI 모델러"],
        "위치": ["부산 해운대구", "울산 남구", "경남 창원시"],
        "예상연봉": ["3,200만원", "3,500만원", "3,400만원"],
        "매칭률": ["95%", "88%", "82%"]
    })
    
    st.dataframe(dummy_jobs, use_container_width=True)
    st.caption("※ 실제 연동 시 입력하신 전공/기술 기반으로 필터링된 결과가 나옵니다.")

# --------------------------------------------------------------------------------
# 3. To-Do & 지원 정책 페이지
# --------------------------------------------------------------------------------
elif menu == "3. To-Do & 지원 정책":
    st.header(" ✧･ﾟ･ 취업 성공을 위한 To-Do 및 꿀혜택 ･ﾟ･ﾟ✧  ")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🗒️ 나의 To-Do List")
        st.checkbox("정보처리기사 실기 준비")
        st.checkbox("부산 IT 직무 채용박람회 사전 신청 (이번주 금요일)")
        st.checkbox("자소서 1차 완성하기")
        
        st.subheader("✏️ 추천 교육 과정 (내일배움카드)")
        st.markdown("- [부산 IT교육센터] 실무 데이터 분석 과정 (전액 무료)")
        st.markdown("- [온라인] 파이썬 백엔드 부트캠프")
        st.caption("고용24 API의 '국민내일배움카드 훈련과정' 데이터를 연동합니다.")

    with col2:
        st.subheader("💰 부울경 청년 지원 정책 모음")
        # 정책을 예쁜 카드로 표시
        with st.expander("🏠 주거/생활 지원 (부산)"):
            st.markdown("- 부산 청년 기쁨 두배 통장: 매월 10만원 저축 시 시에서 10만원 추가 적립")
            st.markdown("- 청년 월세 지원: 월 최대 20만원 지원")
            
        with st.expander("👔 취업 지원 프로그램"):
            st.markdown("- 드림옷장: 면접용 정장 무료 대여 서비스")
            st.markdown("- 부산일자리정보망 직업탐방: 우수 중소/중견기업 현장 견학")
        

