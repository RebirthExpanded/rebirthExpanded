"""Magnezone (SV08 60 -- JP SV8 036; English SSP/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="386d80c2-2389-53e7-bfd7-0335412f8cbe",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=60,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    family_id=81,
    abilities=[
        Attack(
            title="Mighty Magnetism",
            game_text="Your opponent's Active Pokémon is now Confused. During your opponent's next turn, that Pokémon can't retreat.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=ac.condition_attack(SpecialConditions.CONFUSED, no_retreat=True),
        ),
        Attack(
            title="Zap Cannon",
            game_text="During your next turn, this Pokémon can't use Zap Cannon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=180,
            locks_next_turn=True,
        ),
    ],
)
