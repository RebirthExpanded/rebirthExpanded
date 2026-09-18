"""Mega Eelektross ex (ME2PT5 61 / 266 / 278).

  Split Bomb      [LL]       This attack does 60 damage to each of 2 of your
                             opponent's Pokemon. (Don't apply Weakness and
                             Resistance for Benched Pokemon.)
  Disaster Shock  [LLL] 190  You may discard 2 [L] Energy from this Pokemon
                             and make your opponent's Active Pokemon
                             Paralyzed.

Disaster Shock's discard counts provided Energy, not cards (a Double Turbo
pays no [L]); with fewer than 2 [L] attached the question is not asked.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import snipe_attack
from spirit.game.card_effects.pokemon import energy_units_of_type


async def disaster_shock(ctx):
    await ctx.deal_damage()
    lightning = sum(energy_units_of_type(ctx.board, e, PokemonTypes.LIGHTNING.value)
                    for e in ctx.attached_energies(ctx.attacker))
    if lightning < 2 or ctx.defender is None:
        return
    if not await ctx.ask_yes_no(
            "Discard 2 Lightning Energy from this Pokémon to Paralyze your opponent's Active Pokémon?"):
        return
    discarded = await ctx.discard_energy_units_from(
        ctx.attacker, 2,
        predicate=lambda c: energy_units_of_type(ctx.board, c, PokemonTypes.LIGHTNING.value) > 0,
        prompt="Choose 2 Lightning Energy to discard")
    if discarded:
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)

card = PokemonCardDef(
    guid="70ddf21e-0504-59e6-b683-06b5db02f673",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEelektrossex.Name",
    display_name="Mega Eelektross ex",
    searchable_by=["Mega Eelektross ex","Stage 1","Stage 2","ex","SV_Mega","MegaEelektrossex"],
    subtypes=["Stage 1","Stage 2","ex","SV_Mega"],
    collector_number=61,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Split Bomb",
            game_text="This attack does 60 damage to each of 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=snipe_attack(60, pool="any", count=2),
        ),
        Attack(
            title="Disaster Shock",
            game_text="You may discard 2 Lightning Energy from this Pokémon and make your opponent's Active Pokémon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=190,
            effect=disaster_shock,
        ),
    ],
)
