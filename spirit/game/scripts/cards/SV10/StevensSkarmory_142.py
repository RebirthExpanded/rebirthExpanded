"""Steven's Skarmory (SV10 142 -- JP SVOD 004; English DRI/142). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ef0e5fbd-7688-579d-9928-e075f942fcac",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensSkarmory.Name",
    display_name="Steven's Skarmory",
    searchable_by=["Steven's Skarmory", "Basic"],
    subtypes=["Basic"],
    collector_number=142,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=227,
    abilities=[
        Attack(
            title="Razor Wing",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Sonic Double",
            game_text="This attack does 50 damage to 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=ac.snipe_attack(50, pool="any", count=2),
        ),
    ],
)
