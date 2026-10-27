"""Feraligatr (SVPJ 241 -- JP SVP 241; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="7fcf01ee-8d86-5b30-aaae-6f43fff04f50",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Feraligatr.Name",
    display_name="Feraligatr",
    searchable_by=["Feraligatr", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=241,
    set_code="SVPJ",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Deep Diving",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=pc.flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
