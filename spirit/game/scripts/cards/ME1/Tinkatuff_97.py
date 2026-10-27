"""Tinkatuff (ME1 97 -- JP M1L 049; English MEG/97). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def haphazard_hammer(ctx):
    if not getattr(ctx, "evolved_from_hand", True):
        return
    target = ctx.opponent_active()
    if target is None or not await ctx.ask_yes_no("Use Haphazard Hammer?"):
        return
    results = await ctx.flip_coins(1, "Haphazard Hammer")
    if results and results[0] and ctx.attached_energies(target) and not ctx.effects_blocked(target):
        await ctx.discard_energy_from(target, 1, minimum=1,
                                      prompt="Choose an Energy to discard from your opponent's Active Pokémon")


card = PokemonCardDef(
    guid="18e050e2-c335-5dd9-9b6f-78ada702890a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatuff.Name",
    display_name="Tinkatuff",
    searchable_by=["Tinkatuff", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tinkatink.Name",
    family_id=957,
    abilities=[
        Ability(
            title="Haphazard Hammer",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            trigger=Triggers.ON_EVOLVE,
            effect=haphazard_hammer,
        ),
        Attack(
            title="Light Punch",
            game_text="",
            cost={PokemonTypes.METAL: 1},
            damage=30,
        ),
    ],
)
