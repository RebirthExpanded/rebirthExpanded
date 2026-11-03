"""Lucario (BWPJ 327 -- JP WAK 027; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="fbff8878-1271-578b-8c5e-94381d8ac737",
    key="BWPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=327,
    set_code="BWPJ",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Attack(
            title="Magnum Punch",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
