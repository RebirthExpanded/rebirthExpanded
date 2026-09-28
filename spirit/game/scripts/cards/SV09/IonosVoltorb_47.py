from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.card_effects.pokemon import energy_units_of_type


def _is_ionos(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Iono's ")


async def voltaic_chain(ctx):
    """20 + 20 for each [L] Energy attached to all of your Iono's Pokemon."""
    count = sum(energy_units_of_type(ctx.board, e, PokemonTypes.LIGHTNING.value)
                for p in ctx.my_pokemon_in_play() if _is_ionos(p)
                for e in ctx.attached_energies(p))
    await ctx.deal_damage(20 + 20 * count)

card = PokemonCardDef(
    guid="2c7fad05-94bd-5bbd-bca0-4c22d8701633",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosVoltorb.Name",
    display_name="Iono's Voltorb",
    searchable_by=["Iono's Voltorb", "Basic", "IonosVoltorb"],
    subtypes=["Basic"],
    collector_number=47,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=100,
    abilities=[
        Attack(
            title="Voltaic Chain",
            game_text="This attack does 20 more damage for each [L] Energy attached to all of your Iono's Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=voltaic_chain,
        ),
    ],
)
