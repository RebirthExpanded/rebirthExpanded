"""Gabite (SM - Unified Minds 113/236 -- JP SM10a 035/054).

Stage 1 Fighting Pokemon, evolves from Gible. HP 90, weakness Grass x2,
retreat 1.

  Corkscrew Punch  [F] 20
  Sharp Scythe     [FC] 40
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

from spirit.game.data_utils import Attack, PokemonCardDef


card = PokemonCardDef(
    guid="855e8c3b-44e9-599e-93c6-d9cb094f7678",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name",
    display_name="Gabite",
    searchable_by=['Gabite', 'Stage 1', 'Gabite'],
    subtypes=['Stage 1'],
    collector_number=113,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name",
    family_id=443,
    abilities=[
        Attack(title="Corkscrew Punch", game_text="",
               cost={PokemonTypes.FIGHTING: 1}, damage=20),
        Attack(title="Sharp Scythe", game_text="",
               cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1}, damage=40),
    ],
)
