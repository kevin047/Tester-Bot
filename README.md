# 🤖 Tester - Telegram AI Chatbot

A conversational Telegram bot that uses Gemini/OpenAI models to interact with users. Each user gets a separate conversation session with features like `/clear` to reset the chat history and `/exit` to end the session.

---

## 🌟 **Features**
✅ Real-time conversation with Gemini  
✅ User-specific conversation history  
✅ Commands for start, clear, exit, and help  
✅ Command completion and menu integration  
✅ Hosted on Render with free-tier support

---

## 🛠️ **Tech Stack**
- Python 3.x
- OpenAI API
- Gemini API
- Telegram Bot API (python-telegram-bot)

---

## 🚀 **Setup Locally**

### **1. Clone the Repository**
```bash
git clone https://github.com/kevin047/Tester-Bot.git
cd Tester-Bot
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3. Set Environment Variables**
Create a `.env` file and add:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENAI_API_KEY=your_openai_api_key (optional)
GEMINI_API_KEY=your_gemini_api_key
SYSTEM_RULES=your_system_prompt
```

### **4. Run the Bot**
```bash
python main.py
```

---

## 💡 **Commands**
- `/start` — Begin chatting
- `/help` — Show available commands
- `/clear` — Clear conversation history
- `/exit` — End conversation

---

## 📦 **Project Structure**
```plaintext
Tester-Bot
├── main.py         # Main Telegram bot logic
├── connect.py          # OpenAI/Gemini integration
├── requirements.txt
└── .env            # Environment variables
```

---

## 🧩 **Future Improvements**
- Add support for file attachments
- Enhance error handling and logging
- Chat history Feature

---

## 📞 **Contact**
Have questions? Feel free to open an issue or contribute to the project!

---

**Made with ❤️ using Python, OpenAI, Gemini and Telegram!**

