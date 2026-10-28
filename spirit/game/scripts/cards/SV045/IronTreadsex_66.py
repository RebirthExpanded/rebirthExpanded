"""Iron Treads ex (SV045 66 -- JP SV4a 132; English PAF/66, SVP/73). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.data_utils import def_for, subtypes_for


async def iron_clad_roll(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    caps = [c for c in me.children if getattr(def_for(c.archetype_id), "display_name", "") == "Future Booster Energy Capsule"]
    if caps and me not in ctx.knockouts and await ctx.ask_yes_no("Discard all Future Booster Energy Capsules from this Pokémon?"):
        await ctx.discard_cards(caps)
        await pc.apply_protection(ctx, reduce=150)


card = PokemonCardDef(
    guid="bae86071-5274-5c90-9c61-1bb797506556",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronTreadsex.Name",
    display_name="Iron Treads ex",
    searchable_by=["Iron Treads ex", "Basic", "ex", "Future"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=66,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=990,
    abilities=[
        Attack(
            title="Iron-Clad Roll",
            game_text="After doing damage, you may discard all Future Booster Energy Capsules from this Pokémon. If you do, during your opponent's next turn, this Pokémon takes 150 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=iron_clad_roll,
        ),
    ],
)
