from dotenv import load_dotenv

load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "What is SELF-RAG? what is reflection tokens?"}))
    # print(app.invoke(input={"question": "what is agent memory?"}))
    # print(app.invoke(input={"question": "who is jeff shuo? what country was she born in?"}))