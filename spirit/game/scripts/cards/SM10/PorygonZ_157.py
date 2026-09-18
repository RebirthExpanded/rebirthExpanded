"""Porygon-Z (SM - Unbroken Bonds 157/214 -- JP SM10 075/095, the art here).

Stage 2 Colorless Pokemon (evolves from Porygon2). HP 130, weakness
Fighting x2, no resistance, retreat 2.

  Crazy Code  (Ability)   As often as you like during your turn (before
                          your attack), you may attach a Special Energy
                          card from your hand to 1 of your Pokemon.
  Tantrum     [CCC] 120   This Pokemon is now Confused.

Crazy Code is Inferno Fandango's shape: one use keeps attaching until the
player declines. A Special Energy that names who may carry it (Rapid
Strike Energy, Team Rocket's Energy) offers only those Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, def_for
from spirit.game.session.effects import is_special_energy


def _legal_holders(ctx, energy):
    attach_to = getattr(def_for(energy.archetype_id), "attach_to", None)
    return [p for p in ctx.my_pokemon_in_play() if attach_to is None or attach_to(p)]


def _crazy_code_condition(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(is_special_energy(c) for c in (hand.children if hand else []))


async def crazy_code(ctx):
    while True:
        pool = [c for c in ctx.hand() if is_special_energy(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=0, prompt="Choose a Special Energy card to attach (or Done)")
        if not picks:
            return
        holders = _legal_holders(ctx, picks[0])
        if not holders:
            return
        target = await ctx.choose_pokemon(holders, "Choose a Pokémon to attach the Energy to")
        if target is None:
            return
        await ctx.attach_energy(picks[0], target)


card = PokemonCardDef(
    guid="95fde97b-b595-5bac-942f-74f30189263f",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=157,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Crazy Code",
            game_text="As often as you like during your turn (before your attack), you may attach a Special Energy card from your hand to 1 of your Pokémon.",
            activation=Activations.UNLIMITED,
            condition=_crazy_code_condition,
            effect=crazy_code,
        ),
        Attack(
            title="Tantrum",
            game_text="This Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=condition_attack(self_conditions=(SpecialConditions.CONFUSED,)),
        ),
    ],
)
