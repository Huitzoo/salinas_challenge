from sklearn.neighbors import KNeighborsClassifier
import pandas

def create_knn(inputs, labels):
  knn = KNeighborsClassifier(n_neighbors=9)
  knn.fit(inputs, labels)
  return knn

def test_model(knn):
  test_profile = [[22, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]]
  print(knn.predict(test_profile))
  print(knn.predict_proba(test_profile))

if __name__ == '__main__':
  df = pandas.read_csv('dataset.csv')
  training_df = df.iloc[:, :14]
  customer_data = training_df.to_records(index=False)
  customer_data_list = []
  for row in customer_data:
    customer_data_list.append(list(row))
  chosen_bikes = df['motocicleta'].tolist()
  knn = create_knn(customer_data_list, chosen_bikes)
  test_model(knn)