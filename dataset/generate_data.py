import numpy as np
import math
import pandas

customer_segmentation = [
  [30,0,1,5, 0],
  [40,0,9,2, 1],
  [28,1,6,4, 2],
  [20,0,3,3, 3],
  [35,0,8,2, 4],
  [32,1,2,5, 5],
  [25,1,5,4, 6],
  [35,0,7,4, 7],
  [27,0,6,3, 8],
  [37,0,9,4, 9],
  [30,0,0,6, 5]
]
chosen_bikes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5]

def generate_randn_hot_number(number, classes):
  randn_number = generate_randn_number(number)
  if randn_number >= classes:
    randn_number = classes - 1
  hot_encoded_array = hot_encode(randn_number, classes)
  return hot_encoded_array

def generate_randn_number(number):
  randn_number = np.random.normal(size=1, loc=number, scale=number*0.25)
  round_randn_number = math.floor(randn_number[0])
  if round_randn_number < 0:
    round_randn_number = 0
  return round_randn_number

def hot_encode(number, classes):
  hot_encoded_array = [0 for _ in range(classes)]
  hot_encoded_array[number] = 1
  return hot_encoded_array

if __name__ == '__main__':
  expanded_data = []
  for row in customer_segmentation:
    for i in range(100):
      new_row = []
      new_row.append(generate_randn_number(row[0]))
      new_row = new_row + generate_randn_hot_number(row[1], 2)
      new_row = new_row + generate_randn_hot_number(row[2], 10)
      new_row.append(generate_randn_number(row[3]))
      new_row.append(row[4])
      expanded_data.append(new_row)
    new_row = []
    new_row.append(row[0])
    new_row = new_row + hot_encode(row[1], 2)
    new_row = new_row + hot_encode(row[2], 10)
    new_row.append(row[3])
    new_row.append(row[4])
    expanded_data.append(new_row)
  df = pandas.DataFrame.from_records(expanded_data)
  print(df.head())
  df.columns = ['edad', 'sexo_0', 'sexo_1', 'ocupacion_0', 'ocupacion_1', 'ocupacion_2', 'ocupacion_3', 'ocupacion_4', 'ocupacion_5', 'ocupacion_6', 'ocupacion_7', 'ocupacion_8', 'ocupacion_9', 'uso', 'motocicleta']
  df.to_csv('dataset.csv', index=False)