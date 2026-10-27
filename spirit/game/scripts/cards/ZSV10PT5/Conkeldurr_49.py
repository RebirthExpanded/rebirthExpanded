"""Conkeldurr (ZSV10PT5 49 -- JP SV11B 052; English BLK/127, BLK/49). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.effects import is_energy_of_type, is_pokemon_card



class CraftsmanshipPassive(Passive):
    """+40 HP for each Fighting Energy attached (an Ability)."""

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon is not carrier_pokemon(carrier):
            return 0
        return 40 * sum(1 for c in pokemon.children if is_energy_of_type(c, PokemonTypes.FIGHTING))


card = PokemonCardDef(
    guid="8fa113d1-8537-5388-b281-41373e8c065e",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name",
    display_name="Conkeldurr",
    searchable_by=["Conkeldurr", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=49,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name",
    family_id=532,
    abilities=[
        Ability(
            title="Craftsmanship",
            game_text="This Pokémon gets +40 HP for each Fighting Energy attached to it.",
            passive=CraftsmanshipPassive(),
        ),
        Attack(
            title="Swing Around",
            game_text="Flip 2 coins. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=100,
            damage_operator="+",
            effect=ac.flip_damage(coins=2, bonus_per_heads=50),
        ),
    ],
)
