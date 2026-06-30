# Module 4 — Build your first AI automation script 🐍

This is the big one. You're going to build a **real tool** — a log analyzer that reads a log file and uses AI to explain what went wrong. This is basically a stripped-down version of your Day 5 product.

Create a file called `log_analyzer.py`:

```python
import anthropic
import sys

client = anthropic.Anthropic(api_key="YOUR_KEY_HERE")

def analyze_log(log_content: str) -> str:
    """Send log content to Claude and get a DevOps diagnosis."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are a senior SRE analyzing application logs.
When given logs, respond in this exact format:

## 🔍 What happened
[1-2 sentence summary of the incident]

## 🚨 Root cause
[The specific line/error that caused the problem]

## 🔧 Fix
[Concrete steps to resolve it, with commands if applicable]

## ⚠️ Watch out for
[One thing that could make this worse or recur]""",
        messages=[{
            "role": "user",
            "content": f"Analyze these logs and diagnose the problem:\n\n{log_content}"
        }]
    )
    return response.content[0].text

def main():
    # Read from file if provided, otherwise use sample logs
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            logs = f.read()
    else:
        # Sample logs to test with
        logs = """
2024-01-15 10:23:01 INFO  Starting application on port 8080
2024-01-15 10:23:02 INFO  Connected to database at postgres:5432
2024-01-15 10:23:45 INFO  Processing request GET /api/users
2024-01-15 10:24:12 ERROR Connection pool exhausted: max_connections=10 reached
2024-01-15 10:24:12 ERROR Failed to acquire database connection after 30s timeout
2024-01-15 10:24:13 ERROR psycopg2.OperationalError: FATAL: remaining connection slots reserved
2024-01-15 10:24:13 CRITICAL Application health check failed
2024-01-15 10:24:14 ERROR Unhandled exception in request handler
2024-01-15 10:24:14 INFO  Attempting graceful shutdown...
        """

    print("🔍 Analyzing logs...\n")
    result = analyze_log(logs)
    print(result)

if __name__ == "__main__":
    main()
```

Run it two ways:

```bash
# Way 1: use the built-in sample logs
python3 log_analyzer.py

# Way 2: analyze a real log file
python3 log_analyzer.py /var/log/syslog
```

---

## What you just built

That script is the **exact core** of your Day 5 product. The difference between this script and a product that stands out in interviews is just:

- A web UI or CLI wrapper around it
- Accepting different input types (k8s logs, CI failures, app logs)
- Storing results / showing history
- Dockerizing and deploying it

All of which we do on Days 3–5.

---

**Day 2 checklist:**
- ✅ Understand Docker layers and Dockerfile instructions
- ✅ Know how a GitHub Actions CI/CD pipeline is structured
- ✅ Have a cheat sheet for the top 4 Kubernetes errors
- ✅ Built a working AI log analyzer script

Run the script, paste what you get back, and then say **"Day 3 let's go"** — tomorrow we pick your product idea and start building for real. 🚀
