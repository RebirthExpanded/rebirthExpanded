"""Tsareena (SV3 18 -- JP SV2P 009; English OBF/18). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class _NoEvolve(Passive):
    def blocks_evolution(self, player_id, target, carrier):
        return target is carrier_pokemon(carrier) and player_id == target.owning_player_id


async def queenly_heel(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and not ctx.effects_blocked(d):
        ctx.add_passive_through_opponents_turn(d, _NoEvolve())


card = PokemonCardDef(
    guid="8c746f3a-82a2-5551-9a61-a8b07aea95c2",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name",
    display_name="Tsareena",
    searchable_by=["Tsareena", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name",
    family_id=761,
    abilities=[
        Attack(
            title="Queenly Heel",
            game_text="During your opponent's next turn, Pokémon can't be played from your opponent's hand to evolve the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=queenly_heel,
        ),
        Attack(
            title="Spinning Kick",
            game_text="This Pokémon also does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 2},
            damage=160,
            effect=ac.recoil_attack(20),
        ),
    ],
)
