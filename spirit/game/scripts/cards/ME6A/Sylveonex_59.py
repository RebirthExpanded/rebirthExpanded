"""Sylveon ex (ME6A 59 -- JP M6a 059; English 30C/153, 30C/71, MEP/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _harmony(ctx) -> int:
    kinds = set()
    for p in ctx.my_pokemon_in_play():
        for e in ctx.attached_energies(p):
            if is_basic_energy_card(e):
                kinds.update(e.get_attribute(AttrID.POKEMON_TYPES) or [])
    return len(kinds)


card = PokemonCardDef(
    guid="20a20a5f-8fb0-5678-8131-f71087da07d4",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveonex.Name",
    display_name="Sylveon ex",
    searchable_by=["Sylveon ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=59,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Colorful Harmony",
            game_text="This attack does 50 damage for each type of Basic Energy attached to all of your Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=ac.damage_per(_harmony, 50),
        ),
    ],
)
