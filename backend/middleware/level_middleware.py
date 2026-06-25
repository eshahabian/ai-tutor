# این تابع یه متن اضافه به پیام کاربر میچسبونه
# تا Agent بدونه با چه سطحی طرفه

def apply_level_middleware(message: str, student_level: str) -> str:
    """
    این middleware پیام کاربر رو می‌گیره
    و بر اساس سطح دانشجو، دستورالعمل اضافه می‌کنه
    """

    # دستورالعمل برای هر سطح
    level_instructions = {
        "beginner": """
        [STUDENT LEVEL: BEGINNER]
        - از کلمات ساده استفاده کن
        - هر مفهوم رو با یه مثال واقعی توضیح بده
        - از اصطلاحات فنی پرهیز کن
        - قدم به قدم توضیح بده
        """,

        "intermediate": """
        [STUDENT LEVEL: INTERMEDIATE]
        - می‌تونی اصطلاحات فنی استفاده کنی
        - مثال‌های کاربردی بده
        - best practice ها رو هم ذکر کن
        """,

        "advanced": """
        [STUDENT LEVEL: ADVANCED]
        - توضیحات کاملاً فنی و عمیق بده
        - edge case ها رو بررسی کن
        - performance و best practice های پیشرفته رو توضیح بده
        - می‌تونی به مستندات رسمی اشاره کنی
        """,
    }

    # اگه سطح نامعتبر بود، beginner رو انتخاب کن
    instruction = level_instructions.get(student_level, level_instructions["beginner"])

    # دستورالعمل رو به پیام اصلی اضافه کن
    return f"{instruction}\n\nUser message: {message}"