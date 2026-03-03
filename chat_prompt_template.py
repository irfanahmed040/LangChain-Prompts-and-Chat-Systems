from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ("system", "You are a helpful {domain} assistant"), 
    ("human", "Explain in simple words , what is {topic} ")
])

prompt = chat_template.invoke({'domain':"cricket", 'topic':"googly"})

print(prompt)

