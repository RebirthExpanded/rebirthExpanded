"""Life Forest {*} (SM - Lost Thunder 180/214 -- JP SM7b 050/050, the art here).

Stadium, Prism Star.

  "Once during each player's turn, that player may heal 60 damage and
   remove all Special Conditions from 1 of their Pokemon."
  "Whenever any player plays an Item or Supporter card from their hand,
   prevent all effects of that card done to this Stadium card."

The shield is Thunder Mountain's (ShieldedStadiumPassive), so Field
Blower and Lost Vacuum cannot reach it; another Stadium played over it
still replaces it, and Prism Star sends it to the Lost Zone.
"""

from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import ShieldedStadiumPassive
from spirit.game.data_utils import Ability, Activations, StadiumCardDef

HEAL = 60


class LifeForestPassive(ShieldedStadiumPassive):
    """Nothing but the heal; the shield is the shared Prism Star Stadium one."""


async def life_forest(ctx):
    targets = ctx.my_pokemon_in_play()
    if not targets:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose a Pokémon to heal 60 damage from")
    if target is None:
        return
    await ctx.heal(HEAL, target)
    await ctx.cure_all_conditions(target)


ABILITY = Ability(
    title="Life Forest {*}",
    game_text="Once during each player's turn, that player may heal 60 damage and remove all Special Conditions from 1 of their Pokémon.",
    activation=Activations.ONCE_PER_TURN,
    effect=life_forest,
)

card = StadiumCardDef(
    guid="faf4775d-830c-517a-bd08-78c23fd437cf",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeForestPrismStar.Name",
    display_name="Life Forest {*}",
    searchable_by=["Life Forest", "Stadium", "Prism Star", "LifeForest"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=180,
    set_code="SM8",
    rarity=Rarities.Prism,
    ability=ABILITY,
    passive=LifeForestPassive(),
)
