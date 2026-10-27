"""Team Rocket's Weezing (SV10 126 -- JP SV10 105; English DRI/126, DRI/199). Japanese art.
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


def _gas_crew(ctx) -> int:
    return sum(1 for pid in ctx.board.player_ids for p in ctx.board.pokemon_in_play(pid)
               if _name_has("Koffing", "Weezing")(p))


card = PokemonCardDef(
    guid="3cb9f27e-056b-520f-944b-910f98bdfcff",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsWeezing.Name",
    display_name="Team Rocket's Weezing",
    searchable_by=["Team Rocket's Weezing", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=126,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsKoffing.Name",
    family_id=109,
    abilities=[
        Attack(
            title="Explode Together Now",
            game_text="This attack does 40 damage for each Pokémon in play that has \"Koffing\" or \"Weezing\" in its name (both yours and your opponent's).",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(_gas_crew, 40),
        ),
    ],
)
