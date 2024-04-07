from datetime import datetime, date, timedelta
from src.master import run_etl

# define current date
current_date = datetime.now().date()
to_date = current_date.strftime('%Y-%m-%d')

# define previous date
previous_date = current_date - timedelta(days=1)
from_date = previous_date.strftime('%Y-%m-%d')

if __name__ == "__main__":
    run_etl("postgresql://postgres:postgres@localhost", from_date, to_date, 1000) 
 
