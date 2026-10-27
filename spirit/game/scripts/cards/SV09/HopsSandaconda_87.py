"""Hop's Sandaconda (SV09 87 -- JP SV9 054; English JTG/87). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="78c77aac-5740-5158-a1ea-fcdfaefd0974",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSandaconda.Name",
    display_name="Hop's Sandaconda",
    searchable_by=["Hop's Sandaconda", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=87,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsSilicobra.Name",
    family_id=843,
    abilities=[
        Attack(
            title="Rumble",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=ac.condition_attack(no_retreat=True),
        ),
        Attack(
            title="Break Ground",
            game_text="This attack also does 20 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=ac.spread_damage(20, side="mine", also_base=True),
        ),
    ],
)
