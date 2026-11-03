"""Team Rocket's Mimikyu-GX (SMD 10 -- JP SMD 010; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="4496285e-196a-53c4-8487-c0d5822a2a19",
    key="SMD",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMimikyuGX.Name",
    display_name="Team Rocket's Mimikyu-GX",
    searchable_by=["Team Rocket's Mimikyu-GX", "Basic", "GX"],
    subtypes=["Basic", "GX"],
    collector_number=10,
    set_code="SMD",
    regulation_mark="A",
    rarity=Rarities.RareHoloGX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=778,
    abilities=[
        Attack(
            title="Mumble",
            game_text="",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
        Attack(
            title="Ghost Claw",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            damage_operator="+",
            effect=ac.flip_bonus(30),
        ),
        Attack(
            title="Disguise-GX",
            game_text="During your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=100,
            effect=pc.protect_next_turn(prevent=True, effects_too=True),
            gx=True,
        ),
    ],
)
