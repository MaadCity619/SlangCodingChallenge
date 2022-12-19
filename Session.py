from datetime import datetime
from dateutil import parser

epoch_time = datetime(1970, 1, 1)

#O(1)
def turn_into_seconds(date_string):
    final_date = parser.parse(date_string)
    delta = (final_date.replace(tzinfo=None) - epoch_time.replace(tzinfo=None))
    final_date = delta.total_seconds()
    return final_date


class Session:
    def __init__(self, started_at_string, ended_at_string):
        self.ended_at = ended_at_string
        self.started_at = started_at_string
        self.activity_ids = []
        self.duration_seconds = None

    # O(1)
    def update_end_time(self, endTime):
        self.ended_at = endTime

    # O(1)
    def update_start_time(self, startTime):
        self.started_at = startTime

    # O(1)
    def append_act_id(self, actId):
        self.activity_ids.append(actId)

    # O(1)
    def get_total_session_seconds(self):
        self.duration_seconds = (turn_into_seconds(self.ended_at) - turn_into_seconds(self.started_at))
