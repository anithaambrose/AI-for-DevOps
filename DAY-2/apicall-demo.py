
import anthropic
import os 
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001", 
    max_tokens=1000, 
    messages=[
        {
            "role": "user",
            "content": "give me a poen in 3 lines ",
        }
    ],
)
print(message.content[0].text)
 
