"""Quagsire (SVP 156 -- JP SVP 122; English SVP/156). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_card


async def drenched_headbutt(ctx):
    top = list(ctx.deck_top(3))
    if top:
        await ctx.discard_cards(top)
    n = sum(1 for c in top if is_energy_card(c))
    if n:
        await ctx.deal_damage(80 * n)


card = PokemonCardDef(
    guid="75ae9187-8618-5d5f-8dad-0b7ccd694acc",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name",
    display_name="Quagsire",
    searchable_by=["Quagsire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=156,
    set_code="SVP",
    regulation_mark="H",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Rollout",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
        Attack(
            title="Drenched Headbutt",
            game_text="Discard the top 3 cards of your deck. This attack does 80 damage for each Energy card you discarded in this way.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="x",
            effect=drenched_headbutt,
        ),
    ],
)
