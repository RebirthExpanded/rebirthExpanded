"""Steelix (ME1 93 -- JP M1L 045; English MEG/150, MEG/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _six_left(ctx) -> bool:
    return ac.count_prizes_remaining("mine")(ctx) == 6


card = PokemonCardDef(
    guid="15637a1c-bb67-52d2-a987-00cbf5cdfabe",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Attack(
            title="Welcoming Tail",
            game_text="If you have exactly 6 Prize cards remaining, this attack does 200 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=ac.bonus_if(_six_left, 200),
        ),
        Attack(
            title="Skull Bash",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
