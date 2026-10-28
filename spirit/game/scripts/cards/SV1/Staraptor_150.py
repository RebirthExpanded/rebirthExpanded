"""Staraptor (SV1 150 -- JP SV1S 065; English SVI/150). Japanese art.
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

from spirit.game.session.effects import is_basic_pokemon_in_play


card = PokemonCardDef(
    guid="6b3180e6-54dc-5c23-9fba-bc62cab6c685",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staraptor.Name",
    display_name="Staraptor",
    searchable_by=["Staraptor", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=150,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Tailspin Away",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Basic Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=_shield_after_hit(is_basic_pokemon_in_play),
        ),
        Attack(
            title="Power Blast",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
