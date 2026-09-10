"""Relicanth (SV - Temporal Forces 84/162 -- JP SV5K 034/071).

Basic Fighting. HP 100, weakness Grass x2, retreat 1, regulation mark H.

  Ability  Memory Dive  Each of your evolved Pokemon can use any attack
                        from its previous Evolutions. (You still need the
                        necessary Energy to use each attack.)

  Razor Fin  [FC] 30

Memory Energy for the whole side, and Shining Celebi's Time Recall
word-for-word. All three walk the cards tucked under an evolved Pokemon
and hand back their Attacks unchanged, so the costs and effects are the
pre-evolution cards' own.

The difference that matters at the table is the one this pool asked for:
this is an Ability, so an ability lock -- Path to the Peak, Garbotoxin,
Alolan Muk on a Basic like this one -- switches it off, where Memory Energy
keeps working through all of them.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import PreEvolutionAttacksPassive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="b3cf4bab-dcd4-5bfd-9255-a567c933b3e6",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=369,
    abilities=[
        Ability(
            title="Memory Dive",
            game_text="Each of your evolved Pokémon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            passive=PreEvolutionAttacksPassive(),
        ),
        Attack(
            title="Razor Fin",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
