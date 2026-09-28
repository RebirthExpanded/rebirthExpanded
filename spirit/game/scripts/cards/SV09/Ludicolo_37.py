from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive


class VibrantDancePassive(Passive):
    """All of your Pokemon in play get +40 HP; the shared stacking_key keeps
    a second Ludicolo from adding another 40."""
    stacking_key = "VibrantDance"

    def max_hp_bonus(self, pokemon, carrier):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return 0
        return 40


card = PokemonCardDef(
    guid="fef0a601-34cd-5011-9b59-121c5b8ec839",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ludicolo.Name",
    display_name="Ludicolo",
    searchable_by=["Ludicolo", "Stage 2", "Ludicolo"],
    subtypes=["Stage 2"],
    collector_number=37,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lombre.Name",
    family_id=270,
    abilities=[
        Ability(
            title="Vibrant Dance",
            game_text="All of your Pok\u00e9mon in play get +40 HP. The effect of Vibrant Dance doesn't stack.",
            passive=VibrantDancePassive(),
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
