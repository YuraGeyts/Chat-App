# Realtime Chat App 💬

This is a fullstack realtime chat application built with:

- ⚙️ **Backend**: Python + AsyncIO + Socket.IO (`aiohttp`)
- 🖥 **Frontend**: React + Socket.IO Client
- 📂 **Structure**: `App/` contains both `Backend/` and `frontend/`

---

## 📁 Project Structure

App/ ├── Backend/ # Python backend (socket.io server) │ ├── app/ # Application logic (events, state, server) │ ├── main.py # Entry point │ └── ... # Other files ├── frontend/ # React frontend │ ├── src/ # React components │ └── ... # Other files

---

## 🚀 How to Run

### 🔌 Backend

```bash
cd App/Backend
python -m venv venv
venv\Scripts\activate      # or source venv/bin/activate (Linux/macOS)
pip install -r requirements.txt
python main.py
The backend will run on: http://localhost:5000

💻 Frontend

cd App/frontend
npm install
npm start
The frontend will run on: http://localhost:3000

📡 Features
Realtime chat via WebSockets

Username selection

Message broadcasting

Clean architecture

Easy to expand (user list, rooms, history, etc.)

🛠 Tech Stack
Layer	Technology
Frontend	React, Socket.IO
Backend	Python, aiohttp, Socket.IO
Protocol	WebSocket
📌 TODO (Next Features)
 Show online users

 Add chat rooms

 Style the interface

 Store message history