# 🚀 Todo API v1

[![Deploy Status](https://img.shields.io/badge/deploy-live-brightgreen)](https://todo-api-v1-pugr.onrender.com)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)

A production-ready REST API for managing todos, built with FastAPI and deployed on the cloud.

## 🔗 Quick Links

- **🌐 Live API**: https://todo-api-v1-pugr.onrender.com
- **📚 API Documentation**: https://todo-api-v1-pugr.onrender.com/docs
- **📁 Source Code**: https://github.com/HARDIK-WEB-OSS/todo-api-v1

> **⚠️ Note**: Deployed on Render free tier. The first request after 15 minutes of inactivity may take 30-60 seconds as the server spins up from sleep mode.

---

## ✨ Features

- ✅ **Full CRUD Operations** - Create, Read, Update, Delete todos
- ✅ **RESTful Design** - Proper HTTP methods and status codes
- ✅ **Interactive Documentation** - Auto-generated Swagger UI
- ✅ **Data Persistence** - SQLite database with SQLAlchemy ORM
- ✅ **Input Validation** - Pydantic models for request/response validation
- ✅ **Statistics Endpoint** - Track completion rates
- ✅ **Toggle Completion** - Quick status updates
- ✅ **Production Deployment** - Live on Render cloud platform

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **FastAPI** | Modern Python web framework for building APIs |
| **SQLAlchemy** | SQL toolkit and Object-Relational Mapping (ORM) |
| **Pydantic** | Data validation using Python type annotations |
| **SQLite** | Lightweight, serverless database |
| **Uvicorn** | Lightning-fast ASGI server |
| **Render** | Cloud platform for deployment |

---

## 📋 API Endpoints

### Root
- `GET /` - API information and available endpoints

### Todos
- `POST /todos` - Create a new todo
- `GET /todos` - Get all todos (supports pagination)
- `GET /todos/{id}` - Get a specific todo by ID
- `PUT /todos/{id}` - Update a todo
- `DELETE /todos/{id}` - Delete a todo
- `PATCH /todos/{id}/toggle` - Toggle todo completion status

### Statistics
- `GET /stats` - Get todo statistics (total, completed, pending, completion rate)

**Full interactive documentation available at**: https://todo-api-v1-pugr.onrender.com/docs

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Setup

```bash
# Clone the repository
git clone https://github.com/HARDIK-WEB-OSS/todo-api-v1.git
cd todo-api-v1

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Server will start at: **http://localhost:8000**

Interactive docs at: **http://localhost:8000/docs**

---

## 📖 Usage Examples

### Create a Todo

```bash
curl -X POST "https://todo-api-v1-pugr.onrender.com/todos" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Learn FastAPI",
    "description": "Build a REST API with FastAPI"
  }'
```

**Response:**
```json
{
  "id": 1,
  "title": "Learn FastAPI",
  "description": "Build a REST API with FastAPI",
  "completed": false,
  "created_at": "2026-01-15T10:30:00"
}
```

### Get All Todos

```bash
curl "https://todo-api-v1-pugr.onrender.com/todos"
```

### Update a Todo

```bash
curl -X PUT "https://todo-api-v1-pugr.onrender.com/todos/1" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Master FastAPI",
    "completed": true
  }'
```

### Toggle Completion

```bash
curl -X PATCH "https://todo-api-v1-pugr.onrender.com/todos/1/toggle"
```

### Get Statistics

```bash
curl "https://todo-api-v1-pugr.onrender.com/stats"
```

**Response:**
```json
{
  "total": 10,
  "completed": 7,
  "pending": 3,
  "completion_rate": 70.0
}
```

---

## 📁 Project Structure

```
todo-api-v1/
├── main.py              # FastAPI application and routes
├── models.py            # SQLAlchemy database models
├── database.py          # Database configuration
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

---

## 🧪 Testing

### Using the Interactive Docs

1. Visit https://todo-api-v1-pugr.onrender.com/docs
2. Click on any endpoint
3. Click "Try it out"
4. Fill in the parameters
5. Click "Execute"
6. See the response below

### Using cURL (Command Line)

```bash
# Create a todo
curl -X POST "https://todo-api-v1-pugr.onrender.com/todos" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test todo", "description": "Testing the API"}'

# Get all todos
curl "https://todo-api-v1-pugr.onrender.com/todos"

# Get statistics
curl "https://todo-api-v1-pugr.onrender.com/stats"
```

---

## 🎓 What I Learned

Building this project taught me:

- **FastAPI Fundamentals**: Routing, request/response handling, dependency injection
- **Database Integration**: SQLAlchemy ORM, database migrations, query optimization
- **API Design**: RESTful principles, proper HTTP methods and status codes
- **Data Validation**: Pydantic models for request validation and serialization
- **Async Programming**: Understanding async/await in Python
- **Cloud Deployment**: Deploying Python applications on Render
- **Documentation**: Auto-generating API documentation with Swagger/OpenAPI
- **Version Control**: Git workflow, commits, and GitHub collaboration

---

## 🚀 Deployment

This API is deployed on **Render** using the free tier.

### Deployment Configuration

- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Python Version**: 3.13.4
- **Auto-deploy**: Enabled on push to main branch

### Deploy Your Own

1. Fork this repository
2. Create a [Render](https://render.com) account
3. Create a new Web Service
4. Connect your GitHub repository
5. Use the configuration above
6. Deploy!

---

## 🔮 Future Enhancements (Version 2)

- [ ] User authentication (JWT tokens)
- [ ] User-specific todos
- [ ] Task categories/tags
- [ ] Due dates and reminders
- [ ] Priority levels
- [ ] Search and filtering
- [ ] Pagination improvements
- [ ] PostgreSQL for production
- [ ] Unit and integration tests
- [ ] CI/CD pipeline

---

## 👤 Author

**Hardik Agarwal**

- 🌐 Portfolio: [Coming Soon]
- 💼 LinkedIn: [linkedin.com/in/hardik-agarwal](https://www.linkedin.com/in/hardik-agarwal)
- 🐙 GitHub: [@HARDIK-WEB-OSS](https://github.com/HARDIK-WEB-OSS)
- 📧 Email: agarwalhardik549@gmail.com

---

## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy for excellent ORM capabilities
- Render for free hosting
- The Python community

---

## 📊 Project Stats

![GitHub last commit](https://img.shields.io/github/last-commit/HARDIK-WEB-OSS/todo-api-v1)
![GitHub code size](https://img.shields.io/github/languages/code-size/HARDIK-WEB-OSS/todo-api-v1)

---

<p align="center">
  <strong>⭐ Star this repo if you found it helpful!</strong><br>
  Built with ❤️ by Hardik Agarwal | January 2026
</p>
