import streamlit as st
from src.components import UserManagementUI

st.title("ユーザー管理システム")
ui = UserManagementUI()
ui.create_user_form()
ui.user_list()
ui.edit_form()