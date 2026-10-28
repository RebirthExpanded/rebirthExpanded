"""Omastar (SV035 139 -- JP SV2a 139; English MEW/139). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc
from spirit.game.card_effects import attacks_common as ac



class PrimordialTentaclesPassive(Passive):
    """Active: the opponent's Active Pokemon can't retreat."""

    def blocks_retreat(self, pokemon, carrier):
        return (pokemon.owning_player_id != carrier.owning_player_id and pc.is_in_active_spot(carrier)
                and pc.is_in_active_spot(pokemon))


card = PokemonCardDef(
    guid="ae7fc11c-9f6e-5f81-99eb-61d992f5ced2",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Omastar.Name",
    display_name="Omastar",
    searchable_by=["Omastar", "Stage 2"],
    subtypes=["Stage 2"],
    collector_number=139,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Omanyte.Name",
    family_id=138,
    abilities=[
        Ability(
            title="Primordial Tentacles",
            game_text="As long as this Pokémon is in the Active Spot, your opponent's Active Pokémon can't retreat.",
            passive=PrimordialTentaclesPassive(),
        ),
        Attack(
            title="Aqua Split",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2},
            damage=90,
            effect=ac.snipe_attack(30, pool="bench", count=2, also_base=True),
        ),
    ],
)
