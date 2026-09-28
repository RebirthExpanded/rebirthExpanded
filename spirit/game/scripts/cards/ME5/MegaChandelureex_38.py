from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive, effective_retreat_cost


class BindingFlamePassive(Passive):
    """The opponent's Active Pokemon's Retreat Cost is [C] more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id or not is_in_active_spot(pokemon):
            return cost
        return cost + 1


async def phantom_maze(ctx):
    """130 + 50 for each [C] in the opponent's Active's Retreat Cost."""
    defender = ctx.defender
    cost = effective_retreat_cost(ctx.board, defender) if defender is not None else 0
    await ctx.deal_damage(130 + 50 * cost)

card = PokemonCardDef(
    guid="b5efb95a-bdb3-50e5-bd22-6189563d7a3e",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaChandelureex.Name",
    display_name="Mega Chandelure ex",
    searchable_by=["Mega Chandelure ex", "Stage 2", "ex", "SV_Mega", "MegaChandelureex"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=38,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name",
    family_id=607,
    abilities=[
        Ability(
            title="Binding Flame",
            game_text="Your opponent's Active Pok\u00e9mon's Retreat Cost is [C] more.",
            passive=BindingFlamePassive(),
        ),
        Attack(
            title="Phantom Maze",
            game_text="This attack does 50 more damage for each [C] in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            damage_operator="+",
            effect=phantom_maze,
        ),
    ],
)
