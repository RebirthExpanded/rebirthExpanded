"""Deoxys VSTAR (Promo_SWSH 268 -- JP SPD 007; English SP/268). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import is_pokemon_v, subtypes_for

from spirit.game.card_effects.passives_common import is_in_active_spot


def _bench_v(pokemon) -> bool:
    return is_pokemon_v(pokemon.archetype_id) and not is_in_active_spot(pokemon)


def _both_actives_energy(ctx) -> int:
    return sum(len(ctx.attached_energies(p)) for p in (ctx.attacker, ctx.opponent_active()) if p is not None)


card = PokemonCardDef(
    guid="fc4d00fd-2e27-5480-85b6-1f78d8a5f9dc",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysVSTAR.Name",
    display_name="Deoxys VSTAR",
    searchable_by=["Deoxys VSTAR", "VSTAR"],
    subtypes=["VSTAR"],
    collector_number=268,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DeoxysV.Name",
    family_id=386,
    abilities=[
        Attack(
            title="Psychic Javelin",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon V. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=ac.snipe_attack(60, pool=_bench_v, also_base=True),
        ),
        Attack(
            title="Star Force",
            game_text="This attack does 60 damage for each Energy attached to both Active Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="x",
            effect=ac.damage_per(_both_actives_energy, 60),
            vstar=True,
        ),
    ],
)
