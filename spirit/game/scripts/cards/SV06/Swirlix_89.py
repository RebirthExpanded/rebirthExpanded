"""Swirlix (SV06 89 -- JP SV6 051; English TWM/89). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects.pokemon import FestivalLeadPassive


async def sneaky_placement(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(pool, "Choose 1 of your opponent's Pokémon to put 2 damage counters on")
    if target is not None:
        await ctx.deal_damage(20, target=target, apply_modifiers=False, as_counters=True)


card = PokemonCardDef(
    guid="b80d737d-38f1-5ab1-9855-7f1b7e76450a",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swirlix.Name",
    display_name="Swirlix",
    searchable_by=["Swirlix", "Basic"],
    subtypes=["Basic"],
    collector_number=89,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=684,
    abilities=[
        Ability(
            title="Festival Lead",
            game_text="If Festival Grounds is in play, this Pokémon may use an attack it has twice. If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.",
            passive=FestivalLeadPassive(),
        ),
        Attack(
            title="Sneaky Placement",
            game_text="Put 2 damage counters on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=sneaky_placement,
        ),
    ],
)
