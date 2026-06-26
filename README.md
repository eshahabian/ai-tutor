# 🎓 AI Tutor — دستیار آموزشی هوشمند

یک دستیار آموزشی هوشمند برای یادگیری برنامه‌نویسی با استفاده از FastAPI و Next.js

---

## ✨ قابلیت‌ها

- 📝 **Quiz Generator** — تولید کوییز از هر موضوع برنامه‌نویسی
- 💻 **Code Generator** — تولید کد و مثال‌های آموزشی
- 🔍 **GitHub Review** — بررسی پروژه‌های GitHub
- 🗺️ **Learning Roadmap** — مسیر یادگیری شخصی‌سازی شده
- 🎯 **Student Level** — پاسخ‌های متناسب با سطح مبتدی، متوسط، پیشرفته

---

## 🛠️ تکنولوژی‌ها

- **Backend:** FastAPI + LangChain + LangGraph
- **Frontend:** Next.js + Tailwind CSS
- **AI:** GPT-4o-mini

---

## 🚀 نصب و اجرا

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 📁 ساختار پروژه

```
ai-tutor/
├── backend/
│   ├── main.py
│   ├── agent.py
│   ├── tools/
│   │   ├── quiz_tool.py
│   │   ├── code_tool.py
│   │   ├── github_tool.py
│   │   └── roadmap_tool.py
│   └── middleware/
│       ├── level_middleware.py
│       └── context_middleware.py
└── frontend/
    └── app/
        └── page.tsx
```