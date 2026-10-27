"""Noivern (ME2PT5 157 -- JP M2a 131; English ASC/157). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac


def _tooled(ctx) -> bool:
    return ac.has_tool(ctx.attacker)


card = PokemonCardDef(
    guid="298d5467-1ddc-5269-88c8-d966e8ed8f35",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name",
    display_name="Noivern",
    searchable_by=["Noivern", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=157,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name",
    family_id=714,
    abilities=[
        Attack(
            title="Agility",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Enhanced Blade",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 70 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1},
            damage=70,
            damage_operator="+",
            effect=ac.bonus_if(_tooled, 70),
        ),
    ],
)
