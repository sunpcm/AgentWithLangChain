import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

class BriskAgentsLLM:
    """
    兼容 OpenAI 接口规范服务，默认流式响应
    """
    def __init__(self, model: str = None, apiKey: str = None, baseUrl: str = None, timeout: int = None):
        """
        初始化客户端，优先使用传入参数，若没有提供，则从环境变量中夹杂
        """
        self.model = model or os.getenv("LLM_MODEL_ID")
        apiKey = apiKey or os.getenv("LLM_API_KEY")
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or os.getenv("LLM_TIMEOUT")

        if not all([self.model, apiKey, baseUrl]):
            raise ValueError("模型ID，API密钥必须提供或者在.env中定义")

        self.client = OpenAI(api_key=apiKey, base_url=baseUrl, timeout=timeout)

    def think(self, message: List[Dict[str, str]], temperature: float = 0) -> str | None:
        """
        调用大模型进行思考，并返回结果
        """
        print(f"大模型正在思考...")

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=message,
                temperature=temperature,
                stream=True,
            )

            # 处理流式响应
            print("Resp获取成功")
            collected_content = []
            for chunk in response:
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()
            return "".join(collected_content)

        except Exception as e:
            print(f"调用 LLM API 发生错误：{e}")
            return None

# ====示例====

if __name__ == "__main__":
    try:
        llmClient = BriskAgentsLLM()

        exampleMessage = [
            {"role": "system", "content": "you are a helpful assistant that write JS code"},
            {"role":"user", "content": "写一个快速排序"},
        ]

        print("----调用 LLM ----")

        respText = llmClient.think(exampleMessage, temperature=0)
        if respText:
            print("\n\n -----完整模型返回-----")
            print(respText)
    except Exception as e:
        print(f"Agent启动失败： {e}")