"""Team Rocket's Larvitar (SV10 94 -- JP SV10 048; English DRI/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="c52ae3ab-57a8-5772-ba30-3a92c18cecff",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsLarvitar.Name",
    display_name="Team Rocket's Larvitar",
    searchable_by=["Team Rocket's Larvitar", "Basic"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=246,
    abilities=[
        Attack(
            title="Mountain Munch",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.mill_attack(1),
        ),
    ],
)
