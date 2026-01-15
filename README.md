# Todo API v1 - Simple CRUD

A simple REST API for managing todos built with FastAPI.

## Features

- ✅ Create todo
- ✅ Get all todos
- ✅ Get single todo
- ✅ Update todo
- ✅ Delete todo
- ✅ Toggle completion status
- ✅ Get statistics

## Tech Stack

- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **SQLite**: Lightweight database
- **Pydantic**: Data validation

## Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd todo-api-v1

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python main.py
```

Server runs at: http://localhost:8000

## API Documentation

Interactive API docs: http://localhost:8000/docs

### Endpoints

**Create Todo**
```bash
POST /todos
Body: {"title": "Buy milk", "description": "2% milk"}
```

**Get All Todos**
```bash
GET /todos
```

**Get Single Todo**
```bash
GET /todos/1
```

**Update Todo**
```bash
PUT /todos/1
Body: {"title": "Buy almond milk", "completed": true}
```

**Toggle Completion**
```bash
PATCH /todos/1/toggle
```

**Delete Todo**
```bash
DELETE /todos/1
```

**Get Statistics**
```bash
GET /stats
```

## Testing

```bash
# Create a todo
curl -X POST "http://localhost:8000/todos" \
  -H "Content-Type: application/json" \
  -d '{"title": "Test todo", "description": "This is a test"}'

# Get all todos
curl http://localhost:8000/todos

# Get stats
curl http://localhost:8000/stats
```

## Deployment

**Deploy on Render:**

1. Push code to GitHub
2. Go to render.com
3. New → Web Service
4. Connect your repository
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
7. Deploy!

## Project Structure

```
todo-api-v1/
├── main.py          # FastAPI application
├── models.py        # Database models
├── database.py      # Database configuration
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## What I Learned

- FastAPI basics (routing, request handling, response models)
- SQLAlchemy ORM (models, sessions, queries)
- RESTful API design
- Pydantic for data validation
- Deployment on cloud platforms

## Next Steps

- Add user authentication (JWT)
- Add task priorities
- Add due dates
- Add categories/tags

---

Built by Hardik | [LinkedIn](https://www.linkedin.com/in/hardik-agarwal-578238333) | [GitHub](https://github.com/HARDIK-WEB-OSS)
