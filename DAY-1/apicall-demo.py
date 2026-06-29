#calling an API from vcode 
#API key is passed in .env file 
import anthropic
import os 
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001", # selected AI model 
    max_tokens=1000, # defines the no of words in the output
    messages=[
        {
            "role": "user",
          # content is the prompt that we are passing to the anthropic server.
            "content": "give me a poen in 3 lines ",
        }
    ],
)
print(message.content[0].text)
# response gets printed here 
