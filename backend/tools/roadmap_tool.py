from langchain.tools import tool

@tool
def roadmap_tool(goal: str) -> str:
    """
    Create a personalized learning roadmap for a programming goal.
    Use this when the user wants to know how to learn something or asks for a learning path.
    Input should be the learning goal like 'become a backend developer' or 'learn machine learning'.
    """
    return f"GENERATE_ROADMAP:{goal}"