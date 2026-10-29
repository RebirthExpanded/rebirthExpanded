"""Deoxys VMAX (Promo_SWSH 267 -- JP SPD 006; English SP/267). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import is_pokemon_v, subtypes_for


def _vstar_attacker(pokemon) -> bool:
    return "VSTAR" in subtypes_for(pokemon.archetype_id)


card = PokemonCardDef(
    guid="234003f6-2cdb-5a41-a50b-7c6efdae1015",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVMAX.Name",
    display_name="Deoxys VMAX",
    searchable_by=["Deoxys VMAX", "VMAX"],
    subtypes=["VMAX"],
    collector_number=267,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloVMAX,
    hp=330,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VMAX,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    family_id=386,
    abilities=[
        Ability(
            title="Protective DNA",
            game_text="All of your Pokémon take 30 less damage from attacks from your opponent's Pokémon VSTAR (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(30, protects="team", attacker_pred=_vstar_attacker),
        ),
        Attack(
            title="Max Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=su.heal_attack(30),
        ),
    ],
)
