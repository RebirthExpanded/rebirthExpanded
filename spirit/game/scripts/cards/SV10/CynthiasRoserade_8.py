from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.data_utils import def_for
from spirit.game.session.passives import Passive


def _is_cynthias(pokemon) -> bool:
    name = getattr(def_for(pokemon.archetype_id), "display_name", "") or ""
    return name.startswith("Cynthia's ")


class CheerOnToGloryPassive(Passive):
    """+30 from your Cynthia's Pokemon's attacks to the opposing Active,
    before W/R. No "doesn't stack" clause: each Roserade adds its own."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or attacker.owning_player_id != carrier.owning_player_id:
            return
        if _is_cynthias(attacker):
            calc.amount += 30

card = PokemonCardDef(
    guid="a466d1e1-d607-54d0-bac0-ceac82e99111",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoserade.Name",
    display_name="Cynthia's Roserade",
    searchable_by=["Cynthia's Roserade", "Stage 1", "CynthiasRoserade"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasRoselia.Name",
    family_id=315,
    abilities=[
        Ability(
            title="Cheer On to Glory",
            game_text="Attacks used by your Cynthia's Pok\u00e9mon do 30 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=CheerOnToGloryPassive(),
        ),
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
