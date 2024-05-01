class MyOldReport:
    def __init__(self, data: dict) -> None:
        self.data = data
    
    
class MyNewReport:
    def __init__(self, data: list) -> None:
        self.data = data


old_data = {
    "1": "One",
    "2": "Two"}

new_data = ["Three", "Four"]


class OldToNewReportAdapter:
    @staticmethod
    def adapter(old_report: MyOldReport) -> MyNewReport:
        old_list_data = list(old_report.data.values())
        new_report = MyNewReport(old_list_data)
        return new_report


old_report = MyOldReport(old_data)

new_report = OldToNewReportAdapter.adapter(old_report)


print(new_report.data)