import Reader.myReader
from pathlib import Path

result = Reader.myReader.calcSum(3, 4)
print(result)

csv_file_path = Path(__file__).resolve().parent.parent / 'HelloWorld' / 'Data' / 'companies.csv'
file_read_result = Reader.myReader.read_file(csv_file_path)
print(file_read_result)