"""Sinistcha (SV06 22 -- JP SV6 014; English TWM/22). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_energy_of_type, is_pokemon_card


async def cursed_drop(ctx):
    for _ in range(4):
        pool = ctx.opponent_pokemon_in_play()
        if not pool:
            return
        target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put a damage counter on")
        if target is None:
            return
        await ctx.deal_damage(10, target=target, apply_modifiers=False, as_counters=True)


async def spill_the_tea(ctx):
    pool = [e for p in ctx.my_pokemon_in_play() for e in ctx.attached_energies(p)
            if is_energy_of_type(e, PokemonTypes.GRASS)]
    if not pool:
        return
    picks = await ctx.choose_cards(pool, min(3, len(pool)), minimum=0, prompt="Discard up to 3 Grass Energy from your Pokémon")
    if picks:
        await ctx.discard_cards(picks)
        await ctx.deal_damage(70 * len(picks))


card = PokemonCardDef(
    guid="4a6ed808-da63-5f21-b326-f244504243fc",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sinistcha.Name",
    display_name="Sinistcha",
    searchable_by=["Sinistcha", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    family_id=1012,
    abilities=[
        Attack(
            title="Cursed Drop",
            game_text="Put 4 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.GRASS: 1},
            effect=cursed_drop,
        ),
        Attack(
            title="Spill the Tea",
            game_text="Discard up to 3 Grass Energy cards from your Pokémon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.GRASS: 1},
            damage=70,
            damage_operator="x",
            effect=spill_the_tea,
        ),
    ],
)
