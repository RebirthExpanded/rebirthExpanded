"""Raichu (ME2PT5 56 -- JP MC 226; English ASC/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="057a54a0-e490-5371-baac-477e08a890a2",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raichu.Name",
    display_name="Raichu",
    searchable_by=["Raichu", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=56,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    family_id=172,
    abilities=[
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 50 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="+",
            effect=ac.flip_bonus(50),
        ),
        Attack(
            title="Strong Volt",
            game_text="Discard a Lightning Energy from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=ac.self_energy_discard_attack(count=1, energy_type=PokemonTypes.LIGHTNING),
        ),
    ],
)
