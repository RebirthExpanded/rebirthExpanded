"""Polteageist (SV3 98 -- JP SV2P 036; English OBF/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_item_card, is_pokemon_tool


async def antique_collecting(ctx):
    pool = [c for c in ctx.discard_pile() if is_item_card(c) or is_pokemon_tool(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Item or Pokémon Tool cards")
        if picks:
            await ctx.put_in_hand(picks)


async def pour_tea(ctx):
    d = ctx.opponent_active()
    if d is not None:
        await ctx.deal_damage(50, target=d, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="2e10a9a2-ead7-5193-8133-d9f41438a29f",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Polteageist.Name",
    display_name="Polteageist",
    searchable_by=["Polteageist", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=98,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistea.Name",
    family_id=854,
    abilities=[
        Attack(
            title="Antique Collecting",
            game_text="Put up to 2 in any combination of Item cards and Pokémon Tool cards from your discard pile into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=antique_collecting,
        ),
        Attack(
            title="Pour Tea",
            game_text="Put 5 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=pour_tea,
        ),
    ],
)
