"""Haunter (SV035 93 -- JP SV2a 093; English MEW/93). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_supporter_card


async def spirit_return(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = [c for c in ctx.discard_pile(ctx.opponent_id) if is_supporter_card(c)]
    if not pool or not await ctx.ask_yes_no("Use Spirit Return?"):
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter card to put into your opponent's hand")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="7e819597-fa52-5b1b-9215-949447787d78",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Haunter.Name",
    display_name="Haunter",
    searchable_by=["Haunter", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=93,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    family_id=92,
    abilities=[
        Ability(
            title="Spirit Return",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may put a Supporter card from your opponent's discard pile into their hand.",
            trigger=Triggers.ON_EVOLVE,
            effect=spirit_return,
        ),
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
