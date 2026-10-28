"""Revavroom ex (SV3 156 -- JP SV3 127; English OBF/156, OBF/216, OBF/224). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class TuneUpPassive(Passive):
    """This Pokemon may have up to 4 Pokemon Tools attached."""

    def tool_capacity(self, pokemon, carrier):
        return 4 if pokemon is carrier_pokemon(carrier) else 1


card = PokemonCardDef(
    guid="36520a71-1da3-570a-a9cc-f069367b3b08",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroomex.Name",
    display_name="Revavroom ex",
    searchable_by=["Revavroom ex", "Stage 1", "ex"],
    subtypes=["Stage 1", "ex"],
    collector_number=156,
    set_code="SV3",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Ability(
            title="Tune-Up",
            game_text="This Pokémon may have up to 4 Pokémon Tools attached to it. If it loses this Ability, discard Pokémon Tools from it until only 1 remains.",
            passive=TuneUpPassive(),
        ),
        Attack(
            title="Wild Drift",
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=170,
            effect=pc.protect_next_turn(reduce=30),
        ),
    ],
)
