"""Chien-Pao (ME3 54 -- JP M3 053; English POR/54). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.data_utils import def_for, subtypes_for



def _defender_is_ex(ctx) -> bool:
    d = ctx.defender
    return d is not None and "ex" in (subtypes_for(d.archetype_id) or [])


card = PokemonCardDef(
    guid="5d4ba35a-fb9c-5dce-aed9-69b8fb37dec7",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name",
    display_name="Chien-Pao",
    searchable_by=["Chien-Pao", "Basic"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1002,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=su.switch_self_attack(optional=True),
        ),
        Attack(
            title="Rising Blade",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=ac.bonus_if(_defender_is_ex, 80),
        ),
    ],
)
