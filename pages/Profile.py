import streamlit as st
from src.components import ProfileUI

st.title("プロフィール")
ui = ProfileUI()

if not ui.has_users():
    ui.create_profile_form()
    
ui.profile_list()
ui.edit_form()