"""Sigilyph (BW - Plasma Freeze 41/116 -- JP BW9 033/076, the art here).

Basic Psychic Pokemon. HP 90, weakness Lightning x2, resistance Fighting
-20, retreat 1.

  Ability: Toolbox  This Pokemon may have up to 4 Pokemon Tools attached
                    to it. (If this Ability stops working, discard Pokemon
                    Tools from this Pokemon until only 1 remains.)
  Cutting Wind [PCC] 70

The discard when Toolbox stops working is the engine's tool-capacity
check (GameSession._enforce_tool_capacity). The Tools' own effects that go
off together are ordered by Sigilyph's owner: every "when damaged" effect
(Rocky Helmet, Lucky Helmet, Spiky Energy) first, then the Knock Out ones
(Spell Tag, Cursed Shovel, Wishful Baton, Gift Energy, Exp. Share).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.passives import Passive

TOOL_CAPACITY = 4


class ToolboxPassive(Passive):
    def tool_capacity(self, pokemon, carrier):
        return TOOL_CAPACITY if pokemon is carrier else 1


card = PokemonCardDef(
    guid="b71b2764-0172-54a3-b602-45627b19862f",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sigilyph.Name",
    display_name="Sigilyph",
    searchable_by=["Sigilyph", "Basic"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=561,
    abilities=[
        Ability(
            title="Toolbox",
            game_text="This Pokémon may have up to 4 Pokémon Tool cards attached to it. (If this Ability stops working, discard Pokémon Tool cards from this Pokémon until only 1 remains.)",
            passive=ToolboxPassive(),
        ),
        Attack(
            title="Cutting Wind",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
