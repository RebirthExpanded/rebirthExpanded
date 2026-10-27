"""Armarouge (ME5 12 -- JP M5 011; English PBL/12, PBL/86). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card

from spirit.game.models.board import EnergyEntity


def _fire_benched(ctx) -> int:
    return sum(1 for p in ctx.my_bench()
               if any(is_energy_of_type(e, PokemonTypes.FIRE) for e in ctx.attached_energies(p)))


card = PokemonCardDef(
    guid="ecb1e9a1-abae-5732-b94a-be35f5aa5f14",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarouge.Name",
    display_name="Armarouge",
    searchable_by=["Armarouge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Flame Legion",
            game_text="This attack does 40 more damage for each of your Benched Pokémon that has any Fire Energy attached.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=ac.damage_per(_fire_benched, 40, base=40),
        ),
    ],
)
