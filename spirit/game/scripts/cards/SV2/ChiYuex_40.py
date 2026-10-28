"""Chi-Yu ex (SV2 40 -- JP SV2D 016; English PAF/241, PAL/234, PAL/259, PAL/40). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


async def flame_surge(ctx):
    await ctx.deal_damage()
    bench = list(ctx.my_bench())
    if not bench:
        return
    chosen = await ctx.choose_cards(bench, min(3, len(bench)), minimum=0, prompt="Choose up to 3 of your Benched Pokémon")
    for p in chosen:
        picks = await ctx.search_deck(_basic_fire, count=1, minimum=0, prompt="Choose a Basic Fire Energy card to attach")
        if picks:
            await ctx.attach_energy(picks[0], p)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="d6b2c4c4-245b-55a8-9647-1165c2d4f391",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYuex.Name",
    display_name="Chi-Yu ex",
    searchable_by=["Chi-Yu ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=40,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Jealously Singe",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.mill_attack(2),
        ),
        Attack(
            title="Flame Surge",
            game_text="Choose up to 3 of your Benched Pokémon. For each of those Pokémon, search your deck for a Basic Fire Energy card and attach it to that Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=flame_surge,
        ),
    ],
)
