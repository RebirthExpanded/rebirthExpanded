"""Durant (SV4 129 -- JP SV4M 042; English PAR/129). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _durant_counters(ctx) -> int:
    return sum(_counters(ctx.board, p) for p in ctx.my_pokemon_in_play() if p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Durant")


card = PokemonCardDef(
    guid="382f6b08-3cdc-5c34-bd5f-3928084ad36a",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic"],
    subtypes=["Basic"],
    collector_number=129,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=632,
    abilities=[
        Attack(
            title="Swarming Rage",
            game_text="This attack does 20 damage for each damage counter on all of your Durant.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_durant_counters, 20),
        ),
        Attack(
            title="Hard Scissors",
            game_text="During your opponent's next turn, this Pokémon takes 20 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=pc.protect_next_turn(reduce=20),
        ),
    ],
)
