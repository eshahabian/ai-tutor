from langchain.tools import tool

@tool
def code_tool(request: str) -> str:
    """
    Generate code examples and programming tutorials.
    Use this when the user asks for code examples, implementations, or wants to see how something works in code.
    Input should describe what code to generate, like 'FastAPI CRUD example' or 'Python decorator example'.
    """
    return f"GENERATE_CODE:{request}"