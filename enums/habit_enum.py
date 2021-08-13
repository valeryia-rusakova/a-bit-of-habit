from enum import Enum


class HabitType(Enum):
    HEALTHY = 'HEALTHY'
    HELPFUL = 'HELPFUL'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
