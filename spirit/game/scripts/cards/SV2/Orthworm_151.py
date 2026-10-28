"""Orthworm (SV2 151 -- JP SV2P 055; English PAL/151, PAL/224). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class NutritionalIronPassive(Passive):
    """3 or more Metal Energy attached: +100 HP."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return 0
        n = sum(1 for c in pokemon.children if is_energy_of_type(c, PokemonTypes.METAL))
        return 100 if n >= 3 else 0


card = PokemonCardDef(
    guid="7933965d-84b8-587e-a3c6-4cd3a9648a6f",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Orthworm.Name",
    display_name="Orthworm",
    searchable_by=["Orthworm", "Basic"],
    subtypes=["Basic"],
    collector_number=151,
    set_code="SV2",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=968,
    abilities=[
        Ability(
            title="Nutritional Iron",
            game_text="If this Pokémon has 3 or more Metal Energy attached, it gets +100 HP.",
            passive=NutritionalIronPassive(),
        ),
        Attack(
            title="Shoot Through",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=ac.snipe_attack(30, pool="bench", also_base=True),
        ),
    ],
)
