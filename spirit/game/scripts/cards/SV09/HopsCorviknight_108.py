"""Hop's Corviknight (SV09 108 -- JP SV9 068; English JTG/108). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="5ba24324-c07a-5295-b2b8-e72dcb7cea7d",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorviknight.Name",
    display_name="Hop's Corviknight",
    searchable_by=["Hop's Corviknight", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=108,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorvisquire.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Shoot Through",
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ac.snipe_attack(50, pool="bench", also_base=True),
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pokémon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=pc.protect_next_turn(reduce=60),
        ),
    ],
)
