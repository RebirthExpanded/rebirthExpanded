"""Hydreigon (MF 23 -- JP MF 023; English 30C/99). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def three_headed_bite(ctx):
    heads = sum(1 for r in await ctx.flip_coins(3, "Three-Headed Bite") if r)
    target = ctx.opponent_active()
    if heads and target is not None and not ctx.effects_blocked(target) and ctx.attached_energies(target):
        n = min(heads, len(ctx.attached_energies(target)))
        await ctx.discard_energy_from(target, n, minimum=n,
                                      prompt=f"Choose {n} Energy to discard from your opponent's Active Pokémon")


card = PokemonCardDef(
    guid="1e018385-66d6-57eb-9898-6e803dae45d9",
    key="MF",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="MF",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=170,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Attack(
            title="Three-Headed Bite",
            game_text="Flip 3 coins. For each heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=three_headed_bite,
        ),
        Attack(
            title="Pitch-Black Fangs",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=140,
        ),
    ],
)
