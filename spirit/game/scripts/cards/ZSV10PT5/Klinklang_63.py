"""Klinklang (ZSV10PT5 63 -- JP SV11W 067; English BLK/141, BLK/63). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



def _gear_coated(target, carrier) -> bool:
    return (target.owning_player_id == carrier.owning_player_id
            and any(is_energy_of_type(c, PokemonTypes.METAL) for c in target.children))


card = PokemonCardDef(
    guid="6601eb3a-a4b1-57b1-a4ff-17aa56107b3f",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Klinklang.Name",
    display_name="Klinklang",
    searchable_by=["Klinklang", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=63,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Klang.Name",
    family_id=599,
    abilities=[
        Ability(
            title="Gear Coating",
            game_text="All of your Pokémon that have any Metal Energy attached take 20 less damage from attacks from your opponent's Pokémon (after applying Weakness and Resistance).",
            passive=pc.takes_less_passive(20, protects=_gear_coated),
        ),
        Attack(
            title="Hammer In",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
        ),
    ],
)
