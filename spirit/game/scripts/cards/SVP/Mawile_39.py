"""Mawile (SVP 39 -- JP SV3 078; English OBF/143, SVP/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_special_energy


async def special_eater(ctx):
    if not getattr(ctx, "benched_from_hand", True):
        return
    d = ctx.opponent_active()
    pool = [e for e in ctx.attached_energies(d) if is_special_energy(e)] if d is not None else []
    if not pool or not await ctx.ask_yes_no("Use Special Eater?"):
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Special Energy to discard")
    await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="b5bb110e-e34a-56aa-a044-7e07fc25c157",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=303,
    abilities=[
        Ability(
            title="Special Eater",
            game_text="When you play this Pokémon from your hand onto your Bench during your turn, you may discard a Special Energy from your opponent's Active Pokémon.",
            trigger=Triggers.ON_PLAY,
            effect=special_eater,
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
