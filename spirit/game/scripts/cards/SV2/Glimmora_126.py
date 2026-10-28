"""Glimmora (SV2 126 -- JP SV2P 044; English PAL/126). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon



class ShatteringCrystalPassive(Passive):
    """Knocked Out: flip a coin; heads, no Prize cards for it."""

    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier_pokemon(carrier) or count <= 0:
            return 0
        results = await ctx.flip_coins(1, "Shattering Crystal", source=pokemon, flipper_id=pokemon.owning_player_id)
        return -count if results and results[0] else 0


card = PokemonCardDef(
    guid="160ecdab-55e8-5087-bd66-118b16046feb",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmora.Name",
    display_name="Glimmora",
    searchable_by=["Glimmora", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=126,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name",
    family_id=969,
    abilities=[
        Ability(
            title="Shattering Crystal",
            game_text="When this Pokémon is Knocked Out, flip a coin. If heads, your opponent can't take any Prize cards for it.",
            passive=ShatteringCrystalPassive(),
        ),
        Attack(
            title="Poison Petals",
            game_text="Your opponent's Active Pokémon is now Poisoned. During Pokémon Checkup, put 6 damage counters on that Pokémon instead of 1.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=ac.condition_attack(SpecialConditions.POISONED, counters=6),
        ),
    ],
)
