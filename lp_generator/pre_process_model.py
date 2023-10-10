from IModel import IModel
import json
import sys

class pre_process_model(IModel):
    def __init__(self):
        self.final_data = []

    def initialize(self, data):
        self.final_data = self.csv_reader(data)

    def run(self):
        self.write_to_json()

    def is_row_valid(self, row):
        if len(row.split(',')) != 5:
            return False
        else:
            return True

    def csv_reader(self, csv):
        data = []
        for row_number, row in enumerate(csv, start=0):
            if not self.is_row_valid(row):
                print(f"Row {row_number} is not correct, please verify and try again:\n\n{row}")
                sys.exit()
            data.append(row.split(','))  # Split by commas and append
        return data

    def write_to_json(self):
        month_dict = {'01': 'Janeiro', '02': 'Fevereiro', '03': 'Março', '04': 'Abril', '05': 'Maio', '06': 'Junho',
                      '07': 'Julho', '08': 'Agosto', '09': 'Setembro', '10': 'Outubro', '11': 'Novembro',
                      '12': 'Dezembro'}
        for index, row in enumerate(self.final_data):
            # Create a dictionary with named fields
            d, m, y = row[4].split('/')
            date = f'{y.strip()}-{m}-{d}'
            if row[1].lower() != 'agenda':
                row_dict = {
                    "link": row[0],
                    "model": row[1],
                    "name": '[' + month_dict[m][0:3].upper() + '/' + y.strip()[-2:] + '] [' + row[1] + '] [' + row[
                        3].upper() + '] PALESTRA ABERTA - AUTO',
                    "city": row[3],
                    "date": date.strip()  # remove the trailing '\n' if it's present
                }
            else:
                row_dict = {
                    "link": row[0],
                    "model": row[1],
                    "name": row[2],
                    "city": row[3],
                    "date": date.strip() # remove the trailing '\n' if it's present
                }

            filename = f"pre-models/pre-model-{row[2]}-{index}.json"  # Using the first element of the row for the filename
            with open(filename, 'w') as json_file:
                json.dump(row_dict, json_file, indent=4)