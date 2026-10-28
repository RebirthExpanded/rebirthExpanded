"""Ivysaur (SV035 2 -- JP SV2a 002; English MEW/167, MEW/2). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="aa53ed16-411a-5caa-94b1-117d22a8b152",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    family_id=1,
    abilities=[
        Attack(
            title="Leech Seed",
            game_text="Heal 20 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.heal_attack(20),
        ),
        Attack(
            title="Vine Whip",
            game_text="",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
