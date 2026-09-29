from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.session.effects import is_basic_energy


async def snack_seek(ctx):
    """Look at the top card of your deck; you may discard it."""
    top = ctx.deck_top(1)
    if not top:
        return
    idx = await ctx.present_card_choice(top[0], "Discard this card?", ["Discard", "Keep on top"])
    if idx == 0:
        await ctx.discard_cards([top[0]])


async def pick_and_stick(ctx):
    """Up to 2 Basic Energy from your discard pile onto your Pokemon in any
    way you like."""
    pool = [c for c in ctx.discard_pile() if is_basic_energy(c)]
    targets = list(ctx.my_pokemon_in_play())
    if not pool or not targets:
        return
    picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0,
                                   prompt="Choose up to 2 Basic Energy cards to attach.")
    if picks:
        await distribute_energy(ctx, picks, targets)

card = PokemonCardDef(
    guid="563cb4c2-ea8f-5121-8e85-baf1d1e9612f",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpeko.Name",
    display_name="Morpeko",
    searchable_by=["Morpeko", "Basic", "Morpeko"],
    subtypes=["Basic"],
    collector_number=72,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=877,
    abilities=[
        Ability(
            title="Snack Seek",
            game_text="Once during your turn, you may look at the top card of your deck. You may discard that card.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, pokemon: bool(
                board.find_player_area(player_id, "deck").children),
            effect=snack_seek,
        ),
        Attack(
            title="Pick and Stick",
            game_text="Attach up to 2 Basic Energy cards from your discard pile to your Pok\u00e9mon in any way you like.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=0,
            effect=pick_and_stick,
        ),
    ],
)
