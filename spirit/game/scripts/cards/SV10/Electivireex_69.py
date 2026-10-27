"""Electivire ex (SV10 69 -- JP SV9a 035; English DRI/212, DRI/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _two_extra(ctx) -> bool:
    return ac.count_energy("self")(ctx) >= 5


card = PokemonCardDef(
    guid="ccb8b53c-f90d-5745-8cd8-cfb3f367a2e8",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivireex.Name",
    display_name="Electivire ex",
    searchable_by=["Electivire ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=69,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=239,
    abilities=[
        Attack(
            title="Dual Bolt",
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(50, pool="any", count=2),
        ),
        Attack(
            title="High-Voltage Press",
            game_text="If this Pokémon has at least 2 extra Energy attached (in addition to this attack's cost), this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            damage_operator="+",
            effect=ac.bonus_if(_two_extra, 100),
        ),
    ],
)
