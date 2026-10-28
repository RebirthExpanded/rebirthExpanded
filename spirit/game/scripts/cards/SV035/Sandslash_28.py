"""Sandslash (SV035 28 -- JP SV2a 028; English MEW/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="a570295b-4ea5-5bf4-89af-83ec0668bd05",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandslash.Name",
    display_name="Sandslash",
    searchable_by=["Sandslash", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name",
    family_id=27,
    abilities=[
        Attack(
            title="Rumble",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Spike Rend",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 100),
        ),
    ],
)
