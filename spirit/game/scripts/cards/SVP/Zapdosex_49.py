"""Zapdos ex (SVP 49 -- JP SV2a 145; English MEW/145, MEW/192, MEW/202, SVP/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class _TypeFloat(Passive):
    """Energy of the type attached: no Retreat Cost."""

    def __init__(self, ptype):
        self.ptype = ptype

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and any(is_energy_of_type(e, self.ptype) for e in pokemon.children):
            return 0
        return cost
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10


async def multishot_lightning(ctx):
    await ctx.deal_damage()
    pool = [p for p in ctx.opponent_bench() if _counters(ctx.board, p) > 0]
    if pool:
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's damaged Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(90, target=target)


card = PokemonCardDef(
    guid="719cdbd2-58fc-5585-9d6a-6a6232a8c2b3",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zapdosex.Name",
    display_name="Zapdos ex",
    searchable_by=["Zapdos ex", "Basic", "ex"],
    subtypes=["Basic", "ex"],
    collector_number=49,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=145,
    abilities=[
        Ability(
            title="Voltaic Float",
            game_text="If this Pokémon has any Lightning Energy attached, it has no Retreat Cost.",
            passive=_TypeFloat(PokemonTypes.LIGHTNING),
        ),
        Attack(
            title="Multishot Lightning",
            game_text="This attack also does 90 damage to 1 of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=120,
            effect=multishot_lightning,
        ),
    ],
)
