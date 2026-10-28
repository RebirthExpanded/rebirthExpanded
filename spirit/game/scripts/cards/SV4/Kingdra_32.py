"""Kingdra (SV4 32 -- JP SV4K 019; English PAR/32). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


async def whirltide(ctx):
    top = list(ctx.deck_top(6))
    if not top:
        return
    await ctx.reveal_cards(top)
    energy = [c for c in top if is_energy_card(c)]
    if energy:
        await ac.snipe_attack(60 * len(energy), pool="any")(ctx)
        await ctx.discard_cards(energy)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="4f4fc78d-4268-5a11-8f9d-5d4318d8c06d",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=32,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Attack(
            title="Whirltide",
            game_text="Reveal the top 6 cards of your deck. This attack does 60 damage to 1 of your opponent's Pokémon for each Energy card you find there. Then, discard those Energy cards and shuffle the other cards back into your deck. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=whirltide,
        ),
        Attack(
            title="Hydro Splash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
