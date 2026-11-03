"""Tinkaton (SVP 140 -- JP SVP 114; English SVP/140). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _knock_off(ctx):
    """Discard a random card from your opponent's hand."""
    await ctx.deal_damage()
    await ac.discard_random_from_hand(ctx, ctx.opponent_id, count=1)


card = PokemonCardDef(
    guid="eeed5365-a94a-534c-ae65-6d81dcaa0a11",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkaton.Name",
    display_name="Tinkaton",
    searchable_by=["Tinkaton", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=140,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    family_id=957,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=40,
            effect=_knock_off,
        ),
        Attack(
            title="Wild Press",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=220,
            effect=ac.recoil_attack(60),
        ),
    ],
)
