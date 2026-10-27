"""Alolan Golem (SV09 46 -- JP SVM 041; English JTG/46). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="f7c7ff96-1438-5587-831f-0d723d2903ea",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGolem.Name",
    display_name="Alolan Golem",
    searchable_by=["Alolan Golem", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=46,
    set_code="SV09",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Electromagnetic Catapult",
            game_text="Flip a coin until you get tails. This attack does 70 damage for each heads.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=70,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=70),
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pokémon also does 40 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=ac.recoil_attack(40),
        ),
    ],
)
