"""Nidoqueen (SV035 31 -- JP SV2a 031; English MEW/31). Japanese art.
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
    guid="79b96237-727c-5df5-a932-879da921ed5a",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name",
    display_name="Nidoqueen",
    searchable_by=["Nidoqueen", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name",
    family_id=29,
    abilities=[
        Attack(
            title="Queen Press",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=_shield_after_hit(is_basic_pokemon_in_play),
        ),
        Attack(
            title="Lunge Out",
            game_text="",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
