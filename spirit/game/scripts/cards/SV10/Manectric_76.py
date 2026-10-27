"""Manectric (SV10 76 -- JP SV9a 038; English DRI/76). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="5e1a3a3f-a226-5c4b-a83d-842e75315713",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Zap Kick",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Flash Impact",
            game_text="This attack also does 40 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ac.snipe_attack(40, pool="bench", side="mine", also_base=True),
        ),
    ],
)
