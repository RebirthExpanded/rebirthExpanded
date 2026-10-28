"""Cetitan (SV2 55 -- JP SV2P 022; English PAL/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_special_energy


def _special(ctx) -> bool:
    return any(is_special_energy(e) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="204f687a-a310-5cff-840a-65632026c1f7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name",
    display_name="Cetitan",
    searchable_by=["Cetitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Attack(
            title="Icicle Missile",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Special Horn",
            game_text="If this Pokémon has any Special Energy attached, this attack does 140 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_special, 140),
        ),
    ],
)
