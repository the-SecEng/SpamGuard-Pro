# SpamGuard Pro

SpamGuard Pro is a sophisticated spam detection prototype leveraging machine learning techniques with scikit-learn and Python. This project serves as a foundational reference for those interested in developing advanced spam detection systems.

## Screenshot

![SpamGuard Pro Screenshot](https://github.com/goktugerol-dev/SpamGuard-Pro/raw/master/screenshot/screenshot.png)

## Project Overview

The project comprises two primary Python scripts:

1. **`load_dataset.py`**
   - Initializes the project by loading the SMS Spam Collection dataset into a pandas DataFrame.
   - Dataset: [SMS Spam Collection Dataset](https://archive.ics.uci.edu/ml/datasets/sms+spam+collection)
   - Location: `./datasets/SMSSpamCollection`

2. **`spam_detection_model.py`**
   - Implements a robust spam detection model utilizing the Multinomial Naive Bayes classifier.
   - Employs the CountVectorizer from scikit-learn for feature extraction, transforming text messages into a numerical format.
   - Trains the model on a training subset (`X_train` and `y_train`) and evaluates its performance on a test subset (`X_test`).
   - Presents accuracy, confusion matrix, and classification report as key metrics.

## How to Run

1. Open a terminal or command prompt.
2. Navigate to the project's root directory.
3. Execute the following commands:
   - `python load_dataset.py`
   - `python spam_detection_model.py`

## Dependencies

- Python 3.x
- pandas
- scikit-learn

Install dependencies using:
```bash
pip install pandas scikit-learn
```


# Machine Learning Technology

This project harnesses machine learning technology for spam detection:

 - ## Feature Extraction:
- Utilizes the CountVectorizer to convert text messages into a numerical format, creating a matrix of word counts.

- Machine Learning Model:
        Employs the Multinomial Naive Bayes classifier, a powerful algorithm for text classification tasks.

- Training and Prediction:
        Trains the model on a subset of the SMS Spam Collection dataset and evaluates its performance on a separate subset.

- Evaluation Metrics:
        Presents accuracy, confusion matrix, and classification report as essential metrics for assessing model performance.

# License

This project is shared under the **GNU General Public License v3.0**.

### Note

- This project is designed as a foundational reference and is not intended for production use. It provides a starting point for the development of more advanced spam detection systems.

- Feel free to explore, modify, and use the code according to the terms of the GPL-3.0 license.