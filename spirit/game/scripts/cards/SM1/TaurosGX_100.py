from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on, damage_per

card = PokemonCardDef(
    guid="59c69958-da79-558a-adcb-1169560140bf",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TaurosGX.Name",
    display_name="Tauros-GX",
    searchable_by=["Tauros-GX", "Basic", "GX", "TaurosGX"],
    subtypes=["Basic", "GX"],
    collector_number=100,
    set_code="SM1",
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Rage",
            game_text="This attack does 10 more damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("self"), 10, base=20),
        ),
        Attack(
            title="Horn Attack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
        Attack(
            title="Mad Bull-GX",
            game_text="This attack does 30 damage for each damage counter on this Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            gx=True,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 30),
        ),
    ],
)
