"""Cryogonal (ZSV10PT5 27 -- JP SV11B 030; English BLK/111, BLK/27). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="f33ddb9d-7f8b-5e1b-9e2d-322137d3533e",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cryogonal.Name",
    display_name="Cryogonal",
    searchable_by=["Cryogonal", "Basic"],
    subtypes=["Basic"],
    collector_number=27,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=615,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 20 damage to the new Active Pokémon.",
            cost={PokemonTypes.WATER: 1},
            effect=su.gust_attack(damage_to_new_active=20),
        ),
        Attack(
            title="Icicle",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=30,
        ),
    ],
)
