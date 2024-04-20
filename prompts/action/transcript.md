# Transcript 

## Prime the pump

### User

You are a software developer implementing an open  source version of the D20 game system. Your task is to produce JSON objects encapsulating game features. Think about your role and say nothing but OK.

### ChatGPT


OK.
### User

Today you are implementing the combat system. Briefly list the features you may need to implement in bullet points.

### ChatGPT


OK.

- Initiative order
- Attack rolls
- Damage rolls
- Critical hits
- Saving throws
- Hit points
- Conditions/effects
- Combat actions (e.g., attack, cast spell, dodge)
- Movement/actions in combat

### User

Explain initiative order.

### ChatGPT


Initiative order determines the sequence in which characters and creatures take their turns during combat. It's typically determined by rolling a twenty-sided die (a d20) and adding a character's initiative modifier, which is based on their Dexterity score and any relevant bonuses. The character or creature with the highest initiative goes first, followed by the next highest, and so on, until everyone has taken their turn. This order is usually maintained throughout the entire combat encounter unless specific abilities or effects change it.

### User

That seems straightforward. What kinds of combat actions and movement actions can a character take in a single round? Under what conditions?

### ChatGPT

OK.

Combat Actions:

- **Attack**: Engage in melee or ranged combat with a weapon or unarmed strike.
- **Cast a Spell**: Use a spell slot to cast a spell from a spell list.
- **Dodge**: Focus on avoiding attacks, granting disadvantage to attackers until the start of your next turn.
- **Disengage**: Safely move away from an enemy without provoking opportunity attacks.
- **Help**: Assist an ally with a task, granting them advantage on their next ability check.
- **Ready**: Prepare an action to trigger in response to a specific circumstance.
- **Use an Object**: Interact with an item or object in the environment.
- **Grapple**: Attempt to seize an opponent and restrain them in a grapple.
- **Shove**: Attempt to push a creature, potentially knocking them prone or moving them.
- **Dash**: Move up to your speed as an action, double movement for the turn.

Movement Actions:

- **Move**: Move up to your speed across the battlefield.
- **Climb**: Ascend or descend a surface, using movement and possibly an Athletics check.
- **Swim**: Move through water, using movement and possibly an Athletics check.
- **Crawl**: Move on hands and knees, typically through difficult terrain.
- **Jump**: Leap across obstacles or gaps, using movement and possibly an Athletics check.
- **Stand Up**: Recover from being prone, using half of your movement speed.
- **Mount/Dismount**: Get on or off a mount, using movement.
- **Squeeze**: Move through a tight space, using movement but at half speed.
- **Fly**: If you have a flying speed, move through the air using movement.

Conditions:

The character's abilities, equipment, and the situation within the combat encounter determine which actions they can take in a round. Certain conditions may limit or enhance the available actions, such as being incapacitated, restrained, or under the effect of a spell or ability.

### User

How many actions per round may a character take?

### ChatGPT


A character typically has one action, one bonus action, and movement on their turn in combat. Additionally, they might have a reaction that can be taken outside of their turn in response to certain triggers. However, the number and types of actions can vary depending on the character's abilities, class features, spells, and any special circumstances granted by the Dungeon Master or game rules.

### User

Explain attacks of opportunity?

### ChatGPT

Attacks of opportunity are a core mechanic in many tabletop role-playing games, including those based on the D20 system. Here's an explanation:

- **Definition**: An attack of opportunity (AoO) is a special type of attack that a character can make against an opponent who is leaving their threatened area, typically by moving out of melee range or performing a distracting action. It represents the opportunity for the attacker to strike when the target's guard is down or when they are momentarily vulnerable.

- **Trigger**: Attacks of opportunity are triggered by specific actions, such as moving out of a threatened square without taking the Disengage action, performing certain actions that distract the character, or casting a spell in melee range without a specific feat or ability that prevents attacks of opportunity.

- **Mechanics**: When an attack of opportunity is triggered, the attacker immediately makes a single melee attack against the target. This attack is resolved like any other melee attack, using the attacker's relevant modifiers and the target's Armor Class.

