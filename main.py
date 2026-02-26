from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    # print(app.invoke(input={"question": "What is SELF-RAG?"}))
    # input = {"question": "You are a helpful assistant...\nAnswer in bullets...\nQuestion: What is Agentic RAG?"}

    # print(app.invoke(input))
