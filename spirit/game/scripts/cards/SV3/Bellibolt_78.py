"""Bellibolt (SV3 78 -- JP SV3 041; English OBF/201, OBF/78). Japanese art.
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
from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
from spirit.game.session.passives import Passive, carrier_pokemon



class InsulatorPassive(Passive):
    def prevents_damage(self, calc, carrier):
        return bool(calc.is_attack and calc.is_opposing and carrier_pokemon(carrier) is calc.target
                    and calc.attacker is not None and _of_type(calc.attacker, PokemonTypes.LIGHTNING))


card = PokemonCardDef(
    guid="2c3a0f16-5d72-5348-bf0c-3274ed9b0ff0",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name",
    display_name="Bellibolt",
    searchable_by=["Bellibolt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Ability(
            title="Insulator",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Lightning Pokémon.",
            passive=InsulatorPassive(),
        ),
        Attack(
            title="Thunderous Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ac.ignore_effects_attack(),
        ),
    ],
)
