"""Ledian (SV07 3 -- JP SV7 002; English SCR/144, SCR/3, SVP/133). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def glittering_star_pattern(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    pool = [p for p in ctx.opponent_bench() if (p.get_attribute(AttrID.HP, 0) or 0) <= 90]
    if not pool or not await ctx.ask_yes_no("Use Glittering Star Pattern?"):
        return
    target = await ctx.choose_pokemon(pool, "Choose the opponent's new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


card = PokemonCardDef(
    guid="ade70a42-e812-5822-8f9d-11915e33b6d3",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name",
    display_name="Ledian",
    searchable_by=["Ledian", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=3,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name",
    family_id=165,
    abilities=[
        Ability(
            title="Glittering Star Pattern",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may switch in 1 of your opponent's Benched Pokémon that has 90 HP or less remaining to the Active Spot.",
            trigger=Triggers.ON_EVOLVE,
            effect=glittering_star_pattern,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness or Resistance, or by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ac.ignore_effects_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)
