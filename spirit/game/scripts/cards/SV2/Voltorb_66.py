"""Voltorb (SV - Paldea Evolved 66/193 -- JP svM 042/175, Starter Deck
Generations).

Basic Lightning Pokemon. HP 70, weakness Fighting x2, retreat 1,
regulation mark G.

  Lightning Ball  [L]  10
  Rollout         [CC] 20
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="ce91a17c-4871-507e-a2e4-e16c19dc0c35",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name",
    display_name="Voltorb",
    searchable_by=["Voltorb", "Basic"],
    subtypes=["Basic"],
    collector_number=66,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(title="Lightning Ball", game_text="",
               cost={PokemonTypes.LIGHTNING: 1}, damage=10),
        Attack(title="Rollout", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=20),
    ],
)
