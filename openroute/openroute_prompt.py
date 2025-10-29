from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate, FewShotPromptTemplate, PromptTemplate
from common import llm, system_message_template, human_message_template, chat_prompt_template

# resp = llm.stream(prompt)
#
# print(prompt)
# #
# for chunk in resp:
#     print(chunk.content, end="")

example_prompts = "输入：{input}\n输出：{output}"
examples = [
    {"input": "将'Hello'翻译成中文", "output": "你好"},
    {"input": "将'Bye'翻译成中文", "output": "再见"}
]
few_shot_prompt_template = FewShotPromptTemplate(
    examples=examples,
    example_prompt=PromptTemplate.from_template(example_prompts),
    prefix="请将以下英文翻译成中文",
    suffix="输入: {text} \n 输出:",
    input_variables=["text"]
)

# prompt=few_shot_prompt_template.format(text='Ugly')
# resp = llm.stream(prompt)

chain = few_shot_prompt_template | llm

resp = chain.stream(input={"text": 'Nice to meet you'})

for chunk in resp:
    print(chunk.content, end='')