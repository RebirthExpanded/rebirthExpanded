"""Skeledirge (SV1 38 -- JP SVAL 004; English SVI/38). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


async def passionate_singing(ctx):
    await ctx.deal_damage()
    pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Attach up to 2 Basic Energy cards to your Pokémon")
    for card in picks:
        target = await ctx.choose_pokemon(ctx.my_pokemon_in_play(), "Choose 1 of your Pokémon to attach it to")
        if target is not None:
            await ctx.attach_energy(card, target)


card = PokemonCardDef(
    guid="d417d602-5222-5968-92bd-8243fe81546a",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirge.Name",
    display_name="Skeledirge",
    searchable_by=["Skeledirge", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Attack(
            title="Passionate Singing",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to your Pokémon in any way you like.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=passionate_singing,
        ),
        Attack(
            title="Blazing Shout",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=ac.recoil_attack(30),
        ),
    ],
)
