from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.models.board import board_of
from spirit.game.session.effects import is_special_energy
from spirit.game.session.passives import Passive


class TyranniclyGutsyPassive(Passive):
    """+150 HP while this Pokemon has any Special Energy attached."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier:
            return 0
        board = board_of(pokemon)
        if board is None:
            return 0
        return 150 if any(is_special_energy(e) for e in board.attached_energies(pokemon)) else 0


async def wreak_havoc(ctx):
    """160, then mill the opponent's deck once per heads before the first tails."""
    await ctx.deal_damage()
    heads = await ctx.flip_until_tails(ctx.ability.title)
    if heads:
        await ctx.discard_cards(ctx.deck_top(heads, player_id=ctx.opponent_id))

card = PokemonCardDef(
    guid="cba86113-2812-58bd-aa2e-4f245b2b68b5",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrantrum.Name",
    display_name="Tyrantrum",
    searchable_by=["Tyrantrum", "Stage 2", "Tyrantrum"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tyrunt.Name",
    family_id=696,
    abilities=[
        Ability(
            title="Tyrannically Gutsy",
            game_text="If this Pok\u00e9mon has any Special Energy attached, it gets +150 HP.",
            passive=TyranniclyGutsyPassive(),
        ),
        Attack(
            title="Wreak Havoc",
            game_text="Flip a coin until you get tails. For each heads, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=wreak_havoc,
        ),
    ],
)
