"""Pikachu ex (ME6A 48 -- JP M6a 048; English 30C/150, 30C/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.card_effects.trainers import is_basic_energy_card


async def zip_zap_frenzy(ctx):
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, len(pool), minimum=0,
                                   prompt="Attach any number of Basic Energy cards from your hand to your Pokémon.")
    if picks:
        await su.distribute_energy(ctx, picks, ctx.my_pokemon_in_play())


card = PokemonCardDef(
    guid="02bd662e-ae67-551f-bc56-c3a1765d9716",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name",
    display_name="Pikachu ex",
    searchable_by=["Pikachu ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=48,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Zip-Zap Frenzy",
            game_text="You may attach any number of Basic Energy cards from your hand to your Pokémon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=zip_zap_frenzy,
        ),
        Attack(
            title="Thunder",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=ac.recoil_attack(30),
        ),
    ],
)
