#Interactive Devops AI Assistant 
import anthropic
import os
from dotenv import load_dotenv
load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY") )

print("🤖 DevOps AI Assistant — type 'quit' to exit\n")

while True:
    question = input("Your question: ").strip()
    if question.lower() == "quit":
        break
    if not question:
        continue

    print("\nThinking...\n")

    msg = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="""You are a senior DevOps/SRE engineer with 10 years of experience.
Always respond with:
1. A one-line answer
2. Root cause (if applicable)
3. The fix (with code/commands)
4. One thing to watch out for
Keep it concise and practical.""",
        messages=[{"role": "user", "content": question}]
    )

    print(msg.content[0].text)
    print("\n" + "─"*50 + "\n")
