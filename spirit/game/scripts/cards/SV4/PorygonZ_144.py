"""Porygon-Z (SV4 144 -- JP SV4M 050; English PAR/144, PAR/214). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card


def _has_deck(board, player_id, pokemon) -> bool:
    return True


async def buggy_turbo(ctx):
    me = ctx.source
    results = await ctx.flip_coins(1, "Buggy Turbo")
    if results and results[0]:
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if pool:
            picks = await ctx.choose_cards(pool, min(4, len(pool)), minimum=0, prompt="Attach up to 4 Basic Energy cards to this Pokémon")
            for card in picks:
                await ctx.attach_energy(card, me)
    else:
        pool = list(ctx.attached_energies(me))
        if pool:
            picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to discard from this Pokémon")
            await ctx.discard_cards(picks)


card = PokemonCardDef(
    guid="9125f2f0-f9d4-5dd6-89fa-dab1c200ffbe",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=144,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Buggy Turbo",
            game_text="Once during your turn, you may flip a coin. If heads, attach up to 4 Basic Energy cards from your discard pile to this Pokémon. If tails, discard an Energy from this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_deck,
            effect=buggy_turbo,
        ),
        Attack(
            title="Energized Attack",
            game_text="This attack does 40 damage for each Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=ac.damage_per(ac.count_energy("self"), 40),
        ),
    ],
)
