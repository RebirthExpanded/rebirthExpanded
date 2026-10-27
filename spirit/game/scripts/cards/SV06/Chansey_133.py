"""Chansey (SV06 133 -- JP SV6 084; English TWM/133, TWM/187). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.card_effects.trainers import is_basic_energy_card


async def lucky_attachment(ctx):
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Basic Energy card to attach")
    if picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach it to")
        if target is not None:
            await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="f69391c5-1191-5f7d-9821-e0f0dc4371d4",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name",
    display_name="Chansey",
    searchable_by=["Chansey", "Basic"],
    subtypes=["Basic"],
    collector_number=133,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=440,
    abilities=[
        Attack(
            title="Lucky Attachment",
            game_text="Attach a Basic Energy card from your hand to 1 of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lucky_attachment,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_hit_then_lock,
        ),
    ],
)
