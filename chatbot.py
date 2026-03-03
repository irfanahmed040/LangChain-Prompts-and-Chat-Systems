from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
messages = [
    SystemMessage(content="You Are A helpful message")
]

while True: 
    user_input = input("You: ")
    messages.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print("AI: ", result.content)

print(messages)