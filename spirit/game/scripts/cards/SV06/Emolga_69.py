"""Emolga (SV06 69 -- JP SV6 042; English TWM/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8948705c-5a37-58f2-accc-7a89cf44c9cb",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Emolga.Name",
    display_name="Emolga",
    searchable_by=["Emolga", "Basic"],
    subtypes=["Basic"],
    collector_number=69,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=587,
    abilities=[
        Attack(
            title="Sky Wave",
            game_text="This attack also does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ac.spread_damage(10, side="both", also_base=True),
        ),
    ],
)
