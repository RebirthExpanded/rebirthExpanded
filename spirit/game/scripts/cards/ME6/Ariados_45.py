"""Ariados (ME6 45 -- JP M6 045; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
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
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.attributes import PokemonStage


def _basic(pokemon) -> bool:
    return pokemon.get_attribute(AttrID.STAGE) == PokemonStage.BASIC.value


card = PokemonCardDef(
    guid="3d1232c9-55e0-5772-9183-370d2f79d4ab",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ariados.Name",
    display_name="Ariados",
    searchable_by=["Ariados", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spinarak.Name",
    family_id=167,
    abilities=[
        Attack(
            title="Severe Poison",
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 4 damage counters instead of 1 on that Pokémon during Pokémon Checkup.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED, counters=4),
        ),
        Attack(
            title="Stealthy Sting",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=_shield_after_hit(_basic),
        ),
    ],
)
