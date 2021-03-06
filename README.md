# Material Properties CNN

## Instructions

1. Download and place `DEEPstruc` folder inside this project.
2. Run `reshape.py`. A new folder called `DEEPstruc_Normalize` will be generated as output. This script takes all pictures in the original `DEEPstruc` folder and resizes them to 700 pixels wide by 450 pixels high.
3. Run `Model_Definition.py`. This is the CNN Model that will make the predictions. Currently the model is simply fit to the data and makes no predictions before being saved.
4. The model is saved in two files: `simple_model_1.json` & `simple_model_1_weights.h5`. The json file describes the shape of the model and can be retrieved using `keras.models.model_from_json`. The H5PY file contains the trained weights of the latest run and loaded using `keras.models.load_weights`