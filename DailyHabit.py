from Habit import Habit


class DailyHabit(Habit):

    def __init__(self, name, descripition, isComplited):
        super().__init__(self, name, descripition)
        self.isComplited = dict(isComplited)

    def setComplited(self):
        isComplited
