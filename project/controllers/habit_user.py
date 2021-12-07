import datetime

from project.dal.habit import HabitDAL
from project.dal.habit_user import HabitUserDAL


class HabitUserController:
    dal = HabitUserDAL()

    def create_habit_user(self, request):
        habit_id = request.data['habitId']
        user = request.user
        habits_users_list = self.dal.get_habits_users_list(user)
        habit_id_list = habits_users_list.values_list('habit', flat=True)
        if habit_id in habit_id_list:
            return {"Fail": "You’ve already added this habit"}
        habit_instance = HabitDAL.retrieve_habit(habit_id)
        data = {
            'user': request.user,
            'days_checked': 0,
            'habit': habit_instance
        }
        return self.dal.insert_habit_user(data)

    def get_habits_users(self, user):
        return self.dal.get_habits_users_list(user)

    def get_filtered_habits_list(self, habits_id_list):
        return self.dal.get_filtered_habits_list(habits_id_list)

    def daily_check(self, request):
        habit_user = self.dal.get_habit_user(habit=request.data['habitId'], user=request.user)
        if (habit_user.updated_at == habit_user.created_at and habit_user.days_checked == 1) \
                or (habit_user.updated_at + datetime.timedelta(hours=3)).date() == datetime.datetime.today().date():
            return {"Fail": "You’ve already checked-in today"}
        return self.dal.daily_check(habit_user)
