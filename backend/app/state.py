### chat-backend/app/state.py

# Temporary in-memory storage for connected users
# Maps socket session IDs (sid) to usernames
users = {}

room_messages = {
        'general': [],
        'tech': [],
        'random': []
    }