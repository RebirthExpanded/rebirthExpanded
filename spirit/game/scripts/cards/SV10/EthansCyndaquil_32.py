from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack

card = PokemonCardDef(
    guid="6763e17b-78ac-5aa6-b9fa-7a1a16fd7015",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansCyndaquil.Name",
    display_name="Ethan's Cyndaquil",
    searchable_by=["Ethan's Cyndaquil", "Basic", "EthansCyndaquil"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=155,
    abilities=[
        Attack(
            title="Ember",
            game_text="Discard an Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)
