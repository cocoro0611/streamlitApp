import streamlit as st
from src.components import ProfileUI, ExerciseResultUI

st.title("フィットネス記録")

# プロフィール管理
st.header("プロフィール")
profile_ui = ProfileUI()
profile_ui.profile_list()
profile_ui.edit_form()

# 運動記録管理（ユーザーが選択されている場合のみ表示）
if 'editing_user_id' in st.session_state:
    st.header(f"{st.session_state.editing_user_name}さんの運動記録")
    exercise_ui = ExerciseResultUI(st.session_state.editing_user_id)
    exercise_ui.create_exercise_form()
    st.subheader("記録一覧")
    exercise_ui.exercise_list()
    exercise_ui.edit_form()