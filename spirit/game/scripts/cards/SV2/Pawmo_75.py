"""Pawmo (SV2 75 -- JP SVC 008; English PAL/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="6111f30c-312a-52ca-9877-f9c2bde5d2e7",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    display_name="Pawmo",
    searchable_by=["Pawmo", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Static Shock",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title="Electrobullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
