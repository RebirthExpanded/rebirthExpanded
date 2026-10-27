"""Conkeldurr (SV06 105 -- JP SV6 061; English TWM/105). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES



async def tantrum(ctx):
    await ctx.deal_damage()
    if ctx.attacker not in ctx.knockouts:
        await ctx.apply_special_condition(ctx.attacker, SpecialConditions.CONFUSED)


class GutsySwingPassive(Passive):
    """Affected by a Special Condition: Gutsy Swing costs nothing."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and sum(cost.values()) == 4 and (pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or []):
            return {}
        return cost


async def gutsy_swing(ctx):
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="fc765821-6e77-5f3e-9021-d1fd5906e802",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=105,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Attack(
            title="Tantrum",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=80,
            effect=tantrum,
        ),
        Attack(
            title="Gutsy Swing",
            game_text="If this Pokémon is affected by a Special Condition, ignore all Energy in this attack's cost.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=250,
            effect=gutsy_swing,
        ),
    ],
)
card.passive = GutsySwingPassive()
