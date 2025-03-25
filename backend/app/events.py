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
    async def chat_message(sid, data):
        """
        Handle an incoming chat message event.

        Args:
            sid (str): The session ID of the user sending the message.
            data (dict): The data payload containing the message text.

        Returns:
            None
        """
        username = users.get(sid, 'Anonymous')
        message = {
            'username': username,
            'text': data.get('text', '')
        }
        room = data.get('room', 'general')

        room_messages[room].append(message)
        print(f'💬 {username}: {message["text"]}') 
        await sio.emit('chat_message', message, room=room)

    @sio.event
    async def join_room(sid, room_name):
        sio.enter_room(sid, room_name)
        print(f'🚪 {users.get(sid, 'Anonymous')} joined room: {room_name}')
        await sio.emit('chat_message', {'text': f'User {users.get(sid, "Anonymous")} joined the room'}, room=room_name)

    @sio.event
    async def leave_room(sid, room_name):
        sio.leave_room(sid, room_name)
        print(f'🚪 {users.get(sid, "Anonymous")} left room: {room_name}')
        await sio.emit('chat_message', {'text': f'User {users.get(sid, "Anonymous")} left the room'}, room=room_name)

