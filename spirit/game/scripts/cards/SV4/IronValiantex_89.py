"""Iron Valiant ex (SV - Paradox Rift 89/182 -- JP SV4M 038/066, the art here).

Basic Psychic Pokemon ex (Future). HP 220, weakness Metal x2, no
resistance, retreat 2.

  Ability  Tachyon Bits  Once during your turn, when this Pokemon moves
                         from your Bench to the Active Spot, you may put
                         2 damage counters on 1 of your opponent's Pokemon.
  Laser Blade [PPC] 200  During your next turn, this Pokemon can't attack.

Tachyon Bits rides ON_MOVE_TO_ACTIVE, which fires once per entity per
turn and only during its owner's turn (a Boss's Orders gust on the
opponent's turn, or being promoted after a KO on their turn, is not
"during your turn"). Retreat, Switch, Rapid Vernier-style swaps and a
promotion on your own turn all count. The counters are placed, not
attack damage: no Weakness, no attack-effect shields.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def tachyon_bits(ctx):
    """You may put 2 damage counters on 1 of your opponent's Pokemon."""
    targets = ctx.opponent_pokemon_in_play()
    if not targets:
        return
    if not await ctx.ask_yes_no(
            "Put 2 damage counters on 1 of your opponent's Pokémon?"):
        return
    target = await ctx.choose_pokemon(
        targets, "Choose 1 of your opponent's Pokémon")
    if target is None:
        return
    await ctx.deal_damage(20, target=target, apply_modifiers=False,
                          as_counters=True)


card = PokemonCardDef(
    guid="1b820241-8986-518b-aba2-726bd0b75b15",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiantex.Name",
    display_name="Iron Valiant ex",
    searchable_by=["Iron Valiant ex", "Basic", "ex", "Future", "IronValiantex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=89,
    set_code="SV4",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Ability(
            title="Tachyon Bits",
            game_text="Once during your turn, when this Pokémon moves from your Bench to the Active Spot, you may put 2 damage counters on 1 of your opponent's Pokémon.",
            trigger=Triggers.ON_MOVE_TO_ACTIVE,
            effect=tachyon_bits,
        ),
        Attack(
            title="Laser Blade",
            game_text="During your next turn, this Pokémon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            locks_next_turn=True,
        ),
    ],
)
