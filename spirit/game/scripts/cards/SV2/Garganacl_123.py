"""Garganacl (SV2 123 -- JP SV2D 048; English PAF/178, PAL/123). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def blessed_salt(ctx):
    owner = ctx.source.owning_player_id
    for p in list(ctx.board.pokemon_in_play(owner)):
        await ctx.heal(20, p)


card = PokemonCardDef(
    guid="d4852fef-558b-56d7-ba62-798b8b7570dd",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Garganacl.Name",
    display_name="Garganacl",
    searchable_by=["Garganacl", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=123,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Naclstack.Name",
    family_id=932,
    abilities=[
        Ability(
            title="Blessed Salt",
            game_text="During Pokémon Checkup, heal 20 damage from each of your Pokémon.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=blessed_salt,
        ),
        Attack(
            title="Knocking Hammer",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=130,
            effect=ac.mill_attack(1),
        ),
    ],
)
