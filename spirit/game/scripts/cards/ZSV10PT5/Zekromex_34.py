from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_prizes_taken, damage_per

card = PokemonCardDef(
    guid="363c02f3-53d6-5533-a393-23f1da604a55",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zekromex.Name",
    display_name="Zekrom ex",
    searchable_by=["Zekrom ex", "Basic", "ex", "Zekromex"],
    subtypes=["Basic", "ex"],
    collector_number=34,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=644,
    abilities=[
        Attack(
            title="Slash",
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
        Attack(
            title="Voltage Burst",
            game_text="This attack does 50 more damage for each Prize card your opponent has taken. This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            damage_operator="+",
            effect=damage_per(count_prizes_taken("opponent"), 50, base=130, self_damage=30),
        ),
    ],
)
