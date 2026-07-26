# 🍽️ Brothers Restaurant

A full-stack restaurant web application built with **HTML**, **CSS**, **JavaScript**, and **FastAPI**.

This project demonstrates how a frontend communicates with a backend using REST APIs. The application allows users to view restaurant information through a clean web interface while the FastAPI backend handles CRUD (Create, Read, Update, Delete) operations.

## 🚀 Features

* Responsive restaurant website
* FastAPI REST API
* Complete CRUD operations
* Dynamic frontend using JavaScript Fetch API
* Backend and frontend integration
* Clean and modern UI

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* FastAPI
* Pydantic

## 📂 Project Structure

```
brothers-restaurant/
│
├── Frontend
│   ├── index.html
│   ├── menu.html
│   ├── about.html
│   ├── contact.html
│   ├── style.css
│   └── script.js
│
└── Backend
    ├── app.py
    └── requirements.txt
```

## ⚡ API Endpoints

| Method | Endpoint            | Description            |
| ------ | ------------------- | ---------------------- |
| GET    | `/`                 | Home route             |
| GET    | `/restaurants`      | Get all restaurants    |
| GET    | `/restaurants/{id}` | Get a restaurant by ID |
| POST   | `/restaurants`      | Add a restaurant       |
| PUT    | `/restaurants/{id}` | Update a restaurant    |
| DELETE | `/restaurants/{id}` | Delete a restaurant    |

## ▶️ Running the Project

### Backend

```bash
pip install -r requirements.txt
py -m uvicorn app:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

### Frontend

Open the frontend using Live Server or any local web server and visit:

```
http://127.0.0.1:5500
```

## 🔮 Future Improvements

* SQLite database integration
* User authentication
* Restaurant images
* Search functionality
* Categories and filtering
* Responsive mobile design improvements
* Cloud deployment

## 👨‍💻 Author

**Vedant Sharma**-the coding one 

---

⭐ If you like this project, consider giving it a star.
