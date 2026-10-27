"""Regirock (SV09 82 -- JP SV9 049; English JTG/82). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _LessIf(Passive):
    """"This Pokemon takes N less damage from attacks" while pred(pokemon, board)."""

    def __init__(self, amount, pred):
        self.amount, self.pred = amount, pred

    def modify_damage_taken(self, calc, carrier):
        me = carrier_pokemon(carrier)
        if calc.is_attack and calc.is_opposing and me is calc.target and self.pred(me, calc.board):
            calc.amount = max(0, calc.amount - self.amount)

from spirit.game.models.board import EnergyEntity


def _has_energy(me, board) -> bool:
    return any(isinstance(c, EnergyEntity) for c in me.children)


async def breaching_lariat(ctx):
    await ctx.deal_damage(ignore_resistance=True)


card = PokemonCardDef(
    guid="500ab751-a710-5ea5-9bf3-662569503bc8",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regirock.Name",
    display_name="Regirock",
    searchable_by=["Regirock", "Basic"],
    subtypes=["Basic"],
    collector_number=82,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=377,
    abilities=[
        Ability(
            title="Rock Armor",
            game_text="If this Pokémon has any Energy attached, it takes 30 less damage from attacks (after applying Weakness and Resistance).",
            passive=_LessIf(30, _has_energy),
        ),
        Attack(
            title="Breaching Lariat",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            effect=breaching_lariat,
        ),
    ],
)
