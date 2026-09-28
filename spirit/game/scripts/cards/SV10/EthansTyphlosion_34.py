from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.attacks_common import count_discard, damage_per


def _ethans_adventure(card) -> bool:
    return getattr(def_for(card.archetype_id), "display_name", None) == "Ethan's Adventure"

card = PokemonCardDef(
    guid="1d9287e8-a845-536f-918f-86eca1e9ac59",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansTyphlosion.Name",
    display_name="Ethan's Typhlosion",
    searchable_by=["Ethan's Typhlosion", "Stage 2", "EthansTyphlosion"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansQuilava.Name",
    family_id=155,
    abilities=[
        Attack(
            title="Buddy Blast",
            game_text="This attack does 60 more damage for each Ethan's Adventure card in your discard pile.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_discard("mine", _ethans_adventure), 60, base=40),
        ),
        Attack(
            title="Steam Artillery",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
        ),
    ],
)
