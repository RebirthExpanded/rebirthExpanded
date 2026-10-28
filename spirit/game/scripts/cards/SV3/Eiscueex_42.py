"""Eiscue ex (SV3 42 -- JP SV3 020; English OBF/210, OBF/222, OBF/42). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


async def scalding_block(ctx):
    await ctx.deal_damage()
    pool = list(ctx.attached_energies(ctx.attacker))
    if pool and ctx.attacker not in ctx.knockouts:
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to discard from this Pokémon")
        await ctx.discard_cards(picks)
    ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="5238d40e-a61d-501c-bfcd-51633ca84a22",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eiscueex.Name",
    display_name="Eiscue ex",
    searchable_by=["Eiscue ex", "Basic", "ex", "Tera"],
    subtypes=["Basic", "ex", "Tera"],
    collector_number=42,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=875,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Scalding Block",
            game_text="Discard an Energy from this Pokémon. During your opponent's next turn, the Defending Pokémon can't attack.",
            cost={PokemonTypes.WATER: 3},
            damage=160,
            effect=scalding_block,
        ),
    ],
)
