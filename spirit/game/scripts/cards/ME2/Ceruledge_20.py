"""Ceruledge (ME2 20 -- JP M2 020; English MEP/14, PFL/20). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


def _basic_fire(card):
    return is_basic_energy_card(card) and is_energy_of_type(card, PokemonTypes.FIRE)


async def _discard_or_nothing(ctx, pred, n, label):
    if len([c for c in ctx.hand() if pred(c)]) < n:
        return
    paid = await ctx.discard_from_hand(n, minimum=n, predicate=pred, prompt=f"Discard {n} {label} from your hand.")
    if len(paid) >= n:
        await ctx.deal_damage()


async def infernal_slash(ctx):
    await _discard_or_nothing(ctx, _basic_fire, 4, "Basic Fire Energy cards")


card = PokemonCardDef(
    guid="a64644e2-456f-55d0-b76b-36e8794ca080",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ceruledge.Name",
    display_name="Ceruledge",
    searchable_by=["Ceruledge", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Attack(
            title="Infernal Slash",
            game_text="Discard 4 Basic Fire Energy cards from your hand. If you can't discard 4 cards in this way, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=220,
            effect=infernal_slash,
        ),
    ],
)
