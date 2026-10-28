"""Toedscruel ex (SV045 5 -- JP SVP1 002; English OBF/22, PAF/213, PAF/5). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.models.board import EnergyEntity


def _energized_ally(target, carrier) -> bool:
    return target.owning_player_id == carrier.owning_player_id and any(isinstance(c, EnergyEntity) for c in target.children)


def _grassy_bench(ctx) -> int:
    return sum(1 for p in ctx.my_bench() if any(is_energy_of_type(e, PokemonTypes.GRASS) for e in ctx.attached_energies(p)))


card = PokemonCardDef(
    guid="27dc5397-81c3-57f0-b908-01ee2e361ac7",
    key="SV045",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruelex.Name",
    display_name="Toedscruel ex",
    searchable_by=["Toedscruel ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=5,
    set_code="SV045",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name",
    family_id=948,
    abilities=[
        Ability(
            title="Protective Mycelium",
            game_text="Prevent all effects of attacks used by your opponent's Pokémon done to all of your Pokémon that have Energy attached. (Existing effects are not removed. Damage is not an effect.)",
            passive=pc.attack_effect_shield_passive(protects=_energized_ally),
        ),
        Attack(
            title="Colony Rush",
            game_text="This attack does 40 more damage for each of your Benched Pokémon that has any Grass Energy attached.",
            cost={PokemonTypes.GRASS: 2},
            damage=80,
            damage_operator="+",
            effect=ac.damage_per(_grassy_bench, 40, base=80),
        ),
    ],
)
