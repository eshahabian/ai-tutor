"use client";

import { useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [level, setLevel] = useState("beginner");

  const sendMessage = async () => {
    if (!input.trim()) return;

    // پیام کاربر رو اضافه کن
    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      // به backend بفرست
      const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: input,
          thread_id: "user-1",
          student_level: level,
        }),
      });

      const data = await response.json();

      // جواب AI رو اضافه کن
      const aiMessage = { role: "assistant", content: data.response };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error("Error:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-900 text-white flex flex-col">
      
      {/* هدر */}
      <div className="bg-gray-800 p-4 flex items-center justify-between border-b border-gray-700">
        <h1 className="text-xl font-bold text-blue-400">🎓 AI Tutor</h1>
        
        {/* انتخاب سطح */}
        <select
          value={level}
          onChange={(e) => setLevel(e.target.value)}
          className="bg-gray-700 text-white px-3 py-1 rounded-lg border border-gray-600"
        >
          <option value="beginner">مبتدی</option>
          <option value="intermediate">متوسط</option>
          <option value="advanced">پیشرفته</option>
        </select>
      </div>

      {/* پیام‌ها */}
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.length === 0 && (
          <div className="text-center text-gray-500 mt-20">
            <p className="text-4xl mb-4">🤖</p>
            <p className="text-lg">سلام! من دستیار آموزشی هوشمند هستم.</p>
            <p className="text-sm mt-2">می‌تونی ازم کوییز، کد، مسیر یادگیری و بررسی GitHub بخوای!</p>
          </div>
        )}

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}
          >
            <div
              className={`max-w-2xl p-3 rounded-lg whitespace-pre-wrap ${
                msg.role === "user"
                  ? "bg-blue-600 text-white"
                  : "bg-gray-700 text-white"
              }`}
            >
              {msg.content}
            </div>
          </div>
        ))}

        {/* نمایش loading */}
        {loading && (
          <div className="flex justify-start">
            <div className="bg-gray-700 p-3 rounded-lg">
              <span className="animate-pulse">در حال فکر کردن... 🤔</span>
            </div>
          </div>
        )}
      </div>

      {/* باکس ورودی */}
      <div className="bg-gray-800 p-4 border-t border-gray-700">
        <div className="flex gap-2 max-w-4xl mx-auto">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="سوالت رو بپرس..."
            className="flex-1 bg-gray-700 text-white px-4 py-2 rounded-lg border border-gray-600 focus:outline-none focus:border-blue-400"
            dir="rtl"
          />
          <button
            onClick={sendMessage}
            disabled={loading}
            className="bg-blue-600 hover:bg-blue-700 disabled:bg-gray-600 text-white px-6 py-2 rounded-lg transition-colors"
          >
            ارسال
          </button>
        </div>
      </div>

    </main>
  );
}