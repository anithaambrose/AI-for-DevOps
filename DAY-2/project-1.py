import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

msg = client.messages.create(
    model='claude-haiku-4-5-20251001',
    max_tokens=300,
    system='You are a senior DevOps engineer. Be concise.',
    messages=[{'role':'user','content':'Explain what an OOMKill is and how to fix it in Kubernetes. Use bullet points.'}]
)
print(msg.content[0].text)
