
from dotenv import load_dotenv
load_dotenv()

import os

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI

# Verify that the API key is loaded (never print the actual key)
print("API key loaded:", bool(os.getenv("OPENAI_API_KEY")))

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

reflection_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a viral twitter influencer grading a tweet. "
            "Generate critique and recommendations for the user's tweet. "
            "Always provide detailed recommendations, including requests "
            "for length, virality, style, etc.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generation_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a twitter techie influencer assistant tasked "
            "with writing excellent twitter posts. "
            "Generate the best twitter post possible for the user's request. "
            "If the user provides critique, respond with a revised "
            "version of your previous attempts.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

generate_chain = generation_prompt | llm
reflect_chain = reflection_prompt | llm
