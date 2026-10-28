"""Miraidon (SVP 13 -- JP WCS23 009; English SVI/80, SVP/13). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="cd243169-c362-5285-9b38-b85a8db92c5e",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic"],
    subtypes=["Basic"],
    collector_number=13,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Lightning Laser",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
