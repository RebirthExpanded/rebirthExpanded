"""Graveler (SV035 75 -- JP SV2a 075; English MEW/75). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="8a51417d-5b62-5745-90e1-86e098555acc",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Rock Cannon",
            game_text="Flip a coin until you get tails. This attack does 40 damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=40),
        ),
        Attack(
            title="Heavy Impact",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
