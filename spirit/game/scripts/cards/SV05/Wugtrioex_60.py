"""Wugtrio ex (SV05 60 -- JP SV5K 025; English TEF/190, TEF/60). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_energy_card


async def tricolor_pump(ctx):
    pool = [c for c in ctx.hand() if is_energy_card(c)]
    if not pool:
        return
    picks = await ctx.discard_from_hand(min(3, len(pool)), minimum=0, predicate=is_energy_card,
                                        prompt="Discard up to 3 Energy cards from your hand")
    if picks:
        await ac.snipe_attack(60 * len(picks), pool="any")(ctx)


card = PokemonCardDef(
    guid="31ae6614-9a13-5e90-b974-84bb0f0ebfeb",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wugtrioex.Name",
    display_name="Wugtrio ex",
    searchable_by=["Wugtrio ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=60,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wiglett.Name",
    family_id=960,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Tricolor Pump",
            game_text="Discard up to 3 Energy cards from your hand. This attack does 60 damage to 1 of your opponent's Pokémon for each Energy card you discarded in this way. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=tricolor_pump,
        ),
        Attack(
            title="Numbing Hold",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            effect=ac.condition_attack(no_retreat=True),
        ),
    ],
)
