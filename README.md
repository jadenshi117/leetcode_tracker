# LeetCode Pattern Tracker

A full-stack web app for tracking LeetCode problems by algorithmic pattern, so you can see which patterns you've practiced the most and which ones need more work

## Features

- Add a problem with its name, pattern, and difficulty (the solved date is recorded automatically)
- View all saved problems and delete any of them
- Live pattern stats, sorted from least to most practiced, so you know what to study next
- Dark-themed, card-based interface
- REST API built with Flask, with a front-end that talks to it using `fetch`

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Flask, Flask-CORS |
| Front-end | HTML, CSS, JavaScript (no frameworks) |
| Storage | Local `problems.json` file |

## Project Structure

```
leetcode_tracker/
├── app.py             Flask API (routes)
├── tracker.py         Core logic: load, save, add, delete, and count problems
├── index.html         Page structure
├── style.css          Styling
├── script.js          Front-end logic (calls the API)
├── problems.json      Saved problems (created automatically)
└── requirements.txt   Python dependencies
```

## Instillation

You'll need Python 3 and Git installed.

**1. Clone the repo**

```
git clone https://github.com/jadenshi117/leetcode_tracker.git
cd leetcode_tracker
```

**2. Install dependencies**

```
pip install -r requirements.txt
```

**3. Start the API**

```
python app.py
```

The server runs at `http://127.0.0.1:5000`. Visiting that address should show "LeetCode Tracker API is running".

**4. Open the front-end**

Open `index.html` with the VS Code **Live Server** extension (it serves the page at `http://127.0.0.1:5500`). The API and front-end run on different ports, which is why the backend uses Flask-CORS.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/problems` | Returns all saved problems |
| `POST` | `/problems` | Adds a problem. Body: `{"name": "...", "pattern": "...", "difficulty": "..."}` |
| `DELETE` | `/problems/<id>` | Deletes the problem with that id (404 if it doesn't exist) |
| `GET` | `/stats` | Returns each pattern with its solved count, least practiced first |

### Example problem

```json
{
  "id": 1,
  "name": "Valid Parentheses",
  "pattern": "stack",
  "difficulty": "easy",
  "dateSolved": "2026-10-07"
}
```

## Supported Patterns

`two_pointer`, `sliding_window`, `hash_map`, `stack`, `linked_list`, `dynamic_programming`

To add a new pattern, add it to the `knownPatterns` list in `tracker.py`. The dropdown and stats update automatically.

## Design Notes

- **Unique ids:** each problem gets an `id` one higher than the current largest, so ids never clash after a delete.
- **JSON storage:** the file is fully rewritten on every change. That's fine at this scale, and a database like SQLite would be the natural next step for larger data.
- **Separation of concerns:** `tracker.py` handles data logic, `app.py` only exposes it over HTTP, and the front-end only talks to the API.

## Roadmap

- [ ] Edit a problem's pattern or difficulty
- [ ] Move storage from JSON to SQLite
- [ ] Deploy online

## Author

Built by [jadenshi117](https://github.com/jadenshi117).
