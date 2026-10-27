"""Darmanitan (ME2 16 -- JP M2 016; English PFL/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import PokemonTypes as _PT


card = PokemonCardDef(
    guid="052f7200-3c34-5213-9533-c245349cfd0a",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Darmanitan.Name",
    display_name="Darmanitan",
    searchable_by=["Darmanitan", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=16,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name",
    family_id=554,
    abilities=[
        Attack(
            title="Blaze Ball",
            game_text="This attack does 40 more damage for each Fire Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.FIRE), 40, base=40),
        ),
    ],
)
