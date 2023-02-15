from gpt_index import SimpleDirectoryReader, GPTListIndex, readers, GPTSimpleVectorIndex, LLMPredictor, PromptHelper


def ask_lenny():
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    while True: 
        query = input("What do you want to ask Lenny? ")
        response = index.query(query, response_mode="compact", verbose=False)
        print(f"Lenny Bot says: <b>{response.response}</b>")