"""Litten (SMPJ 259 -- JP SMP 259; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="787b2009-87cf-56a0-8848-499fb6a0708e",
    key="SMPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    display_name="Litten",
    searchable_by=["Litten", "Basic"],
    subtypes=["Basic"],
    collector_number=259,
    set_code="SMPJ",
    regulation_mark="B",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=725,
    abilities=[
        Attack(
            title="Scratch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
