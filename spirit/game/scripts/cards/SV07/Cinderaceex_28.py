"""Cinderace ex (SV07 28 -- JP SV7 018; English ASC/38, SCR/157, SCR/28, SVP/163). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="dac2c3f4-9f32-5d02-bf5a-bd9e4ccd29b7",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderaceex.Name",
    display_name="Cinderace ex",
    searchable_by=["Cinderace ex", "Stage 2", "ex", "Tera"],
    subtypes=["Stage 2", "ex", "Tera"],
    collector_number=28,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=320,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    family_id=813,
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Flare Strike",
            game_text="During your next turn, this Pokémon can't use Flare Strike.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=280,
            locks_next_turn=True,
        ),
        Attack(
            title="Garnet Volley",
            game_text="This attack does 180 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.DARKNESS: 1},
            effect=ac.snipe_attack(180, pool="any"),
        ),
    ],
)
