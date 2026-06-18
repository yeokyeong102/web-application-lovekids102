import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(page_title="분수와 나머지 학습", layout="wide")

# 타이틀
st.title("🍕 피자 조각으로 재미있게 배우는 '분수와 나머지' 파티!")

# 환영 인사 및 설명
st.write("""
안녕하세요! 👋 반갑습니다!  
피자 조각 나누기를 통해 **분수**와 **나머지**의 개념을 배워보아요!  
🔑 **핵심 개념**: 피자를 쪼개면 분수가 되고, 친구들과 나누고 남으면 나머지가 된답니다! 🎉
""")

st.divider()

# 사이드바에서 슬라이더 입력받기
st.sidebar.header("🎮 피자 나누기 조이스틱")

# ① 분모 (총 조각 수)
denominator = st.sidebar.slider(
    "① 전체 피자를 총 몇 조각으로 나눌 것인가?",
    min_value=1,
    max_value=16,
    value=8,
    help="분모를 설정하세요 (전체 조각 수)"
)

# ② 분자 (사용할 조각 수)
numerator = st.sidebar.slider(
    "② 그중에서 우리가 꺼내서 사용할 피자는 몇 조각인가?",
    min_value=0,
    max_value=denominator,
    value=4,
    help="분자를 설정하세요 (사용할 조각 수)"
)

# ③ 나누는 수 (친구 수)
friends = st.sidebar.slider(
    "③ 이 피자 조각을 몇 명의 친구가 똑같이 나누어 먹을 것인가?",
    min_value=1,
    max_value=6,
    value=3,
    help="나누는 수를 설정하세요 (친구 수)"
)

st.sidebar.divider()

# 계산
quotient = numerator // friends  # 몫
remainder = numerator % friends  # 나머지

# 시각화
col1, col2 = st.columns(2)

with col1:
    st.subheader("🍕 우리의 피자")
    
    # 원형 차트 그리기
    fig, ax = plt.subplots(figsize=(8, 8))
    
    # 색상 설정
    colors = []
    sizes = []
    labels = []
    
    # 친구들이 공평하게 나눠 가지는 부분
    shared_portion = quotient * friends
    if shared_portion > 0:
        pepperoni_colors = ['#FFB6C1', '#FFA500', '#FFD700', '#FFDAB9', '#FFC0CB', '#FFE4B5']
        for i in range(shared_portion):
            colors.append(pepperoni_colors[i % len(pepperoni_colors)])
            sizes.append(1)
        labels.append(f'친구들이 나눠 먹는 부분 ({shared_portion})')
    
    # 나머지
    if remainder > 0:
        colors.extend(['#F5F5DC'] * remainder)  # 연한 베이지색
        sizes.extend([1] * remainder)
        labels.append(f'남는 나머지 ({remainder})')
    
    # 사용하지 않은 피자
    unused = denominator - numerator
    if unused > 0:
        colors.extend(['#D3D3D3'] * unused)  # 연한 회색
        sizes.extend([1] * unused)
        labels.append(f'안 쓴 피자 ({unused})')
    
    # 파이 차트 그리기
    ax.pie(sizes, colors=colors, startangle=90, wedgeprops=dict(edgecolor='white', linewidth=2))
    ax.set_title("피자 조각 분배", fontsize=14, fontweight='bold', pad=20)
    st.pyplot(fig)

with col2:
    st.subheader("📊 수학으로 배우는 분수와 나머지")
    
    # 분수 설명
    st.markdown(f"""
    **분수 개념:**  
    전체 **{denominator}** 조각 중 **{numerator}** 조각, 즉 **{numerator}/{denominator}** 입니다!
    """)
    
    st.divider()
    
    # 나눗셈 및 나머지 설명
    st.markdown(f"""
    **나눗셈과 나머지:**  
    **{numerator}** ÷ **{friends}** = 몫 **{quotient}** ... 나머지 **{remainder}**
    """)
    
    st.divider()
    
    # 몫과 나머지를 계기판으로 표시
    metric_col1, metric_col2 = st.columns(2)
    with metric_col1:
        st.metric("한 친구가 먹는 양 (몫)", f"{quotient}개", delta=None)
    with metric_col2:
        st.metric("남는 양 (나머지)", f"{remainder}개", delta=None)
    
    st.divider()
    
    # 나머지 알림
    if remainder == 0:
        st.success(f"✨ 완벽해요! 피자가 정확히 **{friends}**명이 균등하게 나눠먹을 수 있어요! 아무것도 남지 않았어요!")
    else:
        st.info(f"ℹ️ **{remainder}**개의 피자가 남았어요! 이것이 **나머지**예요. 더 잘게 나누거나 다음에 먹을 수 있어요!")

st.divider()

# 배달 완료 버튼
if st.button("🎊 배달 완료! Check", use_container_width=True):
    st.balloons()
    st.success("🎉 완료했어요! 오늘도 훌륭하게 배웠어요!")
