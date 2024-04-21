# -*- coding: utf-8 -*-
import openai
import os

class GPTModel:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.model = "gpt-3.5-turbo"
        self.max_token = 250

    def chat_gpt(self, prompt):
        openai.api_key = self.api_key
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "你是一个古诗词智能问答小助手，我会问你中国古诗词相关的问题，并为你提供问题相关的事实信息，你将根据这些事实信息进行回答，并适当进行补充，你明白了吗。"
                },
                {
                    "role": "assistant",
                    "content": "明白了，我会根据提供的事实信息来回答关于中国古诗词的问题。请问有什么问题我可以帮助您解答呢？"
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=self.max_token
        )

        answer = response['choices'][0]['message']['content']
        return answer


if __name__ == '__main__':
    gptModel = GPTModel()
    while 1:
        prompt = input()
        message = gptModel.chat_gpt(prompt)
        print(message)
