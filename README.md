Async Dashboard API
Author: Abd-Alkarem Shaddoud 🔗 Developer Portfolio Project (FastAPI Async Backend)

📌 Overview
A FastAPI-based asynchronous backend project demonstrating modern Python concurrency patterns using async/await, asyncio.TaskGroup, and SQLAlchemy Async ORM.
The project focuses on building high-performance I/O-bound APIs by executing database queries and external API calls concurrently without blocking the event loop.

⚙️ Key Features
⚡ Concurrent database operations using async SQLAlchemy sessions
🔄 Structured concurrency with asyncio.TaskGroup
🌐 Non-blocking external API integration using httpx.AsyncClient
🧪 Integration testing using pytest + httpx.AsyncClient (ASGI transport)

This project demonstrates:
Proper usage of AsyncSession lifecycle management Difference between concurrency vs parallelism in
I/O-bound tasks Handling multiple async dependencies inside a single request Avoiding blocking calls in FastAPI endpoints Structuring async backend code for scalability

📁 Project Structure
app/
├── main.py # FastAPI app entry point
├── db.py # Async database configuration
├── models/ # SQLAlchemy ORM models
├── routers/ │
├── dashboard.py # Async TaskGroup endpoint │
└── crud.py # Async DB + external API logic tests/
tests/
├── test_dashboard.py # Async integration tests
└── seeder.py # Seeding random data fro testing

1.Install dependencies
pip install -r requirements.txt
2.Run the server
uvicorn app.main:app --reload
3.Docker postgres DB
docker compose up
4.seed
data python -m tests.seeder
5.Run tests python -m pytest -q

Example Endpoint GET /dashboard/{user_id}
Returns:

{ "user_data": {}, "orders_data": [], "external_data": [] } 🧪 Testing Strategy Uses pytest-asyncio for async test execution Uses httpx.AsyncClient with ASGI transport Validates full request lifecycle without real HTTP server 📌 Key Learning Outcomes Deep understanding of Python async concurrency model Practical use of TaskGroup vs gather Safe database access patterns in async environments Combining DB + external API calls efficiently Writing testable async FastAPI architectures 📎 Author

👨‍💻 Abd-Alkarem_Shaddoud.dev 🔗 GitHub: https://github.com/Abd-Alkarem-Shaddoud/FastApi-AsyncSample
