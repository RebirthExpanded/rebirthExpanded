"""Eevee (SM - Sun & Moon 101/149 -- JP SM8b 105/150 "GX Ultra Shiny", the art here).

Basic Colorless Pokemon. HP 60, weakness Fighting x2, no resistance,
retreat 2.

  Ability  Energy Evolution  When you attach an Energy card from your hand
                             to this Pokemon during your turn, you may
                             search your deck for a card that evolves from
                             this Pokemon that is the same type as that
                             Energy card and put it onto this Pokemon to
                             evolve it. Then, shuffle your deck.
  Quick Draw [C]  Flip a coin. If heads, draw a card.

ON_ENERGY_ATTACHED, the owner's own hand attach onto Eevee only. The
evolution is effect-driven (Rare Candy shape), so it ignores the
first-turn / just-played gates. "Same type as that Energy card" reads
the types the card provides (a Basic Energy: its one type).
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def energy_evolution(ctx):
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return
    energy = ctx.attached_energy
    if energy is None:
        return
    my_logic_name = ctx.source.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)

    def matches(c):
        if c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) != my_logic_name:
            return False
        return any(energy_provides_type(energy, t)
                   for t in (c.get_attribute(AttrID.POKEMON_TYPES) or []))

    if not any(matches(c) for c in ctx.deck()):
        return
    if not await ctx.ask_yes_no(
            "Search your deck for an Evolution of this Pokémon of the attached Energy's type?"):
        return
    picks = await ctx.search_deck(
        matches, count=1, minimum=0,
        prompt="Choose a card that evolves from this Pokémon of that Energy's type.")
    if picks:
        await ctx.evolve_pokemon(ctx.source, picks[0])
    await ctx.shuffle_deck()


async def quick_draw(ctx):
    heads = await ctx.flip_coins(1, "Quick Draw")
    if heads and heads[0]:
        await ctx.draw_cards(1)


card = PokemonCardDef(
    guid="5f47a1aa-397c-5ee2-9450-e1a332d3dbc0",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SM1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(title="Energy Evolution",
                game_text="When you attach an Energy card from your hand to this Pokémon during your turn, you may search your deck for a card that evolves from this Pokémon that is the same type as that Energy card and put it onto this Pokémon to evolve it. Then, shuffle your deck.",
                trigger=Triggers.ON_ENERGY_ATTACHED,
                effect=energy_evolution),
        Attack(title="Quick Draw",
               game_text="Flip a coin. If heads, draw a card.",
               cost={PokemonTypes.COLORLESS: 1},
               effect=quick_draw),
    ],
)
