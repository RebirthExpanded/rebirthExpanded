"""Dragonite (SV035 149 -- JP SV2a 149; English MEW/149). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class JetCruisePassive(Passive):
    """Your Pokemon in play have no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        return 0 if pokemon.owning_player_id == carrier.owning_player_id else cost


async def dragon_pulse(ctx):
    await ctx.deal_damage()
    top = list(ctx.deck_top(2))
    if top:
        await ctx.discard_cards(top)


card = PokemonCardDef(
    guid="82d93a7d-5c24-51a9-a698-88d3125d2f37",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonite.Name",
    display_name="Dragonite",
    searchable_by=["Dragonite", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=149,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Jet Cruise",
            game_text="Your Pokémon in play have no Retreat Cost.",
            passive=JetCruisePassive(),
        ),
        Attack(
            title="Dragon Pulse",
            game_text="Discard the top 2 cards of your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=180,
            effect=dragon_pulse,
        ),
    ],
)
