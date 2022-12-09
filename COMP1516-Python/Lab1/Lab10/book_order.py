# Aline Hammermuller
# A01276569

import sys
import book_order_utils

def main():
    try:
        if len(sys.argv) != 8:
            print("Invalid number of arguments")
            exit(0)

        order_num = sys.argv[1]
        title = sys.argv[2]
        author = sys.argv[3]
        isbn = sys.argv[4]
        year = sys.argv[5]
        quantity = sys.argv[6]
        cost = sys.argv[7]

        book_order_utils.validate_book_order_details(order_num, title, author, isbn, year, quantity, cost)
        unit_cost = book_order_utils.calculate_per_book_cost(float(cost), int(quantity))
        book_order_utils.write_book_order_details(order_num + ".txt", title, author, isbn, year, quantity, cost, unit_cost)

    except ValueError as e:
        print(f'Value Error: {e}')
    except TypeError as e:
        print(f'Type Error: {e}')
    except ZeroDivisionError:
        print("No Books in Order")


if __name__ == '__main__':
    main()