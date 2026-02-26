import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_openai import OpenAIEmbeddings

load_dotenv()

PERSIST_DIR = "./.chroma"
COLLECTION_NAME = "rag-chroma"

web_urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    "https://weaviate.io/blog/what-is-agentic-rag",
]

pdf_urls = [
    "https://arxiv.org/pdf/2310.11511",
    "https://arxiv.org/pdf/2403.14403",
    "https://arxiv.org/pdf/2401.15884"
]


def ingest_documents():
    """Load documents from URLs, split them, and store in vector database."""
    print("Starting1000, chunk_overlap=20...")
    
    # Load web pages
    print(f"Loading {len(web_urls)} web pages...")
    web_docs = [WebBaseLoader(url).load() for url in web_urls]
    
    # Load PDFs
    print(f"Loading {len(pdf_urls)} PDFs...")
    pdf_docs = [PyPDFLoader(url).load() for url in pdf_urls]
    
    # Combine all documents
    docs = web_docs + pdf_docs
    docs_list = [item for sublist in docs for item in sublist]
    print(f"Loaded {len(docs_list)} total documents")

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)
    print(f"Split into {len(doc_splits)} chunks")

    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name=COLLECTION_NAME,
        embedding=OpenAIEmbeddings(),
        persist_directory=PERSIST_DIR,
    )
    print(f"Ingested {len(doc_splits)} documents into {COLLECTION_NAME}")
    return vectorstore
search_kwargs={"k": 6}

def get_retriever():
    """Get retriever, creating and populating database if it doesn't exist."""
    # Check if database exists and has documents
    if os.path.exists(PERSIST_DIR):
        try:
            vectorstore = Chroma(
                collection_name=COLLECTION_NAME,
                persist_directory=PERSIST_DIR,
                embedding_function=OpenAIEmbeddings(),
            )
            # Test if collection has documents
            test_results = vectorstore.similarity_search("test", k=1)
            if len(test_results) > 0:
                print(f"Using existing vector database with {len(test_results)} documents")
                return vectorstore.as_retriever(search_kwargs={"k": 6})
        except Exception as e:
            print(f"Error loading existing database: {e}")
    
    # Database doesn't exist or is empty, create it
    print("Vector database not found or empty, creating new one...")
    vectorstore = ingest_documents()
    return vectorstore.as_retriever(search_kwargs={"k": 6})


retriever = get_retriever()


if __name__ == "__main__":
    # Force re-ingestion when run directly
    print("Force re-ingesting documents...")
    vectorstore = ingest_documents()
    retriever = vectorstore.as_retriever()
    
    # Test the retriever
    test_query = "What is SELF-RAG?"
    results = retriever.invoke(test_query)
    print(f"\nTest query: '{test_query}'")
    print(f"Retrieved {len(results)} documents")
    if results:
        print(f"First result preview: {results[0].page_content[:200]}...")
