import React from 'react';

// Renders chat messages; ensures messages is always an array
const MessageList = ({ messages = [] }) => {
  console.log('📦 props in MessageList:', messages);
  return (
    <div style={{ maxHeight: '300px', overflowY: 'auto' }}>
      {messages.map((msg, index) => (
        <div key={index}>
          <strong>{msg.username}:</strong> {msg.text}
        </div>
      ))}
    </div>
  );
};

export default MessageList;
