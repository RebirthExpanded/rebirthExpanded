"""Gothorita (BWPJ 323 -- JP WAK 023; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="027ba97f-73cf-57b4-a58a-574a23661498",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gothorita.Name",
    display_name="Gothorita",
    searchable_by=["Gothorita", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=323,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name",
    family_id=574,
    abilities=[
        Attack(
            title="Extrasensory",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
