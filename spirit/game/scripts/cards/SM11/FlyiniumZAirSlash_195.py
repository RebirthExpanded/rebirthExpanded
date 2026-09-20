"""Flyinium Z: Air Slash (SM - Unified Minds 195/236 -- JP SM10b 045/054, the art here).

Pokemon Tool.

  "If the Pokemon this card is attached to has the Air Slash attack, it
   can use the GX attack on this card. (You still need the necessary
   Energy to use this attack.)"

  Speeding Skystrike-GX  [CCCC] 180  Prevent all effects of attacks,
                         including damage, done to this Pokemon during
                         your opponent's next turn. (You can't use more
                         than 1 GX attack in a game.)

The GX attack is a granted ability of the Tool (it joins the holder's
own attack list like Forest Seal Stone's VSTAR Power), gated by the
attack's own condition on the holder having Air Slash; the once-a-game
GX rule and the Energy cost apply as for any GX attack.
"""

from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import has_attack_titled
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.data_utils import Attack, PokemonToolCardDef

_has_air_slash = has_attack_titled("Air Slash")


def _holder_has_air_slash(board, player_id, pokemon) -> bool:
    return _has_air_slash(pokemon)


card = PokemonToolCardDef(
    guid="76e2bb99-69d2-5f7b-a173-02e3ef0f6fcd",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FlyiniumZAirSlash.Name",
    display_name="Flyinium Z: Air Slash",
    searchable_by=["Flyinium Z: Air Slash", "Flyinium Z", "Item", "Pokémon Tool", "FlyiniumZAirSlash"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=195,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Attack(
            title="Speeding Skystrike-GX",
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=180,
            gx=True,
            condition=_holder_has_air_slash,
            effect=protect_next_turn(prevent=True, effects_too=True),
        ),
    ],
)
