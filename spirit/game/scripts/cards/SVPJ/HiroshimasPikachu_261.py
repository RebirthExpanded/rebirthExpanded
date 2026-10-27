"""Hiroshima's Pikachu (SVPJ 261 -- JP SVP 261; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="15d4acb6-6e73-5be1-a1ab-35a4805a8e83",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HiroshimasPikachu.Name",
    display_name="Hiroshima's Pikachu",
    searchable_by=["Hiroshima's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=261,
    set_code="SVPJ",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Renewal Open!",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Ride On",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
    ],
)
