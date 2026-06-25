from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import build_agent
from middleware.level_middleware import apply_level_middleware
from middleware.context_middleware import apply_context_middleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default"
    student_level: str = "beginner"

agent = build_agent()

@app.post("/chat")
async def chat(request: ChatRequest):

    # مرحله ۱ — context middleware
    # اطلاعات کاربر رو به پیام اضافه کن
    message_with_context = apply_context_middleware(
        message=request.message,
        thread_id=request.thread_id,
        student_level=request.student_level,
    )

    # مرحله ۲ — level middleware
    # دستورالعمل سطح دانشجو رو به پیام اضافه کن
    final_message = apply_level_middleware(
        message=message_with_context,
        student_level=request.student_level,
    )

    # مرحله ۳ — پیام نهایی رو به agent بفرست
    config = {
        "configurable": {
            "thread_id": request.thread_id,
        }
    }

    result = agent.invoke(
        {"messages": [{"role": "user", "content": final_message}]},
        config=config,
    )

    return {"response": result["messages"][-1].content}

@app.get("/")
def root():
    return {"status": "AI Tutor is running! 🚀"}