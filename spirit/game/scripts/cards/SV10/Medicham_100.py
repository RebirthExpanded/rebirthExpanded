"""Medicham (SV10 100 -- JP SV10 054; English DRI/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _same_energy(ctx) -> bool:
    return ac.count_energy("self", cards=True)(ctx) == ac.count_energy("defender", cards=True)(ctx)


card = PokemonCardDef(
    guid="5b94c058-dfd9-54de-9707-bbacbee1c5bd",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Medicham.Name",
    display_name="Medicham",
    searchable_by=["Medicham", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=100,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name",
    family_id=307,
    abilities=[
        Attack(
            title="Harmonious Spirit Palm",
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached, this attack does 120 more damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_same_energy, 120),
        ),
    ],
)
