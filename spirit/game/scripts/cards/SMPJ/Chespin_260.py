"""Chespin (SMPJ 260 -- JP SMP 260; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="1cc4905e-0253-5402-96af-2d219602fe76",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Chespin.Name",
    display_name="Chespin",
    searchable_by=["Chespin", "Basic"],
    subtypes=["Basic"],
    collector_number=260,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=650,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=su.heal_attack(10),
        ),
    ],
)
