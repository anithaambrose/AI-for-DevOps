# Module 4 — Build your first AI automation script 🐍

When an interviewer asks "tell me about a project you built," a log analyzer hits every checkbox they care about:

- **AI integration** — you called an external API programmatically
- **DevOps relevance** — logs are the #1 thing SREs deal with daily
- **Problem solving** — you automated something painful and manual
- **Python skills** — file I/O, API calls, error handling, CLI design

Let's build a version good enough to actually demo.

---

## Build it in 4 stages — each one runnable

### Stage 1 — Bare minimum (make sure it works)

```python
# log_analyzer_v1.py
import anthropic

client = anthropic.Anthropic(api_key="YOUR_KEY_HERE")

def analyze(log_text: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="You are a senior SRE. Analyze logs and explain what went wrong in plain English.",
        messages=[{"role": "user", "content": f"Analyze these logs:\n\n{log_text}"}]
    )
    return response.content[0].text

# hardcoded test — just prove it works
test_log = """
2024-01-15 10:23:01 INFO  App started on port 8080
2024-01-15 10:24:12 ERROR Connection pool exhausted: max_connections=10 reached
2024-01-15 10:24:13 FATAL psycopg2.OperationalError: FATAL: remaining connection slots reserved
"""

print(analyze(test_log))
```

Run this first:
```bash
python3 log_analyzer_v1.py
```

Confirm you get a real analysis back before moving to Stage 2.

---

### Stage 2 — Read from a real file + structured output

```python
# log_analyzer_v2.py

import anthropic
import sys

client = anthropic.Anthropic(api_key="YOUR_KEY_HERE")

SYSTEM_PROMPT = """You are a senior SRE analyzing application logs.

Always respond in exactly this format:

## 🔍 What happened
[1-2 sentence plain-English summary of the incident]

## 🚨 Root cause
[The specific error or line that triggered the failure]

## 🔧 Fix
[Step-by-step resolution with commands where relevant]

## ⚠️ How to prevent this
[One concrete change — config, code, or monitoring]

Severity: [CRITICAL / HIGH / MEDIUM / LOW]"""

def analyze(log_text: str) -> str:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": f"Analyze these logs:\n\n{log_text}"}]
    )
    return response.content[0].text

def read_log(path: str) -> str:
    with open(path, "r") as f:
        content = f.read()
    # only send last 200 lines — avoids hitting token limits on huge log files
    lines = content.strip().split("\n")
    return "\n".join(lines[-200:])

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 log_analyzer_v2.py <path-to-log-file>")
        print("Example: python3 log_analyzer_v2.py app.log")
        sys.exit(1)

    path = sys.argv[1]
    print(f"📂 Reading: {path}")

    log_text = read_log(path)
    print(f"📊 Analyzing {len(log_text.split(chr(10)))} lines...\n")

    result = analyze(log_text)
    print(result)

if __name__ == "__main__":
    main()
```

Create a test log file to use with it:

```bash
cat > app.log << 'EOF'
2024-01-15 10:23:01 INFO  Starting application on port 8080
2024-01-15 10:23:02 INFO  Connected to postgres at db:5432
2024-01-15 10:23:45 INFO  Processing GET /api/users (200)
2024-01-15 10:24:11 INFO  Processing GET /api/orders (200)
2024-01-15 10:24:12 ERROR Connection pool exhausted: max_connections=10 reached
2024-01-15 10:24:12 ERROR Failed to acquire DB connection after 30s timeout
2024-01-15 10:24:13 ERROR psycopg2.OperationalError: FATAL: remaining connection slots reserved
2024-01-15 10:24:13 CRITICAL Health check failed — shutting down
2024-01-15 10:24:14 INFO  Graceful shutdown initiated
EOF

python3 log_analyzer_v2.py app.log
```

---

### Stage 3 — Handle multiple log types + errors gracefully

This is the version that goes on GitHub:

