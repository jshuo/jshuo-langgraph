from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI


class GradeAnswer(BaseModel):

    binary_score: bool = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )


llm = ChatOpenAI(
    model="deepseek-chat",
    temperature=0,
    api_key="sk-4c877d83a0704cc98417cb92ec7d3d76",
    base_url="https://api.deepseek.com/v1",
    model_kwargs={"response_format": {"type": "json_object"}}
)
parser = JsonOutputParser(pydantic_object=GradeAnswer)

system = """You are a grader assessing whether an answer addresses / resolves a question \n 
     Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question.
     
     Respond with a JSON object in this exact format: {{"binary_score": true}} or {{"binary_score": false}}"""
answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system),
        ("human", "User question: \n\n {question} \n\n LLM generation: {generation}"),
    ]
)

answer_grader: RunnableSequence = answer_prompt | llm | parser