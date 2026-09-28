from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import bonus_if, damage_counters_on

card = PokemonCardDef(
    guid="4de9711d-9552-54ce-ba1c-61b34a2ef77d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaFeraligatrex.Name",
    display_name="Mega Feraligatr ex",
    searchable_by=["Mega Feraligatr ex", "Stage 2", "ex", "SV_Mega", "MegaFeraligatrex"],
    subtypes=["Stage 2", "ex", "SV_Mega"],
    collector_number=43,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=370,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croconaw.Name",
    family_id=158,
    abilities=[
        Attack(
            title="Mortal Crunch",
            game_text="If your opponent's Active Pok\u00e9mon already has any damage counters on it, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            damage_operator="+",
            effect=bonus_if(lambda ctx: damage_counters_on("defender")(ctx) > 0, 200),
        ),
    ],
)
