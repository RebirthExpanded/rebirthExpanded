"""Probopass (SV10 98 -- JP SV10 052; English DRI/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _stadium(ctx) -> bool:
    return ctx.stadium_in_play() is not None


card = PokemonCardDef(
    guid="c86f85a4-4f16-5a37-8331-b1e47f39d788",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Probopass.Name",
    display_name="Probopass",
    searchable_by=["Probopass", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name",
    family_id=299,
    abilities=[
        Attack(
            title="Power Gem",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Mountain Drop",
            game_text="If a Stadium is in play, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_stadium, 70),
        ),
    ],
)
