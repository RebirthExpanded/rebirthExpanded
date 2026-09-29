from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, carrier_pokemon


class PlentifulPollenPassive(Passive):
    """Rides the Defending Pokemon: if it is Knocked Out during the attacker's
    next turn, the attacker takes 2 more Prize cards. Leaving the Active
    Spot ends it like any effect on the Defending Pokemon."""

    def __init__(self, owner_id, turn):
        self.owner_id = owner_id
        self.turn = turn

    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return 0
        turn_state = ctx.session.turn_state
        if turn_state.turn_number != self.turn or turn_state.active_player_id != self.owner_id:
            return 0
        return 2


async def plentiful_pollen(ctx):
    """30, then mark the Defending Pokemon for 2 extra Prizes next turn."""
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    turn = ctx.session.turn_state.turn_number + 2
    ctx.add_temporary_passive(defender, PlentifulPollenPassive(ctx.player_id, turn), turn)

card = PokemonCardDef(
    guid="aebc6b9c-22c9-51dd-9058-273c3f7ec9f8",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name",
    display_name="Ribombee",
    searchable_by=["Ribombee", "Stage 1", "Ribombee"],
    subtypes=["Stage 1"],
    collector_number=76,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    family_id=742,
    abilities=[
        Attack(
            title="Plentiful Pollen",
            game_text="During your next turn, if the Defending Pok\u00e9mon is Knocked Out, take 2 more Prize cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=plentiful_pollen,
        ),
    ],
)
