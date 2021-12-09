from project.dal.achievement import AchievementDAL
from project.dal.achievement_user import AchievementUserDAL
from project.dal.habit import HabitDAL


class AchievementUserController:
    dal = AchievementUserDAL()

    def get_user_achievements(self, user):
        return self.dal.get_user_achievements(user)

    def create_achievement_user(self, days_checked, habit, user):
        achievement = AchievementDAL.get_achievement_by_amount_to_reach(days_checked)
        habit = HabitDAL.retrieve_habit(habit)
        description = f"You’ve been keeping {habit.name} for {achievement.amount_to_reach} days"
        data = {
            'user': user,
            'achievement': achievement,
            'description': description
        }
        self.dal.insert_user_achievement(data)
