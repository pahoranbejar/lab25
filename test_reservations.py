import json
import shutil
from pathlib import Path

from byu_pytest_utils import check_io, max_score, test_files

ASSIGNMENT = 'reservations.py'

original_inventory = test_files / "original_inventory.json"


def copy_inventory(name) -> Path:
    target = name + ".inventory.json"
    return shutil.copy(original_inventory, target)


def assert_inventory(observed, expected):
    with open(observed) as f:
        obs = json.load(f)
    with open(expected) as f:
        exp = json.load(f)
    assert obs == exp


@max_score(5)
def test_reservations_exit():
    inventory = copy_inventory('exit')
    check_io(test_files / 'exit.txt', ASSIGNMENT, inventory)
    assert_inventory(inventory, test_files / "exit.expected.json")


@max_score(5)
def test_reservations_list_exit():
    inventory = copy_inventory('list_exit')
    check_io(test_files / 'list_exit.txt', ASSIGNMENT, inventory)
    assert_inventory(inventory, test_files / "list_exit.expected.json")


@max_score(5)
def test_reservations_toggle_list_exit():
    inventory = copy_inventory('toggle_list_exit')
    check_io(test_files / 'toggle_list_exit.txt', ASSIGNMENT, inventory)
    assert_inventory(inventory, test_files / "toggle_list_exit.expected.json")


@max_score(5)
def test_reservations_toggle_twice_list_exit():
    inventory = copy_inventory('toggle_twice_list_exit')
    check_io(test_files / 'toggle_twice_list_exit.txt', ASSIGNMENT, inventory)
    assert_inventory(inventory, test_files / "toggle_twice_list_exit.expected.json")


@max_score(5)
def test_reservations_toggle_both_list_exit():
    inventory = copy_inventory('toggle_both_list_exit')
    check_io(test_files / 'toggle_both_list_exit.txt', ASSIGNMENT, inventory)
    assert_inventory(inventory, test_files / "toggle_both_list_exit.expected.json")


@max_score(5)
def test_reservations_repeat_toggle_list_exit():
    inventory = copy_inventory('repeat_toggle_list_exit')
    check_io(test_files / 'repeat_toggle_list_exit_1.txt', ASSIGNMENT, inventory)
    check_io(test_files / 'repeat_toggle_list_exit_2.txt', ASSIGNMENT, inventory)
    assert_inventory(inventory, test_files / "repeat_toggle_list_exit.expected.json")

