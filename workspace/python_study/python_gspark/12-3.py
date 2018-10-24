import csv

def read_car():
    f = open('data/cars.csv', 'r')
    rows = []
    for row in f:
        rows.append(row.strip().split(','))
    f.close()
    return rows


def write_car(rows):
    f = open('data/car_w.txt', 'w', newline='')
    writer = csv.writer(f, delimiter=':') # delimiter(구분자)를 콜론 :으로 준다.
    for row in rows:
        writer.writerow(row)
    f.close()

mycar = read_car()
write_car(mycar)