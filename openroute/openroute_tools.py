from langchain_core.tools import Tool
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate
from common import llm, system_message_template, human_message_template, chat_prompt_template

def add(a,b):
    return a+b

# prompt = chat_prompt_template.format_messages(role='前端', domain='React', question='你擅长什么？')
chain = chat_prompt_template | llm

resp = chain.stream(input={"role": "前端", "domain": "react", "question": "你擅长什么" })

for chunk in resp:
    print(chunk.content, end="")
