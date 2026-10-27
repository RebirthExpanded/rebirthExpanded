"""Carkol (SV05 94 -- JP SV5K 040; English TEF/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="43781e75-b39d-5968-a7d8-f76fdbec01a3",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carkol.Name",
    display_name="Carkol",
    searchable_by=["Carkol", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rolycoly.Name",
    family_id=837,
    abilities=[
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(40),
        ),
        Attack(
            title="Boulder Crush",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
