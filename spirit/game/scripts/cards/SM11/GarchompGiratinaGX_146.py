"""Garchomp & Giratina-GX (SM - Unified Minds 146/236 -- JP SM10a 032/054).

Basic Dragon TAG TEAM Pokemon-GX. HP 270, weakness Fairy x2, no
resistance, retreat 3.

  Linear Attack     [C]      40 damage to 1 of your opponent's Pokemon.
  Calamitous Slash  [PFC] 160+  If your opponent's Active Pokemon already
                               has any damage counters on it, +80.
  GG End-GX         [PPF]    Discard 1 of your opponent's Pokemon and all
                             cards attached to it. With 3 extra [F] Energy
                             attached, discard 2 of them instead.

GG End-GX DISCARDS rather than knocks out, which is the whole point of the
card: no Prize is taken for a Pokemon that leaves this way, and nothing
that watches for a knockout fires. Emptying their Active spot promotes a
new Active for them afterwards -- and with nothing to promote, they lose,
which is the same check a knockout would run.

Calamitous Slash reads damage counters on their Active at the moment it
resolves, so the bonus is decided before its own damage lands.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, has_damage, snipe_attack
from spirit.game.data_utils import Attack, PokemonCardDef
from spirit.game.session.effects import full_stack
from spirit.game.session.legal_actions import attack_cost_satisfied

# The [PPF] cost plus the three extra [F], asked as a single question.
_COST_PLUS_EXTRAS = {"Psychic": 2, "Fighting": 4}


async def gg_end_gx(ctx):
    """Discard 1 of their Pokemon (2 with 3 extra [F]) and everything on it."""
    energies = ctx.attached_energies(ctx.attacker)
    count = 2 if attack_cost_satisfied(_COST_PLUS_EXTRAS, energies, ctx.board) else 1
    lost_active = False
    for _ in range(count):
        candidates = [p for p in ctx.opponent_pokemon_in_play()
                      if not ctx.effects_blocked(p)]
        if not candidates:
            break
        target = await ctx.choose_pokemon(
            candidates, "Choose 1 of your opponent's Pokémon to discard.")
        if target is None:
            break
        lost_active = lost_active or target is ctx.opponent_active()
        await ctx.discard_cards(full_stack(target))
    if lost_active:
        async def _promote():
            if not await ctx.session._promote_new_active(ctx.opponent_id):
                screen_name = ctx.session.players[ctx.opponent_id].screen_name
                await ctx.session.end_game(
                    ctx.player_id, f"{screen_name} has no Pokémon left")
        ctx.deferred_actions.append(_promote)


card = PokemonCardDef(
    guid="cc8eca0a-93ec-576a-8067-2ead3ed2dc38",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GarchompGiratinaGX.Name",
    display_name="Garchomp & Giratina-GX",
    searchable_by=["Garchomp & Giratina-GX", "Basic", "TAG TEAM", "GX",
                   "GarchompGiratinaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=146,
    set_code="SM11",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=445,
    abilities=[
        Attack(
            title="Linear Attack",
            game_text="This attack does 40 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=snipe_attack(40, pool="any"),
        ),
        Attack(
            title="Calamitous Slash",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 80 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.FIGHTING: 1,
                  PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=bonus_if(has_damage("defender"), 80),
        ),
        Attack(
            title="GG End-GX",
            game_text="Discard 1 of your opponent's Pokémon and all cards attached to it. If this Pokémon has at least 3 extra Fighting Energy attached to it (in addition to this attack's cost), discard 2 of your opponent's Pokémon and all cards attached to them instead. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.FIGHTING: 1},
            gx=True,
            effect=gg_end_gx,
        ),
    ],
)
