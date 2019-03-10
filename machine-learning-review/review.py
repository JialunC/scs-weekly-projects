
# coding: utf-8

# # Python Data Science Handbook - Chapter 5

# ## 05.01

# - Fundamentally, machine learning involves building mathematical models to help understand data.

# - "Learning" enters the fray when we give these models tunable parameters that can be adapted to observed data; in this way the program can be considered to be "learning" from the data.

# - **Supervised** learning involves somehow modeling the relationship between measured features of data and some label associated with the data; once this model is determined, it can be used to apply labels to new, unknown data.

#     - This is further subdivided into classification tasks and regression tasks

#     - In classification, the labels are discrete categories, while in regression, the labels are continuous quantities. 

# - **Unsupervised** learning involves modeling the features of a dataset without reference to any label, and is often described as "letting the dataset speak for itself." 

#     - These models include tasks such as clustering and dimensionality reduction

#     - Clustering algorithms identify distinct groups of data, while dimensionality reduction algorithms search for more succinct representations of the data.

# - **Classification**: Predicting discrete labels

# - **Regression**: Predicting continuous labels

# - **Clustering**: Inferring labels on unlabeled data

# - **Dimensionality reduction**: Inferring structure of unlabeled data

#     - In dimensionality reduction, labels or other information are inferred from the structure of the dataset itself

#     - Models that detect and identify lower-dimensional structure in higher-dimensional data

# ## 05.02 - Scikit-Learn

# In[3]:


import seaborn as sns
iris = sns.load_dataset('iris')
iris.head()


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns; sns.set()
sns.pairplot(iris, hue='species', size=1.5);


# Features matrix

# In[8]:


X_iris = iris.drop('species', axis=1)
X_iris.head()


# Target array

# In[11]:


y_iris = iris['species']
y_iris.head()


# ### Scikit-Learn's Estimator API

# ### Basics of the API
# 
# Most commonly, the steps in using the Scikit-Learn estimator API are as follows
# 
# 1. Choose a class of model by importing the appropriate estimator class from Scikit-Learn.
# 2. Choose model hyperparameters by instantiating this class with desired values.
# 3. Arrange data into a features matrix and target vector following the discussion above.
# 4. Fit the model to your data by calling the ``fit()`` method of the model instance.
# 5. Apply the Model to new data:
#    - For supervised learning, often we predict labels for unknown data using the ``predict()`` method.
#    - For unsupervised learning, we often transform or infer properties of the data using the ``transform()`` or ``predict()`` method.
# 
# We will now step through several simple examples of applying supervised and unsupervised learning methods.

# ### Supervised learning example: Simple linear regression

# In[13]:


import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);


# #### 1. Choose a class of model

# In[14]:


from sklearn.linear_model import LinearRegression


# #### 2. Choose model hyperparameters
# 
# An important point is that *a class of model is not the same as an instance of a model*.
# 
# Once we have decided on our model class, there are still some options open to us.
# Depending on the model class we are working with, we might need to answer one or more questions like the following:
# 
# - Would we like to fit for the offset (i.e., *y*-intercept)?
# - Would we like the model to be normalized?
# - Would we like to preprocess our features to add model flexibility?
# - What degree of regularization would we like to use in our model?
# - How many model components would we like to use?
# 
# These are examples of the important choices that must be made *once the model class is selected*.
# These choices are often represented as *hyperparameters*, or parameters that must be set before the model is fit to data.
# 
# In Scikit-Learn, hyperparameters are chosen by passing values at model instantiation.
# 
# For our linear regression example, we can instantiate the ``LinearRegression`` class and specify that we would like to fit the intercept using the ``fit_intercept`` hyperparameter:

# In[15]:


model = LinearRegression(fit_intercept=True)
model


# #### 3. Arrange data into a features matrix and target vector
# 
# Previously we detailed the Scikit-Learn data representation, which requires a two-dimensional features matrix and a one-dimensional target array.
# 
# Here our target variable ``y`` is already in the correct form (a length-``n_samples`` array), but we need to massage the data ``x`` to make it a matrix of size ``[n_samples, n_features]``.
# In this case, this amounts to a simple reshaping of the one-dimensional array:

# In[21]:


X = x[:, np.newaxis]
X.shape


# #### 4. Fit the model to your data
# 
# This can be done with the ``fit()`` method of the model:

# In[22]:


model.fit(X, y)


# This ``fit()`` command causes a number of model-dependent internal computations to take place, and the results of these computations are stored in model-specific attributes that the user can explore.
# 
# In Scikit-Learn, by convention all model parameters that were learned during the ``fit()`` process have trailing underscores; for example in this linear model, we have the following:

# In[23]:


model.coef_


# In[24]:


model.intercept_


# #### 5. Predict labels for unknown data
# 
# Once the model is trained, the main task of supervised machine learning is to evaluate it based on what it says about new data that was not part of the training set.
# In Scikit-Learn, this can be done using the ``predict()`` method.
# For the sake of this example, our "new data" will be a grid of *x* values, and we will ask what *y* values the model predicts:
