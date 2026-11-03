"""Klink (BWPJ 403 -- JP CS1 003; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su

from spirit.game.card_effects.pokemon import is_energy_card


async def _charge_beam(ctx):
    """Printed damage, then flip a coin: heads attaches an Energy card from the discard pile to this Pokemon."""
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if not (results and results[0]):
        return
    cards = [c for c in ctx.recoverable_discard() if is_energy_card(c)]
    if cards:
        picks = await ctx.choose_cards(cards, 1, minimum=1, prompt="Choose an Energy card to attach to this Pokémon.")
        if picks:
            await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="e9e2365c-7dc4-5cb7-8483-9e5abe40b1a5",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klink.Name",
    display_name="Klink",
    searchable_by=["Klink", "Basic"],
    subtypes=["Basic"],
    collector_number=403,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=599,
    abilities=[
        Attack(
            title="Charge Beam",
            game_text="Flip a coin. If heads, attach an Energy card from your discard pile to this Pokémon.",
            cost={PokemonTypes.METAL: 1},
            damage=10,
            effect=_charge_beam,
        ),
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
