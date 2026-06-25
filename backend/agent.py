import os
import dotenv

# این خط باید اول از همه باشه
dotenv.load_dotenv(override=True)

from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

from tools.quiz_tool import quiz_tool
from tools.code_tool import code_tool
from tools.github_tool import github_tool
from tools.roadmap_tool import roadmap_tool


def build_agent():
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("BASE_URL"),
    )

    tools = [quiz_tool, code_tool, github_tool, roadmap_tool]

    system_prompt = """
    You are an intelligent programming tutor assistant.
    
    You have access to these tools:
    - quiz_tool: Generate quizzes about programming topics
    - code_tool: Generate code examples and explanations  
    - github_tool: Review GitHub repositories and give feedback
    - roadmap_tool: Create personalized learning roadmaps
    
    The student's level is provided in the config.
    ALWAYS adapt your response based on student level:
    - beginner: Simple words, lots of examples, no jargon
    - intermediate: Some technical terms, moderate detail
    - advanced: Full technical detail, best practices, edge cases
    
    Always respond in the same language the user writes in.
    If user writes in Persian, respond in Persian.
    """

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=system_prompt,
        checkpointer=MemorySaver(),
    )

    return agent