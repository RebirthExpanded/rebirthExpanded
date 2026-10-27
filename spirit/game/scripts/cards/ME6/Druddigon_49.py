"""Druddigon (ME6 49 -- JP M6 049; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="c861a00b-af63-5d1c-9f8a-cb2becb83bc6",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic"],
    subtypes=["Basic"],
    collector_number=49,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=621,
    abilities=[
        Attack(
            title="Drag Out",
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. This attack does 40 damage to the new Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            effect=su.gust_attack(damage_to_new_active=40, damage_before=0),
        ),
        Attack(
            title="Slash",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
