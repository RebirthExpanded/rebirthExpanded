"""Flamigo ex (SV08 160 -- JP SVP 124; English SSP/160). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _same_energy(ctx) -> bool:
    return ac.count_energy("self", cards=True)(ctx) == ac.count_energy("defender", cards=True)(ctx)


card = PokemonCardDef(
    guid="871757b0-91ff-59a2-8107-638ca94111d4",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigoex.Name",
    display_name="Flamigo ex",
    searchable_by=["Flamigo ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=160,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title="Precise Beak",
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_same_energy, 100),
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=200,
            effect=ac.recoil_attack(30),
        ),
    ],
)
