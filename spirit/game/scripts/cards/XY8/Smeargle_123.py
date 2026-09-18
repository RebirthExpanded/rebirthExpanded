"""Smeargle (XY - BREAKthrough 123/162 -- JP XY8-Bb 053/059, the art here).

Basic Colorless Pokemon. HP 70, weakness Fighting x2, no resistance,
retreat 1.

  Second Coat  (Ability)  Once during your turn (before your attack), you
                          may switch a basic Energy card attached to your
                          Active Pokemon with a different type of basic
                          Energy card from your discard pile.
  Beat         [CC] 30

The switch is a swap: the chosen attached Energy goes to the discard pile
and the chosen discard-pile Energy takes its place on the Active. "A
different type" reads the basic Energy's printed type.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from spirit.game.session.effects import is_basic_energy


def _energy_type(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return types[0] if types else None


def _second_coat_condition(board, player_id, pokemon=None) -> bool:
    """A basic Energy on the Active and one of another type in the discard."""
    active = board.active_pokemon(player_id)
    if active is None:
        return False
    attached = {_energy_type(e) for e in board.attached_energies(active) if is_basic_energy(e)}
    discard = board.find_player_area(player_id, "discard")
    in_discard = {_energy_type(c) for c in (discard.children if discard else []) if is_basic_energy(c)}
    return any(a != d for a in attached for d in in_discard)


async def second_coat(ctx):
    active = ctx.my_active()
    if active is None:
        return
    attached = [e for e in ctx.attached_energies(active) if is_basic_energy(e)]
    pool = [c for c in ctx.discard_pile() if is_basic_energy(c)]
    attached = [e for e in attached if any(_energy_type(c) != _energy_type(e) for c in pool)]
    if not attached:
        return
    picks = await ctx.choose_cards(
        attached, 1, minimum=0,
        prompt="Choose a basic Energy attached to your Active Pokémon to switch.")
    if not picks:
        return
    out = picks[0]
    candidates = [c for c in pool if _energy_type(c) != _energy_type(out)]
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="Choose a basic Energy of a different type from your discard pile.")
    if not picks:
        return
    await ctx.discard_cards([out])
    await ctx.attach_energy(picks[0], active)


card = PokemonCardDef(
    guid="f85a4fef-0077-5712-8aed-a6f7c047b8e2",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Smeargle.Name",
    display_name="Smeargle",
    searchable_by=["Smeargle", "Basic"],
    subtypes=["Basic"],
    collector_number=123,
    set_code="XY8",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=235,
    abilities=[
        Ability(
            title="Second Coat",
            game_text="Once during your turn (before your attack), you may switch a basic Energy card attached to your Active Pokémon with a different type of basic Energy card from your discard pile.",
            activation=Activations.ONCE_PER_TURN,
            condition=_second_coat_condition,
            effect=second_coat,
        ),
        Attack(
            title="Beat",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
