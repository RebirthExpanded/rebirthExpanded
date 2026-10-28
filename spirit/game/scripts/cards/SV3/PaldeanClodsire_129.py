"""Paldean Clodsire (SV3 129 -- JP SV3 069; English OBF/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="aa5826b3-7620-5253-87c3-9d1d17e5ff5c",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanClodsire.Name",
    display_name="Paldean Clodsire",
    searchable_by=["Paldean Clodsire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=129,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name",
    family_id=194,
    abilities=[
        Attack(
            title="Splattering Poison",
            game_text="Both Active Pokémon are now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED, both_actives=True),
        ),
        Attack(
            title="Venoshock",
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(ac.defender_has_condition(SpecialConditions.POISONED), 120),
        ),
    ],
)
