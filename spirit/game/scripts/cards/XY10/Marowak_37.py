"""Marowak (XY - Fates Collide 37/124 -- JP XY-P promo, the art used here).

Stage 1 Fighting Pokemon, evolves from Cubone. HP 100, weakness Grass x2,
retreat 2.

  Ability  Bodyguard  Prevent all effects of attacks done to you or your
                      hand by your opponent's Pokemon. Remove any existing
                      effects.
  Bonemerang  [FC] 60x  Flip 2 coins. This attack does 60 damage times the
                        number of heads.

The shield is on the PLAYER and their hand (blocks_player_attack_effects):
an attack's "your opponent can't play Item cards", hand discards and
shuffles bounce off; on arrival the attack-made play locks already on the
owner are dropped. Effects done to Pokemon are not its business, so
Latios-GX's Clear Vision-GX (which binds the opponent's Pokemon, not the
player) still stops the owner's GX attacks, Bodyguard or no.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import (Ability, Attack, PokemonCardDef,
                                    Triggers)
from spirit.game.session.passives import Passive


class BodyguardPassive(Passive):
    def blocks_player_attack_effects(self, player_id, carrier):
        return carrier.owning_player_id == player_id


async def bodyguard_arrival(ctx):
    """"Remove any existing effects": the attack-made play locks on the
    owner (the ledger says which ones the attacks wrote)."""
    state = ctx.session.turn_state
    mine = [key for name, key in state.attack_effects
            if name == "play_locks" and key in state.play_locks.get(ctx.player_id, [])]
    if not mine:
        return
    state.play_locks[ctx.player_id] = [
        e for e in state.play_locks.get(ctx.player_id, []) if e not in mine]
    state.attack_effects = [(n, k) for n, k in state.attack_effects
                            if not (n == "play_locks" and k in mine)]


card = PokemonCardDef(
    guid="32baf6af-e851-5efb-8d43-eb3904e9c832",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    family_id=104,
    abilities=[
        Ability(
            title="Bodyguard",
            game_text="Prevent all effects of attacks done to you or your hand by your opponent's Pokémon. Remove any existing effects.",
            trigger=(Triggers.ON_EVOLVE, Triggers.ON_PLAY),
            effect=bodyguard_arrival,
            passive=BodyguardPassive(),
        ),
        Attack(
            title="Bonemerang",
            game_text="Flip 2 coins. This attack does 60 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=flip_damage(coins=2, per_heads=60),
        ),
    ],
)
