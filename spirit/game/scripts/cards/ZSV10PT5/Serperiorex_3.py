from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class RegalCheerPassive(Passive):
    """+20 from your Pokemon's attacks to the opposing Active, before W/R.
    No "doesn't stack" clause: each Serperior ex adds its own."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is not None and attacker.owning_player_id == carrier.owning_player_id:
            calc.amount += 20


async def command_the_grass(ctx):
    """150. You may search your deck for up to 3 cards into your hand."""
    await ctx.deal_damage()
    if not ctx.deck() or not await ctx.ask_yes_no("Search your deck for up to 3 cards?"):
        return
    picks = await ctx.search_deck(None, count=3, minimum=0, prompt="Choose up to 3 cards to put into your hand.")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()

card = PokemonCardDef(
    guid="9661f520-a025-59e6-9e98-73aa93bc9312",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperiorex.Name",
    display_name="Serperior ex",
    searchable_by=["Serperior ex", "Stage 2", "ex", "Serperiorex"],
    subtypes=["Stage 2", "ex"],
    collector_number=3,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Regal Cheer",
            game_text="Attacks used by your Pok\u00e9mon do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=RegalCheerPassive(),
        ),
        Attack(
            title="Command the Grass",
            game_text="You may search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=command_the_grass,
        ),
    ],
)
