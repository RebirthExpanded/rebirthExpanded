"""Luxray (SV - Paldea Evolved 71/193 -- JP SV2D 021/071, the art here).

Stage 2 Lightning Pokemon, evolves from Luxio. HP 150, weakness Fighting x2,
no resistance, retreat 1.

  Ability  Swelling Flash  Once during your turn, if this Pokemon is in
                           your hand and you have more Prize cards remaining
                           than your opponent, you may put this Pokemon onto
                           your Bench.
  Wild Charge [LCC] 180  This Pokemon also does 20 damage to itself.

Swelling Flash is a hand Ability: PokemonCardDef.bench_from_hand makes the
legal-action builder offer Luxray as a Bench drop while the Prize counts
line up (it is an Ability, so Garbotoxin reaching the hand switches it off),
and the executor treats it as a PUT, not a play -- no ON_PLAY, no Gapejaw
Bog. "Once during your turn" needs no marker: the card leaves the hand.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef


def _swelling_flash(board, player_id, card) -> bool:
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    mine = board.find_player_area(player_id, "prizePile")
    theirs = board.find_player_area(opponent, "prizePile")
    if not mine or not theirs:
        return False
    return len(mine.children) > len(theirs.children)


card = PokemonCardDef(
    guid="5bff8eb4-1fb7-5123-8971-824462367c63",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxray.Name",
    display_name="Luxray",
    searchable_by=["Luxray", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=71,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    family_id=403,
    bench_from_hand=_swelling_flash,
    abilities=[
        Ability(title="Swelling Flash",
                game_text="Once during your turn, if this Pokémon is in your hand and you have more Prize cards remaining than your opponent, you may put this Pokémon onto your Bench."),
        Attack(title="Wild Charge",
               game_text="This Pokémon also does 20 damage to itself.",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
               damage=180, effect=recoil_attack(20)),
    ],
)
