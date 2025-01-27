import streamlit as st
from src.database.db import SessionLocal
from src.services import UserCRAD

class ProfileUI:
    def __init__(self):
        self.crad = UserCRAD(SessionLocal())

    def has_users(self) -> bool:
        # ユーザーが存在するかどうかを確認
        return len(self.crad.get_all()) > 0

    def create_profile_form(self):
        with st.form("ユーザプロフィール"):
            name = st.text_input(
                "名前"
            )

            col1, col2, col3 = st.columns(3)
            with col1:
                chest_press_weight = st.number_input(
                    f"チェストプレス（kg）",
                    min_value=0,
                    value=0,
                    step=5
                    )
                total_abdominal_weight = st.number_input(
                    f"トータルアブドミナル（kg）",
                    min_value=0,
                    value=0,
                    step=5
                    )
            with col2:
                lat_pulldown_weight = st.number_input(
                    f"ラットプルダウン（kg）",
                    min_value=0,
                    value=0,
                    step=5
                    )
                rotary_torso_weight = st.number_input(
                    f"ロータリートルソー（kg）",
                    min_value=0,
                    value=0,
                    step=5
                    )
            with col3:
                leg_press_weight = st.number_input(
                    f"レッグプレス（kg）",
                    min_value=0,
                    value=0,
                    step=5
                    )

            if st.form_submit_button("作成") and name:
                try:
                    user = self.crad.create(
                        name,
                        chest_press_weight,
                        total_abdominal_weight,
                        lat_pulldown_weight,
                        rotary_torso_weight,
                        leg_press_weight
                        )
                    st.success(f"作成成功: {user.name}")
                except Exception as e:
                    st.error(f"エラー：{e}")

    def profile_list(self):
        for user in self.crad.get_all():
            self.user_row(user)

    def user_row(self, user):
        st.subheader(f"👤 {user.name}")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("チェストプレス", f"{user.chest_press_weight} kg")
            st.metric("トータルアブドミナル", f"{user.total_abdominal_weight} kg")
        with col2:
            st.metric("ラットプルダウン", f"{user.lat_pulldown_weight} kg")
            st.metric("ロータリートルソー", f"{user.rotary_torso_weight} kg")
        with col3:
            st.metric("レッグプレス", f"{user.leg_press_weight} kg")

        # ボタンを横並びに配置
        btn_col1, btn_col2, *_ = st.columns([1, 1, 4])  # 残りのスペースは空けておく
        with btn_col1:
            if st.button("📝 編集", key=f"edit_{user.id}"):
                self.set_editing_user(user)
        # with btn_col2:
        #     if st.button("🗑️ 削除", key=f"delete_{user.id}"):
        #         self.delete_user(user.id)
    
    def delete_user(self, user_id: int):
        try:
            self.crad.delete(user_id)
            st.success("削除完了")
            st.rerun()
        except Exception as e:
            st.error(f"削除エラー： {e}")

    def edit_form(self):
        if 'editing_user_id' in st.session_state:
            with st.form("ユーザー編集"):
                new_name = st.text_input(
                    "名前", 
                    st.session_state.editing_user_name
                )

                col1, col2, col3 = st.columns(3)
                with col1:
                    new_chest_press = st.number_input(
                        f"チェストプレス（kg）",
                        min_value=0,
                        value=st.session_state.editing_user_chest_press,
                        step=5
                    )
                    new_total_abdominal = st.number_input(
                        f"トータルアブドミナル（kg）",
                        min_value=0,
                        value=st.session_state.editing_user_total_abdominal,
                        step=5
                    )
                with col2:
                    new_lat_pulldown = st.number_input(
                        f"ラットプルダウン（kg）",
                        min_value=0,
                        value=st.session_state.editing_user_lat_pulldown,
                        step=5
                    )
                    new_rotary_torso = st.number_input(
                        f"ロータリートルソー（kg）",
                        min_value=0,
                        value=st.session_state.editing_user_rotary_torso,
                        step=5
                    )
                with col3:
                    new_leg_press = st.number_input(
                        f"レッグプレス（kg）",
                        min_value=0,
                        value=st.session_state.editing_user_leg_press,
                        step=5
                    )

                if st.form_submit_button("更新"):
                    self.update_user(
                        new_name,
                        new_chest_press,
                        new_total_abdominal,
                        new_lat_pulldown,
                        new_rotary_torso,
                        new_leg_press
                    )

    def set_editing_user(self, user):
        st.session_state.editing_user_id = user.id
        st.session_state.editing_user_name = user.name
        st.session_state.editing_user_chest_press = user.chest_press_weight
        st.session_state.editing_user_total_abdominal = user.total_abdominal_weight
        st.session_state.editing_user_lat_pulldown = user.lat_pulldown_weight
        st.session_state.editing_user_rotary_torso = user.rotary_torso_weight
        st.session_state.editing_user_leg_press = user.leg_press_weight

    def update_user(self, new_name: str, new_chest_press: float, new_total_abdominal: float,
                   new_lat_pulldown: float, new_rotary_torso: float, new_leg_press: float):
        try:
            self.crad.update(
                st.session_state.editing_user_id,
                new_name,
                new_chest_press,
                new_total_abdominal,
                new_lat_pulldown,
                new_rotary_torso,
                new_leg_press
            )
            for key in list(st.session_state.keys()):
                if key.startswith('editing_user_'):
                    del st.session_state[key]
            st.rerun()
        except Exception as e:
            st.error(f"更新エラー： {e}")