"""Aggron (SV06 122 -- JP SV6 075; English TWM/122). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _damaged_mine(ctx) -> int:
    return sum(1 for p in ctx.my_pokemon_in_play() if _counters(ctx.board, p) > 0)


card = PokemonCardDef(
    guid="34e438d2-9d76-5f00-aeec-dba24faa084e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=122,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Angry Slam",
            game_text="This attack does 50 damage for each of your Pokémon that has any damage counters on it.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            damage_operator="x",
            effect=ac.damage_per(_damaged_mine, 50),
        ),
        Attack(
            title="Guard Claw",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=pc.protect_next_turn(reduce=50),
        ),
    ],
)
