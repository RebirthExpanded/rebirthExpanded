from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.support_common import switch_self_attack

card = PokemonCardDef(
    guid="5ac17848-93f8-5c81-8dd6-b54f14d10375",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaZeraoraex.Name",
    display_name="Mega Zeraora ex",
    searchable_by=["Mega Zeraora ex", "Basic", "ex", "SV_Mega", "MegaZeraoraex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=27,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Thunderous Fist",
            game_text="This attack does 60 damage for each [L] Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_energy("self", PokemonTypes.LIGHTNING), 60),
        ),
        Attack(
            title="Zepto Turn",
            game_text="Switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=150,
            effect=switch_self_attack(),
        ),
    ],
)
