from pydantic import BaseModel


class Action(BaseModel):
    """
    Represents an action in a tabletop RPG.

    :param name: The name of the action.
    :type name: str
    :param action_type: The type of action (e.g., Standard, Move, Full-Round).
    :type action_type: str
    :param aoo: Whether the action may provoke attacks of opportunity (Yes/No/Varies).
    :type aoo: str
    :param description: A description of the action.
    :type description: str
    """

    name: str
    action_type: str
    aoo: str
    description: str

    class Config:
        """
        Configuration settings for the Action class.

        :ivar allow_mutation: Whether instances of Action are mutable or not.
        :vartype allow_mutation: bool
        """
        allow_mutation = False
