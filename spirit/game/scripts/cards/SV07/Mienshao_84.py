"""Mienshao (SV07 84 -- JP SV7 056; English SCR/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _small_hand(ctx) -> bool:
    return len(ctx.hand(ctx.opponent_id)) <= 5


card = PokemonCardDef(
    guid="22999556-0553-5e07-9a5f-e6f0389ee5df",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienshao.Name",
    display_name="Mienshao",
    searchable_by=["Mienshao", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    family_id=619,
    abilities=[
        Attack(
            title="Gale Roundhouse",
            game_text="If your opponent has 5 or fewer cards in their hand, this attack does 60 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_small_hand, 60),
        ),
    ],
)
