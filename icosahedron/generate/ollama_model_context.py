from langchain_ollama import OllamaLLM
import json

from icosahedron.generate.model_context import ModelContext


class OllamaModelContext(ModelContext):
    def get_llm(self):
        return OllamaLLM(model=self.model_name, temperature=self.temperature)

    def interpret_json_result(self, result):
        return json.loads(result)
