"""Melmetal (SV05 117 -- JP SV5M 050; English TEF/117). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="7702c281-3836-57e3-b12c-e881745d3c46",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Melmetal.Name",
    display_name="Melmetal",
    searchable_by=["Melmetal", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=117,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meltan.Name",
    family_id=808,
    abilities=[
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Iron Bash",
            game_text="",
            cost={PokemonTypes.METAL: 4, PokemonTypes.COLORLESS: 1},
            damage=230,
        ),
    ],
)
