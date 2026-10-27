"""Archaludon (SV085 70 -- JP SV7 073; English PRE/70, SCR/107, SCR/155). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac


async def _hit_then_lock(ctx):
    await ctx.deal_damage()
    ac.lock_all_attacks(ctx, ctx.attacker)
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class MetalBridgePassive(Passive):
    """Your Pokemon with Metal Energy attached have no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id and any(
                is_energy_of_type(e, PokemonTypes.METAL) for e in pokemon.children):
            return 0
        return cost


card = PokemonCardDef(
    guid="809377ed-103d-5c76-b28e-e6f943a0fdbe",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Archaludon.Name",
    display_name="Archaludon",
    searchable_by=["Archaludon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=70,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Rare,
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
        Ability(
            title="Metal Bridge",
            game_text="All of your Pokémon that have Metal Energy attached have no Retreat Cost.",
            passive=MetalBridgePassive(),
        ),
        Attack(
            title="Iron Blaster",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=_hit_then_lock,
        ),
    ],
)
