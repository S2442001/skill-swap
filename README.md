# skill-swap
Skill Swap – A Flask Application for Skill Exchange

# Description

A web application where users can register, login, and add skills they want to offer or request. The dashboard automatically matches users who can teach or learn each other’s skills.

# Features

User registration and login (Flask-Login)
Add skills as offered or requested
Dashboard shows matches between users
Many-to-many relationship between Users and Skills
PostgreSQL database backend
Password hashing for secure login

# Usage

Register as a new user
Add skills you want to offer or request
Check dashboard for matches

# Note
Create a .env:
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://username:password@localhost/skill_swap_db

# Tech Stack

Python 3.x
Flask
Flask-WTF
Flask-Login
SQLAlchemy
PostgreSQL
Pandas

# Screenshots

### Register
![Register](screenshots/Register.png)

### Login
![Login](screenshots/Login.png)

### Add Skill
![Add Skill](screenshots/Add_skill.png)

### Dashboard
![Dashboard](screenshots/Dashboard.png)


# Future Improvements

Real-time notifications (WebSockets)
Email notifications
Skill categories
