import json
from abc import ABCMeta, abstractmethod


class Dictable(metaclass=ABCMeta):
    def to_json(self) -> str:
        """Converts instance to a JSON string.

        Returns:
            str: The JSON string representing the instance.
        """
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str):
        """Creates a instance from a JSON string.

        Args:
            json_str (str): The JSON string representing the instance.

        Returns:
            The instance represented by the JSON string.
        """
        data = json.loads(json_str)
        return cls.from_dict(data)

    @abstractmethod
    def to_dict(self):
        """Converts instance to a dictionary.

        Returns:
            dict: The dictionary representing instance.
        """
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data):
        """Creates instance from a dictionary.

        Args:
            data (dict): The dictionary representing instance.

        Returns:
            The instance represented by the dictionary.
        """
        pass
