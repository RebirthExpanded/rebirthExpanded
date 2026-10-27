"""Zarude (ME5 56 -- JP M5 054; English MEP/88, PBL/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _shadowy_on_bench(ctx) -> bool:
    return any(getattr(def_for(e.archetype_id), "display_name", None) == "Shadowy Darkness Energy"
               for p in ctx.my_bench() for e in ctx.attached_energies(p))


card = PokemonCardDef(
    guid="b78f213c-c3df-513a-b965-6e2f536a2f8e",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=893,
    abilities=[
        Attack(
            title="Overhead Throw",
            game_text="This attack also does 30 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=ac.snipe_attack(30, pool="bench", side="mine", also_base=True),
        ),
        Attack(
            title="Shadowy Whip",
            game_text="If your Benched Pokémon have any Shadowy Darkness Energy attached, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(_shadowy_on_bench, 70),
        ),
    ],
)
