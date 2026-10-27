"""Krookodile ex (ME4 55 -- JP MP 046; English CRI/55). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


def _tooled(ctx) -> bool:
    return ac.has_tool(ctx.attacker)


card = PokemonCardDef(
    guid="46fbedcf-2df3-5b21-a03f-77c5a4b8ad40",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Krookodileex.Name",
    display_name="Krookodile ex",
    searchable_by=["Krookodile ex", "Stage 2", "ex"],
    subtypes=["Stage 2", "ex"],
    collector_number=55,
    set_code="ME4",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name",
    family_id=551,
    abilities=[
        Attack(
            title="Corner",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Strong Bite",
            game_text="If this Pokémon has a Pokémon Tool attached, this attack does 140 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=ac.bonus_if(_tooled, 140),
        ),
    ],
)
