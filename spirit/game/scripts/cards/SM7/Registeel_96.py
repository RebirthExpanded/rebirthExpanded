"""Registeel (SM - Celestial Storm 96/168 -- JP SM7 056/096, the art here).

Basic Metal Pokemon. HP 120, weakness Fire x2, resistance Psychic -20,
retreat 3.

  Ability: Exoskeleton  This Pokemon takes 20 less damage from attacks
                        (after applying Weakness and Resistance).
  Silver Fist [MCC] 60+  If your opponent's Active Pokemon has an Ability,
                         this attack does 60 more damage.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.pokemon import has_printed_ability
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


async def silver_fist(ctx):
    defender = ctx.defender
    await ctx.deal_damage(120 if defender is not None and has_printed_ability(defender) else 60)


card = PokemonCardDef(
    guid="8b772621-7042-525c-847e-9f490e54b753",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Registeel.Name",
    display_name="Registeel",
    searchable_by=["Registeel", "Basic"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=379,
    abilities=[
        Ability(
            title="Exoskeleton",
            game_text="This Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(20),
        ),
        Attack(
            title="Silver Fist",
            game_text="If your opponent's Active Pokémon has an Ability, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=silver_fist,
        ),
    ],
)
