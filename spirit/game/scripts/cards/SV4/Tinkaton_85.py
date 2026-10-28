"""Tinkaton (SV4 85 -- JP SV4M 037; English PAR/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _has_metal(ctx) -> bool:
    return any(is_energy_of_type(e, PokemonTypes.METAL) for e in ctx.attached_energies(ctx.attacker))


card = PokemonCardDef(
    guid="09970d85-d183-5a66-96fa-3b9de81d48a4",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=85,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Crushing Blow",
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=ac.discard_opponent_energy_attack(1),
        ),
        Attack(
            title="Alloyed Hammer",
            game_text="If this Pokémon has any Metal Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_has_metal, 120),
        ),
    ],
)
