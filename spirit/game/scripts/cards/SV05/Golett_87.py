"""Golett (SV05 87 -- JP SV5K 035; English TEF/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="d81a2d85-8104-54b3-8c2b-df164c3c6f74",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett", "Basic"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=622,
    abilities=[
        Attack(
            title="Iron Defense",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=pc.flip_protection(prevent=True),
        ),
        Attack(
            title="Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
