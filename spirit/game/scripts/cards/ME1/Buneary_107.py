"""Buneary (ME1 107 -- JP M1S 053; English MEG/107). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="09b14a5c-6a9a-56bd-a1c7-a06c8370d95c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name",
    display_name="Buneary",
    searchable_by=["Buneary", "Basic"],
    subtypes=["Basic"],
    collector_number=107,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=427,
    abilities=[
        Attack(
            title="Charm",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 20 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=pc.debuff_defender_attacks(20),
        ),
        Attack(
            title="Skip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
