"""Vaporeon (Promo_SWSH 72 -- JP SP 071; English SP/72). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import PokemonTypes as _PT
from spirit.game.card_effects.sm4 import submerge_passive


card = PokemonCardDef(
    guid="bd3b85e8-73bd-5a52-bcce-d7de31e8b84b",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="Promo_SWSH",
    regulation_mark="D",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Watery Shroud",
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=submerge_passive,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 20 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=ac.damage_per(ac.count_energy("self", _PT.WATER), 20, base=60),
        ),
    ],
)
