from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="d2d265cd-4cb1-5317-8cc3-86d9cbfa9de1",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsZacianex.Name",
    display_name="Hop's Zacian ex",
    searchable_by=["Hop's Zacian ex", "Basic", "ex", "HopsZacianex"],
    subtypes=["Basic", "ex"],
    collector_number=111,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=888,
    abilities=[
        Attack(
            title="Insta-Strike",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=snipe_attack(30, also_base=True),
        ),
        Attack(
            title="Brave Slash",
            game_text="During your next turn, this Pok\u00e9mon can't use Brave Slash.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=240,
            locks_next_turn=True,
        ),
    ],
)
