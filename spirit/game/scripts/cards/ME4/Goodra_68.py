"""Goodra (ME4 68 -- JP M4 066; English CRI/68, MEP/77). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class SlimySlidingPassive(Passive):
    """The opponent's Active Pokemon retreating flips a coin first; tails
    and nothing is paid or switched (Slimy Sliding; doesn't stack)."""

    def retreat_flip_title(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(pokemon):
            return "Slimy Sliding"
        return None


async def dragon_pulse(ctx):
    await ctx.deal_damage()
    await ctx.discard_cards(ctx.deck_top(1))


card = PokemonCardDef(
    guid="20499a2c-990b-5b04-84c8-a9bd18485f02",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Goodra.Name",
    display_name="Goodra",
    searchable_by=["Goodra", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=68,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sliggoo.Name",
    family_id=704,
    abilities=[
        Ability(
            title="Slimy Sliding",
            game_text="When your opponent's Active Pokémon retreats, your opponent flips a coin. If tails, Energy for its Retreat Cost is not discarded, and they don't switch Pokémon. The effect of Slimy Sliding doesn't stack.",
            passive=SlimySlidingPassive(),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top card of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1},
            damage=160,
            effect=dragon_pulse,
        ),
    ],
)
