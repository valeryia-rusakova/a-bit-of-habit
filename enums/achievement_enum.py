from enum import Enum


class AchievementLevel(Enum):
    WOODEN = "WOODEN"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
