# Module 3 — K8s Debugging with AI ☸️

This is where AI gives juniors an **instant superpower**. Real Kubernetes errors are cryptic.

AI turns them into plain English + a fix.

Here's the cheat sheet of the most common errors you'll see — and the exact prompt to diagnose each one:---

<img width="1440" height="1504" alt="image" src="https://github.com/user-attachments/assets/8a07af04-d690-4c82-8845-9ef3dbc2c83f" />

## First, the mental model: how a pod actually starts

Before you can debug failures, you need to know the happy path. A pod goes through this sequence

<img width="1440" height="550" alt="image" src="https://github.com/user-attachments/assets/38069310-3d5f-418a-b179-a3870976e943" />

## The single command that solves 80% of K8s debugging

If you remember nothing else from this module, remember this:

```bash
kubectl describe pod <pod-name>
```

Scroll to the bottom — the **Events** section. That's where the real story lives.

Everything above it (labels, IPs, mounts) is just metadata. The Events section is a timeline of exactly what Kubernetes tried and what failed.

<img width="1440" height="888" alt="image" src="https://github.com/user-attachments/assets/08e5c08b-cf95-46d3-bcd6-f6e238aad3bd" />


## The 2-command debugging workflow

Every K8s debugging session follows the same two steps:

```bash
# Step 1: see the Kubernetes-level story (scheduling, image pull, restarts)
kubectl describe pod <pod-name>

# Step 2: see the application-level story (why the app itself crashed)
kubectl logs <pod-name> --previous
```

`--previous` is critical — it shows logs from the **last crashed instance**, not the current restart attempt (which might not have logged anything yet).

## Now feed both to AI — this is where it gets powerful

The winning prompt combines both outputs plus your context:

```
You are a senior SRE debugging a Kubernetes issue.

Pod status: CrashLoopBackOff

kubectl describe output:
[paste describe output - just the Events section]

kubectl logs --previous output:
[paste logs]

What is the root cause and the exact fix? If you need more info to be certain, tell me what additional command to run.
```

That last line — *"if you need more info, tell me what to run"* — is a power move. 

It turns AI into an interactive debugging partner instead of a one-shot guesser, and it's exactly how a senior engineer would actually approach an unfamiliar problem.

## Practice it right now — simulated scenario

Here's a realistic broken pod. Try diagnosing it yourself first, then check with AI:

```
Pod: payment-service-6f8b9-x7k2p
Status: CrashLoopBackOff

kubectl logs --previous output:
Traceback (most recent call last):
  File "app.py", line 12, in <module>
    DATABASE_URL = os.environ["DATABASE_URL"]
  File "/usr/local/lib/python3.11/os.py", line 679, in __getitem__
    raise KeyError(key) from None
KeyError: 'DATABASE_URL'
```

**Before you ask AI — what do you think is wrong?** Take a guess, then paste this into your AI tool and compare. This rep — guess first, then verify — is how you build real debugging instincts instead of just becoming AI-dependent.

