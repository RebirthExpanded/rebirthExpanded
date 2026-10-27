"""Galvantula (RSV10PT5 34 -- JP SV11W 031; English WHT/117, WHT/34). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def discharge(ctx):
    cards = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.LIGHTNING)]
    if cards:
        await ctx.discard_cards(cards)
        await ctx.deal_damage(50 * len(cards))


card = PokemonCardDef(
    guid="aa5b6595-d82f-5fe1-b51d-947f0e5a34e0",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy from this Pokémon. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator="x",
            effect=discharge,
        ),
    ],
)
