from datetime import datetime
from operator import itemgetter

class User:
    def __init__(self, userId):
        self.userId = userId
        self.activityList = []
        self.userSessions = []

    def add_activity(self, activity):
        if activity not in self.activityList:
            self.activityList.append(activity)
