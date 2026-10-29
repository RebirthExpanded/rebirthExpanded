"""Lucario VSTAR (Promo_SWSH 214 -- JP SLL 005; English SP/214, SP/291). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import is_pokemon_v, subtypes_for


def _defender_v(ctx) -> bool:
    d = ctx.opponent_active()
    return d is not None and is_pokemon_v(d.archetype_id)


card = PokemonCardDef(
    guid="402883b0-2fbe-5b21-8738-344935275d65",
    key="Promo_SWSH",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioVSTAR.Name",
    display_name="Lucario VSTAR",
    searchable_by=["Lucario VSTAR", "VSTAR"],
    subtypes=["VSTAR"],
    collector_number=214,
    set_code="Promo_SWSH",
    regulation_mark="F",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LucarioV.Name",
    family_id=448,
    abilities=[
        Attack(
            title="Fighting Knuckle",
            game_text="If your opponent's Active Pokémon is a Pokémon V, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            damage_operator="+",
            effect=ac.bonus_if(_defender_v, 120),
        ),
        Attack(
            title="Aura Star",
            game_text="This attack does 70 damage for each Energy attached to all of your opponent's Pokémon. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("opponent"), 70),
            vstar=True,
        ),
    ],
)
