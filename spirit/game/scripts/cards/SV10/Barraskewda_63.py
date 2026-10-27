"""Barraskewda (SV10 63 -- JP SV10 030; English DRI/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="e3a7c5e6-bb8c-5185-a9ba-1543919fb1cd",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barraskewda.Name",
    display_name="Barraskewda",
    searchable_by=["Barraskewda", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arrokuda.Name",
    family_id=846,
    abilities=[
        Attack(
            title="Sharp Fin",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
        Attack(
            title="Dive",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 2},
            damage=60,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
