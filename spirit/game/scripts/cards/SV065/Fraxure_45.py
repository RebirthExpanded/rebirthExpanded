"""Fraxure (SV065 45 -- JP SV6a 045; English SFA/45, SFA/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon

from spirit.game.attributes import TrainerType


class UnnervePassive(Passive):
    """The opponent's Item and Supporter cards do nothing to this Pokemon."""

    def blocks_trainer_effects(self, affected_player_id, trainer_card, trainer_type, carrier,
                               affected_entity=None, board=None):
        holder = carrier_pokemon(carrier)
        return (affected_entity is holder and trainer_card is not None
                and trainer_card.owning_player_id != holder.owning_player_id
                and trainer_type in (TrainerType.ITEM.value, TrainerType.SUPPORTER.value))


async def dragon_pulse(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(1))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="49489eb3-ed90-5231-b411-4e9e03c414b3",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fraxure.Name",
    display_name="Fraxure",
    searchable_by=["Fraxure", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Axew.Name",
    family_id=610,
    abilities=[
        Ability(
            title="Unnerve",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pokémon.",
            passive=UnnervePassive(),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.METAL: 1},
            damage=80,
            effect=dragon_pulse,
        ),
    ],
)
