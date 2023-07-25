import numpy as np


class Param_calculator:
    """Расчёт показателей по строчкам, соответствющим конкретному набору месторождение-вид ГРП"""

    def __init__(self, method, param, df, start_column):
        """
        :param method: методика подсчёта
        :param param: показатель для расчёта
        :param df: датафрейм
        :param start_column: индекс колонки для старта
        """
        self.param = param
        self.start_column = start_column
        self.info_dict = self.info_dict_maker(df)
        if method == 0:
            self.y, self.x = self.avereger()
        else:
            self.y, self.x = self.summer()

    def info_dict_maker(self, df):
        """
        Фильтрация датафрейма по показателю
        :param df: датафрейм
        :return: отфильтрованный датафрейм
        """
        info_dict = df[(df['показатель'] == self.param)].reset_index()
        return info_dict

    def summer(self):
        """
        Массив с суммой по столбцам по каждому году
        :return: массив с суммами, года
        """
        info = []
        years = []
        for i in range(self.start_column + 1, len(self.info_dict.axes[1])):
            df = self.info_dict.iloc[:, i].replace(0, np.nan).dropna()
            info.append(df.sum())
            years.append(self.info_dict.columns.tolist()[i])
        return info, years

    def avereger(self):
        """
        Массив со средними знаечениями по столбцам по каждому году
        :return: массив со средними, года
        """
        info = []
        years = []
        for i in range(self.start_column + 1, len(self.info_dict.axes[1])):
            df = self.info_dict.iloc[:, i].replace(0, np.nan).dropna()
            if len(df) != 0:
                mean_without_zeros = df.mean()
                info.append(mean_without_zeros)
            else:
                info.append(0)
            years.append(self.info_dict.columns.tolist()[i])
        return info, years
