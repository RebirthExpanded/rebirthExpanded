"""Yungoos (SM - Unified Minds 180/236 -- JP SM11 077/094).

Basic Colorless Pokemon. HP 70, weakness Fighting x2, retreat 1.

  Cavernous Chomp  [CC] 30
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="8b88808e-cbfb-54a3-bc22-1789d5ceb86d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yungoos.Name",
    display_name="Yungoos",
    searchable_by=['Yungoos', 'Basic', 'Yungoos'],
    subtypes=['Basic'],
    collector_number=180,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=734,
    abilities=[
        Attack(title="Cavernous Chomp", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=30),
    ],
)
