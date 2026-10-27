"""Delcatty (SV05 131 -- JP SV5M 056; English TEF/131). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac


async def energy_blender(ctx):
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, prompt="Choose an Energy to move (Done to stop)")


card = PokemonCardDef(
    guid="b6007b01-497e-5868-af6f-af588a542102",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=131,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    family_id=300,
    abilities=[
        Attack(
            title="Tail Trickery",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
        Attack(
            title="Energy Blender",
            game_text="You may move any amount of Energy from your Pokémon to your other Pokémon in any way you like.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
            effect=energy_blender,
        ),
    ],
)
