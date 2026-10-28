"""Veluza (SV2 56 -- JP SV2P 023; English PAF/125, PAL/56). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class SlimScrewPassive(Passive):
    """No cards in your hand: Slim Screw costs [W]."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or sum(cost.values()) != 4:
            return cost
        hand = board.find_player_area(pokemon.owning_player_id, "hand")
        return {"Water": 1} if hand is not None and not hand.children else cost


async def slim_screw(ctx):
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="f480cff6-aae2-50d8-9630-c38e7500b0e1",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Attack(
            title="Ram",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Slim Screw",
            game_text="If you have no cards in your hand, this attack can be used for Water.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=slim_screw,
        ),
    ],
)
card.passive = SlimScrewPassive()
