"""Joltik (SV - Stellar Crown 50/142 -- JP SV7 032/102, the art here).

Basic Lightning Pokemon. HP 30, weakness Fighting x2, no resistance,
retreat 1.

  Jolting Charge [C]  Search your deck for up to 2 Basic [G] Energy cards
                      and up to 2 Basic [L] Energy cards and attach them
                      to your Pokemon in any way you like. Then, shuffle
                      your deck.

Two searches (Grass, then Lightning), each found card picking its own
Pokemon; the deck is shuffled once at the end.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_energy


def _basic_of(pokemon_type):
    def pred(card):
        return is_basic_energy(card) and energy_provides_type(card, pokemon_type.value)
    return pred


async def jolting_charge(ctx):
    for pokemon_type, label in ((PokemonTypes.GRASS, "[G]"), (PokemonTypes.LIGHTNING, "[L]")):
        picks = await ctx.search_deck(
            _basic_of(pokemon_type), count=2, minimum=0,
            prompt=f"Choose up to 2 Basic {label} Energy cards to attach to your Pokémon.")
        for energy in picks:
            target = await ctx.choose_pokemon(
                ctx.my_pokemon_in_play(), "Choose a Pokémon to attach the Energy to")
            if target is None:
                target = ctx.source
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="0f7d9615-baff-54a7-9a37-3e03e6810e46",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    display_name="Joltik",
    searchable_by=["Joltik", "Basic"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=595,
    abilities=[
        Attack(title="Jolting Charge",
               game_text="Search your deck for up to 2 Basic [G] Energy cards and up to 2 Basic [L] Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.",
               cost={PokemonTypes.COLORLESS: 1},
               effect=jolting_charge),
    ],
)
