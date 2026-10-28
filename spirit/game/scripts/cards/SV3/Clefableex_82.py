"""Clefable ex (SV3 82 -- JP SVD 048; English OBF/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class LunarZonePassive(Passive):
    """Your Pokemon with Psychic Energy attached have no Retreat Cost."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id == carrier.owning_player_id and any(
                is_energy_of_type(e, PokemonTypes.PSYCHIC) for e in pokemon.children):
            return 0
        return cost


def _psychic(e) -> bool:
    return is_energy_of_type(e, PokemonTypes.PSYCHIC)


async def wondrous_moon(ctx):
    await ctx.deal_damage()
    mine = ctx.my_pokemon_in_play()
    await ctx.move_energy_freely(mine, mine, predicate=_psychic, prompt="Choose a Psychic Energy to move (Done to stop)")


card = PokemonCardDef(
    guid="cdb9089f-425e-552b-8780-895834568ba1",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefableex.Name",
    display_name="Clefable ex",
    searchable_by=["Clefable ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=82,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=173,
    abilities=[
        Ability(
            title="Lunar Zone",
            game_text="All of your Pokémon that have Psychic Energy attached have no Retreat Cost.",
            passive=LunarZonePassive(),
        ),
        Attack(
            title="Wondrous Moon",
            game_text="You may move any amount of Psychic Energy from your Pokémon to your other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=170,
            effect=wondrous_moon,
        ),
    ],
)
