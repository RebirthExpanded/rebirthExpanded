"""Shining Celebi (SM Black Star Promos SM79 -- JP SM3+ 004/072).

Basic Grass. HP 70, weakness Fire x2, retreat 1.

  Ability  Time Recall  Each of your evolved Pokemon can use any attack
                        from its previous Evolutions. (You still need the
                        necessary Energy to use each attack.)

  Leaf Step  [GC] 30

Celebi-EX's Time Recall on a Basic with no rule box, and the same text
Relicanth's Memory Dive carries, so the three share one passive. Being an
Ability, it goes quiet under an ability lock -- which is what separates it
from Memory Energy, whose lending nothing switches off.

The pool's first SM Black Star Promo, so Promo_SM joins the Expanded set
list (it was already registered in sets.json).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import PreEvolutionAttacksPassive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef

card = PokemonCardDef(
    guid="1da3e345-46cc-5844-88fb-3a144c6254bf",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ShiningCelebi.Name",
    display_name="Shining Celebi",
    searchable_by=["Shining Celebi", "Basic", "ShiningCelebi"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=251,
    abilities=[
        Ability(
            title="Time Recall",
            game_text="Each of your evolved Pokémon can use any attack from its previous Evolutions. (You still need the necessary Energy to use each attack.)",
            passive=PreEvolutionAttacksPassive(),
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
