"""Mega Emboar ex (ME2PT5 31 -- JP MC 113; English ASC/273, ASC/31, MEP/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="497e9208-d0d3-582b-98b5-b9f4bf92dd0a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEmboarex.Name",
    display_name="Mega Emboar ex",
    searchable_by=["Mega Emboar ex", "Stage 2", "ex", "SV_Mega"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=31,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=380,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pignite.Name",
    family_id=498,
    abilities=[
        Attack(
            title="Crimson Blast",
            game_text="This Pokémon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=320,
            effect=ac.recoil_attack(60),
        ),
    ],
)
