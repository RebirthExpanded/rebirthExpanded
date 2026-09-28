from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="f03b192a-6553-5727-afd0-fd6da75d0cf9",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsPhantump.Name",
    display_name="Hop's Phantump",
    searchable_by=["Hop's Phantump", "Basic", "HopsPhantump"],
    subtypes=["Basic"],
    collector_number=95,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=708,
    abilities=[
        Attack(
            title="Splashing Dodge",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)
