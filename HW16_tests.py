import pytest
import sqlite_lib as sl
import HW16_SQL as hw16

# 1.
def test_eurovision_winners() -> None:
    sl.connect('eurv_db');

    result: list[tuple] = sl.run_query_select('''
        SELECT COUNT(*) FROM eurovision_winners
    ''');

    assert result == [(68,)];


def test_song_details() -> None:
    sl.connect('eurv_db');

    result: list[tuple] = sl.run_query_select('''
        SELECT COUNT(*) FROM song_details
    ''');

    assert result == [(68,)];

# 4.
def test_find_year_name_type1_true() -> None:
    assert hw16.find_year_name_type1(2024, 'Switzerland') == "Winning song: The Code";


def test_find_year_name_type1_false() -> None:
    assert hw16.find_year_name_type1(2024, 'Sweden') == "wrong...";


def test_find_year_name_type2_true() -> None:
    assert hw16.find_year_name_type1(2024, 'Switzerland') == "Winning song: The Code";


def test_find_year_name_type2_false() -> None:
    assert hw16.find_year_name_type1(2024, 'Sweden') == "wrong...";