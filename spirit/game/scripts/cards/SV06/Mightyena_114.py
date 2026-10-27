"""Mightyena (SV06 114 -- JP SV6 067; English TWM/114). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _mightyena_benched(ctx) -> bool:
    return any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Mightyena" for p in ctx.my_bench())


card = PokemonCardDef(
    guid="79999ed2-f0ad-57d3-a864-c7b4168f0389",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mightyena.Name",
    display_name="Mightyena",
    searchable_by=["Mightyena", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poochyena.Name",
    family_id=261,
    abilities=[
        Attack(
            title="Hunting Pack",
            game_text="If Mightyena is on your Bench, this attack does 90 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_mightyena_benched, 90),
        ),
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
