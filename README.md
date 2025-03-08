# 🗓️ AI-Powered Smart Calendar Backend

This is the **backend** for the AI-Powered Smart Calendar Assistant, built with **FastAPI**.  
It provides **user authentication, event management, and AI-powered smart scheduling** using **PostgreSQL/SQLite, Redis, and machine learning**.

---

## 🚀 Features

✅ **User Authentication** (Register & Login with JWT)  
✅ **CRUD Operations for Events**  
✅ **AI-Powered Smart Scheduling** (Suggests best meeting times)  
✅ **Optimized Performance** (Redis caching for API speedup)  
✅ **Database Integration** (PostgreSQL / SQLite with Alembic migrations)  

---

## 🏗️ Tech Stack

- **Backend:** FastAPI (Python)  
- **Database:** PostgreSQL / SQLite (SQLAlchemy ORM)  
- **Cache:** Redis  
- **Authentication:** JWT (JSON Web Token)  
- **AI:** Machine Learning for Smart Scheduling  
- **Deployment:** AWS (EC2 / Render)  

---

## ⚙️ Installation & Setup

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/ai_calendar_backend.git
cd ai_calendar_backend
2️⃣ Create a Virtual Environment
sh
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
4️⃣ Set Up Environment Variables
Create a .env file in the project root and add:

ini
Copy
Edit
DATABASE_URL=sqlite:///./calendar.db  # Change to PostgreSQL if needed
SECRET_KEY=your_secret_key
REDIS_URL=redis://localhost:6379/0
5️⃣ Run Database Migrations
sh
Copy
Edit
alembic upgrade head
6️⃣ Start the Backend Server
sh
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
Backend will be available at: http://127.0.0.1:8000

📌 API Endpoints
🛠️ Authentication
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	Login & get JWT token
📅 Event Management
Method	Endpoint	Description
POST	/events/create/	Create a new event
GET	/events/user/{user_id}	Get all events for a user
PUT	/events/update/{event_id}	Update an event
DELETE	/events/delete/{event_id}	Delete an event
🤖 AI-Powered Smart Scheduling
Method	Endpoint	Description
GET	/scheduling/smart_suggest_meeting/	Get AI-suggested meeting time
✅ Testing API with Swagger or Postman
Open Swagger UI:
👉 http://127.0.0.1:8000/docs
Test endpoints interactively!
Or use Postman to send requests.
📌 Project Structure
bash
Copy
Edit
ai_calendar_backend/
│── migrations/            # Alembic migration files
│── models/                # Database models
│   ├── user.py            # User authentication models
│   ├── event.py           # Event scheduling models
│── routes/                # API endpoints
│   ├── auth.py            # Authentication APIs
│   ├── events.py          # Event management APIs
│   ├── scheduling.py      # AI-powered scheduling APIs
│── services/              # Business logic
│   ├── database.py        # Database connection
│   ├── redis_cache.py     # Redis caching logic
│   ├── scheduler.py       # AI scheduling logic
│── config.py              # Configuration & environment variables
│── main.py                # FastAPI entry point
│── requirements.txt       # Dependencies
│── alembic.ini            # Alembic migration config
│── .env                   # Environment variables
│── README.md              # Project documentation
🔥 Contributing
Want to improve the project? Follow these steps:

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m "Added new feature")
Push to GitHub (git push origin feature-branch)
Create a Pull Request 🚀
🔥 Contributors
👤 Souvik Ghosh - https://github.com/souvikDevloper

📜 License
This project is licensed under the MIT License.

🚀 Now Push This README to GitHub
sh
Copy
Edit
git add README.md
git commit -m "Added README"
git push origin main