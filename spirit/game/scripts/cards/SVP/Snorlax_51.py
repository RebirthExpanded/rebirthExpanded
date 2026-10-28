"""Snorlax (SVP 51 -- JP SV2a 143; English MEW/143, PAF/202, SVP/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.data_utils import def_for, subtypes_for


def _leftovers(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", "") == "Leftovers"


def _vora_condition(board, player_id, pokemon) -> bool:
    discard = board.find_player_area(player_id, "discard")
    return bool(discard) and any(_leftovers(c) for c in discard.children)


async def voraciousness(ctx):
    pool = [c for c in ctx.discard_pile() if _leftovers(c)]
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Choose up to 2 Leftovers cards")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="d4baf292-adba-5fe0-afdc-20ec8474b473",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snorlax.Name",
    display_name="Snorlax",
    searchable_by=["Snorlax", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=446,
    abilities=[
        Ability(
            title="Voraciousness",
            game_text="Once during your turn, you may put up to 2 Leftovers cards from your discard pile into your hand.",
            activation=Activations.ONCE_PER_TURN,
            condition=_vora_condition,
            effect=voraciousness,
        ),
        Attack(
            title="Thudding Press",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=ac.recoil_attack(30),
        ),
    ],
)
