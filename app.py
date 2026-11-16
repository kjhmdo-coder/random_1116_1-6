import random
import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="오늘의 점심 추천", page_icon="🍱")

st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("버튼을 눌러 오늘 먹을 점심 메뉴를 랜덤으로 뽑아보세요!")

# 점심 메뉴 후보 리스트 (원하는 메뉴를 자유롭게 추가·수정할 수 있습니다)
lunch_menus = [
    "김치찌개",
    "된장찌개",
    "제육볶음",
    "순대국밥",
    "비빔밥",
    "부대찌개",
    "돈까스",
    "초밥",
    "라멘",
    "우동",
    "짜장면",
    "짬뽕",
    "마라탕",
    "쌀국수",
    "파스타",
    "햄버거",
    "샌드위치 & 샐러드",
    "냉면",
]

# 버튼을 눌렀을 때 실행될 동작
if st.button("🎲 오늘의 메뉴 추천받기", type="primary"):
    selected_menu = random.choice(lunch_menus)
    st.success(
        f"오늘의 추천 점심 메뉴는 **{selected_menu}**입니다! 맛있게 드세요 😋"
    )
    st.balloons()

# 등록된 메뉴 목록을 확인할 수 있는 접이식 영역
with st.expander("등록된 전체 메뉴 목록 보기"):
    st.write(", ".join(lunch_menus))
