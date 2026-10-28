"""Houndoom (SV3 133 -- JP SV3 072; English OBF/133). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_evolution_pokemon


def _evolved_defender(ctx) -> bool:
    return ctx.defender is not None and is_evolution_pokemon(ctx.defender)


card = PokemonCardDef(
    guid="cc958a34-c69b-57dd-8cfa-5e96037b9385",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=133,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Attack(
            title="Daring Strike",
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=ac.bonus_if(_evolved_defender, 70),
        ),
        Attack(
            title="Shadow Slash",
            game_text="Discard an Energy from this Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=ac.self_energy_discard_attack(count=1),
        ),
    ],
)
