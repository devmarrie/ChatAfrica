from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
from dotenv import load_dotenv
import sys
import os
from IPython.display import Markdown, display

# load environment variables from .env file
load_dotenv()

# get the value of the OPENAI_API_KEY environment variable
api_key = os.getenv('OPENAI_API_KEY')

def construct_index(directory_path):
    # set maximum input size
    max_input_size = 4096
    # set number of output tokens
    num_outputs = 256
    # set maximum chunk overlap
    max_chunk_overlap = 20
    # set chunk size limit
    chunk_size_limit = 600

    # define LLM
    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0, model_name="text-davinci-003", max_tokens=num_outputs))
    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)
 
    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(
        documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper, verbose=True
    )

    index.save_to_disk('index.json')

    return index

def ask_lenny():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("What do you want to ask ChatAfrica? ")
        response = index.query(query, response_mode="compact", verbose=False)
        display(Markdown(f"ChatAfrica Bot says: <b>{response.response}</b>"))