"""Iron Jugulis (SV4 158 -- JP SV4M 058; English PAR/158, PAR/216). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10
from spirit.game.data_utils import def_for, subtypes_for



async def homing_headbutt(ctx):
    pool = [p for p in ctx.opponent_pokemon_in_play() if _counters(ctx.board, p) > 0]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=min(3, len(pool)), prompt="Choose up to 3 damaged Pokémon")
    for p in picks:
        await ctx.deal_damage(50, target=p)


class BaryonBeamPassive(Passive):
    """Future Booster Energy Capsule attached: Baryon Beam costs [C][C][C]."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and sum(cost.values()) == 5 and any(
                getattr(def_for(c.archetype_id), "display_name", "") == "Future Booster Energy Capsule" for c in pokemon.children):
            return {"Colorless": 3}
        return cost


async def baryon_beam(ctx):
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="27438516-4e8f-58a4-acc0-3690bb52d6bc",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronJugulis.Name",
    display_name="Iron Jugulis",
    searchable_by=["Iron Jugulis", "Basic", "Future"],
    subtypes=["Basic", "Future"],
    collector_number=158,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=993,
    abilities=[
        Attack(
            title="Homing Headbutt",
            game_text="This attack does 50 damage to 3 of your opponent's Pokémon that have any damage counters on them. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=homing_headbutt,
        ),
        Attack(
            title="Baryon Beam",
            game_text="If this Pokémon has a Future Booster Energy Capsule attached, this attack can be used for ColorlessColorlessColorless.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=150,
            effect=baryon_beam,
        ),
    ],
)
card.passive = BaryonBeamPassive()
