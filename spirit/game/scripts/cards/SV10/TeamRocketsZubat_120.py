from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="c144c672-8466-5121-8526-07de40fef8d7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsZubat.Name",
    display_name="Team Rocket's Zubat",
    searchable_by=["Team Rocket's Zubat", "Basic", "TeamRocketsZubat"],
    subtypes=["Basic"],
    collector_number=120,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=41,
    abilities=[
        Attack(
            title="Poison Spray",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=0,
            effect=condition_attack(SpecialConditions.POISONED),
        ),
    ],
)
