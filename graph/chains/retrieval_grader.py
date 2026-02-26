from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-4c877d83a0704cc98417cb92ec7d3d76",
    base_url="https://api.deepseek.com/v1",
    model_kwargs={"response_format": {"type": "json_object"}}
)


class GradeDocuments(BaseModel):
    """Binary score for relevance check on retrieved documents."""

    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )


parser = JsonOutputParser(pydantic_object=GradeDocuments)

system = """You are a grader assessing relevance of a retrieved document to a user question. \n 
    If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant. \n
    Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question.
    
    Respond with a JSON object in this exact format: {{"binary_score": "yes"}} or {{"binary_score": "no"}}"""
grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "Retrieved document: \n\n {document} \n\n User question: {question}"),
    ]
)

retrieval_grader = grade_prompt | llm | parser