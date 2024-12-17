from icosahedron.generate.model_context import ModelContext


class MockOpenAI:
    pass


class MockModelContext(ModelContext):
    def interpret_json_result(self, result):
        pass

    def get_llm(self):
        pass
