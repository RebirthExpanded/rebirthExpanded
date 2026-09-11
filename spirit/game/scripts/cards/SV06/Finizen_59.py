"""Finizen (SV - Twilight Masquerade 59/167 -- JP SV6 034/101).

Basic Water Pokemon. HP 70, weakness Lightning x2, retreat 1.

  Aqua Slash  [W] 30  During your next turn, this Pokemon can't attack.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="fe9669e8-aa02-5eb6-972f-c91fab65b1d6",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    display_name="Finizen",
    searchable_by=["Finizen", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="SV06",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=963,
    regulation_mark="H",
    abilities=[
        Attack(
            title="Aqua Slash",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            locks_next_turn=True,
        ),
    ],
)
