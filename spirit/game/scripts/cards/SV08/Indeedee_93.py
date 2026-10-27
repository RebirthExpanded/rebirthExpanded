"""Indeedee (SV08 93 -- JP SV8 058; English SSP/93, SVP/154). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES

_BY_NAME = {name: cond for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


async def obliging_heal(ctx):
    if not getattr(ctx, "benched_from_hand", True):
        return
    active = ctx.board.active_pokemon(ctx.player_id)
    if active is None or not await ctx.ask_yes_no("Use Obliging Heal?"):
        return
    await ctx.heal(30, active)
    names = [n for n in (active.get_attribute(AttrID.SPECIAL_CONDITIONS) or []) if n in _BY_NAME]
    if names:
        index = 0
        if len(names) > 1:
            index = await ctx.choose("Recover from which Special Condition?", [str(n) for n in names])
        await ctx.cure_condition(active, _BY_NAME[names[index if isinstance(index, int) else 0]])


card = PokemonCardDef(
    guid="fd88f883-cbba-54bd-b89b-e5341267ab18",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name",
    display_name="Indeedee",
    searchable_by=["Indeedee", "Basic"],
    subtypes=["Basic"],
    collector_number=93,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=876,
    abilities=[
        Ability(
            title="Obliging Heal",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may heal 30 damage from your Active Pokémon and have it recover from a Special Condition.",
            trigger=Triggers.ON_PLAY,
            effect=obliging_heal,
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
