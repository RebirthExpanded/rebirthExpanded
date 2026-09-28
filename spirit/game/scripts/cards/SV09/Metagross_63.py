from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import AttrID
from spirit.game.card_effects.attacks_common import bonus_if


def _beldum_and_metang_benched(ctx) -> bool:
    names = {p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) for p in ctx.my_bench()}
    return {"Beldum", "Metang"} <= names

card = PokemonCardDef(
    guid="4c261ab7-c503-5754-8724-d76d11386cd2",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=63,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=60,
        ),
        Attack(
            title="Conjoined Beams",
            game_text="If Beldum and Metang are on your Bench, this attack does 150 more damage.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=130,
            damage_operator="+",
            effect=bonus_if(_beldum_and_metang_benched, 150),
        ),
    ],
)