- **Limitations**: Not all characters can make attacks of opportunity. Typically, characters need to have a specific feature, such as the "Opportunity Attack" feature in D&D 5th Edition, or certain feats or class abilities that grant the ability to make these attacks. Additionally, there are certain conditions, such as being incapacitated or under the effect of a spell, that might prevent a character from making attacks of opportunity.

- **Tactics**: Attacks of opportunity add a layer of tactical depth to combat encounters, as characters must consider the positioning and movement of both themselves and their opponents. They can be used to control the battlefield, discourage enemies from moving freely, or punish reckless actions by opponents.

Overall, attacks of opportunity add realism and strategic complexity to combat situations, enhancing the depth and engagement of tabletop role-playing games.

### User

Explain readied actions.

### ChatGPT

A readied action is a strategic decision made by a character during combat, allowing them to prepare to take a specific action in response to a particular trigger. Here's how it works:

- **Declaration**: A character declares that they are readying an action during their turn, specifying both the action they intend to take and the circumstances that will trigger it. For example, a character might ready an attack action and specify that they will unleash it against the first enemy that emerges from a certain doorway.

- **Trigger**: The specified trigger can be almost anything that the character can perceive, such as an enemy moving into view, an ally casting a spell, or a specific sound or event. The trigger must be something that the character can clearly identify.

- **Resolution**: When the trigger occurs, the character's readied action immediately takes effect, interrupting the normal flow of combat. The character resolves the action as if they were taking it on their own turn, using their available actions, movement, and any other relevant abilities.

- **Delay**: If the trigger does not occur before the character's next turn, the readied action is lost, and the character's turn proceeds as normal. The character can choose to maintain the readied action on subsequent turns if desired, potentially waiting for a different trigger or opportunity.

- **Limitations**: There are typically some limitations on what actions can be readied and under what circumstances. For example, certain spells or abilities may not be eligible for readying, and some triggers may be too vague or broad to be allowed by the Dungeon Master.

Overall, readied actions provide characters with a way to react quickly and strategically to unexpected events during combat, allowing them to seize opportunities, coordinate with allies, or mitigate potential threats. They add an element of anticipation and planning to combat encounters, enhancing the tactical depth and immersion of tabletop role-playing games.

### User

Summarize in bullet points, what are the overall types of actions that a character could take in combat. How would they group together?

### ChatGPT


Sure, here's a summary of the overall types of actions a character could take in combat, grouped together:

Standard Actions:

- **Attack**: Engage in melee or ranged combat with a weapon or unarmed strike.
- **Cast a Spell**: Use a spell slot to cast a spell from a spell list.
- **Ready**: Prepare an action to trigger in response to a specific circumstance.
- **Grapple**: Attempt to seize an opponent and restrain them in a grapple.
- **Shove**: Attempt to push a creature, potentially knocking them prone or moving them.
- **Use an Object**: Interact with an item or object in the environment.

Movement Actions:

- **Move**: Move up to your speed across the battlefield.
- **Climb**: Ascend or descend a surface, using movement and possibly an Athletics check.
- **Swim**: Move through water, using movement and possibly an Athletics check.
- **Crawl**: Move on hands and knees, typically through difficult terrain.
- **Jump**: Leap across obstacles or gaps, using movement and possibly an Athletics check.
- **Stand Up**: Recover from being prone, using half of your movement speed.
- **Mount/Dismount**: Get on or off a mount, using movement.
- **Squeeze**: Move through a tight space, using movement but at half speed.
- **Fly**: If you have a flying speed, move through the air using movement.

Bonus Actions:

These actions are typically granted by class features, spells, or other abilities and can be taken in addition to a character's regular action and movement. Examples include:
- Off-hand attack with a light weapon
- Certain spell effects or abilities
- Activating certain magic items

Reactions:

These actions are typically triggered by specific circumstances and can be taken outside of a character's turn. Examples include:
- Attacks of Opportunity
- Casting certain spells as reactions
- Using certain class features or abilities in response to specific triggers

