"""Bisharp (ZSV10PT5 65 -- JP SV11B 067; English BLK/143, BLK/65). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="de7b8096-3a64-5443-84c4-2d377efeb0b1",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bisharp.Name",
    display_name="Bisharp",
    searchable_by=["Bisharp", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name",
    family_id=624,
    abilities=[
        Attack(
            title="Cut Up",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=40,
        ),
        Attack(
            title="Finishing Blow",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 60 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 60),
        ),
    ],
)
