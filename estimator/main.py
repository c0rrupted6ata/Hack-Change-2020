from package_1.module import best_model
import pandas as pd
import numpy as np

# здесь должно быть подключение к серверу с выводом столбцов
#Сначала нужно подключиться к sql таблице и выгрузить данные строками,
# затем стоит сделать преобразование данных в списки
# В случае если данные выглядят как списки, то перекастуйте их нужные типы после преобразования в нампай массив
# преобразование делается через метод .astype(float)


pgi_param = np.array()
ship_param = np.array()
sku_param = np.array()
#vol_param = np.array()
dis_param = np.array()
wd_param = np.array()
nd_param = np.array()

# Создаем таблицу данных

data ={         'PGI_DATE': pgi_param,
                'SHIP_TO': ship_param,
                'SKU': sku_param,
#                'VOL': vol_param,
                'DISCOUNT': dis_param,
                'WD': wd_param,
                'ND': nd_param,
}

df_test = pd.DataFrame(data)

X = df_test


# Предсказываем значения
y_pred = best_model.predict(X)

# Записываем данные в таблицу
data['VOL'] = y_pred

# Создаем эксель файл с данными и предсказаниями в папке проекта
data.to_csv('./submission.csv',index = False)