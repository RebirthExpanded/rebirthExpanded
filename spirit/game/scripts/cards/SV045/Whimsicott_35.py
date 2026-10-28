"""Whimsicott (SV045 35 -- JP SVEM 008; English PAF/35). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers


card = PokemonCardDef(
    guid="c89ee0fb-b8ee-5fa6-8bf7-f021c1bb1713",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    family_id=546,
    abilities=[
        Attack(
            title="Fairy Wind",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
        ),
    ],
)
