"""Porygon2 (SVP 138 -- JP SV4M 049; English PAR/143, SVP/138). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="39f027c0-58bb-57c8-b0cd-a8b0944daa67",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    display_name="Porygon2",
    searchable_by=["Porygon2", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=138,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    family_id=137,
    abilities=[
        Attack(
            title="Powered Ball",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
