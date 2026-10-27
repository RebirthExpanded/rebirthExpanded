"""Durant (RSV10PT5 70 -- JP SV11W 068; English WHT/150, WHT/70). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.card_effects import attacks_common as ac


card = PokemonCardDef(
    guid="100c8b5b-ed7d-5a0c-84db-45cf6344233c",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Durant.Name",
    display_name="Durant",
    searchable_by=["Durant", "Basic"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="RSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=632,
    abilities=[
        Attack(
            title="Bite Together",
            game_text="If Durant is on your Bench, this attack does 20 more damage.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=ac.bonus_if(ac.named_in_play("Durant"), 20),
        ),
        Attack(
            title="Vise Grip",
            game_text="",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)
