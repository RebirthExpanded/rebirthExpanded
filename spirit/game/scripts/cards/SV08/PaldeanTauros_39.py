"""Paldean Tauros (SV08 39 -- JP SV8 024; English SSP/39). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.effects import is_stage2_pokemon


async def upthrusting_horns(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is None or d in ctx.knockouts or ctx.effects_blocked(d) or not is_stage2_pokemon(d):
        return
    pool = list(ctx.attached_energies(d))
    if pool and await ctx.ask_yes_no("Put 2 Energy attached to your opponent's Active Pokémon into their hand?"):
        n = min(2, len(pool))
        picks = await ctx.choose_cards(pool, n, minimum=n, prompt="Choose 2 Energy")
        if picks:
            await ctx.put_in_hand(picks)


card = PokemonCardDef(
    guid="6ea03da7-1910-507c-adc9-dc7009cdc12a",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=128,
    abilities=[
        Attack(
            title="Upthrusting Horns",
            game_text="You may put 2 Energy attached to your opponent's Active Stage 2 Pokémon into their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=upthrusting_horns,
        ),
        Attack(
            title="Jet Headbutt",
            game_text="",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
