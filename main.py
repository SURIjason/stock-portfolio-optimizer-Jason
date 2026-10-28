from etl.extract import get_local_stock_data
from etl.transform import clean_stock_data
from etl.load import save_to_sqlite

if __name__ == "__main__":
    raw_data = get_local_stock_data()

    if raw_data.empty:
        print("No data to process. Exiting.")
        exit()

    clean_data = clean_stock_data(raw_data)
    save_to_sqlite(clean_data)

    print("ETL pipeline completed using local dataset.")
