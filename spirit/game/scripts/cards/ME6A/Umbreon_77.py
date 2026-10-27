"""Umbreon (ME6A 77 -- JP M6a 077; English 30C/91). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _lost_one(ctx) -> bool:
    return ctx.kos_by_attack_last_turn() > 0


card = PokemonCardDef(
    guid="7a60467f-490e-5382-9621-19c29b42530e",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Umbreon.Name",
    display_name="Umbreon",
    searchable_by=["Umbreon", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=77,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Retaliate",
            game_text="If any of your Pokémon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            damage_operator="+",
            effect=ac.bonus_if(_lost_one, 100),
        ),
        Attack(
            title="Darkness Fang",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
