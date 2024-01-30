# Text Classification using logistic regression and SVM (Support Vector Machine)
In this project I have developed two models, one using logistic regression and other using SVM. As the F1 score for both the models are similar I have chosen logistic regression as the model to integrate with the REST API. Fast API is used to create REST API end points and also a simple html page is developed creating an entire workflow utilising the model.

Logistic regression works well with text data, especially when it is represented using approaches such as TF-IDF. It makes a good starting point for evaluating advanced models. If logistic regression works well, it can be used as a benchmark to compare the performance of advanced models. 

SVMs perform well when the data is linearly separable, and their goal is to locate the hyperplane that optimally separates the classes in the feature space. In many circumstances, even if the original feature space is multidimensional, the data can be successfully split by a hyperplane.

## Project Structure

The entire project structure is described as well as displayed below.

```
│   .gitignore
│   Dockerfile              - configuration file for docker
│   main.py                 - main application file
│   ReadMe.md
│   req.txt                 - list of required modules
│
├───Ml
│       logreg.ipynb        -  Logistic regression model file 
│       sample_data.csv 
│       Svm.ipynb           - SVM model file
│       preprocessor.py     - Reusable preprocessing funtions
│
├───UI
│       front-end.html      - html file for manual testing
├───images
│       output.png          - example of the frontend view

```
## Instructions

- Build the docker image - replace the {image_name} as required 
```
docker build -t {image_name} .
```
- Run the Docker image
```
docker run -p 8000:8000 {image_name}
```

- Once the server is up try localhost:8000, this will return {Hello: World}. Proving that the image is up and running

- Now open the 'UI/front-end.html' file to test the strings manually

### How to use the frontend

- __Output__ - a text field for displaying the predictions
- __Input__ - dynamic number of text fields for inputing the search queries as well as a button to add more text fields
- __Submit__ - a submit button which calls the API end point, predicting using the logistic regression model.

![output](/images/output.png)

## Future Scope

Currently working on integrating different text embeddings for text classification instead of TF-IDF Vectorization, which was also part of the requirements as an optional / plus feature. If time allows this could also be completed by time.