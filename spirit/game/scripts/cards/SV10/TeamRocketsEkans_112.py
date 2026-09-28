from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="fef44507-8109-59f8-8b75-675cc0fbe38b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsEkans.Name",
    display_name="Team Rocket's Ekans",
    searchable_by=["Team Rocket's Ekans", "Basic", "TeamRocketsEkans"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=23,
    abilities=[
        Attack(
            title="Drag Down",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=0,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
