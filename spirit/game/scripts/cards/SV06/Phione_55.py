"""Phione (SV06 55 -- JP SV5a 022; English TWM/175, TWM/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_supporter_card


async def beckon(ctx):
    pool = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter card")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="196a21ec-6691-5c9e-a7cb-5aad399fafb1",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=489,
    abilities=[
        Attack(
            title="Beckon",
            game_text="Put a Supporter card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=beckon,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 20 damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("defender"), 20),
        ),
    ],
)
