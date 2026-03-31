import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(page_title="학과 검색 시스템", layout="centered")

@st.cache_data
def load_data():
    # 1. CSV 파일 읽기 (파일명과 경로가 정확해야 합니다)
    try:
        df = pd.read_csv('worknet_major_master.csv')
        
        # 2. '세부학과명' 컬럼 데이터만 추출
        # 결측치(NaN) 제거 및 중복 제거 후 가나다순 정렬
        major_list = df['세부학과명'].dropna().unique().tolist()
        major_list.sort()
        
        return major_list
    except FileNotFoundError:
        st.error("파일을 찾을 수 없습니다. 'worknet_major_master.csv' 파일이 같은 폴더에 있는지 확인해주세요.")
        return []

# 데이터 로드
departments = load_data()

st.title("🎓 학과 선택 서비스")
st.write("찾으시는 학과의 키워드를 입력해보세요.")

# 3. selectbox에 적용
if departments:
    selected_dept = st.selectbox(
        "본인의 학과를 선택해주세요",
        options=departments,
        index=None,  # 초기 선택값 없음
        placeholder="여기에 학과명을 입력하세요",
        help="입력창에 글자를 치면 해당 글자가 포함된 학과가 아래에 나타납니다."
    )

    # 결과 출력
    if selected_dept:
        st.divider()
        st.success(f"✅ 선택된 학과: **{selected_dept}**")
else:
    st.warning("학과 목록을 불러올 수 없습니다.")