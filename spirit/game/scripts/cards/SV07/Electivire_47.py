"""Electivire (SV07 47 -- JP SV7 029; English SCR/47). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _TeamCantAttack(Passive):
    """Game-level: the owner's Pokemon can't attack during that turn."""

    def __init__(self, owner, turn):
        self.owner, self.turn = owner, turn

    def blocks_attacking(self, pokemon, carrier, board):
        ts = getattr(board, "turn_state", None)
        return ts is not None and ts.turn_number == self.turn and pokemon.owning_player_id == self.owner


async def unleash_lightning(ctx):
    await ctx.deal_damage()
    ctx.add_game_passive(_TeamCantAttack(ctx.player_id, ctx.session.turn_state.turn_number + 2))


card = PokemonCardDef(
    guid="e3494b3c-b155-559b-a82d-eac4f7565b37",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=47,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    family_id=239,
    abilities=[
        Attack(
            title="Electroslug",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
        ),
        Attack(
            title="Unleash Lightning",
            game_text="During your next turn, your Pokémon can't attack. (This includes new Pokémon that come into play.)",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=220,
            effect=unleash_lightning,
        ),
    ],
)
