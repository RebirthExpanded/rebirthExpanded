"""Eevee (Promo_SWSH 127 -- JP SP 163; English SP/127, SP/175, SP/190, SP/212). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_basic_energy


async def _be_prepared(ctx):
    pool = [c for c in ctx.hand() if is_basic_energy(c)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, 1, prompt="Choose a basic Energy card to attach to this Pokémon.")
    if picks:
        await ctx.attach_energy(picks[0], ctx.attacker)


card = PokemonCardDef(
    guid="7d2268c4-d5d3-53e6-9846-c8708e29e431",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic"],
    subtypes=["Basic"],
    collector_number=127,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Attack(
            title="Be Prepared",
            game_text="Attach a basic Energy card from your hand to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_be_prepared,
        ),
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
