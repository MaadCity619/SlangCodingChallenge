from datetime import datetime
from operator import itemgetter
import Session

class User:
    def __init__(self, userId):
        self.userId = userId
        self.activityList = []
        self.userSessions = []

    def add_activity(self, activity):
        if activity not in self.activityList:
            self.activityList.append(activity)




    def make_sessions(self):
        self.activityList = sorted(self.activityList, key=itemgetter(1))
        i = 0
        current_session_object = None
        while i < len(self.activityList):
            if len(self.userSessions) == 0:
                session = Session.Session(self.activityList[i][1], self.activityList[i][2])
                session.append_act_id(self.activityList[i][0])
                self.userSessions.append(session)
                current_session_object = session
            else:
                current_act = self.activityList[i]
                past_act = self.activityList[i - 1]

                if Session.turn_into_seconds(current_act[1]) - Session.turn_into_seconds(past_act[2]) < 300:
                    current_session_object.append_act_id(self.activityList[i][0])
                    current_session_object.update_end_time(self.activityList[i][2])

                else:
                    session = Session.Session(self.activityList[i][1], self.activityList[i][2])
                    session.append_act_id(self.activityList[i][0])
                    self.userSessions.append(session)
                    current_session_object = session

            i = i + 1
            current_session_object.get_total_session_seconds()