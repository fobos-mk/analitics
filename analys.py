import pandas as pd
import numpy as np

from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split


def analitics(data_array):
    data = pd.read_csv("workers_data.csv")

    x = data.drop(['died', 'worker_id', 'date'], axis=1)
    y = data['died']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42, shuffle=True)

    # обучение модели с заданными параметрами
    xgb_model = XGBClassifier(
        learning_rate=0.01,
        n_estimators=1000,
        max_depth=4,
        min_child_weight=2,
        gamma=0,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_alpha=0.005,
        objective='binary:logistic',
        nthread=4,
        scale_pos_weight=1,
        seed=27).fit(x_train, y_train)

    # воспользуемся уже обученной моделью, чтобы сделать прогнозы
    rf_predictions = xgb_model.predict(x_test)

    # создаём массив с данными, которые собираемся скормить модели для того, чтобы она предсказала выгорание
    personal_data = np.array(data_array)

    # передаём модели массив. На выходе получаем массив,
    # где первый элемент строки - вероятность не выгорания, 2 - вероятность, что выгорел
    # print(xgb_model.predict_proba(personal_data))
    return xgb_model.predict_proba(personal_data)


if __name__ == '__main__':
    analitics([[1, 2, 33, 7, 16, 5, 2, 3], [10, 6, 10, 60, 10, 5, 4, 0]])
