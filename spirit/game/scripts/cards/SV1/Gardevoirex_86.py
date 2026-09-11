"""Gardevoir ex (SV - Scarlet & Violet 86/198 -- JP SV1S 028/078).

Stage 2 Psychic Pokemon ex, evolves from Kirlia. HP 310, weakness
Darkness x2, resistance Fighting -30, retreat 2.

  Ability  Psychic Embrace  As often as you like during your turn, you may
                            attach a Basic [P] Energy card from your
                            discard pile to 1 of your [P] Pokemon. If you
                            attached Energy to a Pokemon in this way, put 2
                            damage counters on that Pokemon. You can't use
                            this Ability on a Pokemon that would be
                            Knocked Out.
  Miracle Force  [PPC] 190  This Pokemon recovers from all Special
                            Conditions.

Each use attaches one Energy; targets with 20 HP or less are not offered.
"""

from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import (Ability, Activations, Attack,
                                    PokemonCardDef)
from spirit.game.session.effects import is_basic_energy, is_pokemon_of_type


def _basic_psychic_energy(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)


def _targets(board, player_id):
    return [p for p in board.pokemon_in_play(player_id)
            if is_pokemon_of_type(p, PokemonTypes.PSYCHIC)
            and p.get_attribute(AttrID.HP, 0) > 20]


def _psychic_embrace_condition(board, player_id, pokemon=None) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return any(_basic_psychic_energy(c) for c in (discard.children if discard else [])) \
        and bool(_targets(board, player_id))


async def psychic_embrace(ctx):
    energies = [c for c in ctx.discard_pile() if _basic_psychic_energy(c)]
    targets = _targets(ctx.board, ctx.player_id)
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(energies, 1, minimum=1,
                                   prompt="Choose a Basic [P] Energy card to attach")
    if not picks:
        return
    target = await ctx.choose_pokemon(targets, "Choose a [P] Pokémon to attach it to")
    if target is None:
        return
    await ctx.attach_energy(picks[0], target)
    await ctx.deal_damage(20, target=target, as_counters=True)


async def miracle_force(ctx):
    await ctx.deal_damage()
    await ctx.cure_all_conditions(ctx.attacker)


card = PokemonCardDef(
    guid="761e5e28-e06f-5cb1-b531-d1ae1df92967",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gardevoirex.Name",
    display_name="Gardevoir ex",
    searchable_by=["Gardevoir ex", "Stage 2", "ex", "Gardevoirex"],
    subtypes=["Stage 2", "ex"],
    collector_number=86,
    set_code="SV1",
    rarity=Rarities.RareUltra,
    hp=310,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kirlia.Name",
    family_id=280,
    regulation_mark="G",
    abilities=[
        Ability(title="Psychic Embrace",
                game_text="As often as you like during your turn, you may attach a Basic [P] Energy card from your discard pile to 1 of your [P] Pokémon. If you attached Energy to a Pokémon in this way, put 2 damage counters on that Pokémon. You can't use this Ability on a Pokémon that would be Knocked Out.",
                activation=Activations.UNLIMITED, condition=_psychic_embrace_condition,
                effect=psychic_embrace),
        Attack(title="Miracle Force", game_text="This Pokémon recovers from all Special Conditions.",
               cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1}, damage=190,
               effect=miracle_force),
    ],
)
