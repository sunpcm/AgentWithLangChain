from pydoc import describe

from langchain_core.tools import Tool, tool
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate
from pydantic import BaseModel, Field
from common import llm, system_message_template, human_message_template, chat_prompt_template


class AddInputArgs(BaseModel):
    a: int = Field(description="first number")
    b: int = Field(description="second number")

@tool(
    description="add two numbers",
    args_schema=AddInputArgs

)
def add(a,b):
    print(a)
    print(b)
    return a + b

tool_dict = {
    "add": add,
}

llm_with_tools = llm.bind_tools([add])

chain = chat_prompt_template | llm_with_tools

resp = chain.invoke(input={"role": "计算", "domain": "数学", "question": "100加100等于多少" })

print(resp)

for tool_calls in resp.tool_calls:
    args = tool_calls["args"]
    print(args)
    print('=========')
    func_name = tool_calls["name"]
    tool_func = tool_dict[func_name]
    tool_context = tool_func.invoke(input=args)
    print(tool_context)
    # tool_content = tool_func.invoke()