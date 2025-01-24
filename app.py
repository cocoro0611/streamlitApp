import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import pandas as pd
import matplotlib.pyplot as plt

st.title("サンプルアプリ")
st.caption("これはcocoroのサンプリアプリケーションです")

col1, col2 = st.columns(2)

with col1:
    st.subheader("自己紹介")
    st.text("IT企業勤めの26歳男です。\n" #「\」これはoption + ¥で出せる
            "よろしくお願いします。")

    code = '''
    import streamlit as st

    st.title("サンプルコード")
    '''
    st.code(code, language="python")

    # 画像
    image1 = Image.open("static/images/siba1.jpg")

    response = requests.get("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhjKld93ujSJ-vKCx8FIpy1nGimFgtoWpToBiPLl5aZVW9_W-Eig0bmpD8mpbTKIrw4NfKnhzHqIQE4KA6kReMfm-NjlMG8GPnzrVbBaMGdyEcb-U_vev81rtg0CWCDjU2orYSwrGpHsFoZ/s800/dog_shibainu_black.png")
    image_data = BytesIO(response.content)
    image2 = Image.open(image_data)

    col11, col12 = st.columns(2)

    with col11:
        st.image(image1, width=200)
    with col12:
        st.image(image2, width=200)

    with st.form(key="profile_form"):
        # テキストボックス  
        name = st.text_input("名前")
        address = st.text_input("住所")

        # セレクトボックス
        age_category = st.selectbox(
            "年齢層",
            ("子供（18歳未満）", "大人(18歳以上)")
        )

        # ラジオボタン
        sex_category = st.radio(
            "性別",
            ("男", "女")
        )

        # 複数選択
        hobby = st.multiselect(
            "趣味",
            ("スポーツ", "読書", "プログラミング", "アニメ・映画", "釣り", "料理")
        )

        # チェックボックス
        mail_subscribe = st.checkbox("メールマガジンを購読する")

        # スライダー
        height = st.slider("身長", min_value=110, max_value=210)

        # 日付
        start_date = st.date_input(
            "開始日"
        )

        # カラーピッカー
        color = st.color_picker("テーマカラー","#00f900")

        # ボタン
        submit_btn = st.form_submit_button("送信")
        cancel_btn = st.form_submit_button("キャンセル")
        if submit_btn:
            st.text(f"ようこそ！{name}さん！{address}に書類を送りました") # fは変数値の埋め込み
            st.text(f"年齢層：{age_category}")
            st.text(f"性別：{sex_category}")
            st.text(f"趣味： {', '.join(hobby)}")

with col2:
    # データ分析関連
    df = pd.read_csv("static/data/temperature.csv",index_col="月")
    # st.dataframe(df)
    st.table(df)
    st.line_chart(df)
    st.bar_chart(df["2023年"])

    # matplotlibを使った場合
    fig, ax = plt.subplots()
    ax.plot(df.index, df["2021年"])
    ax.set_title("matplotlib graph")
    st.pyplot(fig)