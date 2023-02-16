#!/usr/bin/env python3

from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
from dotenv import load_dotenv
import sys
import os
from IPython.display import Markdown, display


# load environment variables from .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def ask_ChatAfrica():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True:
        query = input("---- What do you want to ask ChatAfrica Bot?::: \t")
        if query == "exit":
            break
        response = index.query(query, response_mode="compact", verbose=False)
        print(f"ChatAfrica Bot says: {response.response} \n")

if __name__ == "__main__":
    ask_ChatAfrica()
