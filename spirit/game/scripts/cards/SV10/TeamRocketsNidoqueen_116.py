"""Team Rocket's Nidoqueen (SV10 116 -- JP SV10 060; English DRI/116). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _named(prefix):
    def pred(card) -> bool:
        return card is not None and (getattr(def_for(card.archetype_id), "display_name", "") or "").startswith(prefix)
    return pred


def _name_has(*parts):
    def pred(card) -> bool:
        name = (getattr(def_for(card.archetype_id), "display_name", "") or "") if card is not None else ""
        return any(p in name for p in parts)
    return pred


def _nidoking_benched(ctx) -> bool:
    return any(_name_has("Nidoking")(p) for p in ctx.my_bench())


card = PokemonCardDef(
    guid="413d30ee-99c9-535c-acb8-8afdcfa241b7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidoqueen.Name",
    display_name="Team Rocket's Nidoqueen",
    searchable_by=["Team Rocket's Nidoqueen", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=116,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsNidorina.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Love Impact",
            game_text="If a Pokémon that has \"Nidoking\" in its name is on your Bench, this attack does 120 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(_nidoking_benched, 120),
        ),
        Attack(
            title="Mega Kick",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2},
            damage=130,
        ),
    ],
)
