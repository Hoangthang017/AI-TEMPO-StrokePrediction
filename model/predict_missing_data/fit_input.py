def fit_input(input, type_pre):
  from sklearn import preprocessing
  le = preprocessing.LabelEncoder()
  input['gender'] = le.fit_transform(input['gender'])
  input['ever_married'] = le.fit_transform(input['ever_married'])
  input['work_type'] = le.fit_transform(input['work_type'])
  input['Residence_type'] = le.fit_transform(input['Residence_type'])
  input['smoking_status'] = le.fit_transform(input['smoking_status'])
  input['blood'] = le.fit_transform(input['blood'])
  input['bmi'] = input['bmi'].fillna(round (input['bmi'].median(), 2))

  if (type_pre == 'heart_disease'):
    columns = ["gender", "ever_married", "bmi", "smoking_status", "blood"]
  else:
    columns = ["smooking_status", "bmi", "blood","gender", "Residence_type"]
  return input[columns]