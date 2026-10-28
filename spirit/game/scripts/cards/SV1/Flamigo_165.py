"""Flamigo (SV1 165 -- JP SVAL 010; English SVI/165). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ff835ba9-1b77-572a-99ec-cade086f1c4d",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flamigo.Name",
    display_name="Flamigo",
    searchable_by=["Flamigo", "Basic"],
    subtypes=["Basic"],
    collector_number=165,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=973,
    abilities=[
        Attack(
            title="Flap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Nosedive",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=ac.recoil_attack(20),
        ),
    ],
)
