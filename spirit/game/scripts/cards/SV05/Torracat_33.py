"""Torracat (SV05 33 -- JP SV5M 021; English TEF/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fd47bed7-9a8b-5ae0-97f7-169fecfa63d9",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name",
    display_name="Torracat",
    searchable_by=["Torracat", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name",
    family_id=725,
    abilities=[
        Attack(
            title="Bite",
            game_text="",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
        Attack(
            title="Flare Strike",
            game_text="During your next turn, this Pokémon can't use Flare Strike.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            locks_next_turn=True,
        ),
    ],
)
