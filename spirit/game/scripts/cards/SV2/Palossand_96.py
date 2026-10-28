"""Palossand (SV2 96 -- JP SV2D 030; English PAL/96). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _my_stadium(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    return stadium is not None and stadium.owning_player_id == ctx.player_id


card = PokemonCardDef(
    guid="d82c1161-7aac-5d8d-a61d-e4ad1ed1c5a5",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name",
    display_name="Palossand",
    searchable_by=["Palossand", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Spooky Shot",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Earthen Power",
            game_text="If you have a Stadium in play, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_my_stadium, 80),
        ),
    ],
)
