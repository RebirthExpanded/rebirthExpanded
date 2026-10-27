"""Alcremie (ME2 44 -- JP MBD 008; English PFL/44). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="bf32fb7b-a767-55b7-bac3-b90e42dfc8db",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alcremie.Name",
    display_name="Alcremie",
    searchable_by=["Alcremie", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Milcery.Name",
    family_id=868,
    abilities=[
        Attack(
            title="Sweet Circle",
            game_text="This attack does 20 damage for each of your Pokémon in play.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine"), 20),
        ),
    ],
)
