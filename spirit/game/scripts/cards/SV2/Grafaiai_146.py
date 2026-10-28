"""Grafaiai (SV2 146 -- JP SV2D 055; English PAF/190, PAL/146, PAL/223). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import def_for, subtypes_for


async def colorful_graffiti(ctx):
    pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
    if not pool:
        return
    picks = await ctx.discard_from_hand(len(pool), minimum=0, predicate=is_basic_energy_card,
                                        prompt="Discard any number of Basic Energy cards")
    kinds = {getattr(def_for(c.archetype_id), "display_name", "") for c in picks}
    if kinds:
        await ctx.deal_damage(40 * len(kinds))


card = PokemonCardDef(
    guid="a47e2700-2aa6-5349-8d7c-4aebbc728eba",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiai.Name",
    display_name="Grafaiai",
    searchable_by=["Grafaiai", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=146,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED),
        ),
        Attack(
            title="Colorful Graffiti",
            game_text="You may discard as many Basic Energy cards as you like from your hand. This attack does 40 damage for each type of Basic Energy you discarded in this way.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
            damage_operator="x",
            effect=colorful_graffiti,
        ),
    ],
)
