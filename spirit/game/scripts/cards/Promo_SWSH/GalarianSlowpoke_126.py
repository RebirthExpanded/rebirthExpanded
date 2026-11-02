"""Galarian Slowpoke (Promo_SWSH 126 -- JP SP 172; English SP/126). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="98dcdb6c-b901-52c2-af98-e03ff103a8aa",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianSlowpoke.Name",
    display_name="Galarian Slowpoke",
    searchable_by=["Galarian Slowpoke", "Basic"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="Promo_SWSH",
    regulation_mark="E",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=79,
    abilities=[
        Attack(
            title="Everyone Laze Around",
            game_text="Heal 10 damage from each of your Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.heal_targets(10, "each_own"),
        ),
        Attack(
            title="Tail Whap",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
