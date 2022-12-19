# Samuel William Ramirez Ferris
import json
import requests
import User

Users = []
User_Sessions = []

# O(n)
def is_in_list(var, items):
    for item in items:
        if item.userId == var:
            return True
    return False

# O(n)
def find_item_in_list(var, items):
    for item in items:
        if item.userId == var:
            return item
    return None

activities_response = requests.get("https://api.slangapp.com/challenges/v1/activities",
headers={"Authorization":"Basic MTUxOkFhY1VGcFJiT3pQbGc4Tm9uSmJENGN0bldCbC8veFc5U200SStHY3ZGSmc9"})

# O(n * m)
for activity in activities_response.json()['activities']:
    # Easier Handling
    id = activity['id']
    user_id = activity['user_id']
    answered_at_string = activity['answered_at']
    first_seen_at_string = activity['first_seen_at']

    if is_in_list(user_id, Users):
        currentUser = find_item_in_list(user_id, Users)
        currentUser.add_activity([id, first_seen_at_string, answered_at_string])
    else:
        newUser = User.User(user_id)
        newUser.add_activity([id, first_seen_at_string, answered_at_string])
        Users.append(newUser)


# O(n * m)
for user in Users:
    user.make_sessions()


# O(n * m)
for user in Users:
    temp_list = []
    for Session in user.userSessions:
        temp_list.append(Session.__dict__)

    temp_dict = {user.userId: temp_list}
    User_Sessions.append(temp_dict)

temp_dict = {"user_sessions": User_Sessions}



requests.post("https://api.slangapp.com/challenges/v1/activities/sessions",
headers={"Authorization":"Basic MTUxOkFhY1VGcFJiT3pQbGc4Tm9uSmJENGN0bldCbC8veFc5U200SStHY3ZGSmc9"},
json=temp_dict) 