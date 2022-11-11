
import utilities_sets
import utilities_dict


def main():
    set1 = {'apple', 'banana', 'orange', 'peach'}
    set2 = {'banana', 'pineapple', 'peach', 'watermelon'}
    canada_countries_and_capitals = {"Ontario": "Toronto",
                                     "Quebec": "Quebec City",
                                     "Nova Scotia": "Halifax",
                                     "Manitoba": "Winnipeg",
                                     "New Brunswick": "Fredericton",
                                     "British Columbia": "Victoria",
                                     "Saskatchewan": "Regina",
                                     "Prince Edward Island": "Charlottetown",
                                     "Alberta": "Edmonton",
                                     "Newfoundland and Labrador": "St. John's"}

    canada = {"alberta": {"capital": "edmonton", "largest": "calgary", "population": 4262635},
              "british columbia": {"capital": "victoria", "largest": "vancouver", "population": 5000879},
              "manitoba": {"capital": "winnipeg", "largest": "winnipeg", "population": 1342153},
              "newfoundland and labrador": {"capital": "st. john's", "largest": "st. john's", "population": 510550},
              "new brunswick": {"capital": "fredericton", "largest": "moncton", "population": 775610},
              "nova scotia": {"capital": "halifax", "largest": "halifax", "population": 969383},
              "ontario": {"capital": "toronto", "largest": "toronto", "population": 14223942},
              "prince edward island": {"capital": "charlottetown", "largest": "charlottetown", "population": 154331},
              "quebec": {"capital": "quebec city", "largest": "montreal", "population": 8501833},
              "saskatchewan": {"capital": "regina", "largest": "saskatoon", "population": 1132505}}

    utilities_sets.get_total_items(set1)
    utilities_sets.display_all_items(set1)
    utilities_sets.add_item("cantaloupe", set1)
    utilities_sets.remove_item("cantaloupe", set1)
    utilities_sets.get_the_union_of(set1, set2)
    utilities_dict.display_all(canada_countries_and_capitals)
    utilities_dict.get_capital_city("Ontario", canada_countries_and_capitals)
    utilities_dict.add_element("Yukon", "Whitehorse", canada_countries_and_capitals)
    utilities_dict.remove_item("Yukon", canada_countries_and_capitals)
    utilities_dict.get_total_population(canada)
    utilities_dict.get_another_capital_city("alberta", canada)
    utilities_dict.get_largest_city("new brunswick", canada)
    utilities_dict.get_smallest_province(canada)
    utilities_dict.get_largest_province(canada)
    utilities_dict.get_province_description("manitoba", canada)


if __name__ == "__main__":
    main()
