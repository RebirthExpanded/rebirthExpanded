"""Cyclizar (SV1 163 -- JP SVAW 010; English SVI/163). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="38010f6f-da67-5d93-9a0b-4972a5e4c708",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name",
    display_name="Cyclizar",
    searchable_by=["Cyclizar", "Basic"],
    subtypes=["Basic"],
    collector_number=163,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    abilities=[
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=ac.recoil_attack(10),
        ),
    ],
)
