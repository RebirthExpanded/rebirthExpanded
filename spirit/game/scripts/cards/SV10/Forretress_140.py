"""Forretress (SV10 140 -- JP SV10 073; English DRI/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _metal(card) -> bool:
    return is_energy_of_type(card, PokemonTypes.METAL)


async def iron_shake_up(ctx):
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=_metal, prompt="Choose a Metal Energy to move (Done to stop)")


card = PokemonCardDef(
    guid="4ebe2be0-282c-5142-97a5-05ed407da960",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=140,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Iron Shake-Up",
            game_text="You may move any amount of Metal Energy from your Pokémon to your other Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=iron_shake_up,
        ),
        Attack(
            title="Hurricane of Needles",
            game_text="Flip 4 coins. This attack does 80 damage for each heads.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=ac.flip_damage(coins=4, per_heads=80),
        ),
    ],
)
