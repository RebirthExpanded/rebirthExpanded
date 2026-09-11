"""Goodra (XY - Phantom Forces 77/119 -- JP XY-P promo, the art here).

Stage 2 Dragon Pokemon, evolves from Sliggoo. HP 140, weakness Fairy x2,
retreat 3.

  Ability  Slip Trip  Each player can't attach any Pokemon Tool cards from
                      their hand to any of their Pokemon.
  Dragon Pulse  [WYCC] 130  Discard the top card of your deck.

Slip Trip takes the Tool offer off both players' hands (blocks_tool_attach);
Tools already attached stay and keep working.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import mill_attack
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive


class SlipTripPassive(Passive):
    def blocks_tool_attach(self, player_id, carrier):
        return True


card = PokemonCardDef(
    guid="3c993c2b-438c-5e8d-ad0e-9692807d093a",
    key="XY4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=77,
    set_code="XY4",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Slip Trip",
            game_text="Each player can't attach any Pokémon Tool cards from their hand to any of their Pokémon.",
            passive=SlipTripPassive(),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=mill_attack(1, opponent=False),
        ),
    ],
)
