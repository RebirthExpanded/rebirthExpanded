"""Archaludon (ME2 75 -- JP M2 063; English PFL/75). Japanese art.
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

from spirit.game.session.effects import is_basic_pokemon_in_play


card = PokemonCardDef(
    guid="7e883723-b083-584c-9b01-d5ab537c6f6a",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludon.Name",
    display_name="Archaludon",
    searchable_by=["Archaludon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Duraludon.Name",
    family_id=884,
    abilities=[
        Attack(
            title="Coated Attack",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.METAL: 3},
            damage=120,
            effect=_shield_after_hit(is_basic_pokemon_in_play),
        ),
    ],
)
