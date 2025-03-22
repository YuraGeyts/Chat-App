import { io } from 'socket.io-client';

// Connecting to the backend socket
const socket = io('http://localhost:5000', {
    autoConnect: false,
});

export default socket;