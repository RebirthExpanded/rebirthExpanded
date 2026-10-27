"""Voltorb ex (ME2PT5 58 -- JP MC 233; English ASC/58). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="81cf7d17-e45f-5a7a-a993-36772e58fa0a",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorbex.Name",
    display_name="Voltorb ex",
    searchable_by=["Voltorb ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=58,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Hundred-Hitting Ball",
            game_text="Flip a coin until you get tails. This attack does 100 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.flip_damage(until_tails=True, bonus_per_heads=100),
        ),
    ],
)
