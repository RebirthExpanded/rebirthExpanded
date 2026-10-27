"""Miraidon (SV08 69 -- JP SV8 044; English SSP/69). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.data_utils import def_for, subtypes_for


def _has_sub(card, sub) -> bool:
    return card is not None and sub in (subtypes_for(card.archetype_id) or [])



class _CodeProtect(Passive):
    """Rides this Pokemon: while it stays Active, your Future Pokemon take no
    damage from attacks by Pokemon ex."""

    def prevents_damage(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if not (calc.is_attack and calc.is_opposing and me is not None and pc.is_in_active_spot(me)):
            return False
        return (calc.target.owning_player_id == me.owning_player_id and _has_sub(calc.target, "Future")
                and calc.attacker is not None and _has_sub(calc.attacker, "ex"))


async def code_protect(ctx):
    await ctx.deal_damage()
    ctx.add_passive_through_opponents_turn(ctx.attacker, _CodeProtect())


card = PokemonCardDef(
    guid="afdab173-9f99-5d64-b5b0-29607708c79b",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miraidon.Name",
    display_name="Miraidon",
    searchable_by=["Miraidon", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=69,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=1008,
    abilities=[
        Attack(
            title="C.O.D.E.: Protect",
            game_text="During your opponent's next turn, prevent all damage done to each of your Future Pokémon by attacks from Pokémon ex. If this Pokémon is no longer your Active Pokémon, this effect ends.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=code_protect,
        ),
        Attack(
            title="Thunder Claws",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
