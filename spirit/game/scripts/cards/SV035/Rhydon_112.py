"""Rhydon (SV035 112 -- JP SV2a 112; English MEW/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _played_this_turn(ctx, display_name) -> bool:
    for archetype_id, _name, _type in ctx.session.turn_state.trainers_played:
        if getattr(def_for(archetype_id), "display_name", None) == display_name:
            return True
    return False


def _charisma_played(ctx) -> bool:
    return _played_this_turn(ctx, "Giovanni's Charisma")


card = PokemonCardDef(
    guid="473a4864-1eb2-50d3-930c-0ff80f702b6a",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    display_name="Rhydon",
    searchable_by=["Rhydon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=112,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Wrack Down",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Charismatic Drill",
            game_text="If you played Giovanni's Charisma from your hand during this turn, this attack does 140 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            effect=ac.bonus_if(_charisma_played, 140),
        ),
    ],
)
