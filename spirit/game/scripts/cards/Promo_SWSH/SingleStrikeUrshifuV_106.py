"""Single Strike Urshifu V (Promo_SWSH 106 -- JP SF 006; English SP/106). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def _brawny_knuckle(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="21f78c41-2b88-558d-96d1-cf00a464a988",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SingleStrikeUrshifuV.Name",
    display_name="Single Strike Urshifu V",
    searchable_by=["Single Strike Urshifu V", "Basic", "V", "Single Strike"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=106,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Low Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
        ),
        Attack(
            title="Brawny Knuckle",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 4},
            damage=180,
            effect=_brawny_knuckle,
        ),
    ],
)
