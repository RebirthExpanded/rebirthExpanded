"""Boltund (ME2 31 -- JP M2 031; English PFL/31). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7d63b1a4-3080-594a-9ab2-e429b6f4eb97",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Boltund.Name",
    display_name="Boltund",
    searchable_by=["Boltund", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamper.Name",
    family_id=835,
    abilities=[
        Attack(
            title="Electric Run",
            game_text="Flip a coin. If heads, this attack does 70 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="+",
            effect=ac.flip_bonus(70),
        ),
    ],
)
