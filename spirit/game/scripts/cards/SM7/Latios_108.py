"""Latios {*} (SM - Celestial Storm 108/168 -- JP SM7 067/096, the art here).

Basic Dragon Pokemon, Prism Star. HP 140, weakness Fairy x2, no
resistance, retreat 1.

  Dragon Fleet  [CC] 50x  This attack does 50 damage for each of your [N]
                          Evolution Pokemon in play.

Prism Star: one per deck, Lost Zone instead of the discard pile (from the
rarity / subtype). A V-UNION or VMAX counts as an Evolution Pokemon only
if it is one by stage; Dragon-type Basics and Latios itself do not count.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import is_evolution_pokemon, is_pokemon_of_type


def _dragon_evolution(pokemon) -> bool:
    return is_evolution_pokemon(pokemon) and is_pokemon_of_type(pokemon, PokemonTypes.DRAGON)


card = PokemonCardDef(
    guid="77311a0f-7197-5966-b6c3-1cb2337637d9",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosPrismStar.Name",
    display_name="Latios {*}",
    searchable_by=["Latios", "Basic", "Prism Star"],
    subtypes=["Basic", "Prism Star"],
    collector_number=108,
    set_code="SM7",
    rarity=Rarities.Prism,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    family_id=381,
    abilities=[
        Attack(
            title="Dragon Fleet",
            game_text="This attack does 50 damage for each of your [N] Evolution Pokémon in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", _dragon_evolution), 50),
        ),
    ],
)
