# 🦥 TLaaS – Too Lazy as a Service (FastAPI Practice Project)

(But let’s be honest, you're probably too lazy to read it.....)

![lazy cat](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTNscTVxemZyNWxqZWE3dmo0aGw5dWR4aWc3MjJhMXh5ancxZXhvYiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/pVkmGyqYRt4qY/giphy.gif)

---

This is a personal project I created to learn FastAPI in Python.

It’s a playful excuse-generating API that’s mostly too lazy to do anything…
but when it does, it response with a solid (and very questionable) excuses for any occasion.

#### 📀 Tech Stack: FastAPI, Uvicorn, Docker, Render

---

## 🧪 Features

- `GET /excuse` – Get a random excuse from all categories.
- `GET /excuse/{category}` – Get a random excuse from a specific category.
- `GET /excuse/{category}?tag=cat` – Filter excuses by category **and** tag (e.g., cat-related excuses for work).
- `GET /excuse/categories` – See available categories/tags.
- `POST /excuse/custom` – Generate a custom excuse for any task.
- (lazy) error messages included.
- Random “too lazy to work” refusals

---

## 🔎 API Documentation

Explore and test the API via interactive Swagger UI:

🟢 [https://too-lazy-as-a-service.onrender.com/docs](https://too-lazy-as-a-service.onrender.com/docs)

Or if you prefer ReDoc style:

🟢 [https://too-lazy-as-a-service.onrender.com/redoc](https://too-lazy-as-a-service.onrender.com/redoc)

## 🔥 Example Usage

### Example Lazy Refusal Response

```json
{
  "excuse": "Nah. Too lazy to do that right now.",
  "status": "the API is refusing to work. Try again later (or don’t)"
}
```

### `GET /excuse`

```json
{
  "excuse": "I'm on a productivity detox program.",
  "category": "general"
}
```

### `GET /excuse/work?tag=cat`

```json
{
  "excuse": "My cat deleted my files by walking on the keyboard.",
  "category": "work"
}
```

### `POST /excuse/custom`

```json
{ "task": "folding laundry" }
```

Response:

```json
{
  "excuse": "I got distracted by the documentary about folding laundry.",
  "topic": "folding laundry",
  "believability": "Varies by audience"
}
```

---

### ✨ Future Ideas (or maybe not, I’m lazy)

- Rate limiting (“You’ve asked for too many excuses. Try being productive.”)
- Frontend for lazy click-to-excuse generation
- AI-powered excuse generation (via OpenAI or LLMs)

### Disclaimer:

- If you're a future employer or future teammate: This project is meant to be fun and does **not represent my actual work ethic or personality.** (Well… maybe just a little.)
- The API is built purely for the sake of practicing API design, request handling, and having fun while learning.
