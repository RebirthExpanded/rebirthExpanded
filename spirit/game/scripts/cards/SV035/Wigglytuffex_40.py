"""Wigglytuff ex (SV035 40 -- JP SV2a 040; English MEW/187, MEW/40, PAF/222). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac

from spirit.game.attributes import TrainerType
from spirit.game.session.effects import is_special_energy


class ExpandingBodyPassive(Passive):
    """Special Energy attached: +100 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is carrier_pokemon(carrier) and any(is_special_energy(c) for c in pokemon.children):
            return 100
        return 0


def _supporter_played(ctx) -> bool:
    return any(ttype == TrainerType.SUPPORTER.value for _a, _n, ttype in ctx.session.turn_state.trainers_played)


card = PokemonCardDef(
    guid="fa0be2ec-5aa4-59de-8698-8f0dcd59bceb",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wigglytuffex.Name",
    display_name="Wigglytuff ex",
    searchable_by=["Wigglytuff ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=40,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    family_id=174,
    abilities=[
        Ability(
            title="Expanding Body",
            game_text="If this Pokémon has any Special Energy attached, it gets +100 HP.",
            passive=ExpandingBodyPassive(),
        ),
        Attack(
            title="Friend Tackle",
            game_text="If you played a Supporter card from your hand during this turn, this attack does 90 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=ac.bonus_if(_supporter_played, 90),
        ),
    ],
)
