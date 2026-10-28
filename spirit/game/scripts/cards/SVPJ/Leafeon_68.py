"""Leafeon (SVPJ 68 -- JP SVP 068; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import CLIENT_SPECIAL_CONDITION_NAMES

_BY_NAME = {name: cond for cond, name in CLIENT_SPECIAL_CONDITION_NAMES.items()}


async def _cure_all(ctx, pokemon):
    for name in list(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
        if name in _BY_NAME:
            await ctx.cure_condition(pokemon, _BY_NAME[name])


async def aroma_wind(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await _cure_all(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="8dff025d-ff18-54bb-b72e-b30422c6f329",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeon.Name",
    display_name="Leafeon",
    searchable_by=["Leafeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="SVPJ",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Aroma Wind",
            game_text="This Pokémon recovers from all Special Conditions.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=aroma_wind,
        ),
    ],
)
