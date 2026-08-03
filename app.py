import streamlit as st

st.set_page_config(
    page_title="수학 실험실",
    page_icon="📐"
)

st.title("📐 나의 수학웹 실험실")
st.write("숫자를 입력하면 제곱과 세제곱을 계산합니다.")

number = st.number_input(
    "숫자를 입력하세요.",
    value=2.0
)

st.subheader("계산 결과")

st.write("제곱:, {number ** 2:.3f}")
st.write("세제곱:, {number ** 3:.4f}")

if st.button("인사하기"):
    st.success("수학 실험실에 오신 것을 환영합니다!")
