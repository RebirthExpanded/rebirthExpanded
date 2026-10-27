"""Fukuoka's Pikachu (SVPJ 289 -- JP SVP 289; English Japan only). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import support_common as su


card = PokemonCardDef(
    guid="96564d7b-395f-56f7-9d34-1dfb5d4ace1d",
    key="SVPJ",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FukuokasPikachu.Name",
    display_name="Fukuoka's Pikachu",
    searchable_by=["Fukuoka's Pikachu", "Basic"],
    subtypes=["Basic"],
    collector_number=289,
    set_code="SVPJ",
    regulation_mark="I",
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Renewal Open!",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=su.draw_attack(2),
        ),
        Attack(
            title="Gourmet Tour",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=su.heal_attack(30),
        ),
    ],
)
