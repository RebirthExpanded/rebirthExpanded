"""Scizor ex (SV05 111 -- JP SV5M 044; English TEF/111, TEF/195). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def _discard_attached(ctx, pred, upto, prompt):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if pred(e)]
    if not pool:
        return []
    picks = await ctx.choose_cards(pool, min(upto, len(pool)), minimum=0, prompt=prompt)
    if picks:
        await ctx.discard_cards(picks)
    return picks


def _metal(e) -> bool:
    return is_energy_of_type(e, PokemonTypes.METAL)


async def cross_breaker(ctx):
    picks = await _discard_attached(ctx, _metal, 2, "Discard up to 2 Metal Energy from this Pokémon")
    if picks:
        await ctx.deal_damage(120 * len(picks))


card = PokemonCardDef(
    guid="1961979c-3aee-5930-ac5b-b1e93826ceba",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizorex.Name",
    display_name="Scizor ex",
    searchable_by=["Scizor ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=111,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=pc.protect_next_turn(reduce=50),
        ),
        Attack(
            title="Cross Breaker",
            game_text="Discard up to 2 Metal Energy from this Pokémon. This attack does 120 damage for each card you discarded in this way.",
            cost={PokemonTypes.METAL: 2},
            damage=120,
            damage_operator="x",
            effect=cross_breaker,
        ),
    ],
)
