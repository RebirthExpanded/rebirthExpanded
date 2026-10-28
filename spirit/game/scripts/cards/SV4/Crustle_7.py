"""Crustle (SV4 7 -- JP SV4K 005; English PAR/183, PAR/7). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_evolution_pokemon


class _CragBash(Passive):
    def modify_damage_taken(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                and calc.attacker is not None and is_evolution_pokemon(calc.attacker)):
            calc.amount = max(0, calc.amount - 100)


async def crag_bash(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _CragBash())


card = PokemonCardDef(
    guid="48fbaf50-b04e-5167-890c-90dcd3e2f592",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=7,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Attack(
            title="Confront",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Crag Bash",
            game_text="During your opponent's next turn, this Pokémon takes 100 less damage from attacks from Evolution Pokémon (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=crag_bash,
        ),
    ],
)
