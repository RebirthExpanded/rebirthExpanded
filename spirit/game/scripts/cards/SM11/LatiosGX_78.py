"""Latios-GX (SM - Unified Minds 78/236 -- JP SM11 034/094).

Basic Psychic Pokemon-GX. HP 170, weakness Psychic x2, retreat 0.

  Ability  Power Bind  If you have 4 or fewer Pokemon in play, this
                       Pokemon can't attack.
  Tag Purge  [PCC] 120  During your opponent's next turn, prevent all
                        damage done to this Pokemon by attacks from TAG
                        TEAM Pokemon.
  Clear Vision-GX  [P]  For the rest of this game, your opponent can't use
                        any GX attacks.

Clear Vision is an effect of an attack on the opponent (TurnState
.gx_blocks): Pokemon Ranger removes it, Misty & Lorelei does not get past
it, and a Pokemon shielded from Latios-GX's attack effects (Keldeo-GX's
Pure Heart) is not bound by it. A GX attack the opponent already used
stays used whatever happens to the ban.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, subtypes_for
from spirit.game.session.passives import Passive, carrier_pokemon


class PowerBindPassive(Passive):
    def blocks_attacking(self, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        return len(board.pokemon_in_play(pokemon.owning_player_id)) <= 4


class TagPurgeShield(Passive):
    """No damage from TAG TEAM attackers reaches the carrier."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target is not carrier_pokemon(carrier) or calc.attacker is None:
            return False
        return "TAG TEAM" in subtypes_for(calc.attacker.archetype_id)


async def tag_purge(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, TagPurgeShield())


async def clear_vision_gx(ctx):
    ctx.session.turn_state.block_gx_attacks(ctx.opponent_id, ctx.attacker)


card = PokemonCardDef(
    guid="d7697756-efc7-5d3b-b01b-ee7f414658de",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiosGX.Name",
    display_name="Latios-GX",
    searchable_by=["Latios-GX", "Basic", "GX", "LatiosGX"],
    subtypes=["Basic", "GX"],
    collector_number=78,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=381,
    abilities=[
        Ability(
            title="Power Bind",
            game_text="If you have 4 or fewer Pokémon in play, this Pokémon can't attack.",
            passive=PowerBindPassive(),
        ),
        Attack(
            title="Tag Purge",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from TAG TEAM Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=tag_purge,
        ),
        Attack(
            title="Clear Vision-GX",
            game_text="For the rest of this game, your opponent can't use any GX attacks. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=0,
            gx=True,
            effect=clear_vision_gx,
        ),
    ],
)
