import openai


class ModelContext:
    delimiter: str
    model_name: str
    temperature: float
    max_tokens: int

    def __init__(
        self,
        model_name: str,
        delimiter: str = None,
        temperature: float = 0.0,
        max_tokens: int = -1,
    ):
        if delimiter is None:
            delimiter = "####"
        self.delimiter = delimiter
        self.model_name = model_name
        self.temperature = temperature
        if max_tokens < 0:
            max_tokens = 500
        self.max_tokens = max_tokens


class OpenAIModelContext(ModelContext):
    client: openai.OpenAI

    def __init__(self, client: openai.OpenAI, model_name: str = None, **kwargs):
        self.client = client
        if model_name is None:
            model_name = self._default_gpt()
        super().__init__(model_name, **kwargs)

    @staticmethod
    def _default_gpt():
        return "gpt-4o-mini"