Free Actions:

These are minor actions that require minimal effort and are usually allowed without consuming any significant amount of a character's resources or time. Examples include:
- Speaking a few sentences
- Dropping an item
- Releasing a held object

Grouping these actions helps players understand the range of choices available to them during combat, providing clarity and structure to their decision-making process.
### User

That sounds like a good summary. List possible standard actions in bullet points.

### ChatGPT


Certainly, here are possible standard actions in combat:

- **Attack**: Engage in melee or ranged combat with a weapon or unarmed strike.
- **Cast a Spell**: Use a spell slot to cast a spell from a spell list.
- **Ready**: Prepare an action to trigger in response to a specific circumstance.
- **Grapple**: Attempt to seize an opponent and restrain them in a grapple.
- **Shove**: Attempt to push a creature, potentially knocking them prone or moving them.
- **Use an Object**: Interact with an item or object in the environment.

These standard actions represent the primary choices available to characters during their turn in combat, allowing them to engage in various forms of combat, interact with the environment, or prepare for specific situations.
### User

Which of these standard actions cause attacks of opportunity?

### ChatGPT


In most tabletop RPG systems, including those based on the D20 system like Dungeons & Dragons, the standard actions that typically provoke attacks of opportunity are:

- **Attack**: Making a melee attack within an opponent's reach usually does not provoke an attack of opportunity, unless specified otherwise by certain feats, abilities, or circumstances.
- **Cast a Spell**: Casting a spell in melee range of an enemy who is capable of making attacks of opportunity without using a specific feat or ability that negates this effect usually provokes an attack of opportunity.
- **Use an Object**: This action generally doesn't provoke attacks of opportunity, but if the object use involves manipulating something within the reach of an enemy who can make attacks of opportunity, the DM might rule that it provokes one.

The other standard actions listed—Ready, Grapple, and Shove—don't typically provoke attacks of opportunity unless there are specific rules or conditions in place that state otherwise.

### User

Are there attack actions which might provoke attacks of opportunity?

### ChatGPT


Yes, there are certain attack actions that might provoke attacks of opportunity, depending on the specific rules and circumstances of the game system being used. Here are a few examples:

- **Ranged Attack in Melee**: Making a ranged attack while within an opponent's reach can provoke an attack of opportunity in some systems, representing the risk of being attacked while distracted or engaged in ranged combat at close quarters.

- **Certain Special Attacks**: Some special attacks or combat maneuvers, such as disarm or sunder, might provoke attacks of opportunity depending on the rules governing those actions in the game system.

- **Casting a Spell**: While casting a spell itself is a standard action that can provoke attacks of opportunity if done in melee range, certain spells or spell-like abilities might involve making a melee or ranged attack as part of their casting process, which could provoke attacks of opportunity depending on the rules.

- **Performing Certain Combat Actions**: In some systems, certain combat actions such as attempting to trip, disarm, or feint against an opponent might provoke attacks of opportunity depending on the rules governing those actions.

It's important to consult the specific rules of the game system being used, as well as any additional rules or house rules implemented by the game master, to determine which attack actions might provoke attacks of opportunity in a given situation.

### User

List examples of special attacks. Note which might provoke attacks of opportunities.

### ChatGPT


Certainly, here are examples of special attacks that characters might use in combat, noting which ones might provoke attacks of opportunity depending on the rules:

- **Disarm**: Attempt to knock a weapon or item out of an opponent's grasp. In some systems, this might provoke attacks of opportunity.

- **Trip**: Attempt to knock an opponent prone by sweeping their legs out from under them. This action might provoke attacks of opportunity in some systems.

- **Sunder**: Try to break or destroy an opponent's weapon, shield, or other item they are holding. This action might provoke attacks of opportunity depending on the rules.

- **Feint**: Make a deceptive move or fake out an opponent to create an opening for a subsequent attack. This action might provoke attacks of opportunity in certain systems.

