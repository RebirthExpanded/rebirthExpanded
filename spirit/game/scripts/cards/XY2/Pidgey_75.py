"""Pidgey (XY - Flashfire 75/106).

Basic Colorless Pokemon. HP 60, weakness Lightning x2, resistance
Fighting -20, retreat 1.

  Peck Off [C] 10  Before doing damage, discard all Pokemon Tool cards
                   attached to your opponent's Active Pokemon.

"Before doing damage" is the whole of the ordering: the Tools go first, so
one that would have changed the damage (Muscle Band and friends) is
already gone when the 10 lands. Both Tool trainer types count -- the
XY-era Team Flare Hyper Gear is a Pokemon Tool F.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, TrainerType
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


async def peck_off(ctx):
    """Strip the Defending Pokemon's Tools, then hit for 10."""
    defender = ctx.defender
    tools = [c for c in (defender.children if defender else [])
             if c.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES]
    if tools:
        await ctx.discard_cards(tools)
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="f25ec856-3563-55dd-9190-27b03e825c3a",
    key="XY2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name",
    display_name="Pidgey",
    searchable_by=["Pidgey", "Basic", "Pidgey"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="XY2",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=16,
    abilities=[
        Attack(
            title="Peck Off",
            game_text=("Before doing damage, discard all Pokémon Tool cards "
                       "attached to your opponent's Active Pokémon."),
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=peck_off,
        ),
    ],
)
