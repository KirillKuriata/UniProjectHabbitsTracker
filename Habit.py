from collections import namedtuple


class Habit:

    def __init__(self, calendarOfCompleting, name, descripition):
        self.calendarOfCompleting = dict(calendarOfCompleting)
        self.name = name
        self.description = descripition


