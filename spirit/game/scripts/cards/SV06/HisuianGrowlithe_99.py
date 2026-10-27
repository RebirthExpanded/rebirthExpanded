"""Hisuian Growlithe (SV06 99 -- JP SV5a 041; English TWM/181, TWM/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


async def _discard_any_stadium(ctx):
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="51aae690-8138-5fad-8f6e-1e0040c2ccc3",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    display_name="Hisuian Growlithe",
    searchable_by=["Hisuian Growlithe", "Basic"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=58,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={},
            effect=_discard_any_stadium,
        ),
        Attack(
            title="Take Down",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=ac.recoil_attack(10),
        ),
    ],
)
