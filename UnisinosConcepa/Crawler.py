from concepa_dataset_builder import ByDateDatasetBuilder
from Concepa import Concepa
from datetime import datetime
from datetime import timedelta

def CrawlerByDate(startDate: datetime, endDate: datetime):
    days_between = endDate.__sub__(startDate).days
    if (not days_between > 0):
        raise Exception(
            "Dates in wrong format or order. Should have at least one day between the dates.")

    with ByDateDatasetBuilder() as persister:
        for days in range(0, days_between):
            query_date = startDate + timedelta(days=days)
            concepa = Concepa()
            response = concepa.GetByDate(302, query_date)
            persister.Save(response.ToCsv())

if __name__ == "__main__":
    #a = GetByDate(302, '26/04/2018')
    # print(a)
    CrawlerByDate(datetime(2018, 2, 1), datetime(2018, 5, 1))
