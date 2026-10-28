"""Ampharos ex (SVP 16 -- JP SVAL 007; English SVP/16). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def thunderstrike_tail(ctx):
    pool = list(ctx.attached_energies(ctx.attacker))
    if len(pool) >= 2 and await ctx.ask_yes_no("Discard 2 Energy from this Pokémon for 100 more damage?"):
        picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Choose 2 Energy to discard")
        await ctx.discard_cards(picks)
        await ctx.deal_damage(240)
    else:
        await ctx.deal_damage(140)


card = PokemonCardDef(
    guid="7b96b8fa-ecdc-54dc-b102-27a49bad7185",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ampharosex.Name",
    display_name="Ampharos ex",
    searchable_by=["Ampharos ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=16,
    set_code="SVP",
    regulation_mark="G",
    rarity=Rarities.RarePromo,
    hp=330,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Flaaffy.Name",
    family_id=179,
    abilities=[
        Attack(
            title="Electro Ball",
            game_text="",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
        Attack(
            title="Thunderstrike Tail",
            game_text="You may discard 2 Energy from this Pokémon to have this attack do 100 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            damage_operator="+",
            effect=thunderstrike_tail,
        ),
    ],
)
