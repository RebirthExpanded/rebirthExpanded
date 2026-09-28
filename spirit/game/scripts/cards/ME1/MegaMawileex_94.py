from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken, damage_counters_on, damage_per


async def huge_bite(ctx):
    """260, or 30 base if the opponent's Active already has damage counters."""
    await ctx.deal_damage(30 if damage_counters_on("defender")(ctx) > 0 else 260)

card = PokemonCardDef(
    guid="bdfea014-565d-5545-ae88-1e9cfff5efdb",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaMawileex.Name",
    display_name="Mega Mawile ex",
    searchable_by=["Mega Mawile ex", "Basic", "ex", "SV_Mega", "MegaMawileex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=94,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=303,
    abilities=[
        Attack(
            title="Gobble Down",
            game_text="This attack does 80 damage for each Prize card you have taken.",
            cost={PokemonTypes.METAL: 2},
            damage=80,
            damage_operator="x",
            effect=damage_per(count_prizes_taken("mine"), 80),
        ),
        Attack(
            title="Huge Bite",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack's base damage is 30.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=huge_bite,
        ),
    ],
)
