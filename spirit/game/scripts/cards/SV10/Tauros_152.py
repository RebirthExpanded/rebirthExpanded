"""Tauros (SV10 152 -- JP SV9a 053; English DRI/152). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


card = PokemonCardDef(
    guid="bf60acb8-8238-5f4a-9ff3-6bb2a95a2ef5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Horn Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Clean Hit",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 50 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_defender, 50),
        ),
    ],
)
