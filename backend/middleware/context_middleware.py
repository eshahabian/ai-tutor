# یه دیکشنری برای نگه داشتن اطلاعات هر کاربر
# کلید: thread_id (شناسه کاربر)
# مقدار: اطلاعات کاربر
user_contexts = {}


def get_context(thread_id: str) -> dict:
    """
    اطلاعات ذخیره شده یه کاربر رو برگردون
    اگه کاربر جدیده، یه دیکشنری خالی برگردون
    """
    if thread_id not in user_contexts:
        user_contexts[thread_id] = {
            "student_level": "beginner",      # سطح پیش‌فرض
            "favorite_technologies": [],        # تکنولوژی‌های موردعلاقه
            "studied_topics": [],               # موضوعاتی که خونده
            "current_roadmap": None,            # مسیر یادگیری فعلی
            "conversation_count": 0,            # تعداد مکالمات
        }
    return user_contexts[thread_id]


def update_context(thread_id: str, message: str, student_level: str):
    """
    بعد از هر پیام، اطلاعات کاربر رو آپدیت کن
    """
    context = get_context(thread_id)

    # تعداد مکالمات رو یکی اضافه کن
    context["conversation_count"] += 1

    # سطح دانشجو رو آپدیت کن
    context["student_level"] = student_level

    # اگه کاربر از تکنولوژی خاصی حرف زد، یادداشت کن
    technologies = ["python", "javascript", "react", "fastapi", "django", "nodejs"]
    for tech in technologies:
        if tech in message.lower() and tech not in context["favorite_technologies"]:
            context["favorite_technologies"].append(tech)


def apply_context_middleware(message: str, thread_id: str, student_level: str) -> str:
    """
    اطلاعات context رو به پیام اضافه کن
    تا Agent بدونه این کاربر کیه و چی خونده
    """
    # اول context رو آپدیت کن
    update_context(thread_id, message, student_level)

    # بعد context فعلی رو بگیر
    context = get_context(thread_id)

    # اگه اطلاعاتی داریم، به پیام اضافه کن
    context_info = ""

    if context["favorite_technologies"]:
        techs = ", ".join(context["favorite_technologies"])
        context_info += f"\n- User's favorite technologies: {techs}"

    if context["studied_topics"]:
        topics = ", ".join(context["studied_topics"])
        context_info += f"\n- Topics already studied: {topics}"

    if context["current_roadmap"]:
        context_info += f"\n- Current learning path: {context['current_roadmap']}"

    # اگه context اطلاعاتی داشت، به پیام اضافه کن
    if context_info:
        return f"[USER CONTEXT:{context_info}]\n\nUser message: {message}"

    # اگه کاربر جدیده، پیام رو همونطور برگردون
    return message