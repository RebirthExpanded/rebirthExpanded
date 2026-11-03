"""Meloetta (BWPJ 325 -- JP WAK 025; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9b639956-7251-5124-ae7e-17c40016e3a2",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name",
    display_name="Meloetta",
    searchable_by=["Meloetta", "Basic"],
    subtypes=["Basic"],
    collector_number=325,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=648,
    abilities=[
        Attack(
            title="Slap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Psychic Magic",
            game_text="Flip 2 coins. If both of them are heads, this attack does 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=ac.flip_bonus(40, coins=2),
        ),
    ],
)
