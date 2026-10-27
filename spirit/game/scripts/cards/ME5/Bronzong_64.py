"""Bronzong (ME5 64 -- JP M5 062; English PBL/64). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.session.effects import is_evolution_pokemon


class _LessFromEvolutions(Passive):
    def modify_damage_taken(self, calc, carrier):
        if (calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                and calc.attacker is not None and is_evolution_pokemon(calc.attacker)):
            calc.amount = max(0, calc.amount - 100)


async def metal_block(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _LessFromEvolutions())


card = PokemonCardDef(
    guid="a11eeb34-9e00-5547-8e6e-9e2bc516e78f",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name",
    display_name="Bronzong",
    searchable_by=["Bronzong", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name",
    family_id=436,
    abilities=[
        Attack(
            title="Gentle Slap",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=40,
        ),
        Attack(
            title="Metal Block",
            game_text="During your opponent's next turn, this Pokémon takes 100 less damage from attacks from Evolution Pokémon (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=metal_block,
        ),
    ],
)
