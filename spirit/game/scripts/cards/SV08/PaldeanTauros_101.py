"""Paldean Tauros (SV08 101 -- JP SV8 063; English SSP/101). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac

from spirit.game.session.effects import is_basic_pokemon_in_play


async def blocking_stomp(ctx):
    await ctx.deal_damage()
    d = ctx.opponent_active()
    if d is not None and d not in ctx.knockouts and is_basic_pokemon_in_play(d):
        ac.lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="c8432764-d856-5b43-bf9c-dfc2189d3006",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name",
    display_name="Paldean Tauros",
    searchable_by=["Paldean Tauros", "Basic"],
    subtypes=["Basic"],
    collector_number=101,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="Smash Kick",
            game_text="",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title="Blocking Stomp",
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=blocking_stomp,
        ),
    ],
)
