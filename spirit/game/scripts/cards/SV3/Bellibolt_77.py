"""Bellibolt (SV3 77 -- JP SVD 042; English OBF/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b51d8ab7-1349-56f0-9f45-40a7b8fc5dd5",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name",
    display_name="Bellibolt",
    searchable_by=["Bellibolt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Attack(
            title="Electrobullet",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
