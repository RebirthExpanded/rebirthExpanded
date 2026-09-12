"""Luxio (BW - Next Destinies 45/99 -- JP BKZ 006, the art here).

Stage 1 Lightning Pokemon, evolves from Shinx. HP 80, weakness Fighting x2,
no resistance, retreat 0.

  Quick Turn [L] 20x  Flip 2 coins. This attack does 20 damage times the
                      number of heads.
  Bite [CC] 30
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.data_utils import Attack, PokemonCardDef

card = PokemonCardDef(
    guid="0989017e-c9ce-5e50-9fce-6298a97cb8e4",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Luxio.Name",
    display_name="Luxio",
    searchable_by=["Luxio", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="BW4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name",
    family_id=403,
    abilities=[
        Attack(title="Quick Turn",
               game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
               cost={PokemonTypes.LIGHTNING: 1},
               damage=20, damage_operator="x",
               effect=flip_damage(coins=2, per_heads=20)),
        Attack(title="Bite", game_text="",
               cost={PokemonTypes.COLORLESS: 2}, damage=30),
    ],
)
