"""Hypno (SV065 17 -- JP SV6a 017; English SFA/17). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class DaydreamPassive(Passive):
    """Their manual Energy attach from hand to this Pokemon ends their turn."""

    def ends_turn_on_hand_attach(self, receiver, attaching_player_id, carrier):
        holder = carrier_pokemon(carrier)
        return receiver is holder and attaching_player_id == holder.owning_player_id


async def daydream(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and not ctx.effects_blocked(d):
        ctx.add_passive_through_opponents_turn(d, DaydreamPassive())


card = PokemonCardDef(
    guid="c75bccc9-9877-5b2e-98ff-65538289fdb6",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Attack(
            title="Daydream",
            game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pokémon, their turn ends.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=daydream,
        ),
    ],
)
