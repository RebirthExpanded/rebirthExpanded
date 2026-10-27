"""Dustox (ME2PT5 15 -- JP M2a 008; English ASC/15, ASC/220). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


def _opp_active_has_energy(board, player_id, pokemon) -> bool:
    other = next((pid for pid in board.player_ids if pid != player_id), None)
    active = board.active_pokemon(other) if other else None
    from spirit.game.models.board import EnergyEntity
    return active is not None and any(isinstance(c, EnergyEntity) for c in active.children)


async def boisterous_wind(ctx):
    results = await ctx.flip_coins(1, "Boisterous Wind")
    target = ctx.opponent_active()
    if not (results and results[0]) or target is None or not ctx.attached_energies(target):
        return
    picks = await ctx.choose_cards(list(ctx.attached_energies(target)), 1, minimum=1,
                                   prompt="Choose an Energy to put into your opponent's hand")
    if picks:
        await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="4d8c4ec7-b78b-541f-9a99-eedec2ac5c91",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dustox.Name",
    display_name="Dustox",
    searchable_by=["Dustox", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=15,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cascoon.Name",
    family_id=265,
    abilities=[
        Ability(
            title="Boisterous Wind",
            game_text="Once during your turn, you may use this Ability. Flip a coin. If heads, put an Energy attached to your opponent's Active Pokémon into their hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_opp_active_has_energy,
            effect=boisterous_wind,
        ),
        Attack(
            title="Twilight Poison",
            game_text="Your opponent's Active Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.GRASS: 2},
            damage=100,
            effect=ac.condition_attack(SpecialConditions.ASLEEP, SpecialConditions.POISONED),
        ),
    ],
)
