# taken from
# https://www.tensorflow.org/tutorials/estimator/linear
# also used on
# https://www.freecodecamp.org/learn/machine-learning-with-python/tensorflow/core-learning-algorithms-the-training-process
# for
# https://colab.research.google.com/drive/15Cyy2H7nT40sGR7TBN5wBvgTd57mVKay#scrollTo=OO0mBu_WaVXp

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import clear_output
from six.moves import urllib

import tensorflow.compat.v2.feature_column as fc

import tensorflow as tf

# Load dataset.
dftrain = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/train.csv') # training data
dfeval = pd.read_csv('https://storage.googleapis.com/tf-datasets/titanic/eval.csv') # testing data
#print(dftrain.head())
y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')
#dftrain.age.hist(bins=20)
#dftrain.sex.value_counts().plot(kind='barh')
#plt.show()

CATEGORICAL_COLUMNS = ['sex', 'n_siblings_spouses', 'parch', 'class', 'deck',
                       'embark_town', 'alone']
NUMERIC_COLUMNS = ['age', 'fare']

feature_columns = []

# print(">>> Unique sex columns")
# print(dftrain['sex'].unique())
# print(">>> Unique embark_town columns")
# print(dftrain['embark_town'].unique()) 
for feature_name in CATEGORICAL_COLUMNS:
  vocabulary = dftrain[feature_name].unique()  # gets a list of all unique values from the given categorical column
  feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
  feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))

#print(feature_columns)

def make_input_fn(data_df, label_df, num_epochs=10, shuffle=True, batch_size=32):
  def input_function():
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
    if shuffle:
      ds = ds.shuffle(1000)
    ds = ds.batch(batch_size).repeat(num_epochs)
    return ds
  return input_function

train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

# After adding all the base features to the model, let's train the model. 
# Training a model is just a single command using the tf.estimator API:

# Derived Feature Columns
# Now you reached an accuracy of 75%. Using each base feature column separately 
# may not be enough to explain the data. For example, the correlation between 
# age and the label may be different for different gender.
# Therefore, if you only learn a single model weight for gender="Male" and 
# gender="Female", you won't capture every age-gender combination 
# (e.g. distinguishing between gender="Male" AND age="30" 
# AND gender="Male" AND age="40").

# To learn the differences between different feature combinations, 
# you can add crossed feature columns to the model 
# (you can also bucketize age column before the cross column):
age_x_gender = tf.feature_column.crossed_column(['age', 'sex'], hash_bucket_size=100)

derived_feature_columns = [age_x_gender]
linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns+derived_feature_columns)
linear_est.train(train_input_fn)

# Now let's evaluate the model. We will evaluate it on the training data for now.
result = list(linear_est.evaluate(eval_input_fn))
# print(result)
#print(result['accuracy'])

# Since the model is trained, let's do some predictions now.
# clear_output()
result = list(linear_est.predict(eval_input_fn))
# Let's look at the first prediction:
print(dfeval.loc[0])
print(result[0]['probabilities'])
# Let's look at the second prediction:
print(dfeval.loc[1])
print(result[1]['probabilities'])
# Let's look at the third prediction:
print(dfeval.loc[2])
print(result[2]['probabilities'])
# Let's look at the fourth prediction:
print(dfeval.loc[3])
print(result[3]['probabilities'])

clear_output()

