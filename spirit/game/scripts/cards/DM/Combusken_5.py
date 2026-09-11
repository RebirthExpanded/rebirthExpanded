"""Combusken (SM - Dragon Majesty 5/70 -- JP SM6b 012/066, the art here).

Stage 1 Fire Pokemon. HP 80, weakness Water x2, no resistance, retreat 1.

  Ability  Natural Cure  Whenever you attach an Energy card from your hand
                         to this Pokemon, remove all Special Conditions
                         from it.
  Lunge [CC] 60  Flip a coin. If tails, this attack does nothing.

ON_ENERGY_ATTACHED carries who attached and to what; only the owner's
attach onto Combusken itself counts (an effect attach is not "from your
hand" and never fires it).
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing
from spirit.game.data_utils import Ability, Attack, PokemonCardDef, Triggers


async def natural_cure(ctx):
    if ctx.attaching_player_id != ctx.player_id or ctx.energy_receiver is not ctx.source:
        return
    await ctx.cure_all_conditions(ctx.source)


card = PokemonCardDef(
    guid="4d9b3ed9-8cd9-5d8a-b775-78399f47c48c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    display_name="Combusken",
    searchable_by=["Combusken", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="DM",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    family_id=255,
    abilities=[
        Ability(title="Natural Cure",
                game_text="Whenever you attach an Energy card from your hand to this Pokémon, remove all Special Conditions from it.",
                trigger=Triggers.ON_ENERGY_ATTACHED,
                effect=natural_cure),
        Attack(title="Lunge",
               game_text="Flip a coin. If tails, this attack does nothing.",
               cost={PokemonTypes.COLORLESS: 2},
               damage=60, effect=flip_or_nothing()),
    ],
)
