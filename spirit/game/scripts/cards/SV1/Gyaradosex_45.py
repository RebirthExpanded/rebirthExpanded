"""Gyarados ex (SV1 45 -- JP SV1S 014; English SVI/225, SVI/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="eea805f1-e4a5-5963-aa21-7ee45bec9a7f",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyaradosex.Name",
    display_name="Gyarados ex",
    searchable_by=["Gyarados ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=45,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Waterfall",
            game_text="",
            cost={PokemonTypes.WATER: 3},
            damage=100,
        ),
        Attack(
            title="Tyrannical Tail",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 180 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 2},
            damage=180,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 180),
        ),
    ],
)
