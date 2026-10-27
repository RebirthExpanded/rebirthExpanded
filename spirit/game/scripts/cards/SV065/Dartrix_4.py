"""Dartrix (SV065 4 -- JP SV6a 004; English SFA/4). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for

from spirit.game.session.effects import is_pokemon_card


def _united_wings(ctx) -> int:
    return sum(1 for c in ctx.discard_pile() if is_pokemon_card(c)
               and any(getattr(a, "title", "") == "United Wings" for a in getattr(def_for(c.archetype_id), "abilities", [])))


card = PokemonCardDef(
    guid="96e56007-923d-5be9-82f4-33e3df307fbb",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    display_name="Dartrix",
    searchable_by=["Dartrix", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=4,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name",
    family_id=722,
    abilities=[
        Attack(
            title="United Wings",
            game_text="This attack does 20 damage for each Pokémon in your discard pile that has the United Wings attack.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_united_wings, 20),
        ),
        Attack(
            title="Cutting Wind",
            game_text="",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)
