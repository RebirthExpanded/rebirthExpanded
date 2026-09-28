from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import bonus_if


def _tr_energy(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Team Rocket's Energy"


def _has_tr_energy(ctx) -> bool:
    return any(_tr_energy(e) for e in ctx.attached_energies(ctx.attacker))


async def jamming_wing(ctx):
    """30; you may move an Energy from their Active to 1 of their Benched Pokemon."""
    await ctx.deal_damage()
    defender = ctx.defender
    bench = ctx.opponent_bench()
    if defender is None or not bench or ctx.effects_blocked(defender):
        return
    energies = ctx.attached_energies(defender)
    if not energies or not await ctx.ask_yes_no(
            "Move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon?"):
        return
    picks = await ctx.choose_cards(energies, 1, prompt="Choose an Energy to move")
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.move_energy(picks[0], target)

card = PokemonCardDef(
    guid="50f893c0-988d-5946-ae46-1c40f50f6fe5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsZapdos.Name",
    display_name="Team Rocket's Zapdos",
    searchable_by=["Team Rocket's Zapdos", "Basic", "TeamRocketsZapdos"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=145,
    abilities=[
        Attack(
            title="Jamming Wing",
            game_text="You may move an Energy from your opponent's Active Pok\u00e9mon to 1 of their Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=jamming_wing,
        ),
        Attack(
            title="Wicked Thunder",
            game_text="If this Pok\u00e9mon has any Team Rocket's Energy attached, this attack does 60 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bonus_if(_has_tr_energy, 60),
        ),
    ],
)