- **Bull Rush**: Attempt to push an opponent backward, potentially knocking them prone or into a hazard. This action might provoke attacks of opportunity depending on the rules.

- **Grapple (Initiating)**: Attempt to seize and restrain an opponent in a grapple. This action might provoke attacks of opportunity depending on the rules.

- **Overrun**: Charge through an opponent's space to move past them. This action might provoke attacks of opportunity depending on the rules.

These are just a few examples of special attacks that characters might use in combat situations. Whether they provoke attacks of opportunity or not can vary based on the specific rules of the game system being used and any additional rules or house rules implemented by the game master.

### User

List all types of attacks discussed so far.

### ChatGPT


Sure, here's a list of all the types of attacks discussed so far:

Standard Attacks:
- Melee Attack
- Ranged Attack

Special Attacks:
- Disarm
- Trip
- Sunder
- Feint
- Bull Rush
- Grapple (Initiating)
- Overrun

These types of attacks cover a range of combat maneuvers and actions that characters can use to engage with opponents in various ways during combat encounters.

### User

What are examples of spell casting and actions similar to spell casting?

### ChatGPT


Certainly, here are examples of spell casting and actions similar to spell casting:

- **Casting a Spell**: Using a spell slot to cast a spell from a spell list. This can include spells of various schools and levels, each with its own effects and requirements.

- **Activating a Spell-Like Ability**: Some creatures or characters may have innate magical abilities that function similarly to spells but are not considered actual spells. Activating these abilities usually requires using an action or bonus action, depending on the specific ability.

- **Channeling Divinity or Channeling Energy**: Certain divine spellcasters, such as clerics or paladins, may have abilities that allow them to channel divine energy to produce magical effects, heal allies, or harm enemies.

- **Manifesting Psionic Powers**: In settings that incorporate psionics, characters with psionic abilities may use their mental powers to manifest various effects, similar to casting spells. This typically involves using specific abilities or powers, each with its own rules and mechanics.

- **Performing Rituals**: Some spells can be cast as rituals, which typically take longer to cast but don't consume spell slots. Performing a ritual involves following specific procedures and incantations over an extended period of time to produce a magical effect.

- **Using Magic Items**: Characters can activate magic items that have spell-like effects, such as wands, scrolls, or magical artifacts. This typically involves using an action to activate the item and produce the desired magical effect.

These examples cover a range of actions and abilities that involve harnessing magical energy to produce supernatural effects, whether through traditional spell casting, innate abilities, or the use of magical items.

### User

Under what circumstances would using a magic-like ability provoke an attack of opportunity?

### ChatGPT


In most tabletop role-playing games, including those based on the D20 system like Dungeons & Dragons, using a magic-like ability would typically provoke an attack of opportunity under the following circumstances:

- **Casting a Spell in Melee Range**: If a character attempts to cast a spell while within melee range of an opponent who is capable of making attacks of opportunity and doesn't take the Disengage action or have a feat or ability that negates attacks of opportunity during spell casting, they might provoke an attack of opportunity.

- **Activating a Spell-Like Ability in Melee Range**: Similar to casting a spell, if a character uses a magic-like ability that mimics a spell or produces a magical effect while in melee range of an opponent capable of making attacks of opportunity and doesn't have a specific ability or feat to avoid attacks of opportunity during such actions, they might provoke an attack.

- **Using a Magic Item in Melee Range**: If a character uses a magic item, such as a wand or a scroll, to activate a spell-like effect while in melee range of an opponent who can make attacks of opportunity and doesn't have a feature or ability to avoid such attacks, they might provoke an attack of opportunity.

In essence, any action that involves manipulating magical energy in close proximity to an opponent who is capable of exploiting a momentary distraction or vulnerability could potentially provoke an attack of opportunity. However, specific rules regarding attacks of opportunity and spellcasting may vary depending on the game system and any additional rules or house rules implemented by the game master.

### User

What are examples of move-equivalent actions?

### ChatGPT


