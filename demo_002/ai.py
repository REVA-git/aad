from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import json

load_dotenv()

prompt_template = PromptTemplate(
    template="""You are a helpful assistant. you will answer questions and help with tasks.
    {question}
    """,
    input_variables=["question"],
)

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chain = prompt_template | llm
