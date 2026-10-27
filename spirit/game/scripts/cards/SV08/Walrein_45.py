"""Walrein (SV08 45 -- JP SV8 029; English SSP/45). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.models.board import EnergyEntity


class _FrigidFangs(Passive):
    """Game-level: during that turn, the opponent's Pokemon with 2 or less
    Energy attached can't attack."""

    def __init__(self, victim, turn):
        self.victim, self.turn = victim, turn

    def blocks_attacking(self, pokemon, carrier, board):
        ts = getattr(board, "turn_state", None)
        if ts is None or ts.turn_number != self.turn or pokemon.owning_player_id != self.victim:
            return False
        return sum(1 for c in pokemon.children if isinstance(c, EnergyEntity)) <= 2


async def frigid_fangs(ctx):
    await ctx.deal_damage()
    ctx.add_game_passive(_FrigidFangs(ctx.opponent_id, ctx.session.turn_state.turn_number + 1))


card = PokemonCardDef(
    guid="f012c7e4-7c90-529b-96c6-86be35e7c926",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Walrein.Name",
    display_name="Walrein",
    searchable_by=["Walrein", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sealeo.Name",
    family_id=363,
    abilities=[
        Attack(
            title="Frigid Fangs",
            game_text="During your opponent's next turn, Pokémon that have 2 or less Energy attached can't attack. (This includes new Pokémon that come into play.)",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=frigid_fangs,
        ),
        Attack(
            title="Megaton Fall",
            game_text="This Pokémon also does 50 damage to itself.",
            cost={PokemonTypes.WATER: 2},
            damage=170,
            effect=ac.recoil_attack(50),
        ),
    ],
)
