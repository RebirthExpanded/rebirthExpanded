from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.session.effects import is_basic_energy


def _basic_lightning(card) -> bool:
    return is_basic_energy(card) and is_lightning_energy(card)


def _flashing_draw_condition(board, player_id, pokemon) -> bool:
    return any(_basic_lightning(c) for c in pokemon.children)


async def flashing_draw(ctx):
    """Discard a Basic [L] Energy from this Pokemon, then draw until 6."""
    pool = [e for e in ctx.attached_energies(ctx.source) if _basic_lightning(e)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Discard a Basic [L] Energy from this Pokémon")
    if not picks:
        return
    await ctx.discard_cards(picks)
    await ctx.draw_until(6)

card = PokemonCardDef(
    guid="1f8be600-97d5-54fc-a88d-58eda2a9921a",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosKilowattrel.Name",
    display_name="Iono's Kilowattrel",
    searchable_by=["Iono's Kilowattrel", "Stage 1", "IonosKilowattrel"],
    subtypes=["Stage 1"],
    collector_number=55,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosWattrel.Name",
    family_id=940,
    abilities=[
        Ability(
            title="Flashing Draw",
            game_text="You must discard a Basic [L] Energy from this Pok\u00e9mon in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_flashing_draw_condition,
            effect=flashing_draw,
        ),
        Attack(
            title="Mach Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
