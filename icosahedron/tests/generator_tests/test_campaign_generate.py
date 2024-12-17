from icosahedron.campaign import names_generator


def test_default_name_template():
    assert names_generator.default_name_prompt_template


def test_name_generator(context):
    name_generator = names_generator.NameGenerator(context=context)
    assert (
        name_generator.prompt_template == names_generator.default_name_prompt_template
    )
    prompt_formatted_str = name_generator.prompt_formatted_str(
        culture="Dwarven", number=42, gender="female"
    )
    assert "Dwarven" in prompt_formatted_str
    assert "42" in prompt_formatted_str
    assert "female" in prompt_formatted_str
