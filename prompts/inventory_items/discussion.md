# Discussion

## Prompts to prime the pump

- Tell me about the D20 game system.
- What does a player do in D20?
- What is a PC?
- What tools does a player use to keep track of attributes and inventory of a PC during a D20 game session?
- What rules must a player follow related to inventory and equipment?
- Create a PC named Alice, a level 3 wizard.
- Alice adventures until she is level five. She now has more spells and has acquired more equipment. Modify Alice's details.
- Alice adventures more and reaches level 7. Modify Alice's details, equipment, and spells.
- Describe Alice's equipment in detail.
- What attributes and statistics would Alice need to keep track of related to these items in her inventory?
- List these attributes for Alice's bedroll.
- List these attributes for Alice's quarter staff.
- List these attributes for Alice's Ring of Protection.
- Which items Alice owns must she equip to use?
- List the attributes of Alice's Wand of Magic Missiles.
- List properties of Alice's spellbook.
- Alice has a friend named Eve who is a level 7 cleric. Create Eve similarly to Alice.
- List properties of Eve's shield.
- List properties of Eve's chain mail.
- List properties of Eve's mace.
- List properties of Eve's holy symbol.


## Prompts to generate python code

- List the properties of Alice's bedroll as a python dictionary.
- List properties of several of Alice's items as a list of dictionaries in python. List spellbook, wand of magic missiles, ring of protection, rations, waterskin.
- List properties of several of Eve's items in a list of dictionaries in python. List chain mail, mace, shield, holy symbol.
- Create a python class for inventory items with `__init__` and functions to and from dict.
- Add condition and value properties to `InventoryItem`.
- Write a unittest test class to test `__init__`, `to_dict`, and `from_dict`. Use Alice's spellbook as example data.
- What properties do armor items have?
- List five common armor types in D20.
- What properties of chain mail armor must Eve keep track of while playing D20?
- Extend the `InventoryItem` class to `ArmorItem` class and add these properties. Also give an example of chain mail armor represented as a python dictionary.
- That implementation of `ArmorItem` has neglected the condition property of `InventoryItem`. Try again.
- What properties do weapons have in D20?
- Extend the `InventoryItem` class to `WeaponItem` and add these properties. Also give examples of Eve's mace and Alice's bow as python dictionaries representing these items.
- Give the example of Eve's mace as a python dictionary.
- Give the example of Alice's quarterstaff as a python dictionary.
- What ranged weapons would a wizard likely use?
- What ranged weapons would a cleric likely use?
- Give Eve a heavy crossbow and describe its properties.
- Give Eve's heavy crossbow as an example of a python dictionary representing the `WeaponItem` class.
- Write a unittest test case testing `ArmorItem` using Eve's chain mail as an example.
- Write a unittest test case testing `WeaponItem` using Eve's mace as an example.
- What different kinds of magic items exist in D20?
- What properties do magic rings have?
- Extend the `InventoryItem` class for magic rings by adding these properties. Also give an example of Alice's Ring of Protection as a python dictionary.

## Branch for generated raw results

Raw results are in branch [generate/inventory](https://github.com/newexo/d20-ai/tree/generate/inventory).

## Steps to make code actually work

Recorded steps to make code actually work in commit history of branch [refactor/inventory](https://github.com/newexo/d20-ai/tree/refactor/inventory).

1. Delete unused code and fix imports. After this, 8 tests fail with errors.
2. Requested a new unit test for init of ArmorItem. This test fails with an error. Fixed so that test failed without 
error.
3. MagicRing tests consistently have incorrect argument and non-existent fields, magic_type and bonus. After fixing 
errors from MagicRing tests, now 4 tests fail and 5 fail with error.
4. ArmorItem tests consistently have incorrect argument and non-existent fields. Fixed errors. Now 8 tests fail, but 
none with error.
5. All tests for InventoryItem were passing. ArmorItem called super init with arguments in incorrect order. Fixing that 
fixed two failures. The last failure related to ArmorItem was caused by calling ArmorItem with arguments in correct
order.
6. There were two failures for WeaponItem. Some of these were caused by incorrect ordering of arguments for super init.
7. Fix tests for MagicRing.

## Final refactor

Does not seem necessary.

## Documentation comments

Does not seem necessary.
