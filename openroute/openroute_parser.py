from langchain.output_parsers import DatetimeOutputParser
from langchain_core.prompts import ChatPromptTemplate

from openroute.common import llm, chat_prompt_template

parser = DatetimeOutputParser()
instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages([
    ("system", f"必须按照以下格式返回日期时间：{instructions}"),
    ("human", "请将以下自然语言转换为标准日期时间格式：{text}")
])

chain = prompt | llm | parser

resp = chain.invoke({"text": "二零二五年五月一日上午十点十分"})

print(resp)