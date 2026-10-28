"""Scovillain ex (SV05 22 -- JP SVP 089; English TEF/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def two_headed_crushing(ctx):
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)
    top = list(ctx.deck_top(1, player_id=ctx.opponent_id))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="38959163-ac50-56a6-8f51-a4d1ccee6e75",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scovillainex.Name",
    display_name="Scovillain ex",
    searchable_by=["Scovillain ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=22,
    set_code="SV05",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Capsakid.Name",
    family_id=951,
    abilities=[
        Attack(
            title="Chili Snapper Bind",
            game_text="Your opponent's Active Pokémon is now Burned. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED, no_retreat=True),
        ),
        Attack(
            title="Two-Headed Crushing",
            game_text="Discard a random card from your opponent's hand. Discard the top card of your opponent's deck.",
            cost={PokemonTypes.GRASS: 2},
            damage=140,
            effect=two_headed_crushing,
        ),
    ],
)
