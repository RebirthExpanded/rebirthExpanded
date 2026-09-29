from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import damage_per
from spirit.game.session.effects import is_special_energy

card = PokemonCardDef(
    guid="2c67a09e-e3e0-5b30-936c-34bec73acf31",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinccino.Name",
    display_name="Cinccino",
    searchable_by=["Cinccino", "Stage 1", "Cinccino"],
    subtypes=["Stage 1"],
    collector_number=137,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Minccino.Name",
    family_id=572,
    abilities=[
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title="Special Roll",
            game_text="This attack does 70 damage for each Special Energy card attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="x",
            effect=damage_per(lambda ctx: sum(1 for e in ctx.attached_energies(ctx.attacker) if is_special_energy(e)), 70),
        ),
    ],
)
