"""Glaceon VSTAR (Promo_SWSH 197 -- JP S12a 217; English SP/197). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="677c33ad-e89e-5fef-9e29-4649ab0eb23d",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonVSTAR.Name",
    display_name="Glaceon VSTAR",
    searchable_by=["Glaceon VSTAR", "VSTAR"],
    subtypes=["VSTAR"],
    collector_number=197,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloVSTAR,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonV.Name",
    family_id=471,
    abilities=[
        Attack(
            title="Icicle Shot",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Crystal Star",
            game_text="During your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=220,
            effect=pc.protect_next_turn(prevent=True, effects_too=True),
            vstar=True,
        ),
    ],
)
