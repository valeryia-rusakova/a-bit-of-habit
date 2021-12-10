from enum import Enum


class AchievementLevel(Enum):
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


class HabitType(Enum):
    HEALTHY = 'HEALTHY'
    HELPFUL = 'HELPFUL'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
