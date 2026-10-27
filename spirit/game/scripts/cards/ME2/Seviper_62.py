"""Seviper (ME2 62 -- JP M2 052; English PFL/62). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for


def _mega_ex(pokemon) -> bool:
    subs = subtypes_for(pokemon.archetype_id) or []
    return "SV_Mega" in subs and "ex" in subs
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


def _of_type(pokemon, t) -> bool:
    return t.value in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])



class ExcitedPowerPassive(Passive):
    """A Darkness Mega Evolution Pokemon ex in play: this Pokemon's attacks do
    120 more to the opponent's Active (before W/R) (an Ability)."""

    def modify_damage_dealt(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.attacker is me and calc.to_active and calc.is_opposing):
            return
        if any(_mega_ex(p) and _of_type(p, PokemonTypes.DARKNESS)
               for p in calc.board.pokemon_in_play(me.owning_player_id)):
            calc.amount += 120


card = PokemonCardDef(
    guid="d8653e0f-fcf7-5061-a715-79cb55e2b911",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Seviper.Name",
    display_name="Seviper",
    searchable_by=["Seviper", "Basic"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=336,
    abilities=[
        Ability(
            title="Excited Power",
            game_text="If you have any Darkness Mega Evolution Pokémon ex in play, attacks used by this Pokémon do 120 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=ExcitedPowerPassive(),
        ),
        Attack(
            title="Pitch-Black Fangs",
            game_text="",
            cost={PokemonTypes.DARKNESS: 3},
            damage=120,
        ),
    ],
)
