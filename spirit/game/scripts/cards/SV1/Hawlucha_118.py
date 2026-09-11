"""Hawlucha (SV - Scarlet & Violet 118/198 -- JP SV1S 045/078, the art here).

Basic Fighting Pokemon. HP 70, weakness Psychic x2, no resistance, retreat 1.

  Ability  Flying Entry  When you play this Pokemon from your hand onto
                         your Bench during your turn, you may put 1 damage
                         counter on each of 2 of your opponent's Benched
                         Pokemon.
  Wing Attack [FCC] 70

ON_PLAY fires only for a hand play (Nest Ball's bench put never reaches
it). With a single opposing bencher the one counter still goes on.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def flying_entry(ctx):
    """You may put 1 damage counter on each of 2 of their Benched Pokemon."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no(
            "Put 1 damage counter on each of 2 of your opponent's Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(
        bench, min(2, len(bench)), minimum=min(2, len(bench)),
        prompt="Choose 2 of your opponent's Benched Pokémon")
    for target in picks:
        await ctx.deal_damage(10, target=target, apply_modifiers=False,
                              as_counters=True)


card = PokemonCardDef(
    guid="d8637f4a-fb37-5331-9d3b-343801dc48fa",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hawlucha.Name",
    display_name="Hawlucha",
    searchable_by=["Hawlucha", "Basic"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=701,
    abilities=[
        Ability(title="Flying Entry",
                game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may put 1 damage counter on each of 2 of your opponent's Benched Pokémon.",
                trigger=Triggers.ON_PLAY,
                effect=flying_entry),
        Attack(title="Wing Attack", game_text="",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
               damage=70),
    ],
)
