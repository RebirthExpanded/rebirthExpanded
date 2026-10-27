"""Reshiram (ME6A 8 -- JP M6a 008; English 30C/14). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



def _has_energy_type(t):
    def cond(ctx) -> bool:
        return any(is_energy_of_type(e, t) for e in ctx.attached_energies(ctx.attacker))
    return cond


card = PokemonCardDef(
    guid="64aee5bc-2284-5ec1-9eb4-2de1ab27b0a4",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Reshiram.Name",
    display_name="Reshiram",
    searchable_by=["Reshiram", "Basic"],
    subtypes=["Basic"],
    collector_number=8,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=643,
    abilities=[
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
        Attack(
            title="Laser Flame",
            game_text="If this Pokémon has any Lightning Energy attached, this attack does 80 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_has_energy_type(PokemonTypes.LIGHTNING), 80),
        ),
    ],
)
