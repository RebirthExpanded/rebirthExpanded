"""Pachirisu (ME1 51 -- JP M1S 033; English MEG/51). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

async def electrified_incisors_watch(ctx):
    if not ctx.attack_used_last_turn(title="Electrified Incisors", entity=ctx.source):
        return
    if ctx.attaching_player_id != ctx.opponent_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None or receiver is not ctx.opponent_active():
        return
    await ctx.deal_damage(80, target=receiver, apply_modifiers=False, as_counters=True)


async def electrified_incisors(ctx):
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="9ff5e449-9d8e-530a-a63e-8ba75b0a8a62",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=417,
    abilities=[
        Attack(
            title="Electrified Incisors",
            game_text="During your opponent's next turn, whenever they attach an Energy card from their hand to the Defending Pokémon, place 8 damage counters on that Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=electrified_incisors,
        ),
    ],
)
card.abilities.append(Ability(
    title="Electrified Incisors",
    game_text="During your opponent's next turn, whenever they attach an Energy card from their hand to the Defending Pok\u00e9mon, place 8 damage counters on that Pok\u00e9mon.",
    trigger=Triggers.ON_ENERGY_ATTACHED,
    effect=electrified_incisors_watch,
))
