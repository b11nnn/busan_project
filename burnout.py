import streamlit as st

def main():
    # 기본 설정
    st.set_page_config(page_title="취업 번아웃 진단", layout="wide")
    
    # 커스텀 CSS 적용 (글자 크기, 색상, 디자인 요소)
    st.markdown("""
    <style>
        .title-text { font-size: 2.5rem; font-weight: 800; color: #111; margin-bottom: 0.5rem; }
        .sub-text { font-size: 1.1rem; color: #555; margin-bottom: 2rem; }
        .busan-blue { color: #005bac; font-size: 1.8rem; font-weight: 700; margin-top: 2rem; margin-bottom: 0.5rem; }
        .instruction-text { font-size: 1.2rem; color: #444; margin-bottom: 1.5rem; background-color: #f0f4f8; padding: 10px; border-radius: 8px; }
        .question-text { font-size: 1.2rem; font-weight: 600; color: #222; margin-bottom: 0.5rem; margin-top: 1rem; }
        .report-box { background-color: #f4f9ff; border-left: 6px solid #005bac; padding: 25px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-top: 20px; margin-bottom: 30px; }
        .report-title { font-size: 1.5rem; font-weight: 700; color: #005bac; margin-bottom: 15px; }
        .report-content { font-size: 1.15rem; line-height: 1.7; color: #333; }
        .program-link { font-size: 1.15rem; color: #333; text-decoration: none; padding: 8px 0; display: block; border-bottom: 1px solid #eee; }
        .program-link:hover { color: #005bac; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

    # 헤더 영역
    st.markdown("<div class='title-text'>취업준비생 번아웃 정밀 진단 시스템</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-text'>최유진·홍지영(2023)의 억제 효과 연쇄 붕괴 모델 기반 심층 분석</div>", unsafe_allow_html=True)
    st.markdown("---")

    # [데이터 및 가중치 정의] 부연 설명 모두 제거
    s_q = [
        ("취업에 실패하지는 않을지 항상 불안하고 초조하다.", 0.80),
        ("어떤 일이 있어도 꼭 취업을 해야 하지만 자꾸만 자신감이 없어진다.", 0.79),
        ("열심히 공부하려고 하지만 취업걱정 때문에 집중이 잘 안된다.", 0.74),
        ("취업문제에 대하여 부모님의 기대가 너무 커서 부담스럽다.", 0.73),
        ("지방대학 출신 등 환경적 요인 때문에 불리한 것 같다.", 0.67)
    ]
    
    o_q = [
        ("나는 내가 목표한 바를 이룰 수 있다고 믿는다.", 0.91),
        ("나는 어려운 상황이 닥쳐도 잘 대처할 자신이 있다.", 0.82),
        ("나는 다른 사람들과 잘 지낼 수 있다고 믿는다.", 0.76),
        ("나의 장래는 밝고 희망적이다.", 0.72),
        ("나는 전반적으로 나의 삶에 만족한다.", 0.69)
    ]
    
    e_q = [
        ("앞으로 5년 동안의 나의 진로 계획을 세울 수 있다.", 0.82),
        ("나의 능력이나 적성에 대하여 정확하게 파악할 수 있다.", 0.77),
        ("내가 하고 싶은 일을 한 가지 결정할 수 있다.", 0.76),
        ("관심 있는 직업에 관한 정보를 찾아낼 수 있다.", 0.71),
        ("선택한 분야가 안 된다면 다른 길을 선택할 수 있다.", 0.69)
    ]

    # 1. 취업 스트레스
    st.markdown("<div class='busan-blue'>1단계: 취업 스트레스 지수</div>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>다음 문항에 대해 평소 느끼는 정도를 선택해주세요. (1: 전혀 그렇지 않다 ~ 5: 매우 그렇다)</div>", unsafe_allow_html=True)
    s_scores = []
    for i, (txt, weight) in enumerate(s_q):
        st.markdown(f"<div class='question-text'>{i+1}. {txt}</div>", unsafe_allow_html=True)
        score = st.radio("", [1, 2, 3, 4, 5], index=2, horizontal=True, key=f"s_{i}", label_visibility="collapsed")
        s_scores.append(score)

    st.markdown("<br>", unsafe_allow_html=True)

    # 2. 낙관성
    st.markdown("<div class='busan-blue'>2단계: 성향적 낙관성</div>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>다음 문항에 대해 평소 느끼는 정도를 선택해주세요. (1: 전혀 그렇지 않다 ~ 5: 매우 그렇다)</div>", unsafe_allow_html=True)
    o_scores = []
    for i, (txt, weight) in enumerate(o_q):
        st.markdown(f"<div class='question-text'>{i+1}. {txt}</div>", unsafe_allow_html=True)
        score = st.radio("", [1, 2, 3, 4, 5], index=2, horizontal=True, key=f"o_{i}", label_visibility="collapsed")
        o_scores.append(score)

    st.markdown("<br>", unsafe_allow_html=True)

    # 3. 자기효능감
    st.markdown("<div class='busan-blue'>3단계: 진로결정 자기효능감</div>", unsafe_allow_html=True)
    st.markdown("<div class='instruction-text'>다음 문항에 대해 평소 느끼는 정도를 선택해주세요. (1: 전혀 그렇지 않다 ~ 5: 매우 그렇다)</div>", unsafe_allow_html=True)
    e_scores = []
    for i, (txt, weight) in enumerate(e_q):
        st.markdown(f"<div class='question-text'>{i+1}. {txt}</div>", unsafe_allow_html=True)
        score = st.radio("", [1, 2, 3, 4, 5], index=2, horizontal=True, key=f"e_{i}", label_visibility="collapsed")
        e_scores.append(score)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # 진단 결과 버튼
    if st.button("진단 및 처방 결과 확인하기", use_container_width=True):
        # 점수 계산
        S = sum(s * q[1] for s, q in zip(s_scores, s_q))
        O = sum((6 - o) * q[1] for o, q in zip(o_scores, o_q))
        E = sum((6 - e) * q[1] for e, q in zip(e_scores, e_q))
        BI = (S * 1.0) + (O * 0.41) + (E * 0.86)

        # 단계 판정
        if BI <= 12.0: stage, name = 2, "안전 지대"
        elif BI <= 18.9: stage, name = 4, "열정적 적응"
        elif BI <= 22.4: stage, name = 5, "방어선 균열기"
        elif BI <= 25.8: stage, name = 6, "심리적 잠복기"
        elif BI <= 29.2: stage, name = 7, "임계 번아웃"
        elif BI <= 32.7: stage, name = 8, "효능감 고갈기"
        elif BI <= 36.1: stage, name = 9, "행동 정지기"
        else: stage, name = 10, "완전 번아웃"

        st.markdown("---")
        st.markdown(f"<div class='busan-blue' style='font-size:2rem;'>진단 결과: {stage}단계 [{name}]</div>", unsafe_allow_html=True)
        
        # [로직 개선] 단계에 따라 낙관성 파괴 여부를 다르게 서술하여 모순 해결
        if stage <= 4:
            report_content = f"현재 취업 스트레스 지수는 {S:.2f}점입니다. 취업에 대한 부담감이 다소 존재하지만, 당신의 내면에는 미래에 대한 낙관성과 스스로 해낼 수 있다는 자기효능감이 단단하게 자리잡고 있습니다. 스트레스가 심리적 자산을 파괴하지 못하고 오히려 적절한 긴장감과 추진력으로 작용하고 있는 건강한 상태입니다. 지금의 페이스를 유지하시길 바랍니다."
        elif stage <= 6:
            report_content = f"현재 취업 스트레스 지수는 {S:.2f}점입니다. 스트레스가 지속되면서 미래에 대한 긍정적인 기대인 낙관성이 서서히 영향을 받기 시작했습니다. 심리적 방어선에 작은 균열이 생기고 피로감이 누적되는 시기입니다. 아직 목표를 향해 나아갈 힘은 충분하지만, 스트레스가 더 깊어지기 전에 정서적인 환기와 휴식이 필요한 과도기 상태입니다."
        elif stage <= 8:
            report_content = f"현재 취업 스트레스 지수는 {S:.2f}점입니다. 누적된 스트레스로 인해 낙관성이 꺾이면서, 취업 계획을 세우고 실행할 수 있다는 자기효능감마저 흔들리고 있습니다. 논문에서 경고하는 '억제 효과'가 발생한 구간으로, 취업 준비를 하려 할수록 오히려 심리적 고통이 커져 노력이 겉돌게 되는 위험한 상태입니다. 무리한 계획보다는 멘탈 회복이 우선되어야 합니다."
        else:
            report_content = f"현재 취업 스트레스 지수는 {S:.2f}점입니다. 스트레스가 심리적 방어선을 완전히 무너뜨려 낙관성과 자기효능감이 극도로 고갈되었습니다. 마음의 엔진이 꺼져버려 실질적인 취업 준비 행동을 이어나가기 힘든 심각한 번아웃 상태입니다. 이는 단순한 의지 부족이 아닌 심리적 마비 상태이므로, 당장의 취업 스펙보다 전문가의 도움이나 적극적인 치유를 통해 마음을 돌보는 것이 가장 시급합니다."

        # 미감 개선 리포트 출력
        st.markdown(f"""
        <div class='report-box'>
            <div class='report-title'>정밀 분석 리포트</div>
            <div class='report-content'>{report_content}</div>
        </div>
        """, unsafe_allow_html=True)

        # 맞춤형 프로그램 추천 (누적 및 단계 라벨링 숨김)
        st.markdown("<div class='busan-blue'>맞춤형 추천 프로그램</div>", unsafe_allow_html=True)
        st.markdown("<div style='margin-bottom: 15px; font-size: 1.1rem; color: #555;'>현재 상태에서 도움을 받을 수 있는 실질적인 지원 프로그램들입니다.</div>", unsafe_allow_html=True)
        
        # 사용자 모르게 리스트업
        programs = []
        if stage >= 1:
            programs.append(("부산일자리정보망 취업지원정책", "https://www.busanjob.net/03_part/part00.asp"))
        if stage >= 5:
            programs.append(("부산청년플랫폼 커뮤니티 활동", "https://www.instagram.com/busan_c_youth/"))
            programs.append(("부산청년 만원문화패스", "https://young.busan.go.kr/index.nm?menuCd=234"))
        if stage >= 7:
            programs.append(("부산일자리정보망 1:1 심층 상담", "https://www.busanjob.net/04_cons/cons01.asp"))
        if stage >= 9:
            programs.append(("부산광역정신건강복지센터 마음건강 온라인 상담", "https://www.busaninmaum.com/?sid=29"))
        if stage >= 10:
            programs.append(("부산청년마음건강센터 청춘소설 집중 상담", "https://www.youngmind.or.kr/sub.php?menukey=13"))

        # HTML로 예쁘게 출력
        html_links = ""
        for name, url in programs:
            html_links += f"<a href='{url}' target='_blank' class='program-link'>▶ {name} 알아보기</a>"
        
        st.markdown(f"<div>{html_links}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()