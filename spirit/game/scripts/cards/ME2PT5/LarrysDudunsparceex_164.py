"""Larry's Dudunsparce ex (ME2PT5 164 -- JP MC 577; English ASC/164). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="da0fe7e4-1ae5-51e2-9713-e7a816a69c6e",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysDudunsparceex.Name",
    display_name="Larry's Dudunsparce ex",
    searchable_by=["Larry's Dudunsparce ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=164,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LarrysDunsparce.Name",
    family_id=206,
    abilities=[
        Attack(
            title="Work Rush",
            game_text="Flip a coin for each Energy attached to this Pokémon. This attack does 80 damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            damage_operator="x",
            effect=ac.flip_damage(per_heads=80, coins_from=ac.count_energy("self")),
        ),
    ],
)
