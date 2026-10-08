"""Alakazam (SV - Twilight Masquerade 82/167 -- JP SV6 049/101, the art here).

Stage 2 Psychic Pokemon, evolves from Kadabra. HP 140, weakness Darkness
x2, resistance Fighting -30, retreat 1.

  Strange Hacking [P]      Your opponent's Active Pokemon is now Confused.
                           You may move any number of damage counters from
                           your opponent's Pokemon to their other Pokemon in
                           any way you like.
  Psychic         [P] 10+  50 more damage for each Energy attached to your
                           opponent's Active Pokemon.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.data_utils import Attack, PokemonCardDef


async def strange_hacking(ctx):
    defender = ctx.defender
    if defender is not None:
        await ctx.apply_special_condition(defender, SpecialConditions.CONFUSED)
    theirs = ctx.opponent_pokemon_in_play()
    if len(theirs) > 1:
        await ctx.move_damage_counters_freely(theirs, theirs)


card = PokemonCardDef(
    guid="bd2918d8-7a9c-580c-afc6-67c8951bfc1c",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=82,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Strange Hacking",
            game_text="Your opponent's Active Pokémon is now Confused. You may move any number of damage counters from your opponent's Pokémon to their other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=strange_hacking,
        ),
        Attack(
            title="Psychic",
            game_text="This attack does 50 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_energy("defender"), 50, base=10),
        ),
    ],
)
