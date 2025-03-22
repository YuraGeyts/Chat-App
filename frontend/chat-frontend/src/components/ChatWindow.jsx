import React, { useEffect, useState } from 'react';
import socket from '../socket';
import MessageList from './MessageList';
import MessageInput from './MessageInput';

const ChatWindow = ({ username }) => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    // Listen for incoming messages
    socket.on('chat_message', (data) => {
      setMessages((prev) => [...prev, data]);
    });

    // Cleanup on unmount
    return () => {
      socket.off('chat_message');
    };
  }, []);

  const sendMessage = (text) => {
    // Emit the message to the server
    socket.emit('chat_message', { text });
  };

  console.log('💡 messages:', messages);

  return (
    <div>
      <h2>Welcome, {username}</h2>
      <MessageList messages={messages} />
      <MessageInput onSend={sendMessage} />
    </div>
  );
};

export default ChatWindow;
