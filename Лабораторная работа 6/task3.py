OUTPUT_FILE = "output.csv"


def to_csv_file(filename, headers: list, rows: list, delimiter=",", new_line="\n") -> None:
    with open(filename, 'w') as output_file:
        for i in range(len(headers)):
            output_file.write(headers[i] + delimiter if i != len(headers)-1 else headers[i])
        output_file.write(new_line)
        for data_row in rows:
            for i in range(len(data_row)):
                output_file.write(data_row[i] + delimiter if i != len(data_row)-1 else data_row[i])
            output_file.write(new_line)


headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file(OUTPUT_FILE, headers_list, data)

with open(OUTPUT_FILE) as output_f:
    for line in output_f:
        print(line, end="")
