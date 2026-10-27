"""Shedinja (ME1 61 -- JP M1S 043; English MEG/144, MEG/61). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


def _own(ctx) -> int:
    return _counters(ctx.board, ctx.attacker)


def _defender_counters(ctx) -> int:
    return _counters(ctx.board, ctx.defender) if ctx.defender is not None else 0



class FragileHuskPassive(Passive):
    """KO'd by damage from an opposing Pokemon ex's attack: no Prize cards."""

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return count
        attacker = getattr(ctx, "ko_attacker", None)
        if (getattr(ctx, "ko_from_attack", False) and attacker is not None
                and attacker.owning_player_id != pokemon.owning_player_id
                and "ex" in (subtypes_for(attacker.archetype_id) or [])):
            return 0
        return count


card = PokemonCardDef(
    guid="36a313e5-0ce9-5c8f-8835-5a64490621be",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Fragile Husk",
            game_text="If this Pokémon is Knocked Out by damage from an attack from your opponent's Pokémon ex, your opponent can't take any Prize cards for it.",
            passive=FragileHuskPassive(),
        ),
        Attack(
            title="Damage Beat",
            game_text="This attack does 20 damage for each damage counter on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator="x",
            effect=ac.damage_per(_defender_counters, 20),
        ),
    ],
)
