# Module 1 — Docker + AI 🐳

### First, understand what Docker actually does

Before AI can help you write Dockerfiles, you need the mental model:### Now use AI to generate a Dockerfile — and understand every line

## What problem does Docker actually solve?

Before Dockerfiles, here's the pain: "it works on my machine" but breaks in production because of different OS versions, missing dependencies, different Python versions, etc.

Docker's fix: **package your app + everything it needs into one portable unit** that runs identically everywhere — your laptop, a teammate's laptop, AWS, anywhere.

<img width="1440" height="606" alt="image" src="https://github.com/user-attachments/assets/b19abc46-c042-4ece-8438-2730514a80a0" />

The 7 instructions that make up 95% of all Dockerfiles

<img width="1440" height="800" alt="image" src="https://github.com/user-attachments/assets/0b5c59c3-5043-4c24-b38f-2da2145169c1" />

The single most important concept: layer caching

This is the #1 thing that separates a junior-written Dockerfile from a senior-written one, and it's also the #1 thing AI gets wrong if you don't prompt for it.## 

<img width="1440" height="708" alt="image" src="https://github.com/user-attachments/assets/c33c561b-b0de-42d8-9fc9-c06888ade912" />


Here's the exact prompt template — use this format every time and AI will get layer ordering, security, and size right:

```
You are a senior DevOps engineer.

Write a production-ready Dockerfile for:
- Language/runtime: [e.g. Python 3.11 / Node 20 / Go 1.22]
- Framework: [e.g. Flask, Express, none]
- Entry point: [e.g. app.py, index.js]
- Port: [e.g. 8000]

Requirements:
- Use a slim/alpine base image to minimize size
- Order instructions for optimal layer caching (deps before code)
- Run as a non-root user (security best practice)
- Add a .dockerignore recommendation too

Explain each instruction with an inline comment.
```

### Try it right now

Paste that prompt into your CLI tool from Day 1 (or claude.ai), filling in your own stack. If you don't have a real project handy, use this test case:

> *Python 3.11, Flask app, entry point `app.py`, port 8000*

You'll get something like this — and now you'll understand **why** every line is there, not just copy-paste it:

```dockerfile
FROM python:3.11-slim                    # minimal base, fewer CVEs

WORKDIR /app

COPY requirements.txt .                  # deps layer first (cached)
RUN pip install --no-cache-dir -r requirements.txt

COPY . .                                 # code layer last (changes often)

RUN useradd -m appuser && chown -R appuser /app
USER appuser                             # don't run as root — security

EXPOSE 8000

CMD ["python", "app.py"]
```

And a `.dockerignore` (stops junk from bloating your image):
```
__pycache__/
*.pyc
.git
.env
venv/
```

---

## Task 

1. Run that prompt with your own project (or the Flask test case)
2. Build it: `docker build -t myapp .`
3. Run it: `docker run -p 8000:8000 myapp`
4. Paste back what you get — especially if anything errors out, since debugging this *with* AI is itself great practice

