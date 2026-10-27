"""Centiskorch (SV05 37 -- JP SV5K 011; English TEF/37). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="9e7a4c99-edf5-5528-af5d-af43e32cf655",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Centiskorch.Name",
    display_name="Centiskorch",
    searchable_by=["Centiskorch", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sizzlipede.Name",
    family_id=850,
    abilities=[
        Attack(
            title="Singe",
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=ac.condition_attack(SpecialConditions.BURNED),
        ),
        Attack(
            title="Charring Breath",
            game_text="If your opponent's Active Pokémon isn't Burned, this attack does nothing.",
            cost={PokemonTypes.FIRE: 2},
            damage=180,
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.BURNED), 0, else_nothing=True),
        ),
    ],
)
