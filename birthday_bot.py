import requests
import time

# Define a list of users with channel_id, username, and birthdate
user_list = [
    {"channel_id": "---", "username": "---", "birthdate": "01-01"},
    {"channel_id": ""---",", "username": ""---",", "birthdate": "02-02"}
]

# Your Discord API authorization token
authorization_token = "NDgyMjIwOTMyODk5OTMwMTEy.G4LZ2v.H7-aYtfP23OTt5kJbk4TID-8Gb2GsghODpoka8"


# Function to send a birthday message
def send_birthday_message(channel_id, username):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    payload = {"content": f"Happy Birthday {username} 🎉 | (only a test for my script)"}
    headers = {"authorization": authorization_token}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print(f"Sent Birthday Message to {username}")
    else:
        print(f"Failed to send Birthday Message to {username}")


# Function to check and send birthday messages
def check_and_send_birthday_messages():
    current_date = time.strftime("%m-%d")
    for user in user_list:
        if user["birthdate"] == current_date:
            send_birthday_message(user["channel_id"], user["username"])


# Set the timer to check for birthdays once a day (adjust as needed)
while True:
    check_and_send_birthday_messages()
    time.sleep(86400)  # 86400 seconds in a day
