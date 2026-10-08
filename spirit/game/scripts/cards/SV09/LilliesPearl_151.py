from spirit.game.data_utils import PokemonToolCardDef, def_for
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive, carrier_pokemon, ko_by_opposing_attack_damage


def _is_lillies_pokemon(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Lillie's ")


class LilliesPearlPassive(Passive):
    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return count
        if not _is_lillies_pokemon(pokemon):
            return count
        if not ko_by_opposing_attack_damage(ctx, pokemon):
            return count
        return max(0, count - 1)


card = PokemonToolCardDef(
    guid="f2c517b6-f0d5-5886-9b0b-79fed97bd954",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LilliesPearl.Name",
    display_name="Lillie's Pearl",
    searchable_by=["Lillie's Pearl", "Pokémon Tool", "LilliesPearl"],
    subtypes=["Pokémon Tool"],
    collector_number=151,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=LilliesPearlPassive(),
)
