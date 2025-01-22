import streamlit as st

st.title("コーヒー予測アプリ")
st.caption("お好みの条件を選んで、あなたにぴったりのコーヒーを見つけましょう")

st.subheader("コーヒーの好みを教えてください")
with st.form(key="profile_form"):
    # 焙煎度のスライダー
    roast = st.slider("焙煎度", min_value=1, max_value=5)
    st.markdown(
        '<div style="display: flex; justify-content: space-between; margin-top: -15px;">'
        '<span>浅煎り</span>'
        '<span>深煎り</span>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # 酸味のスライダー
    acidity = st.slider("酸味", min_value=1, max_value=5)
    st.markdown(
        '<div style="display: flex; justify-content: space-between; margin-top: -15px;">'
        '<span>穏やか</span>'
        '<span>鮮やか</span>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # コクのスライダー
    body = st.slider("コク", min_value=1, max_value=5)
    st.markdown(
        '<div style="display: flex; justify-content: space-between; margin-top: -15px;">'
        '<span>さっぱり</span>'
        '<span>しっかり</span>'
        '</div>',
        unsafe_allow_html=True
    )
    
    submit_btn = st.form_submit_button("これで診断する")

if submit_btn:
    st.subheader("診断結果")
    st.text(f"あなたの好みの条件:")
    st.text(f"・焙煎度：{roast}")
    st.text(f"・酸味：{acidity}")
    st.text(f"・コク：{body}")