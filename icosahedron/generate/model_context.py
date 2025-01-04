from abc import ABCMeta, abstractmethod


class ModelContext(metaclass=ABCMeta):
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

    @abstractmethod
    def get_llm(self):
        pass

    @abstractmethod
    def interpret_json_result(self, result):
        pass
