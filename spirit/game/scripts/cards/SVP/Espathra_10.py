"""Espathra (SVP 10 -- JP SVP 006; English SVP/10). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="4f6f3954-3142-5579-8c4c-02c04746442e",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name",
    display_name="Espathra",
    searchable_by=["Espathra", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name",
    family_id=955,
    abilities=[
        Attack(
            title="Aurora Gain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=su.heal_attack(30),
        ),
        Attack(
            title="Super Psy Bolt",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
