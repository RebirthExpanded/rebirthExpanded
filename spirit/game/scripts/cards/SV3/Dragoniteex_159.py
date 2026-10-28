"""Dragonite ex (SV3 159 -- JP SVD 090; English OBF/159). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


async def mighty_meteor(ctx):
    results = await ctx.flip_coins(1, "Mighty Meteor")
    if results and results[0]:
        await ctx.deal_damage(280)
    else:
        await ctx.deal_damage(140)
        ac.lock_all_attacks(ctx, ctx.attacker)


card = PokemonCardDef(
    guid="4d2f526b-3cc7-503d-8f4d-e27b14995e1b",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragoniteex.Name",
    display_name="Dragonite ex",
    searchable_by=["Dragonite ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=159,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=330,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Wing Attack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
        Attack(
            title="Mighty Meteor",
            game_text="Flip a coin. If heads, this attack does 140 more damage. If tails, during your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=140,
            damage_operator="+",
            effect=mighty_meteor,
        ),
    ],
)
