"""Porygon (SV035 137 -- JP SV2a 137; English MEW/137). Japanese art.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Activations, Attack, PokemonCardDef, Triggers

from spirit.game.session.passives import Passive, carrier_pokemon


_TYPES = [("Grass", "GRASS"), ("Fire", "FIRE"), ("Water", "WATER"), ("Lightning", "LIGHTNING"), ("Psychic", "PSYCHIC"),
          ("Fighting", "FIGHTING"), ("Darkness", "DARKNESS"), ("Metal", "METAL"), ("Dragon", "DRAGON")]


class _WeaknessIs(Passive):
    def __init__(self, ptype):
        self.ptype = ptype

    def modify_weakness(self, calc, carrier):
        if calc.target is carrier_pokemon(carrier) and calc.weak_types:
            calc.weak_types = [self.ptype.value]


async def conversion_4(ctx):
    d = ctx.opponent_active()
    if d is None or ctx.effects_blocked(d):
        return
    index = await ctx.choose("Choose a type", [label for label, _ in _TYPES])
    if isinstance(index, int) and 0 <= index < len(_TYPES):
        ctx.add_temporary_passive(d, _WeaknessIs(getattr(PokemonTypes, _TYPES[index][1])))


card = PokemonCardDef(
    guid="04cb6b83-e850-565a-b1e6-0027282e03e4",
    key="SV035",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon.Name",
    display_name="Porygon",
    searchable_by=["Porygon", "Basic"],
    subtypes=["Basic"],
    collector_number=137,
    set_code="SV035",
    regulation_mark="G",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=137,
    abilities=[
        Attack(
            title="Conversion 4",
            game_text="Choose Grass, Fire, Water, Lightning, Psychic, Fighting, Darkness, Metal, or Dragon type. Until the Defending Pokémon leaves the Active Spot, its Weakness is now that type. (The amount of Weakness doesn't change.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=conversion_4,
        ),
    ],
)
