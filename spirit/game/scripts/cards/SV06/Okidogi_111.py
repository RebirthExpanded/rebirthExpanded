"""Okidogi (SV - Twilight Masquerade 111/167 -- JP SV6 064/101, the art here).

Basic Darkness Pokemon. HP 130, weakness Grass x2, retreat 2.

  Adrena-Brain  (Ability)  If this Pokemon has any Energy attached, its
                           maximum HP is increased by 100, and its attacks
                           do 100 more damage to your opponent's Active
                           Pokemon.
  Good Punch    [DCC] 70

Both halves ride one passive, read live: the Energy leaving takes the
HP bonus with it (resync_effective_max_hp), and the boost only counts
against the opposing Active, as printed.
"""

from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.data_utils import Ability, Attack, PokemonCardDef
from spirit.game.session.effects import is_energy_card
from spirit.game.session.passives import Passive, carrier_pokemon

HP_BONUS = 100
DAMAGE_BONUS = 100


def _has_energy(pokemon) -> bool:
    return any(is_energy_card(child) for child in pokemon.children)


class _AdrenaBrainPassive(Passive):
    """+100 max HP and +100 damage to the opposing Active while any Energy
    is attached to the holder."""

    def max_hp_bonus(self, pokemon, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if holder is not pokemon:
            return 0
        return HP_BONUS if _has_energy(pokemon) else 0

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        holder = carrier_pokemon(carrier) or carrier
        if calc.attacker is not holder or not calc.to_active:
            return
        if _has_energy(holder):
            calc.amount += DAMAGE_BONUS


card = PokemonCardDef(
    guid="c24b3db3-0134-5f9c-9aa5-223b1b80d9e8",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Okidogi.Name",
    display_name="Okidogi",
    searchable_by=["Okidogi", "Basic"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=1014,
    abilities=[
        Ability(
            title="Adrena-Brain",
            game_text="If this Pokémon has any Energy attached, its maximum HP is increased by 100, and its attacks do 100 more damage to your opponent's Active Pokémon.",
            passive=_AdrenaBrainPassive(),
        ),
        Attack(
            title="Good Punch",
            game_text="",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
