"""Tinkatuff (SV4 84 -- JP SV4M 036; English PAR/84). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _has_metal(ctx) -> bool:
    return any(is_energy_of_type(e, PokemonTypes.METAL) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="ddacf079-7eee-5162-9e45-d83230588fbc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    display_name="Tinkatuff",
    searchable_by=["Tinkatuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=84,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Alloy Aswing",
            game_text="If this Pokémon has any Metal Energy attached, this attack does 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(_has_metal, 40),
        ),
    ],
)
