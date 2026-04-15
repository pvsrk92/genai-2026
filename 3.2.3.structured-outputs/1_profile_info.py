from typing import Annotated
from pydantic import BaseModel, Field
from pydantic_ai import Agent
import logfire
from dotenv import load_dotenv

load_dotenv(override=True)
logfire.configure()
logfire.instrument_pydantic_ai()

class ProfileInfo(BaseModel):
    name: Annotated[str, Field(description="Full name, properly capitalized")]
    experience_years: Annotated[int, Field(description="Years of experience", ge=0, le=100)]
    skills: Annotated[list[str], Field(description="Technical skills found")]

agent = Agent(
    #'ollama:llama3-groq-tool-use:8b',
    'groq:llama-3.3-70b-versatile',
    instructions="You are a helpful assistant to extract structure",
    output_type=ProfileInfo,
    retries=5
)

user_prompt = "Krishna is an SharePoint Engineer with 12+ years of experience, skilled in .Net and React."
response = agent.run_sync(user_prompt)
print(response.output)
print(response.usage())