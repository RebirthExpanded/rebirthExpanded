"""Serperior (ME3 6 -- JP M3 006; English MEP/64, POR/6). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.data_utils import def_for


def _rosa_in_discard(ctx) -> bool:
    return any(getattr(def_for(c.archetype_id), "display_name", None) == "Rosa's Encouragement"
               for c in ctx.discard_pile())


card = PokemonCardDef(
    guid="eebf8843-4f6d-5f41-a67c-f92e35b46cf3",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=6,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Attack(
            title="Regal Command",
            game_text="This attack does 20 damage for each of your Pokémon in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine"), 20),
        ),
        Attack(
            title="Solar Coiling",
            game_text="If Rosa's Encouragement is in your discard pile, this attack does 150 more damage.",
            cost={PokemonTypes.GRASS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_rosa_in_discard, 150),
        ),
    ],
)
