from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class LazyHowlPassive(Passive):
    """Rides the Defending Pokemon through the opponent's next turn: an
    Energy card attached to it from their hand ends their turn -- the
    manual attach, or an effect's (Welder: its draw 3 first, then the turn
    ends). Leaving the Active Spot ends it; Pokemon Ranger removes it."""

    def ends_turn_on_hand_attach(self, receiver, attaching_player_id, carrier):
        holder = carrier_pokemon(carrier)
        return (holder is not None and receiver is holder
                and attaching_player_id == holder.owning_player_id)


async def lazy_howl(ctx):
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    ctx.add_passive_through_opponents_turn(defender, LazyHowlPassive())

card = PokemonCardDef(
    guid="87b7bd6f-532e-585b-9c02-7c06c408b215",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name",
    display_name="Slakoth",
    searchable_by=["Slakoth", "Basic", "Slakoth"],
    subtypes=["Basic"],
    collector_number=167,
    set_code="SM11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=287,
    abilities=[
        Attack(
            title="Lazy Howl",
            game_text="During your opponent's next turn, if they attach an Energy card from their hand to the Defending Pok\u00e9mon, their turn ends.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=lazy_howl,
        ),
        Attack(
            title="Hang Down",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
