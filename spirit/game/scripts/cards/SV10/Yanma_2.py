from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import opponent_switches


async def whirlwind(ctx):
    """The opponent switches their Active out; they choose the new Active."""
    defender = ctx.defender
    if defender is not None and not ctx.effects_blocked(defender):
        await opponent_switches(ctx)

card = PokemonCardDef(
    guid="82926fb6-5941-59a0-b8c4-f0aeb71d7f64",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic", "Yanma"],
    subtypes=["Basic"],
    collector_number=2,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=193,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=whirlwind,
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
