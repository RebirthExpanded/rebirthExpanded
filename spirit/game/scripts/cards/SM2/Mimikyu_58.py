"""Mimikyu (SM - Guardians Rising 58/145 -- JP SM2L 025/050).

Basic Psychic Pokemon. HP 70, no weakness, retreat 1.

  Filch    [C]   Draw 2 cards.
  Copycat  [PC]  If your opponent's Pokemon used an attack that isn't a GX
                 attack during their last turn, use it as this attack.

The attack copied is whichever one of THEIR Pokemon used last turn, read
off the turn ledger by title and looked up on that Pokemon's own card, so
it comes with its printed damage and effect. A GX attack is not copied,
and with nothing used last turn the attack does nothing. The copy goes
through the shared copy path, so a copied attack that copies (Copycat
into Copycat) fizzles on the re-entry guard.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import draw_attack
from spirit.game.data_utils import Attack, PokemonCardDef, def_for


def _their_last_attacks(board, player_id):
    """(pokemon-or-None, Attack) for each attack their side used last turn."""
    found = []
    for used_id, archetype_id, title in board.turn_state.attacks_used_last_turn:
        entity = board.get_entity(used_id)
        if entity is not None and entity.owning_player_id == player_id:
            continue
        definition = def_for(archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if isinstance(ability, Attack) and ability.title == title \
                    and not getattr(ability, "gx", False):
                found.append((entity, ability))
    return found


def _copycat_condition(board, player_id, pokemon) -> bool:
    return bool(_their_last_attacks(board, player_id))


async def copycat(ctx):
    """Use the attack their Pokemon used last turn as this attack."""
    options = _their_last_attacks(ctx.board, ctx.player_id)
    if not options:
        return
    if len(options) == 1:
        chosen = options[0][1]
    else:
        picked = await ctx.choose_attack_to_copy(options, "Choose an attack to copy")
        if picked is None:
            return
        chosen = picked[1]
    await ctx.use_attack(chosen)


card = PokemonCardDef(
    guid="b81efe38-1ece-521b-9aef-4243687b96b8",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="SM2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Copycat",
            game_text="If your opponent's Pokémon used an attack that isn't a GX attack during their last turn, use it as this attack.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            condition=_copycat_condition,
            effect=copycat,
        ),
    ],
)
