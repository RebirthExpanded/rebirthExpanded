"""Palafin (SVP 36 -- JP SV3 031; English OBF/200, OBF/62, PAF/124, PAF/225, SVP/36). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def justice_kick(ctx):
    if ctx.entered_active_this_turn(ctx.attacker):
        await ctx.deal_damage()


card = PokemonCardDef(
    guid="2c86690f-aff0-563a-8134-715056cf228c",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=36,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Jet Punch",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
        Attack(
            title="Justice Kick",
            game_text="If this Pokémon didn't move from the Bench to the Active Spot this turn, this attack does nothing.",
            cost={PokemonTypes.WATER: 2},
            damage=210,
            effect=justice_kick,
        ),
    ],
)
