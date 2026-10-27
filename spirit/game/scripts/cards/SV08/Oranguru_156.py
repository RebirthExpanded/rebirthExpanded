"""Oranguru (SV08 156 -- JP SV8 090; English SSP/156). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon



class _ColorlessWeakness(Passive):
    def modify_weakness(self, calc, carrier):
        if calc.target is carrier_pokemon(carrier) and calc.weak_types:
            calc.weak_types = [PokemonTypes.COLORLESS.value]


async def now_youre_in_my_power(ctx):
    d = ctx.opponent_active()
    if d is not None and not ctx.effects_blocked(d):
        ctx.add_passive_through_own_next_turn(d, _ColorlessWeakness())


card = PokemonCardDef(
    guid="c96f4180-e5a4-5ea2-8e9d-244c5e068a47",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oranguru.Name",
    display_name="Oranguru",
    searchable_by=["Oranguru", "Basic"],
    subtypes=["Basic"],
    collector_number=156,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=765,
    abilities=[
        Attack(
            title="Now You're in My Power",
            game_text="Until the end of your next turn, the Defending Pokémon's Weakness is now Colorless. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=now_youre_in_my_power,
        ),
        Attack(
            title="Smack",
            game_text="",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
