"""Kommo-o (ME6A 91 -- JP M6a 091; English 30C/112, 30C/143). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="b91dffcb-124f-58d1-af56-a000e357bc6f",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=91,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Attack(
            title="Blazing Uppercut",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=250,
        ),
    ],
)
