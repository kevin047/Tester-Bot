# import openai
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SYSTEM_RULES = os.getenv("SYSTEM_RULES")

# client = openai.Client(api_key=OPENAI_API_KEY)

# class GPTchat:
#     def __init__(self):
#         self.user_conversations=[]

#     def reply(self, message: str) -> str:
#         self.user_conversations.append({"role":"user", "content":message})

#         response = client.chat.completions.create(
#             model = 'gpt-4o-mini-2024-07-18',
#             messages = self.user_conversations,
#             max_completion_tokens=2000
#         )

#         reply = response['choices'][0]['message']['content'].strip()
#         self.user_conversations.append({"role":"assistant", "content": reply})
#         return reply
    
#     def clear_conversation(self) -> None:
#         self.user_conversations=[]


class Gchat:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.chat = self.client.chats.create(model="gemini-2.0-flash")
        self.system_prompt= SYSTEM_RULES
        self.chat.send_message(self.system_prompt)

    def reply(self, message: str) -> str:
        response = self.chat.send_message(message)
        return response.text
    
    def clear_conversation(self) -> None:
        self.chat = self.client.chats.create(model="gemini-2.0-flash")
        self.chat.send_message(self.system_prompt)

    
