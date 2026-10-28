"""Zangoose (SV1 147 -- JP SV1S 062; English SVI/147). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="9ef79aa8-00aa-5d02-876a-e8b25255af99",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic"],
    subtypes=["Basic"],
    collector_number=147,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Drag Off",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.gust_attack(damage_to_new_active=30),
        ),
        Attack(
            title="Slashing Claw",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
