from icosahedron.campaign.names_generator import NameGenerator
from icosahedron.generate.ollama_model_context import OllamaModelContext


def test_generate_names():
    generator = NameGenerator(context=OllamaModelContext(model_name="gemma2", temperature=0))
    j = generator.generate(number=10)
    assert len(j) == 10
    expected = {"name", "etymology", "origin", "gender"}
    for item in j:
        assert set(item.keys()) == expected
        assert type(item["name"]) is str
        assert type(item["etymology"]) is str
        assert type(item["origin"]) is str
        assert item["gender"] == "male"

    generator = NameGenerator(context=OllamaModelContext(model_name="mistral-nemo", temperature=0))
    j = generator.generate(number=10)
    assert len(j) == 10
    for item in j:
        assert set(item.keys()) == expected
        assert type(item["name"]) is str
        assert type(item["etymology"]) is str
        assert type(item["origin"]) is str
        assert item["gender"] == "male"

    j = generator.generate(culture="Dwarven (mountain dwarf)", gender="female", number=4)
    assert len(j) == 4
    for item in j:
        assert set(item.keys()) == expected
        assert type(item["name"]) is str
        assert type(item["etymology"]) is str
        assert type(item["origin"]) is str
        assert item["gender"] == "female"
