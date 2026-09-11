"""Technical Machine: Blindside (SV - Paradox Rift 176/182 -- JP SV3a 057/062).

Pokemon Tool.

  "The Pokemon this card is attached to can use the attack on this card.
   (You still need the necessary Energy to use this attack.) If this card
   is attached to 1 of your Pokemon, discard it at the end of your turn."

  Blindside [CCC]  This attack does 100 damage to 1 of your opponent's
                   Pokemon that has any damage counters on it. (Don't
                   apply Weakness and Resistance for Benched Pokemon.)

Technical Machine: Devolution's shape: the borrowed Attack plus the
END_OF_TURN Ability that discards the Tool. Only damaged opposing Pokemon
are offered; with none the attack does nothing.
"""

from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import discard_self_tool_at_end_of_turn
from spirit.game.data_utils import (Ability, Attack, PokemonToolCardDef,
                                    Triggers)

TM_BLINDSIDE = "Technical Machine: Blindside"


async def blindside(ctx):
    damaged = [p for p in ctx.opponent_pokemon_in_play()
               if p.get_attribute(AttrID.HP, 0) < ctx.max_hp(p)]
    if not damaged:
        return
    target = await ctx.choose_pokemon(
        damaged, "Choose 1 of your opponent's Pokémon that has damage counters on it")
    if target is None:
        return
    await ctx.deal_damage(100, target=target)


card = PokemonToolCardDef(
    granted_abilities=[
        Attack(
            title="Blindside",
            game_text="This attack does 100 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=blindside,
        ),
        Ability(
            title=TM_BLINDSIDE,
            game_text="If this card is attached to 1 of your Pokémon, discard it at the end of your turn.",
            trigger=Triggers.END_OF_TURN,
            effect=discard_self_tool_at_end_of_turn(TM_BLINDSIDE),
        ),
    ],
    guid="f5ce164c-a247-549d-99e7-9e8859ea7968",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TechnicalMachineBlindside.Name",
    display_name=TM_BLINDSIDE,
    searchable_by=["Technical Machine: Blindside", "Item", "Pokémon Tool",
                   "TechnicalMachineBlindside"],
    subtypes=["Item", "Pokémon Tool"],
    collector_number=176,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
)
