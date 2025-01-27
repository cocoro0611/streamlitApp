from sqlalchemy.orm import Session
from datetime import datetime
from src.database.models import ExerciseResult

class ExerciseResultCRAD:
    def __init__(self, db: Session):
        self.db = db

    def create(
            self,
            user_id: int,
            date: datetime,
            running_distance: int = 0,
            swimming_distance: int = 0,
            chest_press_count: int = 0,
            lat_pulldown_count: int = 0,
            leg_press_count: int = 0,
            total_abdominal_count: int = 0,
            rotary_torso_count: int = 0
            ):
        """運動記録を作成"""
        exercise_result = ExerciseResult(
            user_id=user_id,
            date=date,
            running_distance=running_distance,
            swimming_distance=swimming_distance,
            chest_press_count=chest_press_count,
            lat_pulldown_count=lat_pulldown_count,
            leg_press_count=leg_press_count,
            total_abdominal_count=total_abdominal_count,
            rotary_torso_count=rotary_torso_count
        )
        self.db.add(exercise_result)
        self.db.commit()
        self.db.refresh(exercise_result)
        return exercise_result

    def get_all(self):
        """全ての運動記録を取得"""
        return self.db.query(ExerciseResult).all()

    def get_by_user(self, user_id: int):
        """特定ユーザーの全運動記録を取得"""
        return self.db.query(ExerciseResult)\
            .filter(ExerciseResult.user_id == user_id)\
            .order_by(ExerciseResult.date.desc())\
            .all()

    def get_by_date_range(self, user_id: int, start_date: datetime, end_date: datetime):
        """特定ユーザーの日付範囲内の運動記録を取得"""
        return self.db.query(ExerciseResult)\
            .filter(
                ExerciseResult.user_id == user_id,
                ExerciseResult.date >= start_date,
                ExerciseResult.date <= end_date
            )\
            .order_by(ExerciseResult.date.desc())\
            .all()

    def get_by_id(self, result_id: int):
        """IDで運動記録を取得"""
        return self.db.query(ExerciseResult)\
            .filter(ExerciseResult.id == result_id)\
            .first()

    def update(
            self,
            result_id: int,
            running_distance: int = None,
            swimming_distance: int = None,
            chest_press_count: int = None,
            lat_pulldown_count: int = None,
            leg_press_count: int = None,
            total_abdominal_count: int = None,
            rotary_torso_count: int = None,
            date: datetime = None
            ):
        """運動記録を更新"""
        result = self.db.query(ExerciseResult)\
            .filter(ExerciseResult.id == result_id)\
            .first()
        
        if result:
            if running_distance is not None:
                result.running_distance = running_distance
            if swimming_distance is not None:
                result.swimming_distance = swimming_distance
            if chest_press_count is not None:
                result.chest_press_count = chest_press_count
            if lat_pulldown_count is not None:
                result.lat_pulldown_count = lat_pulldown_count
            if leg_press_count is not None:
                result.leg_press_count = leg_press_count
            if total_abdominal_count is not None:
                result.total_abdominal_count = total_abdominal_count
            if rotary_torso_count is not None:
                result.rotary_torso_count = rotary_torso_count
            if date is not None:
                result.date = date

            self.db.commit()
            self.db.refresh(result)
        return result

    def delete(self, result_id: int):
        """運動記録を削除"""
        result = self.db.query(ExerciseResult)\
            .filter(ExerciseResult.id == result_id)\
            .first()
        if result:
            self.db.delete(result)
            self.db.commit()
            return True
        return False

    def delete_by_user(self, user_id: int):
        """ユーザーの全運動記録を削除"""
        results = self.db.query(ExerciseResult)\
            .filter(ExerciseResult.user_id == user_id)\
            .all()
        for result in results:
            self.db.delete(result)
        self.db.commit()
        return True