"""Yveltal (ME6A 79 -- JP M6a 079; English 30C/100). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import passives_common as pc


card = PokemonCardDef(
    guid="bc56f45f-8384-52c3-9568-acfa51254ccf",
    key="ME6A",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="ME6A",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Ability(
            title="Life-Locked",
            game_text="Your opponent's Active Pokémon can't be healed.",
            passive=pc.healing_block_passive(lambda target, carrier: target.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(target)),
        ),
        Attack(
            title="Dark Cutter",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