```python
# log_analyzer_v3.py — production-ready version
import anthropic
import sys
import os
from pathlib import Path

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", "YOUR_KEY_HERE"))

LOG_TYPES = {
    "app":   "application service log",
    "k8s":   "Kubernetes pod/event log",
    "nginx": "Nginx access/error log",
    "ci":    "CI/CD pipeline output",
}

SYSTEM_PROMPT = """You are a senior SRE analyzing {log_type} logs.

Respond in exactly this format:

## 🔍 What happened
[Plain-English summary — what failed and when]

## 🚨 Root cause
[The specific error/line that caused the problem. Quote it.]

## 🔧 Fix
[Numbered steps to resolve it. Include commands.]

## ⚠️ Prevention
[One config, code, or monitoring change to stop this recurring]

Severity: [CRITICAL / HIGH / MEDIUM / LOW]
Confidence: [HIGH / MEDIUM / LOW — how certain you are given the available logs]"""

def analyze(log_text: str, log_type: str = "app") -> str:
    system = SYSTEM_PROMPT.format(log_type=LOG_TYPES.get(log_type, "application"))

    try:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1500,
            system=system,
            messages=[{"role": "user", "content": f"Analyze these logs:\n\n{log_text}"}]
        )
        return response.content[0].text

    except anthropic.APIConnectionError:
        return "❌ Could not connect to Anthropic API. Check your internet connection."
    except anthropic.AuthenticationError:
        return "❌ Invalid API key. Check your ANTHROPIC_API_KEY."
    except anthropic.RateLimitError:
        return "❌ Rate limit hit. Wait a moment and retry."

def read_log(path: str, tail: int = 200) -> str:
    p = Path(path)

    if not p.exists():
        print(f"❌ File not found: {path}")
        sys.exit(1)

    if p.stat().st_size == 0:
        print(f"❌ File is empty: {path}")
        sys.exit(1)

    with open(p, "r", errors="replace") as f:
        lines = f.readlines()

    # tail last N lines to stay within token limits
    return "".join(lines[-tail:])

def print_header(path: str, log_type: str, line_count: int):
    print("\n" + "="*50)
    print(f"  🤖 AI Log Analyzer")
    print("="*50)
    print(f"  File     : {path}")
    print(f"  Log type : {LOG_TYPES.get(log_type, log_type)}")
    print(f"  Lines    : {line_count} (last 200 analyzed)")
    print("="*50 + "\n")

def main():
    if len(sys.argv) < 2:
        print("\nUsage:")
        print("  python3 log_analyzer_v3.py <log-file> [log-type]")
        print("\nLog types:", ", ".join(LOG_TYPES.keys()), "(default: app)")
        print("\nExamples:")
        print("  python3 log_analyzer_v3.py app.log")
        print("  python3 log_analyzer_v3.py pod.log k8s")
        print("  python3 log_analyzer_v3.py /var/log/nginx/error.log nginx\n")
        sys.exit(1)

    path     = sys.argv[1]
    log_type = sys.argv[2] if len(sys.argv) > 2 else "app"

    log_text   = read_log(path)
    line_count = len(log_text.split("\n"))

    print_header(path, log_type, line_count)
    print("🔍 Analyzing...\n")

    result = analyze(log_text, log_type)
    print(result)
    print()

if __name__ == "__main__":
    main()
```

Run it:
```bash
# set your API key properly (better than hardcoding)
export ANTHROPIC_API_KEY="your-key-here"

# analyze an app log
python3 log_analyzer_v3.py app.log

# analyze a k8s log
python3 log_analyzer_v3.py pod.log k8s
```

---

### Stage 4 — What makes this interview-ready

Three things to add before showing this to anyone:

**1. A proper README.md**
```markdown
# AI Log Analyzer

Diagnose application failures instantly using AI.

## Usage
\```bash
export ANTHROPIC_API_KEY="your-key"
python3 log_analyzer_v3.py <log-file> [app|k8s|nginx|ci]
\```

## What it does
Reads the last 200 lines of any log file and returns:
- Plain-English summary of what failed
- Root cause with the specific error quoted
- Step-by-step fix with commands
- Prevention recommendation
- Severity + confidence rating

## Supported log types
| Type | Description |
|------|-------------|
| app  | Application/service logs |
| k8s  | Kubernetes pod/event logs |
| nginx| Nginx access/error logs |
| ci   | CI/CD pipeline output |
```

**2. A requirements.txt**
```
anthropic>=0.25.0
```

**3. A `.env.example`**
```
ANTHROPIC_API_KEY=your-key-here
```

---Run Stage 1 first, paste back what you get, then build up through the stages. Each one is runnable on its own — don't skip ahead until the previous stage works.

When you've got v3 running, say **"Day 3 let's go"** and we'll pick your product and start building the real thing. 🚀


OR 

Follow Below version - **real log analyzer tool** — a log analyzer that reads a log file and uses AI to explain what went wrong. This is basically a stripped-down version of your Day 5 product.

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

