from project.dal.achievement_user import AchievementUserDAL


class AchievementUserController:
    dal = AchievementUserDAL()

    def get_user_achievements(self, user):
        return self.dal.get_user_achievements(user)
