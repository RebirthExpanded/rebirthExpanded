"""Shaymin (ME3 3 -- JP M3 003; English POR/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.effects import is_energy_card


async def send_flowers(ctx):
    bench = [p for p in ctx.my_bench() if PokemonTypes.GRASS.value in (p.get_attribute(AttrID.POKEMON_TYPES) or [])]
    if bench:
        picks = await ctx.search_deck(is_energy_card, count=1, minimum=0,
                                      prompt="Choose an Energy card to attach to 1 of your Benched Grass Pokémon.")
        if picks:
            target = await ctx.choose_pokemon(bench, "Choose a Benched Grass Pokémon")
            if target is not None:
                await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="8d949d11-ba9d-5aaa-b2b7-b72eb0a096ea",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin", "Basic"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=492,
    abilities=[
        Attack(
            title="Send Flowers",
            game_text="Search your deck for an Energy card and attach it to 1 of your Benched Grass Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=send_flowers,
        ),
        Attack(
            title="Leaf Step",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
