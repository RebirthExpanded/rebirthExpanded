"""Mawile (SV05 112 -- JP SV5M 045; English TEF/112). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="62001110-50a8-54c8-9602-e3d86cb41315",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mawile.Name",
    display_name="Mawile",
    searchable_by=["Mawile", "Basic"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=303,
    abilities=[
        Attack(
            title="Invite and Strike",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot. This attack does 30 damage to the new Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.gust_attack(damage_to_new_active=30),
        ),
        Attack(
            title="Sharp Fang",
            game_text="",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
