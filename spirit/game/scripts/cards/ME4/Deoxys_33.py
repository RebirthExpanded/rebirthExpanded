"""Deoxys (ME4 33 -- JP M4 033; English CRI/33). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class _ShieldFrom(Passive):
    """"Prevent all damage done to this Pokemon by attacks from <kind>"
    during the opponent's next turn."""

    def __init__(self, attacker_pred):
        self.attacker_pred = attacker_pred

    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None and self.attacker_pred(calc.attacker))


def _shield_after_hit(attacker_pred):
    async def effect(ctx):
        await ctx.deal_damage()
        ctx.add_passive_through_opponents_turn(ctx.attacker, _ShieldFrom(attacker_pred))
        if ctx.attacker.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(ctx.attacker.entity_id)
    return effect

from spirit.game.attributes import AbilityTypes
from spirit.game.data_utils import ABILITIES_BY_ID


def _has_ability(pokemon) -> bool:
    for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
        ability = ABILITIES_BY_ID.get(entry.get("abilityID")) if isinstance(entry, dict) else None
        if ability is not None and ability.ability_type == AbilityTypes.POKE_ABILITY:
            return True
    return False
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


card = PokemonCardDef(
    guid="1d824a69-12e1-588c-973a-2703d245fbe5",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Deoxys.Name",
    display_name="Deoxys",
    searchable_by=["Deoxys", "Basic"],
    subtypes=["Basic"],
    collector_number=33,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=386,
    abilities=[
        Attack(
            title="Psy Protection",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Pokémon that have an Ability.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=_shield_after_hit(_has_ability),
        ),
    ],
)
