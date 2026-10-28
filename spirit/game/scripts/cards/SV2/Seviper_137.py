"""Seviper (SV2 137 -- JP SV1a 056; English PAL/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


card = PokemonCardDef(
    guid="006c1086-3102-5d47-a51c-6228ab032051",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=336,
    abilities=[
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title="Cross-Cut",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 50 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_defender, 50),
        ),
    ],
)
