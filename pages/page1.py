import streamlit as st
from prisma import Prisma
import asyncio

# Prismaインスタンスをグローバルで1つだけ作成
prisma = Prisma()

async def init_prisma():
    if not prisma.is_connected():
        await prisma.connect()

async def create_user(email: str, name: str):
    await prisma.connect()
    try:
        user = await prisma.user.create(
            data={
                'email': email,
                'name': name
            }
        )
        return user
    finally:
        await prisma.disconnect()

async def get_users():
    await prisma.connect()
    try:
        users = await prisma.user.find_many()
        return users
    finally:
        await prisma.disconnect()

async def update_user(user_id: int, new_name: str):
    await prisma.connect()
    try:
        user = await prisma.user.update(
            where={
                'id': user_id
            },
            data={
                'name': new_name
            }
        )
        return user
    finally:
        await prisma.disconnect()

async def delete_user(user_id: int):
    await prisma.connect()
    try:
        await prisma.user.delete(
            where={
                'id': user_id
            }
        )
        return True
    finally:
        await prisma.disconnect()

def main():
    st.title("ユーザー管理システム")

    # Create操作
    with st.form(key='create_user_form'):
        st.subheader("新規ユーザー作成")
        email = st.text_input("メールアドレス")
        name = st.text_input("名前")
        submit = st.form_submit_button("作成")

        if submit and email and name:
            try:
                user = asyncio.run(create_user(email, name))
                st.success(f"ユーザーを作成しました: {user.name}")
            except Exception as e:
                st.error(f"エラー: {str(e)}")
        elif submit:
            st.error("メールアドレスと名前を入力してください")

    # Read & Delete操作
    st.subheader("ユーザー一覧")
    try:
        users = asyncio.run(get_users())
        for user in users:
            col1, col2, col3, col4 = st.columns([2, 2, 1, 1])
            with col1:
                st.write(f"Email: {user.email}")
            with col2:
                st.write(f"Name: {user.name}")
            with col3:
                if st.button("編集", key=f"edit_{user.id}"):
                    st.session_state.editing_user_id = user.id
                    st.session_state.editing_user_name = user.name
            with col4:
                if st.button("削除", key=f"delete_{user.id}"):
                    if asyncio.run(delete_user(user.id)):
                        st.success("ユーザーを削除しました")
                        st.rerun()

        # Update操作（編集モード）
        if 'editing_user_id' in st.session_state:
            st.subheader("ユーザー編集")
            with st.form(key='update_user_form'):
                new_name = st.text_input(
                    "新しい名前", 
                    value=st.session_state.editing_user_name
                )
                update_submit = st.form_submit_button("更新")
                
                if update_submit and new_name:
                    try:
                        user = asyncio.run(update_user(
                            st.session_state.editing_user_id, 
                            new_name
                        ))
                        st.success(f"更新しました: {user.name}")
                        del st.session_state.editing_user_id
                        del st.session_state.editing_user_name
                        st.rerun()
                    except Exception as e:
                        st.error(f"エラー: {str(e)}")

            if st.button("編集をキャンセル"):
                del st.session_state.editing_user_id
                del st.session_state.editing_user_name
                st.rerun()

    except Exception as e:
        st.error(f"データの取得に失敗: {str(e)}")

if __name__ == "__main__":
    main()