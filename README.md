🔐 Flask JWT Authentication with SQLite & Session Timeout

📌 Project Overview

This project is a secure authentication system built using Flask, SQLite3, and JSON Web Tokens (JWT). It provides user registration and login functionality with password hashing, JWT-based authentication, cookie-based token storage, and automatic session timeout for inactive users. The application demonstrates how to build a secure login system without relying on server-side authentication sessions.

🚀 Features

User Registration
User Login Authentication
Password Hashing using Werkzeug
JWT Token Generation & Verification
Cookie-Based Authentication
SQLite3 Database Integration
Automatic Session Timeout (Idle Logout)
Secure Logout Functionality
Server-Side Form Validation
Simple HTML Templates using Flask render_template

🛠️ Technologies Used

Python
Flask
SQLite3
PyJWT
Werkzeug Security
HTML5
Jinja2 Templates

📂 Project Structure

flask-jwt-auth-sqlite-session-timeout/
│
├── app.py                    # Main Flask Application
├── config.py                 # Configuration (Optional)
├── requirements.txt          # Project Dependencies
├── README.md
├── .gitignore
├── pythonjwt.db
│
├── static/
│   ├── css/
│   │   ├── auth.css
│   │   ├── dashboard.css
│   │   └── style.css
│   │
│   ├── js/
│   │   └── session_timeout.js
│   │
│   └── images/
│       ├── logo.png
│       └── background.jpg
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
│
└── screenshots/
    ├── login.png
    ├── register.png
    └── dashboard.png

🔄 Application Workflow

User registers with a username and password.
Password is securely hashed before storing it in SQLite.
User logs in with valid credentials.
Flask verifies the password hash.
A JWT token is generated upon successful authentication.
The token is stored securely in a browser cookie.
Protected pages verify the JWT before granting access.
If the user remains inactive beyond the configured timeout, the session expires and the user is redirected to the login page.
Logout removes the JWT cookie and clears the session.

🎯 Learning Outcomes
This project demonstrates:

JWT Authentication in Flask
Secure Password Hashing
Cookie-Based Authentication
Session Timeout Management
SQLite3 CRUD Operations
Flask Routing & Templates
Secure User Authentication Best Practices

📜 License

This project is created for learning and educational purposes and can be extended with features such as role-based authentication, email verification, refresh tokens, password reset, and database migration.
