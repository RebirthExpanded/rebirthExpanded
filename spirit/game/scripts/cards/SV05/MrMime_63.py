"""Mr. Mime (SV05 63 -- JP SV5M 031; English TEF/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac

from spirit.game.data_utils import TRAINER_EFFECTS_BY_GUID, unimplemented
from spirit.game.session.effects import is_supporter_card


async def look_alike_show(ctx):
    hand = list(ctx.hand(ctx.opponent_id))
    if not hand:
        return
    await ctx.reveal_hand(of_player=ctx.opponent_id, to_player=ctx.player_id)
    pool = [c for c in hand if is_supporter_card(c)
            and TRAINER_EFFECTS_BY_GUID.get((c.archetype_id or "").lower()) not in (None, unimplemented)]
    if not pool or not await ctx.ask_yes_no("Use the effect of a Supporter card in your opponent's hand?"):
        return
    picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose a Supporter card")
    if picks:
        await TRAINER_EFFECTS_BY_GUID[(picks[0].archetype_id or "").lower()](ctx)


card = PokemonCardDef(
    guid="ed0416b6-6fcd-5eb4-ba5f-6fb1941a1c5a",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MrMime.Name",
    display_name="Mr. Mime",
    searchable_by=["Mr. Mime", "Basic"],
    subtypes=["Basic"],
    collector_number=63,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=439,
    abilities=[
        Attack(
            title="Look-Alike Show",
            game_text="Your opponent reveals their hand. You may use the effect of a Supporter card you find there as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=look_alike_show,
        ),
        Attack(
            title="Eerie Wave",
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            effect=ac.condition_attack(SpecialConditions.CONFUSED),
        ),
    ],
)
