from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.models.board import board_of
from spirit.game.session.effects import is_special_energy
from spirit.game.session.passives import Passive, carrier_pokemon


class MightyShellPassive(Passive):
    """No damage from, and no effects of, attacks by an opposing Pokemon
    with any Special Energy attached (Aegislash-EX's Mighty Shield shape)."""

    @staticmethod
    def _special(board, attacker) -> bool:
        return attacker is not None and any(
            is_special_energy(e) for e in board.attached_energies(attacker))

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if calc.target is not carrier_pokemon(carrier):
            return False
        return self._special(calc.board, calc.attacker)

    def blocks_attack_effects(self, target, carrier, source=None):
        if target is not carrier_pokemon(carrier) or source is None:
            return False
        if source.owning_player_id == carrier.owning_player_id:
            return False
        board = board_of(carrier)
        return board is not None and self._special(board, source)

card = PokemonCardDef(
    guid="fed8f456-6720-58be-b046-ec63e8726799",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name",
    display_name="Carracosta",
    searchable_by=["Carracosta", "Stage 2", "Carracosta"],
    subtypes=["Stage 2"],
    collector_number=23,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=564,
    abilities=[
        Ability(
            title="Mighty Shell",
            game_text="Prevent all damage from and effects of attacks done to this Pok\u00e9mon by your opponent's Pok\u00e9mon that have any Special Energy attached.",
            passive=MightyShellPassive(),
        ),
        Attack(
            title="Big Bite",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
