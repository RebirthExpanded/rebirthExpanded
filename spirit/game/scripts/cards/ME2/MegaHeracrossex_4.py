from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack


async def juggernaut_horn(ctx):
    """100 + the attack damage this Pokemon took during the opponent's last turn."""
    await ctx.deal_damage(100 + ctx.damage_taken_last_turn(ctx.attacker))

card = PokemonCardDef(
    guid="0e32c600-f369-5e29-85ba-882d661c5aef",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaHeracrossex.Name",
    display_name="Mega Heracross ex",
    searchable_by=["Mega Heracross ex", "Basic", "ex", "SV_Mega", "MegaHeracrossex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=4,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=214,
    abilities=[
        Attack(
            title="Juggernaut Horn",
            game_text="If this Pok\u00e9mon was damaged by an attack during your opponent's last turn, this attack does that much more damage.",
            cost={PokemonTypes.GRASS: 2},
            damage=100,
            damage_operator="+",
            effect=juggernaut_horn,
        ),
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.GRASS: 3},
            damage=170,
            effect=mill_attack(2),
        ),
    ],
)
