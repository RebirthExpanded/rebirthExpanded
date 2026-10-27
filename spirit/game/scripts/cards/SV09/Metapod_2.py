"""Metapod (SV09 2 -- JP SV9 002; English JTG/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _HardenShield(Passive):
    def modify_damage_taken(self, calc, carrier):
        if calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target and calc.amount <= 60:
            calc.amount = 0


async def harden(ctx):
    ctx.add_passive_through_opponents_turn(ctx.attacker, _HardenShield())


card = PokemonCardDef(
    guid="88fd2c6f-c435-57fb-881e-f75ab0a667c2",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    display_name="Metapod",
    searchable_by=["Metapod", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks if that damage is 60 or less.",
            cost={PokemonTypes.GRASS: 1},
            effect=harden,
        ),
    ],
)
