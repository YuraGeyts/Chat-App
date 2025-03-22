import React, { useState } from 'react';
import socket from './socket';
import UsernameForm from './components/UsernameForm';
import ChatWindow from './components/ChatWindow';

function App() {
  const [username, setUsername] = useState('');
  const [connected, setConnected] = useState(false);

  const handleUsernameSubmit = (name) => {
    setUsername(name);

    // Connect to the socket server
    socket.connect();

    // Send username to server
    socket.emit('set_username', { username: name });

    setConnected(true);
  };

  return (
    <div className="App">
      {!connected ? (
        <UsernameForm onSubmit={handleUsernameSubmit} />
      ) : (
        <ChatWindow username={username} />
      )}
    </div>
  );
}

export default App;
