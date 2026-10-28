"""Krokorok (SV1 116 -- JP SV1S 043; English SVI/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _last_prize(ctx) -> bool:
    return ac.count_prizes_remaining("opponent")(ctx) == 1


card = PokemonCardDef(
    guid="daa30969-dd85-5695-8f6d-0f3d39e54411",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    display_name="Krokorok",
    searchable_by=["Krokorok", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=116,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Payback",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 90 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_last_prize, 90),
        ),
        Attack(
            title="Corkscrew Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
    ],
)
