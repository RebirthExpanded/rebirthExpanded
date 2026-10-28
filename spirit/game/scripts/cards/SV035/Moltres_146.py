"""Moltres (SV035 146 -- JP SV2a 146; English MEW/146). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class FlareFloatPassive(Passive):
    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon is carrier and any(is_energy_of_type(e, PokemonTypes.FIRE) for e in pokemon.children):
            return 0
        return cost


async def blazing_flight(ctx):
    pool = [e for e in ctx.attached_energies(ctx.attacker) if is_energy_of_type(e, PokemonTypes.FIRE)]
    if len(pool) < 2:
        return
    picks = await ctx.choose_cards(pool, 2, minimum=2, prompt="Choose 2 Fire Energy to discard")
    await ctx.discard_cards(picks)
    await ac.snipe_attack(120, pool="bench")(ctx)


card = PokemonCardDef(
    guid="71cffca2-04b7-553b-a4ee-30cf1729736c",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic"],
    subtypes=["Basic"],
    collector_number=146,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=146,
    abilities=[
        Ability(
            title="Flare Float",
            game_text="If this Pokémon has any Fire Energy attached, it has no Retreat Cost.",
            passive=FlareFloatPassive(),
        ),
        Attack(
            title="Blazing Flight",
            game_text="Discard 2 Fire Energy from this Pokémon. This attack does 120 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 3},
            effect=blazing_flight,
        ),
    ],
)
