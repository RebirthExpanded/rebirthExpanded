"""Tornadus (ME6 59 -- JP M6 059; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for


_FORCES = {"Tornadus", "Thundurus", "Landorus", "Enamorus"}


class IncarnateUnityPassive(Passive):
    """With Tornadus, Thundurus, Landorus and Enamorus all in play, this
    Pokemon's attacks need no Colorless Energy (an Ability)."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        names = {getattr(def_for(p.archetype_id), "display_name", None) for p in board.pokemon_in_play(carrier.owning_player_id)}
        if _FORCES <= names:
            cost = {k: v for k, v in cost.items() if k != "Colorless"}
        return cost


async def screw_dive(ctx):
    await ctx.deal_damage()
    if len(ctx.hand()) < 6 and await ctx.ask_yes_no("Draw cards until you have 6 cards in your hand?"):
        await ctx.draw_until(6)


card = PokemonCardDef(
    guid="becd7266-b799-5e7d-8bb7-e94742368531",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tornadus.Name",
    display_name="Tornadus",
    searchable_by=["Tornadus", "Basic"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=641,
    abilities=[
        Ability(
            title="Incarnate Unity",
            game_text="If you have Tornadus, Thundurus, Landorus, and Enamorus in play, this Pokémon's attacks cost no Colorless Energy.",
            passive=IncarnateUnityPassive(),
        ),
        Attack(
            title="Screw Dive",
            game_text="You may draw cards until you have 6 cards in your hand.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=screw_dive,
        ),
    ],
)
