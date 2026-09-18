"""Mega Audino ex (ME2PT5 172).

  Kaleidowaltz  [C]        Flip 3 coins. For each heads, search your deck for
                           up to 2 Basic Energy cards and attach them to your
                           Pokemon in any way you like. Then, shuffle your deck.
  Ear Force     [CCC] 20+  This attack does 80 more damage for each Energy
                           attached to your opponent's Active Pokemon.

Kaleidowaltz searches once for up to 2 x heads Energy (the same cards the
three separate searches would find) and places each on a Pokemon of your
choice; the deck is shuffled even on three tails.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.session.effects import is_basic_energy


async def kaleidowaltz(ctx):
    heads = sum(1 for h in await ctx.flip_coins(3, "Kaleidowaltz") if h)
    if heads:
        picks = await ctx.search_deck(
            is_basic_energy, count=2 * heads, minimum=0,
            prompt=f"Choose up to {2 * heads} Basic Energy cards to attach to your Pokémon.")
        for energy in picks:
            target = await ctx.choose_pokemon(
                ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
            if target is not None:
                await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="d274bba8-a07a-5325-a481-15c939461cd7",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAudinoex.Name",
    display_name="Mega Audino ex",
    searchable_by=["Mega Audino ex","Basic","ex","SV_Mega","MegaAudinoex"],
    subtypes=["Basic","ex","SV_Mega"],
    collector_number=172,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Kaleidowaltz",
            game_text="Flip 3 coins. For each heads, search your deck for up to 2 Basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=kaleidowaltz,
        ),
        Attack(
            title="Ear Force",
            game_text="This attack does 80 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 80, base=20),
        ),
    ],
)
