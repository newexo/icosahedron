import pytest
from action import Action

@pytest.fixture
def sample_action_data():
    return {
        "name": "Attack",
        "action_type": "Standard",
        "aoo": "Yes",
        "description": "Engage in melee or ranged combat with a weapon or unarmed strike."
    }

def test_action_initialization(sample_action_data):
    action = Action(**sample_action_data)
    assert action.name == "Attack"
    assert action.action_type == "Standard"
    assert action.aoo == "Yes"
    assert action.description == "Engage in melee or ranged combat with a weapon or unarmed strike."

def test_action_loading_from_dict(sample_action_data):
    action = Action.parse_obj(sample_action_data)
    assert action.name == "Attack"
    assert action.action_type == "Standard"
    assert action.aoo == "Yes"
    assert action.description == "Engage in melee or ranged combat with a weapon or unarmed strike."

def test_action_saving_to_dict(sample_action_data):
    action = Action(**sample_action_data)
    action_dict = action.dict()
    assert action_dict == sample_action_data