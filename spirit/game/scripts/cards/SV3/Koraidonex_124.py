"""Koraidon ex (SV3 124 -- JP SVD 068; English OBF/124). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b187676f-d957-51e3-a0cb-5827d87f07fe",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidonex.Name",
    display_name="Koraidon ex",
    searchable_by=["Koraidon ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=124,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Splitting Beam",
            game_text="This attack also does 20 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=ac.snipe_attack(20, pool="bench", count=2, also_base=True),
        ),
        Attack(
            title="Gaia Press",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=ac.recoil_attack(30),
        ),
    ],
)
