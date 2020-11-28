import pandas as pd
import numpy as np
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# здесь должно быть подключение к серверу с выводом столбцов


pgi_train_param = np.array()
ship_train_param = np.array()
sku_train_param = np.array()
vol_train_param = np.array()
dis_train_param = np.array()
wd_train_param = np.array()
nd_train_param = np.array()

data_train ={   'PGI_DATE': pgi_train_param,
                'SHIP_TO': ship_train_param,
                'SKU': sku_train_param,
                'DISCOUNT': dis_train_param,
                'WD': wd_train_param,
                'ND': nd_train_param,
                'VOL': vol_train_param
}

df = pd.DataFrame(data_train)

# Числовые признаки
num_cols = [
    'DISCOUNT',
    'WD',
    'ND',
]

# Категориальные признаки
cat_cols = [
    'PGI_DATE',
    'SHIP_TO',
    'SKU'
]

# Список всех признаков
feature_cols = num_cols + cat_cols

# Целевая переменная
target_col = 'VOL'


# Создаем данные для обучения без столбца с целевой переменной
X_origin = df.iloc[:,:-1]
y = df[target_col]

# Сплитим данные на тест и треин для обучения и проверки
X_train_origin, X_test_origin, y_train_origin, y_test_origin = train_test_split(X_origin, y, test_size=0.2, random_state=42)

# Создаем модель
boosting_model = CatBoostRegressor(cat_features = cat_cols)
# Обучаем модель
boosting_model = boosting_model.fit(X_train_origin, y_train_origin)
# считам ошибку
error = mean_squared_error(y_test_origin, boosting_model.predict(X_test_origin))

best_model = boosting_model










