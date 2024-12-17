import openai
from langchain_openai import ChatOpenAI
import json

from icosahedron.generate.model_context import ModelContext


class OpenAIModelContext(ModelContext):
    client: openai.OpenAI

    def __init__(self, client: openai.OpenAI = None, model_name: str = None, **kwargs):
        if client is None:
            client = openai.OpenAI()
        self.client = client
        if model_name is None:
            model_name = self._default_gpt()
        super().__init__(model_name, **kwargs)

    @staticmethod
    def _default_gpt():
        return "gpt-4o-mini"

    def get_llm(self):
        return ChatOpenAI(
            model_name=self.model_name,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        ).bind(response_format={"type": "json_object"})

    def interpret_json_result(self, result):
        return json.loads(result.content)