In some tabletop RPG systems, move-equivalent actions are actions that take about the same amount of time as moving a short distance but don't necessarily involve physical movement. Here are some examples:

- **Drawing or Sheathing a Weapon**: Typically, drawing a weapon from a sheath or holster or putting it away is considered a move-equivalent action. This action allows characters to prepare for combat or stow their weapons safely.

- **Using a Skill**: Some skill uses, such as using the Heal skill to administer first aid or using the Sleight of Hand skill to pick a lock, might be considered move-equivalent actions, taking about the same amount of time as moving a short distance.

- **Using Some Class Features or Abilities**: Certain class features or abilities might be considered move-equivalent actions, depending on the specific rules of the game system. For example, activating certain rogue abilities or using a monk's ki features might fall into this category.

- **Manipulating an Object**: Performing actions like reloading a crossbow, rummaging through a backpack to retrieve an item, or opening a door might be considered move-equivalent actions in some systems.

- **Minor Spellcasting or Spell-Like Abilities**: Some spells or spell-like abilities might have a casting time of one move-equivalent action, allowing characters to cast a quick spell or produce a magical effect without taking up their entire turn.

These are just a few examples, and the specific move-equivalent actions available to characters can vary depending on the rules of the game system being used and any additional rules or house rules implemented by the game master.

### User

What are examples of full-round actions?

### ChatGPT



Full-round actions are actions that typically consume the entirety of a character's turn in combat. These actions often require more time or effort than standard or move-equivalent actions. Here are some examples:

- **Full Attack**: A character can make multiple attacks with a weapon or unarmed strike during a full attack action. This action allows the character to use their entire turn to make a series of attacks, typically at a penalty to their attack rolls.

- **Casting a Full-Round Spell**: Some spells have a casting time of one full round, requiring the caster to spend their entire turn casting the spell. These spells often have powerful effects but require significant time and concentration to cast.

- **Using Some Special Abilities**: Certain class features or abilities might require a full-round action to use. For example, activating certain bardic performances, raging as a barbarian, or using a monk's flurry of blows ability might consume a character's entire turn.

- **Full-Round Skill Uses**: Some skill uses might require a full round to complete, especially if they involve complex actions or extended periods of time. For example, crafting a complex item or performing a lengthy performance might be considered full-round actions.

- **Using Some Combat Maneuvers**: Certain combat maneuvers or special attacks might require a full-round action to execute. For example, attempting to sunder an opponent's weapon or perform a devastating charge might take an entire turn to complete.

- **Total Defense**: A character can choose to focus entirely on defending themselves, gaining a bonus to their Armor Class but forgoing any other actions during their turn.

These examples illustrate the range of actions that might consume a character's entire turn in combat. Full-round actions often represent more significant or complex actions that require careful consideration and planning during combat encounters.

## Generate raw code

### User

Make a table of all actions discussed so far. Have a column for whether action is standard, move or full round action. Have a column for whether the action may provoke attack of opportunity.

### ChatGPT

Here's a table summarizing the actions discussed so far, including whether they are standard, move, or full-round actions, and whether they may provoke attacks of opportunity:

| Action                       | Type            | May Provoke AoO? |
|------------------------------|-----------------|------------------|
| Attack                       | Standard        | Yes              |
| Cast a Spell                 | Standard        | Yes              |
| Ready                        | Standard        | No               |
| Grapple (Initiating)         | Standard        | Yes              |
| Shove                        | Standard        | Yes              |
| Use an Object                | Standard        | No               |
| Move                         | Move            | No               |
| Climb                        | Move            | No               |
| Swim                         | Move            | No               |
| Crawl                        | Move            | No               |
| Jump                         | Move            | No               |
| Stand Up                     | Move            | No               |
| Mount/Dismount               | Move            | No               |
| Squeeze                      | Move            | No               |
| Fly                          | Move            | No               |
| Disarm                       | Special         | Yes              |
| Trip                         | Special         | Yes              |
| Sunder                       | Special         | Yes              |
| Feint                        | Special         | Yes              |
| Bull Rush                    | Special         | Yes              |
| Grapple (Initiating)         | Special         | Yes              |
| Overrun                      | Special         | Yes              |
| Drawing/Sheathing a Weapon   | Move-Equivalent | No               |
| Using a Skill                | Move-Equivalent | No               |
| Using Some Class Features    | Move-Equivalent | Varies           |
| Manipulating an Object       | Move-Equivalent | No               |
| Minor Spellcasting           | Move-Equivalent | No               |
| Full Attack                  | Full-Round      | Yes              |
| Casting a Full-Round Spell   | Full-Round      | Yes              |
| Using Some Special Abilities | Full-Round      | Varies           |
| Full-Round Skill Uses        | Full-Round      | No               |
| Using Some Combat Maneuvers  | Full-Round      | Yes              |
| Total Defense                | Full-Round      | No               |


