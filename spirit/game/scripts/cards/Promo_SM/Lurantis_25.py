"""Lurantis (SM Black Star Promo 25 -- JP TAG TEAM GX Premium Trainer Box
002/035, the art here).

Stage 1 Grass Pokemon (evolves from Fomantis). HP 100, weakness Fire x2,
no resistance, retreat 2.

  Sunny Day   (Ability)  The attacks of your [G] Pokemon and [R] Pokemon do
                         20 more damage to your opponent's Active Pokemon
                         (before applying Weakness and Resistance).
  Solar Beam  [GGC] 80

Sunny Day has no Active/Bench clause and stacks per Lurantis in play.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import team_damage_boost_passive
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_pokemon_of_type


def _grass_or_fire(pokemon) -> bool:
    return (is_pokemon_of_type(pokemon, PokemonTypes.GRASS)
            or is_pokemon_of_type(pokemon, PokemonTypes.FIRE))


card = PokemonCardDef(
    guid="a510b967-151b-5316-a6fa-d6aac57c32ae",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lurantis.Name",
    display_name="Lurantis",
    searchable_by=["Lurantis", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=25,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fomantis.Name",
    family_id=753,
    abilities=[
        Ability(
            title="Sunny Day",
            game_text="The attacks of your [G] Pokémon and [R] Pokémon do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20, attacker_pred=_grass_or_fire),
        ),
        Attack(
            title="Solar Beam",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
