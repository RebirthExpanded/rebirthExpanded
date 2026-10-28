"""Whiscash (SV3 109 -- JP SV2D 039; English OBF/109). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def raging_and_rocking(ctx):
    n = sum(1 for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIGHTING))
    top = list(ctx.deck_top(n, player_id=ctx.opponent_id)) if n else []
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="9128111a-1e7c-5ccf-9848-afcd2bb95aab",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whiscash.Name",
    display_name="Whiscash",
    searchable_by=["Whiscash", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=109,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    family_id=339,
    abilities=[
        Attack(
            title="Raging and Rocking",
            game_text="For each Fighting Energy attached to this Pokémon, discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=raging_and_rocking,
        ),
        Attack(
            title="Land Crush",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=140,
        ),
    ],
)
