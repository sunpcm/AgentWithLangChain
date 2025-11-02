import json
from langchain.agents import initialize_agent, AgentType
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from openroute.common import create_calc_tools, llm, chat_prompt_template


class Output(BaseModel):
    args: str = Field("输入的入参")
    result: str = Field("返回的结果")
    think: str = Field("思考过程")

parser = JsonOutputParser(pydantic_object=Output)
format_instructions = parser.get_format_instructions();

print(format_instructions)
#
agent = initialize_agent(
    tools=create_calc_tools(),
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

prompt = chat_prompt_template.format_messages(
    role="计算",
    domain="实用工具进行数学计算",
    question=f"""
请阅读下面的问题，并返回一个严格的 JSON 对象，不要使用 Markdown 代码块包裹！
格式要求：
{format_instructions}

问题:
100+100=?
"""
)

#
resp = agent.invoke(prompt)
#
print(resp)
print("resp output==================================")
print(resp["output"])
print("type(resp[output]==================================")
print(type(resp["output"]))
print("json.loads(resp[output])==================================")
print(json.loads(resp["output"]))
print("type(json.loads(resp[output]))==================================")
print(type(json.loads(resp["output"])))