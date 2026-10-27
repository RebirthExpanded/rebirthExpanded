"""Iron Hands (SV05 61 -- JP SVHM 006; English TEF/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _ex_or_v(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or [] if pokemon is not None else []
    return "ex" in subs or any(s in subs for s in ("V", "VMAX", "VSTAR", "V-UNION"))


def _defender_ex_or_v(ctx) -> bool:
    return ctx.defender is not None and _ex_or_v(ctx.defender)


card = PokemonCardDef(
    guid="6b354223-141f-5e97-9fee-379b9e19cee9",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronHands.Name",
    display_name="Iron Hands",
    searchable_by=["Iron Hands", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=61,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=992,
    abilities=[
        Attack(
            title="Volt Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Superalloy Hands",
            game_text="If your opponent's Active Pokémon is a Pokémon ex or Pokémon V, this attack does 80 more damage.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_defender_ex_or_v, 80),
        ),
    ],
)
