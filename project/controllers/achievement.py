from project.dal.achievement import AchievementDAL


class AchievementController:
    dal = AchievementDAL()

    def get_achievement_queryset(self):
        return self.dal.get_achievements_list()
