"""Hoopa ex (SV4 98 -- JP SV3a 029; English PAR/226, PAR/98). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ff93c0c9-23cb-54fc-b0d8-f629488d3529",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoopaex.Name",
    display_name="Hoopa ex",
    searchable_by=["Hoopa ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=98,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=720,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Energy Crush",
            game_text="This attack does 50 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=50,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("opponent"), 50),
        ),
        Attack(
            title="Bandit's Fist",
            game_text="During your next turn, this Pokémon can't use Bandit's Fist.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=200,
            locks_next_turn=True,
        ),
    ],
)
