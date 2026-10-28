"""Rotom (SV1 70 -- JP SV1V 030; English SVI/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_item_card


async def junk_hunt(ctx):
    pool = [c for c in ctx.discard_pile() if is_item_card(c)]
    if pool:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Item card")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="114e9e19-0692-5b82-ac19-001cbed6783d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rotom.Name",
    display_name="Rotom",
    searchable_by=["Rotom", "Basic"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Attack(
            title="Junk Hunt",
            game_text="Put an Item card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=junk_hunt,
        ),
        Attack(
            title="Thunder Shock",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
