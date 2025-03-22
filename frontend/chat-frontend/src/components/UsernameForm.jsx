import React, { useState } from 'react';

const UsernameForm = ({ onSubmit }) => {
  const [name, setName] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name.trim()) {
      onSubmit(name.trim());
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Enter your username</h2>
      <input
        type="text"
        placeholder="Your name..."
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <button type="submit">Join Chat</button>
    </form>
  );
};

export default UsernameForm;
