"""Makuhita (JP HGSS-era print "HSZp" 021, the art here -- pool-local
Promo_BW 901: no English print with this text).

Basic Fighting Pokemon. HP 70, weakness Psychic x2, no resistance,
retreat 2.

  Arm Thrust [FF] 30
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="55758830-5e70-5636-9c4e-6310f099dde7",
    key="Promo_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    display_name="Makuhita",
    searchable_by=["Makuhita", "Basic"],
    subtypes=["Basic"],
    collector_number=901,
    set_code="Promo_BW",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=296,
    abilities=[
        Attack(title="Arm Thrust", game_text="",
               cost={PokemonTypes.FIGHTING: 2}, damage=30),
    ],
)
