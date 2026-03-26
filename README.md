# Async Dashboard API

developed by Abd-Alkarem_Shaddoud.dev

## Overview

A **FastAPI** backend project demonstrating **asynchronous Python** using `async/await`, `asyncio.TaskGroup`, and **Async SQLAlchemy**.

This project highlights:

- **Parallel database queries**: Fetching user and orders concurrently.
- **Non-blocking I/O**: All endpoints are async and can handle multiple requests simultaneously.
- **Async external API call**: Demonstrates concurrency across multiple I/O sources.
- **Error handling in TaskGroup**: Ensures safe execution of parallel tasks.

## Project Structure

- `app/` - FastAPI app and async DB setup
- `routers/dashboard.py` - Async endpoint with TaskGroup
- `crud.py` - Async DB operations and mock external API
- `tests/` - Async unit tests using pytest-asyncio

## Running the Project

1. Install dependencies:

```bash
pip install -r requirements.txt
```
