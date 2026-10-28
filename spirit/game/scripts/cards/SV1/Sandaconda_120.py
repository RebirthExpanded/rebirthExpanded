"""Sandaconda (SV1 120 -- JP SV1S 047; English SVI/120). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import full_stack


async def sandstorm_spray(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    n = min(2, len(pool))
    if not n:
        return
    picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy to discard from this Pokémon")
    await ctx.discard_cards(picks)
    d = ctx.opponent_active()
    if picks and d is not None and not ctx.effects_blocked(d):
        await ctx.shuffle_into_deck(full_stack(d), ctx.opponent_id)


card = PokemonCardDef(
    guid="5a000052-fc18-572b-97de-626f10363198",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sandaconda.Name",
    display_name="Sandaconda",
    searchable_by=["Sandaconda", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=120,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Skull Bash",
            game_text="",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title="Sandstorm Spray",
            game_text="Discard 2 Energy from this Pokémon. If you discarded any Energy in this way, your opponent shuffles their Active Pokémon and all attached cards into their deck.",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            effect=sandstorm_spray,
        ),
    ],
)
