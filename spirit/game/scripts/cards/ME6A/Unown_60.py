"""Unown (ME6A 60 -- JP M6a 060; English 30C/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def mysterious_signal(ctx):
    defender = ctx.defender
    await ctx.deal_damage()
    if defender is not None and defender in ctx.knockouts:
        ctx.extra_prizes += 1


card = PokemonCardDef(
    guid="8a94698c-e913-5156-8637-53f9f8827325",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Unown.Name",
    display_name="Unown",
    searchable_by=["Unown", "Basic"],
    subtypes=["Basic"],
    collector_number=60,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=201,
    abilities=[
        Attack(
            title="Mysterious Signal",
            game_text="If your opponent's Pokémon is Knocked Out by damage from this attack, take 1 more Prize card.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=40,
            effect=mysterious_signal,
        ),
    ],
)
