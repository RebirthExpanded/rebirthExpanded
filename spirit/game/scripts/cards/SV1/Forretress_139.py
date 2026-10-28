"""Forretress (SV1 139 -- JP SV1V 057; English SVI/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac
from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="854aab38-580c-5c02-a482-3ce189325f82",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=139,
    set_code="SV1",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Continuous Spin",
            game_text="Flip a coin until you get tails. This attack does 50 damage for each heads.",
            cost={PokemonTypes.METAL: 1},
            damage=50,
            damage_operator="x",
            effect=ac.flip_damage(until_tails=True, per_heads=50),
        ),
        Attack(
            title="Rolling Shell",
            game_text="During your opponent's next turn, this Pokémon takes 50 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=pc.protect_next_turn(reduce=50),
        ),
    ],
)
