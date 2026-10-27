"""Grapploct (SV08 113 -- JP SV7a 033; English SSP/113). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10



class RagingTentaclesPassive(Passive):
    """Damaged: Raging Tentacles costs a single Fighting Energy."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and sum(cost.values()) == 3 and _counters(board, pokemon) > 0:
            return {"Fighting": 1}
        return cost


async def raging_tentacles(ctx):
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="252b6615-4a9b-54be-9ada-74277a448cd1",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name",
    display_name="Grapploct",
    searchable_by=["Grapploct", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=113,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name",
    family_id=852,
    abilities=[
        Attack(
            title="Chop",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
        ),
        Attack(
            title="Raging Tentacles",
            game_text="If this Pokémon has any damage counters on it, this attack can be used for Fighting.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=raging_tentacles,
        ),
    ],
)
card.passive = RagingTentaclesPassive()
