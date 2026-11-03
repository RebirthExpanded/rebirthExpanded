"""Cetitan ex (SV10 65 -- JP SV10 032; English DRI/210, DRI/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


async def _crushing_press(ctx):
    """You may discard a Stadium in play. If you do, this attack does 140 more damage."""
    bonus = 0
    if ctx.stadium_in_play() is not None and await ctx.ask_yes_no(
            "Discard the Stadium in play for 140 more damage?"):
        if await ctx.discard_stadium() is not None:
            bonus = 140
    await ctx.deal_damage(ctx.ability.damage + bonus)


card = PokemonCardDef(
    guid="eea45a8e-264e-5732-b22f-ca035fdba61a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitanex.Name",
    display_name="Cetitan ex",
    searchable_by=["Cetitan ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=65,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Ability(
            title="Snow Camouflage",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.",
            passive=pc.OmegaBarrierPassive(),
        ),
        Attack(
            title="Crushing Press",
            game_text="You may discard a Stadium in play. If you do, this attack does 140 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=_crushing_press,
        ),
    ],
)
