from icosahedron.campaign.names_generator import NameGenerator
from icosahedron.generate.openai_model_context import OpenAIModelContext


def test_generate_names(load_env):
    generator = NameGenerator(context=OpenAIModelContext(max_tokens=1000))
    j = generator.generate(number=10)['characters']
    assert len(j) == 10
    expected = {"name", "etymology", "origin", "gender"}
    for item in j:
        assert set(item.keys()) == expected
        assert type(item["name"]) is str
        assert type(item["etymology"]) is str
        assert type(item["origin"]) is str
        assert item["gender"] == "male"
