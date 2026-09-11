"""Manaphy-EX (XY - BREAKpoint 32/122 -- JP XY9-B 021/080).

Basic Water Pokemon-EX. HP 120, weakness Grass x2, retreat 1.

  Ability  Aqua Tube  Each of your Pokemon that has any [W] Energy attached
                      to it has no Retreat Cost.
  Mineral Pump  [WW] 60  Heal 30 damage from each of your Benched Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import retreat_free_when
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.models.board import BoardState


def _has_water_energy(pokemon, carrier) -> bool:
    if pokemon.owning_player_id != carrier.owning_player_id:
        return False
    return any(energy_provides_type(e, PokemonTypes.WATER.value)
               for e in BoardState.attached_energies(pokemon))


async def mineral_pump(ctx):
    await ctx.deal_damage()
    for pokemon in list(ctx.my_bench()):
        await ctx.heal(30, pokemon)


card = PokemonCardDef(
    guid="4eb77b31-3279-5cd6-a31a-a745defad562",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ManaphyEX.Name",
    display_name="Manaphy-EX",
    searchable_by=["Manaphy-EX", "Basic", "EX", "ManaphyEX"],
    subtypes=["Basic", "EX"],
    collector_number=32,
    set_code="XY9",
    rarity=Rarities.RareHoloEX,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=490,
    abilities=[
        Ability(
            title="Aqua Tube",
            game_text="Each of your Pokémon that has any [W] Energy attached to it has no Retreat Cost.",
            passive=retreat_free_when(_has_water_energy),
        ),
        Attack(
            title="Mineral Pump",
            game_text="Heal 30 damage from each of your Benched Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=mineral_pump,
        ),
    ],
)
