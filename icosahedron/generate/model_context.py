import openai


class ModelContext:
    client: openai.OpenAI
    delimiter: str
    model: str
    temperature: float
    max_tokens: int

    def __init__(
        self,
        client: openai.OpenAI,
        delimiter: str = None,
        model: str = None,
        temperature: float = 0.0,
        max_tokens: int = -1,
    ):
        self.client = client
        if delimiter is None:
            delimiter = "####"
        self.delimiter = delimiter
        if model is None:
            model = self._default_gpt()
        self.model = model
        self.temperature = temperature
        if max_tokens < 0:
            max_tokens = 500
        self.max_tokens = max_tokens

    @staticmethod
    def _default_gpt():
        return "gpt-4o-mini"
