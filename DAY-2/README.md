# 🚀 Day 2 Agenda - API CALL & RESPONSE

Today, you'll build something real: a Python program that talks to an AI model and gets a response back.

## 🎯 Today's Goal

By the end of Day 2, you'll:
`
Install the required Python package
Understand what an API call is
Write your first AI script
Send a prompt to an AI model
Receive and print the response
`

### Under current folder - refer to apicall-demo.py program 

## Step 1: Create a Project Folder
Open your terminal and run:

## Step 2: Create a Python Virtual Environment in visual code 

## Step 3: Install the SDK in Terminal 
sudo apt install python3
pip install anthropic

## Step 4: Get an API Key
Go to Claude Platform
Create an account - buy credits
Generate an API key , Copy the key

Important: Never share your API key publicly, save them in .env 

## Step 5: Set the API Key in Your Terminal

On macOS/Linux: using EXPORT KEY = value
On Windows (PowerShell): as env variable

## Step 6: Create Your First AI Program

Create a file called apicall-demo.py

```
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
```
## Step 7: Run the Program

🎉 Congratulations — you just built your first API call is made.

🧠 Understanding Every Line
1. Import the SDK - This gives your Python program the ability to talk to the AI service.

2. Create a Client - This authenticates your program using your API key.

3. Send a Prompt - This is the actual API call.

Your program sends:
`
The model name
A system instruction
The user's question
`
4. Read the Response

The AI's answer comes back in a structured object, and this line extracts the text.

🛠️ Mini Exercise - Project-1.py

Change the user prompt to: "Explain what an OOMKill is and how to fix it in Kubernetes. Use bullet points."
Run the script again.

🎯 Today's Challenge 1 - Go to Simple Projects Folder

Create a new file called devops_helper.py 

The program should ask the user for a question:
Then send that question to the AI and print the response.

Example:
Use model= claude-sonnet-4-6 ,
    max_tokens=1024,
    system = You are a senior DevOps/SRE engineer with 10 years of experience.
    Always respond with:
    1. A one-line answer
    2. Root cause (if applicable)
    3. The fix (with code/commands)
    4. One thing to watch out for
    Keep it concise and practical.

Input: what is kubernetes

Output: 🤖 DevOps AI Assistant — type 'quit' to exit

  Your question: what is kubernetes
  
  Thinking...
  
  **Kubernetes (K8s) is an open-source container orchestration platform that automates deploying, scaling, and managing containerized applications.**
  
  ---
🎯 Today's Challenge 2  - Go to Simple Projects Folder 

Create a new file called AICmdAssistant.py
Example:
You will type a request such as:  "give me linux command to check for disk space, kubernetes pods status check, aws s3 bucklet list"
Notice how the AI can generate Linux commands for you.

Input
Find files larger than 2GB

Output
find / -type f -size +2G

# Do this using OpenAI.

Step 1: Install the OpenAI package
Open Terminal and run:


Step 2: Get an API key

For learning, you can use OpenAI's API (paid) or a free alternative later. Since the goal is understanding the workflow, we'll use the standard approach first.

Go to: platform.openai.com/api-keys

Create a new secret key and copy it.
Keep it private. Never upload it to GitHub.

Step 3: Create your AI script
Create a file named ai_cmd_assistant.py and paste this code:

```
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()
client = anthropic.Anthropic(
api_key=os.getenv("ANTHROPIC_API_KEY")
)

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "give me linux command to check for disk space, kubernetes pods status check, aws s3 bucklet list ",
        }
    ],
)
print(message.content[0].text)
```

Replace YOUR_API_KEY_HERE with your actual API key.

Step 4: Run it to display output of linux commands.

💡 Understand Every Line

👉🏻 from openai import OpenAI - Imports the OpenAI library.

👉🏻client = OpenAI(api_key="...") - Creates a connection to the AI service.

👉🏻 prompt = "..." - This is your question to the AI.

👉🏻 client.chat.completions.create(...) - Sends the prompt to the model.

👉🏻 print(response.choices[0].message.content) - Prints the AI's answer.

✅ Why This Matters for DevOps

| You ask   | AI returns | 
| "Check disk usage" | df -h |
| "Compress logs" | tar -czvf logs.tar.gz logs/ |
| "Find listening ports" | ss -tulnp |
| "Check Kubernetes pods" | kubectl get pods -A |

You have built a Linux command assistant.

🏁 End of Day 2

Once you've completed the challenge, you'll officially have:

Written your first AI-powered Python application
Made your first API call
Used AI to answer DevOps questions



