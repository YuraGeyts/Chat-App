import React from 'react';

// Display currently connected users
const UserList = ({users}) => {
    return (
        <div>
        <h2>Users</h2>
        <ul>
            {users.map((user, index) => (
            <li key={index}>{user}</li>
            ))}
        </ul>
        </div>
    );
}

export default UserList;