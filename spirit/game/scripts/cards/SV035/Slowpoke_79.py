"""Slowpoke (SV035 79 -- JP SV2a 079; English MEW/79). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES

_BY_NAME = {name: cond for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


async def sea_bathing(ctx):
    me = ctx.attacker
    await ctx.heal(30, me)
    for name in list(me.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        if name in _BY_NAME:
            await ctx.cure_condition(me, _BY_NAME[name])


card = PokemonCardDef(
    guid="69f522b1-02f8-5f8b-9064-791925146c3b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slowpoke.Name",
    display_name="Slowpoke",
    searchable_by=["Slowpoke", "Basic"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=79,
    abilities=[
        Attack(
            title="Sea Bathing",
            game_text="Heal 30 damage from this Pokémon, and it recovers from all Special Conditions.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=sea_bathing,
        ),
        Attack(
            title="Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
