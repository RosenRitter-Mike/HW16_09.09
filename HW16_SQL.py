import sqlite_lib as sl

# 2.
def last_10_winners() -> None:
    sl.connect('eurv_db');

    result: list[tuple] = sl.run_query_select('''
            SELECT * FROM eurovision_winners
            ORDER BY year DESC
            LIMIT 10
        ''');

    print("Year | Country       | Winner             | Host Country    | Song Name          ");
    print("===========================================================================");
    for winner in result:
        print(f" {winner[0]:4}  {winner[1]:15}  {winner[2]:20} {winner[3]:15} {winner[4]:20}");


last_10_winners();
# 3.
# a.
def get_year_and_country() ->list[any]:
    res: list[any] =[];
    try:
        res.append(int(input("Enter year? ")));
        res.append(input("Enter country? "));
    except Exception as e:
       print(f"An {e} -- Error -- has occurred");

    return res;

def find_year_name_type1(year: int, country: str) -> str:
    sl.connect('eurv_db');

    result: list[tuple] = sl.run_query_select(f"SELECT song_name FROM eurovision_winners WHERE year = {year} "
                                              f"AND country LIKE '{country}';");

    if not len(result):
        return "wrong...";
    else:
        return f"Winning song: {result[0][0]}";

# b.
def find_year_name_type2(year: int, country: str) -> str:
    sl.connect('eurv_db');

    result = sl.run_query_select(f"SELECT * FROM eurovision_winners;");
    res = list(filter(lambda winner: winner[1] == country and winner[0] == year, result));

    if not len(res):
        return "wrong...";
    else:
        return f"Winning song: {res[0][2]}";


print(find_year_name_type1(2024, 'Switzerland'));
print(find_year_name_type1(2024, 'Sweden'));
# print(find_year_name_type2(2024, 'Switzerland'));
# print(find_year_name_type2(2024, 'Sweden'));

# 5.
def change_song_genre() -> None:
    in_list = get_year_and_country();
    res1 = find_year_name_type1(in_list[0], in_list[1]);

    if res1 == 'wrong...':
        print("wrong");
    else:
        # sl.connect('eurv_db');
        print(res1);
        current_genre = sl.run_query_select(f'SELECT genre FROM song_details WHERE year = {in_list[0]};');
        print(current_genre[0][0]);
        new_genre = input("Change genre to: ");
        if new_genre == current_genre[0][0]:
            print("enter a different genre...");
        else:
            sl.run_query_update(f"UPDATE song_details SET genre = '{new_genre}' WHERE year = {in_list[0]};")
            print("Genre updated successfully.")
            print("done...");

change_song_genre();