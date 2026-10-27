"""Poochyena (SV06 113 -- JP SV6 066; English TWM/113). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="efe0ccfe-6ef7-5085-8960-5b7e04d9bea3",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    display_name="Poochyena",
    searchable_by=["Poochyena", "Basic"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=261,
    abilities=[
        Attack(
            title="Continuous Steps",
            game_text="Flip a coin until you get tails. This attack does 10 damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=10),
        ),
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
