"""Omanyte (SV035 138 -- JP SV2a 138; English MEW/138, MEW/180). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def tentacular_return(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d) or not ctx.attached_energies(d):
        return
    picks = await ctx.choose_cards(list(ctx.attached_energies(d)), 1, minimum=1, prompt="Choose an Energy to put into your opponent's hand")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="ff2e5539-93f4-5d6b-b917-13298bac843b",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    display_name="Omanyte",
    searchable_by=["Omanyte", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.trainer.AntiqueHelixFossil.Name",
    family_id=138,
    abilities=[
        Attack(
            title="Tentacular Return",
            game_text="Put an Energy attached to your opponent's Active Pokémon into their hand.",
            cost={PokemonTypes.WATER: 2},
            damage=50,
            effect=tentacular_return,
        ),
    ],
)
