"""Poncho-wearing Pikachu (XYPJ 230 -- JP XYP 230; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc

_fly = ac.flip_or_nothing(then=pc.protect_next_turn(prevent=True, effects_too=True))


card = PokemonCardDef(
    guid="bac40307-10e8-52c2-9ba7-2bb1677284c1",
    key="XYPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PonchowearingPikachu.Name",
    display_name="Poncho-wearing Pikachu",
    searchable_by=["Poncho-wearing Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=230,
    set_code="XYPJ",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=172,
    abilities=[
        Attack(
            title="Pika Punch",
            game_text="",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Fly?",
            game_text="Flip a coin. If tails, this attack does nothing. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=_fly,
        ),
    ],
)
