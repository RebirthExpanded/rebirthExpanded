"""Miraidon ex (SV05 122 -- JP SVHM 011; English TEF/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="4bbdf131-3c6c-5b7c-b070-ef79b019d738",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidonex.Name",
    display_name="Miraidon ex",
    searchable_by=["Miraidon ex", "Basic", "ex", "Future"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=122,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=1008,
    abilities=[
        Attack(
            title="Repulsion Bolt",
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            damage=60,
            damage_operator="+",
            effect=ac.bonus_if(ac.has_damage("defender"), 100),
        ),
        Attack(
            title="Cyber Drive",
            game_text="During your next turn, this Pokémon can't use Cyber Drive.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=220,
            locks_next_turn=True,
        ),
    ],
)