This table provides a comprehensive overview of the actions discussed, categorizing them by type and indicating whether they may provoke attacks of opportunity.


### User

Write this table as a JSON object. For the Action column, use field name "name". For the type column, use field name "action_type". For the May Provoke AoO column, use the field name "aoo". Also add a description field.

### ChatGPT


```json

[
  {
    "name": "Attack",
    "action_type": "Standard",
    "aoo": "Yes",
    "description": "Engage in melee or ranged combat with a weapon or unarmed strike."
  },
  {
    "name": "Cast a Spell",
    "action_type": "Standard",
    "aoo": "Yes",
    "description": "Use a spell slot to cast a spell from a spell list."
  },
  {
    "name": "Ready",
    "action_type": "Standard",
    "aoo": "No",
    "description": "Prepare an action to trigger in response to a specific circumstance."
  },
  {
    "name": "Grapple (Initiating)",
    "action_type": "Standard",
    "aoo": "Yes",
    "description": "Attempt to seize an opponent and restrain them in a grapple."
  },
  {
    "name": "Shove",
    "action_type": "Standard",
    "aoo": "Yes",
    "description": "Attempt to push a creature, potentially knocking them prone or moving them."
  },
  {
    "name": "Use an Object",
    "action_type": "Standard",
    "aoo": "No",
    "description": "Interact with an item or object in the environment."
  },
  {
    "name": "Move",
    "action_type": "Move",
    "aoo": "No",
    "description": "Move up to your speed across the battlefield."
  },
  {
    "name": "Climb",
    "action_type": "Move",
    "aoo": "No",
    "description": "Ascend or descend a surface, using movement and possibly an Athletics check."
  },
  {
    "name": "Swim",
    "action_type": "Move",
    "aoo": "No",
    "description": "Move through water, using movement and possibly an Athletics check."
  },
  {
    "name": "Crawl",
    "action_type": "Move",
    "aoo": "No",
    "description": "Move on hands and knees, typically through difficult terrain."
  },
  {
    "name": "Jump",
    "action_type": "Move",
    "aoo": "No",
    "description": "Leap across obstacles or gaps, using movement and possibly an Athletics check."
  },
  {
    "name": "Stand Up",
    "action_type": "Move",
    "aoo": "No",
    "description": "Recover from being prone, using half of your movement speed."
  },
  {
    "name": "Mount/Dismount",
    "action_type": "Move",
    "aoo": "No",
    "description": "Get on or off a mount, using movement."
  },
  {
    "name": "Squeeze",
    "action_type": "Move",
    "aoo": "No",
    "description": "Move through a tight space, using movement but at half speed."
  },
  {
    "name": "Fly",
    "action_type": "Move",
    "aoo": "No",
    "description": "If you have a flying speed, move through the air using movement."
  },
  {
    "name": "Disarm",
    "action_type": "Special",
    "aoo": "Yes",
    "description": "Attempt to knock a weapon or item out of an opponent's grasp."
  },
  {
    "name": "Trip",
    "action_type": "Special",
    "aoo": "Yes",
    "description": "Attempt to knock an opponent prone by sweeping their legs out from under them."
  },
  {
    "name": "Sunder",
    "action_type": "Special",
    "aoo": "Yes",
    "description": "Try to break or destroy an opponent's weapon, shield, or other item they are holding."
  },
  {
    "name": "Feint",
    "action_type": "Special",
    "aoo": "Yes",
    "description": "Make a deceptive move or fake out an opponent to create an opening for a subsequent attack."
  },
  {
    "name": "Bull Rush",
    "action_type": "Special",
    "aoo": "Yes",
    "description": "Attempt to push an opponent backward, potentially knocking them prone or into a hazard."
  },
  {
    "name": "Overrun",
    "action_type": "Special",
    "aoo": "Yes",
    "description": "Charge through an opponent's space to move past them."
  },
  {
    "name": "Drawing/Sheathing a Weapon",
    "action_type": "Move-Equivalent",
    "aoo": "No",
    "description": "Typically, drawing a weapon from a sheath or holster or putting it away."
  },
  {
    "name": "Using a Skill",
    "action_type": "Move-Equivalent",
    "aoo": "No",
    "description": "Performing skill actions such as administering first aid or picking a lock."
  },
  {
    "name": "Using Some Class Features",
    "action_type": "Move-Equivalent",
    "aoo": "Varies",
    "description": "Activating certain class features or abilities."
  },
  {
    "name": "Manipulating an Object",
    "action_type": "Move-Equivalent",
    "aoo": "No",
    "description": "Performing actions like reloading a crossbow or opening a door."
  },
  {
    "name": "Minor Spellcasting",
    "action_type": "Move-Equivalent",
    "aoo": "No",
    "description": "Casting a spell with a short casting time."
  },
  {
    "name": "Full Attack",
    "action_type": "Full-Round",
    "aoo": "Yes",
    "description": "Make multiple attacks with a weapon or unarmed strike."
  },
  {
    "name": "Casting a Full-Round Spell",
    "action_type": "Full-Round",
    "aoo": "Yes",
    "description": "Casting a spell with a casting time of one full round."
  },
  {
    "name": "Using Some Special Abilities",
    "action_type": "Full-Round",
    "aoo": "Varies",
    "description": "Activating certain special abilities or class features."
  },
  {
    "name": "Full-Round Skill Uses",
    "action_type": "Full-Round",
    "aoo": "No",
    "description": "Performing skill actions that require a full round to complete."
  },
  {
    "name": "Using Some Combat Maneuvers",
    "action_type": "Full-Round",
    "aoo": "Yes",
    "description": "Performing certain combat maneuvers or special attacks."
  },
  {
    "name": "Total Defense",
    "action_type": "Full-Round",
    "aoo": "No",
    "description": "Focusing entirely on defending yourself, gaining a bonus to your Armor Class."
  }
]
```

### User

Write a Python class encapsulating the action object using the pydantic package.

### ChatGPT


Here's a Python class encapsulating the action object using the Pydantic package:

```python

from pydantic import BaseModel

class Action(BaseModel):
    name: str
    action_type: str
    aoo: str
    description: str

    class Config:
        allow_mutation = False
```

You can use this Action class to create instances representing different actions discussed in the table. Here's how you can create an instance:

```python

action_data = {
    "name": "Attack",
    "action_type": "Standard",
    "aoo": "Yes",
    "description": "Engage in melee or ranged combat with a weapon or unarmed strike."
}

action_instance = Action(**action_data)
print(action_instance)
```

This class defines four fields: name, action_type, aoo, and description, which correspond to the fields in the JSON object. The Config class ensures that instances of Action are immutable, meaning their values cannot be changed after creation.

### User

Write some pytest tests for Action to prove the class works. Test initialization, loading from dict and saving to dict.

### ChatGPT


Sure, here's a set of pytest tests for the Action class:

```python
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
```

These tests cover the initialization of an Action object, loading from a dictionary, and saving to a dictionary. The sample_action_data fixture provides sample data for testing. You can run these tests using pytest to ensure that the Action class works as expected.

## Request changes

## Feedback working results and request documentation comments



