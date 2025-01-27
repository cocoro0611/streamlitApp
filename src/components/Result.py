import streamlit as st
from datetime import datetime
from src.database.db import SessionLocal
from src.services import ExerciseResultCRAD

class ExerciseResultUI:
    def __init__(self, user_id: int):
        self.crad = ExerciseResultCRAD(SessionLocal())
        self.user_id = user_id

    def create_exercise_form(self):
        with st.form("運動記録"):
            date = st.date_input(
                "日付",
                value=datetime.now()
            )

            col1, col2 = st.columns(2)
            with col1:
                running_distance = st.number_input(
                    "ランニング距離（m）",
                    min_value=0,
                    value=0,
                    step=100
                )
                swimming_distance = st.number_input(
                    "水泳距離（m）",
                    min_value=0,
                    value=0,
                    step=100
                )

            col1, col2, col3 = st.columns(3)
            with col1:
                chest_press_count = st.number_input(
                    "チェストプレス（回）",
                    min_value=0,
                    value=0,
                    step=1
                )
                total_abdominal_count = st.number_input(
                    "トータルアブドミナル（回）",
                    min_value=0,
                    value=0,
                    step=1
                )
            with col2:
                lat_pulldown_count = st.number_input(
                    "ラットプルダウン（回）",
                    min_value=0,
                    value=0,
                    step=1
                )
                rotary_torso_count = st.number_input(
                    "ロータリートルソー（回）",
                    min_value=0,
                    value=0,
                    step=1
                )
            with col3:
                leg_press_count = st.number_input(
                    "レッグプレス（回）",
                    min_value=0,
                    value=0,
                    step=1
                )

            if st.form_submit_button("記録"):
                try:
                    result = self.crad.create(
                        self.user_id,
                        datetime.combine(date, datetime.min.time()),
                        running_distance,
                        swimming_distance,
                        chest_press_count,
                        lat_pulldown_count,
                        leg_press_count,
                        total_abdominal_count,
                        rotary_torso_count
                    )
                    st.success(f"記録完了: {result.date.strftime('%Y-%m-%d')}")
                except Exception as e:
                    st.error(f"エラー：{e}")

    def exercise_list(self):
        results = self.crad.get_by_user(self.user_id)
        for result in results:
            self.exercise_row(result)
            st.divider()

    def exercise_row(self, result):
        st.subheader(f"📅 {result.date.strftime('%Y-%m-%d')}")
        
        # 有酸素運動
        st.write("🏃‍♂️ 有酸素運動")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ランニング", f"{result.running_distance} m")
        with col2:
            st.metric("水泳", f"{result.swimming_distance} m")

        # マシントレーニング
        st.write("💪 マシントレーニング")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("チェストプレス", f"{result.chest_press_count} 回")
            st.metric("トータルアブドミナル", f"{result.total_abdominal_count} 回")
        with col2:
            st.metric("ラットプルダウン", f"{result.lat_pulldown_count} 回")
            st.metric("ロータリートルソー", f"{result.rotary_torso_count} 回")
        with col3:
            st.metric("レッグプレス", f"{result.leg_press_count} 回")

        # ボタン
        btn_col1, btn_col2, *_ = st.columns([1, 1, 4])
        with btn_col1:
            if st.button("📝 編集", key=f"edit_{result.id}"):
                self.set_editing_result(result)
        with btn_col2:
            if st.button("🗑️ 削除", key=f"delete_{result.id}"):
                self.delete_result(result.id)

    def delete_result(self, result_id: int):
        try:
            self.crad.delete(result_id)
            st.success("削除完了")
            st.rerun()
        except Exception as e:
            st.error(f"削除エラー： {e}")

    def edit_form(self):
        if 'editing_result_id' in st.session_state:
            with st.form("運動記録編集"):
                date = st.date_input(
                    "日付",
                    value=st.session_state.editing_result_date
                )

                col1, col2 = st.columns(2)
                with col1:
                    running_distance = st.number_input(
                        "ランニング距離（m）",
                        min_value=0,
                        value=st.session_state.editing_result_running,
                        step=100
                    )
                    swimming_distance = st.number_input(
                        "水泳距離（m）",
                        min_value=0,
                        value=st.session_state.editing_result_swimming,
                        step=100
                    )

                col1, col2, col3 = st.columns(3)
                with col1:
                    chest_press_count = st.number_input(
                        "チェストプレス（回）",
                        min_value=0,
                        value=st.session_state.editing_result_chest_press,
                        step=1
                    )
                    total_abdominal_count = st.number_input(
                        "トータルアブドミナル（回）",
                        min_value=0,
                        value=st.session_state.editing_result_total_abdominal,
                        step=1
                    )
                with col2:
                    lat_pulldown_count = st.number_input(
                        "ラットプルダウン（回）",
                        min_value=0,
                        value=st.session_state.editing_result_lat_pulldown,
                        step=1
                    )
                    rotary_torso_count = st.number_input(
                        "ロータリートルソー（回）",
                        min_value=0,
                        value=st.session_state.editing_result_rotary_torso,
                        step=1
                    )
                with col3:
                    leg_press_count = st.number_input(
                        "レッグプレス（回）",
                        min_value=0,
                        value=st.session_state.editing_result_leg_press,
                        step=1
                    )

                if st.form_submit_button("更新"):
                    self.update_result(
                        date,
                        running_distance,
                        swimming_distance,
                        chest_press_count,
                        lat_pulldown_count,
                        leg_press_count,
                        total_abdominal_count,
                        rotary_torso_count
                    )

    def set_editing_result(self, result):
        st.session_state.editing_result_id = result.id
        st.session_state.editing_result_date = result.date
        st.session_state.editing_result_running = result.running_distance
        st.session_state.editing_result_swimming = result.swimming_distance
        st.session_state.editing_result_chest_press = result.chest_press_count
        st.session_state.editing_result_lat_pulldown = result.lat_pulldown_count
        st.session_state.editing_result_leg_press = result.leg_press_count
        st.session_state.editing_result_total_abdominal = result.total_abdominal_count
        st.session_state.editing_result_rotary_torso = result.rotary_torso_count

    def update_result(
            self,
            date: datetime,
            running_distance: int,
            swimming_distance: int,
            chest_press_count: int,
            lat_pulldown_count: int,
            leg_press_count: int,
            total_abdominal_count: int,
            rotary_torso_count: int
        ):
        try:
            self.crad.update(
                st.session_state.editing_result_id,
                running_distance=running_distance,
                swimming_distance=swimming_distance,
                chest_press_count=chest_press_count,
                lat_pulldown_count=lat_pulldown_count,
                leg_press_count=leg_press_count,
                total_abdominal_count=total_abdominal_count,
                rotary_torso_count=rotary_torso_count,
                date=datetime.combine(date, datetime.min.time())
            )
            # 編集状態をクリア
            for key in list(st.session_state.keys()):
                if key.startswith('editing_result_'):
                    del st.session_state[key]
            st.rerun()
        except Exception as e:
            st.error(f"更新エラー： {e}")