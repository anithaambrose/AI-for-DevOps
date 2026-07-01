import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

msg = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=1024,
    system='You are a senior DevOps engineer. Be concise.',
    messages=[{'role':'user','content':"Write a GitHub Actions workflow for:"
               "Language: Python 3.11"
               "Test command: pytest"
               "Trigger: run tests on every push or PR"
               "Deploy step : build docker image & push to docker hub"
               "but ONLY after tests pass, and ONLY on push to main"
               "Use Github secrets for credentials, never hardcode them"
               "Explain each job and step with an one line inline comment."
    }]
)

print(msg.content[0].text)
