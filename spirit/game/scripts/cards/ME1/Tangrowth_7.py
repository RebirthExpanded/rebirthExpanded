"""Tangrowth (ME1 7 -- JP M1S 002; English MEG/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


def _two_extra(ctx) -> bool:
    return ac.count_energy("self")(ctx) >= 6


card = PokemonCardDef(
    guid="12a37806-aa7c-5822-b547-4ef224a63350",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name",
    display_name="Tangrowth",
    searchable_by=["Tangrowth", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    family_id=114,
    abilities=[
        Attack(
            title="Absorb",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Pumped-Up Whip",
            game_text="If this Pokémon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 140 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(_two_extra, 140),
        ),
    ],
)
