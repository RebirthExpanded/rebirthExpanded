"""Mismagius (SV2 88 -- JP SV1a 035; English PAL/212, PAL/88). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def magical_flick(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    d = ctx.opponent_active()
    bench = ctx.opponent_bench()
    if d is None or not bench or not ctx.attached_energies(d) or not await ctx.ask_yes_no("Use Magical Flick?"):
        return
    picks = await ctx.choose_cards(list(ctx.attached_energies(d)), 1, minimum=1, prompt="Choose an Energy to move")
    dest = await ctx.choose_pokemon(bench, "Choose 1 of your opponent's Benched Pokémon") if picks else None
    if dest is not None:
        await ctx.move_energy(picks[0], dest)


card = PokemonCardDef(
    guid="6fa7477f-b13b-56d7-9250-23cb4b69542f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=88,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Magical Flick",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=magical_flick,
        ),
        Attack(
            title="Psychic Sphere",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
