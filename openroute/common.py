from langchain_core.prompts import ChatMessagePromptTemplate, ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import SecretStr
from os import environ
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(
    model="minimax/minimax-m2:free",
    base_url="https://openrouter.ai/api/v1",
    api_key=SecretStr(environ.get("API_KEY")),
    streaming=True,
)

system_message_template =  ChatMessagePromptTemplate.from_template(
    template="你是一个{role}专家，擅长回答{domain}问题",
    role="system"
)
human_message_template = ChatMessagePromptTemplate.from_template(
    template="用户的问题是: {question}",
    role="user"
)

chat_prompt_template = ChatPromptTemplate.from_messages([
    system_message_template,
    human_message_template
])