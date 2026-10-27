"""Arven's Toedscruel (SV10 110 -- JP SV9a 048; English DRI/110). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su
from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="ad0f5f33-26dc-54fc-a438-0cdfc0d10f4a",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensToedscruel.Name",
    display_name="Arven's Toedscruel",
    searchable_by=["Arven's Toedscruel", "Stage 1"],
    subtypes=["Stage 1"],
    collector_number=110,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ArvensToedscool.Name",
    family_id=948,
    abilities=[
        Attack(
            title="Pull",
            game_text="Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=su.gust_attack(),
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=ac.recoil_attack(30),
        ),
    ],
)
