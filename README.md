# INF8801A Projet
Here you will find a (partial) reimplementation of the article [Face Sketch Recognition](https://www.ee.cuhk.edu.hk/~xgwang/papers/wangTcsvt04.pdf) written by Xiaoou Tang and Xiaogang Wang in 2004.

It also features an implementation of a GAN in order to compare performances.

## Repo organisation
### Files
On the root folder you will find the main notebooks used for our code.
- `implementation.ipynb` is the code containing the article implementation and the comparison with AI model.
- `Pix2Pix.ipynb` contains the implementation of a GAN for sketch recognition.
- `plots.ipynb` contains the code used to generate some plots for our presentation.
- `data-treat.py` is a script used to rename the files in order to ease the link between photos and sketches files.

### Get the data
You can get the dataset on Kaggle [here](https://www.kaggle.com/datasets/arbazkhan971/cuhk-face-sketch-database-cufs).

It is expected for the data to be in a `data/` folder at the root of the project. Only the `photos/` and `sketches/` folder will be of use.

**Important:** To run the notebooks, you'll need to execute the `dat-treat.py` script in order to rename the files so that they'll work correctly with the rest.

## Requirements
Having a python install working. A conda environment have been used for the run of the notebooks using python 3.11.8.

The necessary python packages are listed in `requirements/txt`. You can install them via
```bash
pip install -r requirements.txt
```
