# class Report: <- bad pattern
#     def __init__(self, data: str):
#         self.data = data
#
#     def generate(self):
#         return f"Report {self.data}"
#
#     def save_to_file(self, filename):
#         with open(filename, "w") as file:
#             file.write(self.generate())

class Report:
    def __init__(self, data: str):
        self.data = data

    def generate(self):
        return f"Raport {self.data}"

class ReportSaver:
    def save_to_file(self, report: Report, filename: str):
        with open(filename, "w") as file:
            file.write(report.generate())


report_1 = Report("sdfgsghdfghfsdghdsfgsdf")
report_2 = Report("gsdrfdrfshdcvbgghdxgfhgdhdghdfghd")

report_saver = ReportSaver()

report_saver.save_to_file(report_1, "report1.txt")
report_saver.save_to_file(report_2, "report2.txt")