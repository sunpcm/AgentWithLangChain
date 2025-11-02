from openroute.common import llm
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.agents import initialize_agent, AgentType
from langchain_core.prompts import PromptTemplate

tools = [PythonREPLTool()]
tool_names = ['PythonREPLTool']

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

prompt_template = PromptTemplate.from_template(template="""
尽你所能回答用户的问题或执行用户的命令，你可以使用以下工具：[{tool_names}]
--
请按照以下格式返回结果：
```
# 思考的过程
- question：你必须回答的问题
- think：你考虑应该怎么做
- Action：要采取的行动，应该是{tool_names}中的一个
- Action Input：行动的输入
- observe：行动的结果
...（这个思考/行动/行动输入/观察可以重复N次）
# 最终答案
对原始输入问题的最终答案
```
--
注意：
- PythonREPLTool工具的入参是python代码，不允许添加 ```py 标记
--
要求：{input}
""")

prompt = prompt_template.format(
    tool_names=tool_names,
    input="""
1. 向/Users/sunpcm/code/AgentWithLangChain目录的.temp文件夹下下写入一个新文件，名称为：index.html
2. 写一个在线教育产品的官网，包含3个tab，分别是：首页、实战课、体系课和关于我们
3. 首页展示3个模块，分别是：热门课程、上新课程、爆款课程
4. 关于我们展示平台的联系方式等基本信息    
"""
)

resp = agent.invoke(prompt)

print(resp)