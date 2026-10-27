"""Crawdaunt (ME1 85 -- JP M1L 037; English MEG/85). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES

from spirit.game.session.passives import effective_max_hp


def _counters(board, pokemon) -> int:
    return max(0, effective_max_hp(board, pokemon) - pokemon.get_attribute(AttrID.HP, 0)) // 10



class CuttingRipostePassive(Passive):
    """Damaged: Cutting Riposte costs a single Darkness Energy."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier or sum(cost.values()) != 3:
            return cost
        if _counters(board, pokemon) > 0:
            return {"Darkness": 1}
        return cost


async def cutting_riposte(ctx):
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="d70cbae1-f903-59be-b7ef-b73f0cc021e6",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crawdaunt.Name",
    display_name="Crawdaunt",
    searchable_by=["Crawdaunt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=85,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Corphish.Name",
    family_id=341,
    abilities=[
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Cutting Riposte",
            game_text="If this Pokémon has any damage counters on it, this attack can be used for Darkness.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=cutting_riposte,
        ),
    ],
)
card.passive = CuttingRipostePassive()
