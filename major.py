import streamlit as st
import pandas as pd
import os

@st.cache_data
def load_data():
    # 1. 현재 파이썬 파일(.py)이 있는 폴더 경로를 구합니다.
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. 그 폴더 안에 있는 csv 파일의 절대 경로를 만듭니다.
    file_path = os.path.join(current_dir, 'worknet_major_master.csv')
    
    try:
        # 깃허브에 올릴 때 UTF-8로 저장했다면 'utf-8-sig'가 가장 안전합니다.
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        
        major_list = df['세부학과명'].dropna().unique().tolist()
        major_list.sort()
        return major_list
    except FileNotFoundError:
        st.error(f"파일을 찾을 수 없습니다. 경로를 확인해주세요: {file_path}")
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
