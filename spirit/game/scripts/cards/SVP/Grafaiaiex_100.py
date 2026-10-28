"""Grafaiai ex (SVP 100 -- JP SVP 088; English SVP/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="7ee49fef-568f-59a8-8d06-aeac472d05df",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiaiex.Name",
    display_name="Grafaiai ex",
    searchable_by=["Grafaiai ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=100,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Numbing Saliva",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Toxic Throw",
            game_text="Your opponent's Active Pokémon is now Poisoned. During your next turn, this Pokémon can't use Toxic Throw.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=ac.condition_attack(SpecialConditions.POISONED),
            locks_next_turn=True,
        ),
    ],
)
