from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_scaled_damage
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


def _basic_water(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.WATER.value)

card = PokemonCardDef(
    guid="de149d14-05a0-5c43-9f81-092d850f856c",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Avalugg.Name",
    display_name="Avalugg",
    searchable_by=["Avalugg", "Stage 1", "Avalugg"],
    subtypes=["Stage 1"],
    collector_number=24,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name",
    family_id=712,
    abilities=[
        Attack(
            title="Iceberg Breaker",
            game_text="Discard the top 6 cards of your deck, and this attack does 60 damage for each Basic [W] Energy card you discarded in this way.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            damage_operator="x",
            effect=mill_scaled_damage(6, 60, pred=_basic_water),
        ),
        Attack(
            title="Frost Stamp",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=160,
        ),
    ],
)
