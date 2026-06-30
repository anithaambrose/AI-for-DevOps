
# Module 2 — CI/CD + AI ⚙️

CI/CD = every time you push code, it automatically builds, tests, and deploys. GitHub Actions is the most common tool. 

## What is CI/CD, actually?

**CI (Continuous Integration):** every time you push code, it automatically gets built and tested — catching bugs before they reach anyone else.

**CD (Continuous Deployment):** if those tests pass, the code automatically gets deployed — no manual SSH-ing into servers and copying files.

GitHub Actions is GitHub's built-in automation engine — you write a YAML file, and GitHub runs it on their servers every time you push.## Building a real pipeline, step by step

<img width="1440" height="1008" alt="image" src="https://github.com/user-attachments/assets/f03d48f5-c716-4f4f-bf79-74f78282d98a" />

### Building Real Pipeline 

Let's build a pipeline for a Python app: test on every push, then build+push a Docker image only when merging to `main`.

<img width="1440" height="1540" alt="image" src="https://github.com/user-attachments/assets/5b173b73-2fc4-419a-8d9c-37384b6ea466" />

### AI Prompt template for any CI/CD Pipeline.

```
You are a senior DevOps engineer.

Write a GitHub Actions workflow for:
- Language: [e.g. Python 3.11 / Node 20]
- Test command: [e.g. pytest / npm test]
- Trigger: run tests on every push and PR
- Deploy step: build a Docker image and push to Docker Hub,
  but ONLY after tests pass, and ONLY on pushes to main
- Use GitHub secrets for credentials, never hardcode them

Explain each job and step with inline comments.
```

## How to actually set this up (do this now)

1. In your repo, create the folder structure: `.github/workflows/ci.yml`
2. Paste in a generated pipeline (use the prompt above with your real stack, or copy the example above)
3. Add your Docker Hub credentials as secrets:
   - GitHub repo → **Settings → Secrets and variables → Actions → New repository secret**
   - Add `DOCKER_USERNAME` and `DOCKER_TOKEN` (generate a token at hub.docker.com → Account Settings → Security)
4. Push to GitHub
5. Go to the **Actions** tab in your repo — watch it run live

## One debugging tip that'll save you hours

When a workflow fails, GitHub shows you raw logs that can be cryptic. The move: copy the **failed step's full log output** and paste it to AI with this prompt:

```
This GitHub Actions step failed:
[paste the exact log output]

Here is my workflow YAML:
[paste relevant job]

What's the root cause and how do I fix it?
```



