"""Blitzle (SM - Lost Thunder 81/214 -- JP SM12a 045/173, the art here;
first printed as JP SM8 039/095).

Basic Lightning Pokemon. HP 70, weakness Fighting x2, resistance Metal -20,
retreat 1.

  Flop      [L] 10
  Zap Kick  [LC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="ed6a6167-b40c-595e-9187-980871e19d56",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    display_name="Blitzle",
    searchable_by=['Blitzle', 'Basic', 'Blitzle'],
    subtypes=['Basic'],
    collector_number=81,
    set_code="SM8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=522,
    abilities=[
        Attack(title="Flop", game_text="",
               cost={PokemonTypes.LIGHTNING: 1}, damage=10),
        Attack(title="Zap Kick", game_text="",
               cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1}, damage=20),
    ],
)
