from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class SnipersEyePassive(Passive):
    """With exactly 4 cards in the opponent's hand, this Pokemon's attacks
    ignore every [C] in their costs."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon or "Colorless" not in cost:
            return cost
        opponent = next((pid for pid in board.player_ids if pid != pokemon.owning_player_id), None)
        hand = board.find_player_area(opponent, "hand") if opponent else None
        if hand is not None and len(hand.children) == 4:
            del cost["Colorless"]
        return cost


async def crushing_arrow(ctx):
    """240, then discard an Energy from the opponent's Active Pokemon."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if energies:
        picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to discard")
        if picks:
            await ctx.discard_cards(picks)

card = PokemonCardDef(
    guid="bbdbcd04-7a2c-5544-953b-03f682cdbdbf",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueyeex.Name",
    display_name="Decidueye ex",
    searchable_by=["Decidueye ex", "Stage 2", "ex", "Decidueyeex"],
    subtypes=["Stage 2", "ex"],
    collector_number=12,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Ability(
            title="Sniper's Eye",
            game_text="If your opponent has exactly 4 cards in their hand, ignore all [C] Energy in the costs of attacks used by this Pok\u00e9mon.",
            passive=SnipersEyePassive(),
        ),
        Attack(
            title="Crushing Arrow",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=240,
            effect=crushing_arrow,
        ),
    ],
)
