"""Arcanine (SV10 28 -- JP SV10 014; English DRI/28). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _dark(pokemon) -> bool:
    return PokemonTypes.DARKNESS.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])


card = PokemonCardDef(
    guid="e2e02957-2426-5540-8315-9067156c91f9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name",
    display_name="Arcanine",
    searchable_by=["Arcanine", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name",
    family_id=58,
    abilities=[
        Attack(
            title="Flare",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Punishing Fang",
            game_text="If your opponent's Active Pokémon is a Darkness Pokémon, this attack does 100 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=ac.bonus_if(ac.active_is(_dark), 100),
        ),
    ],
)
