# Machine-Learning-Image-Classification-Nutrition
Machine learning with Tensoflow and Keras to identify fruit images using Flask, SQL, HTML, JavaScript, CSS, Pandas, Python, Google Colab, Tableau, JSON, API, Dashboarding, D3, and Plotly.

- - -

## Problem: How Nutritious are Fruits and Vegetables?

### Proposal:

Using Tensorflow and Keras, we will use image classifications of fruits and vegetables from the ImageNet dataset to identify the fruits/vegetables.  After identification of the fruit/vegetable, a nutrition table will display with API data pulled from the USDA Agricultural Research Service. We will also use Tableau and forms of D3 to create chart analysis of certain nutrition data that compares the 10 different common fruits and/or vegetables, such as relative sugar content.  A drop down menu will allow the user to select between different types of nutrition to look up.

An app will be created to allow an upload of a picture of a fruit or vegetable from the user.  The ultimate long term goal for the project is to be able to see a fruit in person, take a picture using a smartphone, uploading it into the app, and have the app identify the fruit with its nutrition data.

We used TensorFlow, Keras, Flask, Google Colab, Python, D3, Tableau, MatPlotLib, JavaScript, HTML, CSS, and SQL.

### The Process:

In the end result, we used 10 different fruits as a starter for the machine learning image classification process, which were apple, bananas, blueberry, fig, lemon, orange, peach, persimmon, tomato, and watermelon.

* Image sets of roughly 1000 images of each fruit was downloaded from the ImageNet using API and JDownloader 2.
* Additional images were pulled from Kaggle using the Fruits360 Dataset.
* Nutrition data was pulled from the USDA: Food Data Central using API to determine each fruits nutrition and portion size.
* The percent daily values for each fruit was taken from the FDA site in PDF form.

Using Google Colab, Jupyter Notebook, Tensorflow, and Keras, we trained the model using 100 epochs to achieve over 92% accuracy, and the model was saved as an H5 file.

For the nutrition information, data was pulled using an API in JSON format.  Pandas was used to create and clean the data-frames.  The resulting data was exported into a CSV file.

A Flask app was created to upload images, which then uses the H5 model to identify the fruit, predict the fruit name, display the nutrition table, and display a nutrition comparison chart.  The process also used JavaScript, CSS, HTML, D3, and Plotly to create the dashboard and display the results.

Tableau was used to create a summary and presentation of the process and results.

### Where main files are:

In the main fold, the <b>Fruits_Tensorflow.ipynb</b> file contains the codes for the machine learning process of the image classification.  The <b>fruits_tensorflow-100-New10-360.h5</b> file is the saved model.

The "Final" folder contains <b>app.py</b> file, which contains the codes for the dashboard, user interface, references to the HTML files, and JavaScript.  The "static" folder contains CSV data files, and JSON file.  The "templates" folder contains the HTML files, which also contains the coding for JavaScript, CSS, D3, and Plotly within the HTML files.

The Tableau folder contains the Tableau file for the presentation, charts, and graphs.

### The results:

To run the app, go to the "Final" folder, and run app.py through github bash by using the command "python app.py".  A web link will display, so copy and paste it into a web browser.  Libraries will need to be installed for flask_dropzone, flask_uploads, tkinter, PIL, numpy, and tensorflow.  In the web app, click on the drop files box and choose a fruit picture.  The model will then run and identify the fruit.  The results page will display the fruit name, nutrition data, and comparison chart.  The drop down menu can be selected to change different types of nutrition comparisons.

### Conclusion:

There is still quite a bit more that can be worked to expand the usefulness of the app.  This was a good start which was able to identify 10 different fruits; however, the ultimate goal is for the app to identify over 100 fruits and vegetables.  That will require more processing power than our personal computers or Google Colab can handle.  The next stage after that is for the app to work in smartphones.