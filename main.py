
from data_fetch import pull_data

from data_fetch import get_quote  #, pull_data_from_storage
# from db_tools import dbControl, build_tables, write_quote


def main():
    data = pull_data("PICLE", "OFFICE", 1)   # "PICLE" "FILE" / "OFFICE" "HOME"
    print(data)
    for row in range(1, data.row_max+1):
        quote = get_quote(row, data)
        print(row, quote)

    # x = dbControl("quote.sqlite")
    # with x as db:
    #     build_tables(db)
    #     for row in range(1, data.row_max + 1):  # data.row_max + 1
    #         quote: tuple = get_quote(row, data)
    #         write_quote(quote, db)
    #
    #     # write_quote(test_quote[0], db)
    #     # write_quote(test_quote[1], db)
    #     x.inform_db()


if __name__ == "__main__":
    print(f"main -->> dir() ={[x for x in dir() if x[:2] != '__']}")
    main()
