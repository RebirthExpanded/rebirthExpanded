from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.support_common import switch_self_attack

card = PokemonCardDef(
    guid="fd617fc0-9f06-5358-b58a-7ed782f2c9e4",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLatiasex.Name",
    display_name="Mega Latias ex",
    searchable_by=["Mega Latias ex", "Basic", "ex", "SV_Mega", "MegaLatiasex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=100,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=380,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Illusory Impulse",
            game_text="Discard all Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=300,
            effect=self_energy_discard_attack(all_energy=True),
        ),
    ],
)
