"""Ambipom (SV4 146 -- JP SV4M 052; English PAR/146). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="45a3f2a2-30d0-52c3-b667-db9312d2cd02",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ambipom.Name",
    display_name="Ambipom",
    searchable_by=["Ambipom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    family_id=190,
    abilities=[
        Attack(
            title="Collect",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Hand Fling",
            game_text="This attack does 20 damage for each card in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_hand("mine"), 20),
        ),
    ],
)
