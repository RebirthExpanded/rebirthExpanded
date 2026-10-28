"""Froslass ex (SV4 3 -- JP SV3a 001; English PAR/217, PAR/3). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers
from spirit.game.card_effects.pokemon import TeraRulePassive

from spirit.game.card_effects import attacks_common as ac
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects import passives_common as pc



class EvanescentPassive(Passive):
    """Knocked Out in the Active Spot: flip; heads, 1 fewer Prize card."""

    async def extra_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is not carrier_pokemon(carrier) or count <= 0:
            return 0
        if pokemon.parent is None or pokemon.parent.get_attribute(AttrID.NAME) != "activePokemonArea":
            return 0
        results = await ctx.flip_coins(1, "Evanescent", source=pokemon, flipper_id=pokemon.owning_player_id)
        return -1 if results and results[0] else 0
from spirit.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES


card = PokemonCardDef(
    guid="3f8ee6a1-eba9-56e3-876b-cb9640beb567",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslassex.Name",
    display_name="Froslass ex",
    searchable_by=["Froslass ex", "Stage 1", "ex", "Tera"],
    subtypes=["Stage 1", "ex", "Tera"],
    collector_number=3,
    set_code="SV4",
    regulation_mark="G",
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    family_id=361,
    passive=TeraRulePassive(),
    abilities=[
        Ability(
            title="Evanescent",
            game_text="If this Pokémon is in the Active Spot and is Knocked Out, flip a coin. If heads, your opponent takes 1 fewer Prize card.",
            passive=EvanescentPassive(),
        ),
        Attack(
            title="Frost Bullet",
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2},
            damage=140,
            effect=ac.snipe_attack(20, pool="bench", also_base=True),
        ),
    ],
)
