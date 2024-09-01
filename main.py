from src.controller.historicalController import HistorialSearch

if __name__ == "__main__":

    user_agent = "Mozilla/5.0 (Windows NT 5.1; rv:40.0) Gecko/20100101 Firefox/40.0"
    url = "udemy.com"

    hsearch = HistorialSearch(url, user_agent)
    hsearch.search_snapshots_by_extensions()