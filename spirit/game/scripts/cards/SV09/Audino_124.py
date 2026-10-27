"""Audino (SV09 124 -- JP SVM 106; English JTG/124). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_supporter_card


async def beckon(ctx):
    pool = [c for c in ctx.discard_pile() if is_supporter_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter card")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="902c5432-a5d9-51c4-af53-ef69cf950e47",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name",
    display_name="Audino",
    searchable_by=["Audino", "Basic"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=531,
    abilities=[
        Attack(
            title="Beckon",
            game_text="Put a Supporter card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=beckon,
        ),
        Attack(
            title="Zen Headbutt",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
    ],
)
