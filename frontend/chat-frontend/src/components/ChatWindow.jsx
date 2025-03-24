import React, { useEffect, useState } from 'react';
import socket from '../socket';
import MessageList from './MessageList';
import MessageInput from './MessageInput';
import UserList from './UserList';

const ChatWindow = ({ username }) => {
  const [messages, setMessages] = useState([]);
  const [onlineUsers, setOnlineUsers] = useState([]);

  useEffect(() => {
    // Listen for incoming messages
    socket.on('chat_message', (data) => {
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
    socket.emit('chat_message', { text });
  };

  return (
    <div>
      <h2>Welcome, {username}</h2>
      <UserList users={onlineUsers} />
      <MessageList messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};

export default ChatWindow;
