"""Hakama Pikachu (SMPJ 208 -- JP SMP 208; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b375ef1b-959e-5185-aef1-c84b1cbcb83e",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HakamaPikachu.Name",
    display_name="Hakama Pikachu",
    searchable_by=["Hakama Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=208,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Excuse Me",
            game_text="Switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.switch_self_attack(),
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 10 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(10),
        ),
    ],
)
