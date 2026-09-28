from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_scaled_damage
from spirit.game.card_effects.passives_common import protect_next_turn
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.effects import is_basic_energy


def _basic_water(card) -> bool:
    return is_basic_energy(card) and energy_provides_type(card, PokemonTypes.WATER.value)

card = PokemonCardDef(
    guid="edd6bfeb-28a8-576c-a1e8-a4a2ea5bd666",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaAbomasnowex.Name",
    display_name="Mega Abomasnow ex",
    searchable_by=["Mega Abomasnow ex", "Stage 1", "ex", "SV_Mega", "MegaAbomasnowex"],
    subtypes=["Stage 1", "ex", "SV_Mega"],
    collector_number=36,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    family_id=459,
    abilities=[
        Attack(
            title="Hammer-lanche",
            game_text="Discard the top 6 cards of your deck, and this attack does 100 damage for each Basic [W] Energy card that you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=100,
            damage_operator="x",
            effect=mill_scaled_damage(6, 100, pred=_basic_water),
        ),
        Attack(
            title="Frost Barrier",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 3},
            damage=200,
            effect=protect_next_turn(reduce=30),
        ),
    ],
)
