"""Torterra ex (SV05 12 -- JP SV5K 005; English TEF/12, TEF/185). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import support_common as su
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])



def _grass(p) -> bool:
    return _of_type(p, PokemonTypes.GRASS)


card = PokemonCardDef(
    guid="afafd6e7-6c72-5bbb-8f36-68cb5e260a17",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Torterraex.Name",
    display_name="Torterra ex",
    searchable_by=["Torterra ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=12,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=340,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grotle.Name",
    family_id=387,
    abilities=[
        Attack(
            title="Forest March",
            game_text="This attack does 30 damage for each of your Grass Pokémon in play.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="x",
            effect=ac.damage_per(ac.count_in_play("mine", _grass), 30),
        ),
        Attack(
            title="Jungle Hammer",
            game_text="Heal 50 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=su.heal_attack(50),
        ),
    ],
)
