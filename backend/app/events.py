### chat-backend/app/events.py

from .state import users, room_messages

# This function registers all event handlers with the given socket.io server
def register(sio):

    @sio.event
    async def connect(sid, environ):
        """
        Handle a new client connection.

        Args:
            sid (str): The session ID of the client.
            environ (dict): The environment dictionary containing request information.

        Returns:
            None
        """
        print(f'🔌 Connected: {sid}')
        await sio.enter_room(sid, 'general')

    @sio.event
    async def disconnect(sid):
        """
        Handle the disconnection of a user.

        This function is called when a user disconnects from the server. It removes the user from the
        `users` dictionary and emits a 'user_disconnected' event to notify other connected clients.

        Args:
            sid (str): The session ID of the disconnected user.

        Returns:
            None
        """
        username = users.pop(sid, 'Anonymous')
        print(f'❌ Disconnected: {username} ({sid})')
        await sio.emit('user_list', list(users.values()))

    @sio.event
    async def set_username(sid, data):
        """
        Asynchronously sets the username for a given session ID (sid) and updates the user list.

        Args:
            sid (str): The session ID of the user.
            data (dict): A dictionary containing user data. Expected to have a key 'username'.

        Sets:
            users[sid] (str): The username associated with the session ID. Defaults to 'Anonymous' if not provided.

        Emits:
            'user_list': An event with the updated list of usernames to all connected clients.

        Prints:
            A message indicating the session ID and the set username.
        """
        username = data.get('username', 'Anonymous')
        users[sid] = username
        print(f'👤 {sid} set as {username}')
        await sio.emit('user_list', list(users.values()))

    @sio.event
    async def join_room(sid, room_name):
        """
        Handles a user joining a chat room.
        Args:
            sid (str): The session ID of the user joining the room.
            room_name (str): The name of the chat room to join.
        Functionality:
            - Adds the user to the specified chat room.
            - Logs a message indicating the user has joined the room.
            - Sends the chat history of the room to the user.
            - Broadcasts a message to the room notifying others of the user's arrival.
        """
        sio.enter_room(sid, room_name)
        print(f'🔑 {users.get(sid, "Anonymous")} joined room: {room_name}')
    
        await sio.emit('chat_message', room_messages.get(room_name, []), room=room_name)
    
        await sio.emit('chat_message', {'text': f'User {users.get(sid, "Anonymous")} joined the room'}, room=room_name)

    @sio.event
    async def leave_room(sid, room_name):
        """
        Handles the event of a user leaving a chat room.
        Args:
            sid (str): The session ID of the user leaving the room.
            room_name (str): The name of the room the user is leaving.
        Behavior:
            - Removes the user from the specified room.
            - Logs a message indicating the user has left the room.
            - Sends a notification to the remaining users in the room about the user's departure.
        """
        sio.leave_room(sid, room_name)
        print(f'🚪 {users.get(sid, "Anonymous")} left room: {room_name}')
        
        await sio.emit('chat_message', {'text': f'User {users.get(sid, "Anonymous")} left the room'}, room=room_name)

    @sio.event
    async def chat_message(sid, data):
        """
        Handles a chat message event from a client.
        Args:
            sid (str): The session ID of the client sending the message.
            data (dict): A dictionary containing the message data. Expected keys:
                - 'text' (str): The text of the message (default is an empty string if not provided).
                - 'room' (str): The name of the chat room to send the message to (default is 'general').
        Behavior:
            - Retrieves the username associated with the session ID. Defaults to 'Anonymous' if not found.
            - Constructs a message dictionary containing the username and message text.
            - Adds the message to the specified chat room's message history.
            - Logs the message to the console.
            - Emits the message to all clients in the specified chat room.
        Emits:
            'chat_message': Sends the constructed message to all clients in the specified room.
        """
        username = users.get(sid, 'Anonymous')
        message = {
            'username': username,
            'text': data.get('text', '')
        }
        room = data.get('room', 'general')
        
        room_messages[room].append(message)
    
        print(f'💬 {username}: {message["text"]} in room {room}')
        
        await sio.emit('chat_message', message, room=room)