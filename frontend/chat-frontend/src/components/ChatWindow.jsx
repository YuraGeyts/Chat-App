import React, { useEffect, useState } from 'react';
import socket from '../socket';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import UserList from './UserList';

const ChatWindow = ({ username }) => {
  const [messages, setMessages] = useState([]);
  const [onlineUsers, setOnlineUsers] = useState([]);
  const [currentRoom, setCurrentRoom] = useState('general'); // Default room

  useEffect(() => {
    // Listen for incoming messages
    socket.on('chat_message', (data) => {
      console.log('Received message:', data);
      setMessages((prev) => [...prev, data]);
    });

    // Listen for updated user list
    socket.on('user_list', (data) => {
      setOnlineUsers(data);
    });

    // Cleanup on unmount
    return () => {
      socket.off('chat_message');
      socket.off('user_list');
    };
  }, []);

  const sendMessage = (text) => {
    socket.emit('chat_message', { text, room: currentRoom });
  };

  const joinRoom = (roomName) => {
    if (roomName !== currentRoom) {
      socket.emit('leave_room', currentRoom);  // Leave the previous room
      socket.emit('join_room', roomName);      // Join the new room
      setMessages([]);                          // Clear messages when changing rooms
      setCurrentRoom(roomName);
    }
  };

  return (
    <div>
      <h2>Welcome, {username}</h2>
      <UserList users={onlineUsers} />
      <div>
        <h3>Rooms:</h3>
        <button onClick={() => joinRoom('general')}>General</button>
        <button onClick={() => joinRoom('random')}>Random</button>
        <button onClick={() => joinRoom('news')}>News</button>
      </div>
      <MessageList messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};

export default ChatWindow;
