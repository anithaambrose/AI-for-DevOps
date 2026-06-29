
# 📅 Day 1 Agenda

Today, we're going to understand **what AI actually is** from a software engineer's perspective.

By the end of today, you'll understand:

* What an LLM is
* How ChatGPT works (at a high level)
* How developers use AI
* What an API is in this context
* Build your first AI program tomorrow

---

# Step 1: What is AI?

Think of AI as a very knowledgeable assistant.

Traditional software works like this:

```text
Input
   ↓
Rules written by developer
   ↓
Output
```

Example:

```python
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
```

The developer explicitly defines the logic.

---

AI works differently:

```text
Input
   ↓
Large Language Model (LLM)
   ↓
Generated Output
```

Instead of writing all the rules yourself, you ask the model to generate a response based on what it has learned.

---

# Step 2: What is an LLM?

An **LLM (Large Language Model)** is a program trained on a massive amount of text so it can understand and generate human language.

Examples include:

* ChatGPT
* Claude
* Gemini
* Llama

An LLM predicts the most likely next words based on the input it receives.

---

# Step 3: Think Like a DevOps Engineer

Imagine a production issue.

Instead of manually reading 20,000 log lines:

```text
Application
      ↓
CloudWatch Logs
      ↓
You read logs
      ↓
Find error after 30 minutes
```

With AI:

```text
Application
      ↓
CloudWatch Logs
      ↓
Python Program
      ↓
LLM
      ↓
Summary + Root Cause + Suggested Fix
```

Notice something?

The AI is just **one component** in a larger system.

As a DevOps engineer, your value comes from integrating AI into workflows—not from building the AI model itself.

---

# Step 4: How Developers Actually Use AI

Most developers don't train their own language models.

Instead, they call an API.

Here's a simplified example:

```python
question = "Explain Docker"

response = AI(question)

print(response)
```

In reality, the program sends your prompt to an AI service, which returns a response.

You can think of it like using AWS services:

```text
Your Program
     ↓
AWS Lambda API
     ↓
AWS executes function
```

Similarly:

```text
Your Program
     ↓
LLM API
     ↓
LLM generates response
```

---

# Step 5: Your Future AI Applications

Over the coming weeks, you'll build things like:

✅ AI Log Analyzer

```text
Upload log
      ↓
Python
      ↓
AI
      ↓
Root Cause
```

---

✅ AI Shell Assistant

```text
"Create a zip file"
      ↓
      AI
      ↓
zip -r project.zip project/
```

---

✅ AI Kubernetes Assistant

```text
"Pod is CrashLoopBackOff"
      ↓
      AI
      ↓
Possible reasons
kubectl commands
Recommended fix
```

---

# Step 6: The Skills You'll Learn

By the end of this journey, you'll be comfortable with:

### Python

Using it to automate tasks and call AI APIs.

### REST APIs

Communicating with AI services.

### Prompt Engineering

Writing effective prompts that produce useful outputs.

### LLM APIs

Connecting your applications to models.

### RAG (Retrieval-Augmented Generation)

Giving AI access to your own documentation or logs.

### AI Agents

Creating systems that can perform multiple steps automatically.

---

# 🎯 Today's Mini Exercise

I don't want you to write code yet.

Instead, answer these three questions in your own words. Don't worry about being perfect—this helps me understand your current thinking.

1. **What is the difference between traditional software and AI-based software?**

2. **In your own words, what is an LLM?**

3. **Can you think of one repetitive DevOps task that AI could help automate?**

   * It could involve AWS, Linux, Docker, Kubernetes, Git, CI/CD, or logs.

---
