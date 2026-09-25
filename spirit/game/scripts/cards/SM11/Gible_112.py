"""Gible (SM - Unified Minds 112/236 -- JP SM10a 034/054).

Basic Fighting Pokemon. HP 60, weakness Grass x2, retreat 1.

  Stampede         [F] 10
  Headbutt Bounce  [FC] 30
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="883f21ee-63c2-506e-ab7c-3fc122e97190",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    display_name="Gible",
    searchable_by=['Gible', 'Basic', 'Gible'],
    subtypes=['Basic'],
    collector_number=112,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=443,
    abilities=[
        Attack(title="Stampede", game_text="",
               cost={PokemonTypes.FIGHTING: 1}, damage=10),
        Attack(title="Headbutt Bounce", game_text="",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=30),
    ],
)
