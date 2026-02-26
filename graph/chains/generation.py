from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-4c877d83a0704cc98417cb92ec7d3d76",
    base_url="https://api.deepseek.com/v1"
)
prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()