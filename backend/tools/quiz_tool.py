from langchain.tools import tool

@tool
def quiz_tool(topic: str) -> str:
    """
    Generate a programming quiz about a specific topic.
    Use this when the user asks for a quiz or test about any programming subject.
    Input should be the topic name like 'Python lists' or 'React hooks'.
    """
    return f"GENERATE_QUIZ:{topic}"