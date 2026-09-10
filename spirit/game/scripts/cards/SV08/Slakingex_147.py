"""Slaking ex (SV - Surging Sparks 147/191).

Stage 2 Colorless Pokemon ex. HP 340, weakness Fighting x2, no resistance,
retreat 4.

  Ability  Born to Slack  If your opponent has no Pokemon ex or Pokemon V
                          in play, this Pokemon can't attack.

  Great Swing [CC] 280  Discard an Energy from this Pokemon.

The second user of blocks_attacking, and the reason it belongs on the
Passive rather than on the Attack: this is an ABILITY that stops attacking,
so an ability lock lifts it. Under Garbotoxin or Path to the Peak, Slaking
ex swings at anything.

"Pokemon ex or Pokemon V" goes through the pool's own predicates, so
Pokemon V covers VSTAR, VMAX and V-UNION (is_pokemon_v) and ex covers the
uppercase XY-era EX as well (is_pokemon_ex) -- the bundling the SV cards in
this pool already rely on.

The check is on the OPPONENT's board only, and on their whole board:
a Benched Pokemon ex is enough to switch the attack back on.
"""

from spirit.game.data_utils import (PokemonCardDef, Attack, Ability,
                                    is_pokemon_ex, is_pokemon_v)
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.passives import Passive


class BornToSlackPassive(Passive):
    """No opposing Pokemon ex or V in play, no attacking."""

    def blocks_attacking(self, pokemon, carrier, board):
        if pokemon is not carrier:
            return False
        opponent_id = next(
            (pid for pid in board.player_ids if pid != carrier.owning_player_id),
            None,
        )
        if opponent_id is None:
            return False
        return not any(
            is_pokemon_ex(p.archetype_id) or is_pokemon_v(p.archetype_id)
            for p in board.pokemon_in_play(opponent_id)
        )


card = PokemonCardDef(
    guid="42b60990-d893-56ab-a8b0-1ebb3ccbc705",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakingex.Name",
    display_name="Slaking ex",
    searchable_by=["Slaking ex", "Stage 2", "ex", "Slakingex"],
    subtypes=["Stage 2", "ex"],
    collector_number=147,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vigoroth.Name",
    family_id=287,
    abilities=[
        Ability(
            title="Born to Slack",
            game_text="If your opponent has no Pokémon ex or Pokémon V in play, this Pokémon can't attack.",
            passive=BornToSlackPassive(),
        ),
        Attack(
            title="Great Swing",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=280,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
