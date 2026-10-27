"""Landorus (ME6 40 -- JP M6 040; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.data_utils import def_for, subtypes_for


_FORCES = {"Tornadus", "Thundurus", "Landorus", "Enamorus"}


class IncarnateUnityPassive(Passive):
    """With Tornadus, Thundurus, Landorus and Enamorus all in play, this
    Pokemon's attacks need no Colorless Energy (an Ability)."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if pokemon is not carrier:
            return cost
        names = {getattr(def_for(p.archetype_id), "display_name", None) for p in board.pokemon_in_play(carrier.owning_player_id)}
        if _FORCES <= names:
            cost = {k: v for k, v in cost.items() if k != "Colorless"}
        return cost


async def gaia_crush(ctx):
    await ctx.deal_damage()
    if ctx.stadium_in_play() is not None:
        await ctx.discard_stadium()


card = PokemonCardDef(
    guid="1cc5f129-afa6-5d80-8fb9-ef61ff9c1e21",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Landorus.Name",
    display_name="Landorus",
    searchable_by=["Landorus", "Basic"],
    subtypes=["Basic"],
    collector_number=40,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=645,
    abilities=[
        Ability(
            title="Incarnate Unity",
            game_text="If you have Tornadus, Thundurus, Landorus, and Enamorus in play, this Pokémon's attacks cost no Colorless Energy.",
            passive=IncarnateUnityPassive(),
        ),
        Attack(
            title="Gaia Crush",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=gaia_crush,
        ),
    ],
)
