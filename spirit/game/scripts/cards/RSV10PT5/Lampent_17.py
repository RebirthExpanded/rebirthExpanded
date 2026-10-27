"""Lampent (RSV10PT5 17 -- JP SV11B 016; English WHT/102, WHT/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="b6c0c851-e571-5b10-b3db-1da543004e85",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    display_name="Lampent",
    searchable_by=["Lampent", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name",
    family_id=607,
    abilities=[
        Attack(
            title="Fire Blast",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
