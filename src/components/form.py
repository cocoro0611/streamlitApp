import streamlit as st
from src.database.db import SessionLocal
from src.services import UserCRUD

class UserManagementUI:
   def __init__(self):
       self.crud = UserCRUD(SessionLocal())

   def create_user_form(self):
       with st.form("新規ユーザー"):
           email = st.text_input("メールアドレス")
           name = st.text_input("名前")
           if st.form_submit_button("作成") and email and name:
               try:
                   user = self.crud.create(email, name)
                   st.success(f"作成成功: {user.name}")
               except Exception as e:
                   st.error(f"エラー: {e}")

   def user_list(self):
       st.subheader("ユーザー一覧")
       for user in self.crud.get_all():
           self.user_row(user)

   def user_row(self, user):
       col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
       col1.write(f"Email: {user.email}")
       col2.write(f"Name: {user.name}")
       if col3.button("編集", key=f"edit_{user.id}"):
           self.set_editing_user(user)
       if col4.button("削除", key=f"delete_{user.id}"):
           self.delete_user(user.id)

   def edit_form(self):
       if 'editing_user_id' in st.session_state:
           with st.form("ユーザー編集"):
               new_name = st.text_input("新しい名前", st.session_state.editing_user_name)
               if st.form_submit_button("更新"):
                   self.update_user(new_name)

   def set_editing_user(self, user):
       st.session_state.editing_user_id = user.id
       st.session_state.editing_user_name = user.name

   def delete_user(self, user_id: int):
       try:
           self.crud.delete(user_id)
           st.success("削除完了")
           st.rerun()
       except Exception as e:
           st.error(f"削除エラー: {e}")

   def update_user(self, new_name: str):
       try:
           self.crud.update(st.session_state.editing_user_id, new_name)
           del st.session_state.editing_user_id
           del st.session_state.editing_user_name
           st.rerun()
       except Exception as e:
           st.error(f"更新エラー: {e}")