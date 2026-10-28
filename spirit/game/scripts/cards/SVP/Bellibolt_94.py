"""Bellibolt (SVP 94 -- JP SVP 052; English SVP/94). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def two_bump_bolt(ctx):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.LIGHTNING)]
    picks = []
    if pool:
        picks = await ctx.choose_cards(pool, min(2, len(pool)), minimum=0, prompt="Discard up to 2 Lightning Energy")
        if picks:
            await ctx.discard_cards(picks)
    await ctx.deal_damage(10 + 80 * len(picks))


card = PokemonCardDef(
    guid="336af708-68aa-5cb0-9277-bdc732a8e8ec",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name",
    display_name="Bellibolt",
    searchable_by=["Bellibolt", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=94,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Attack(
            title="Thunder Wave",
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=ac.condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Two Bump Bolt",
            game_text="You may discard up to 2 Lightning Energy from this Pokémon. This attack does 80 more damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=two_bump_bolt,
        ),
    ],
)
