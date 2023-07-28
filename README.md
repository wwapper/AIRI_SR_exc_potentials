# AIRI_SR_exc_potentials
Репозиторий проекта "Аппроксимация обменно-корреляционных функционалов в квантовой химии математическими выражениями с помощью символьной регрессии", выполненного в рамках летней школы AIRI

_Авторы: Ким Павел, Кулаев Кирилл_</br>
_Куратор: Рябов Александр_


Репозиторий состоит из папок, каждая из которых содержит в себе файл .ipynb и опционально дополнительные файлы, необходимые для корректного запуска кода в jupyter-файле.</br>

**ВАЖНО**</br>
В силу большого числа зависимостей при установке пакетов, **настоятельно рекомендуется запускать .ipynb файлы в среде Google Colab, дополнительные файлы (при наличии) копировать из папки в директорию /content**. Только так авторы могут гарантировать воспроизводимость полученных результатов.</br>

<h2>Структура репозитория:</h2></br>

- Директория _"GA символьная ререссия"_ содержит часть работы, посвященной изучению возможностей генетического алгоритма для решения задач символьной регрессии
  - Директория _"GA предсказание формул известных потенциалов"_ содержит используемые в коде датасеты и .ipynb файл, код в котором решает задачу символьной регрессии с помощью генетического алгоритма для уже известных функционалов в приближении LDA: lda_x, lda_c_chachiyo, lda_c_pw_mod.
  - Директория _"GA предсказание формулы нейросетевого потенциала"_ содержит используемый в коде датасет и .ipynb файл, код в котором решает задачу символьной регрессии с помощью генетического алгоритма для нейросетевого обменно-корреляционного функционала, аналитический вид которого неизвестен.

- Директория _"Meta NN символьная регрессия"_ содержит часть работы, посвященной изучению возможностей нейронной сети-трансформера от Meta для решения задач символьной регрессии
  - Директория _"NN предсказание формул известных потенциалов"_ содержит используемые в коде датасеты и .ipynb файл, код в котором решает задачу символьной регрессии с помощью нейросети-трансформера для уже известных функционалов в приближении LDA: lda_x, lda_c_chachiyo, lda_c_pw_mod.
  - Директория _"NN предсказание формулы нейросетевого потенциала"_ содержит используемый в коде датасет и .ipynb файл, код в котором решает задачу символьной регрессии с помощью нейросети-трансформера для нейросетевого обменно-корреляционного функционала, аналитический вид которого неизвестен.

- Директория _Генерация потенциалов_ содержит часть работы по генерации используемых датасетов (.csv файлов).
  - Директория _Генерация известных потенциалов_ содержит .ipynb файл с кодом для расчета известных обменно-крреляционных потенциалов (lda_x, lda_c_chachiyo, lda_c_pw_mod) с помощью пакета pycsf на процедурно сгенерированных значениях электронной плотности и используемый для расчетов электронной плотности атома ртути UGBS базис. Результат выполнения кода - список директорий, в каждой из которых содержится четыре .csv файла (две колонки: x_0 - электронная плотность, y - расчитанный обменно-корреляционный потенциал) - трейн и тест для первого эксперимента (_first-файлы, значения электронной плотности от 0 до 1000), и трейн и тест датасет для второго эксперимента (_second-файлы, значения электронной плотности от 0 до 1000000 ).
  - Директория _Генерация нейросетевого потенциала_ содержит .ipynb файл с кодом для расчета нейросетевого обменно-корреляционного потенциала неизвестного аналитического вида на рассчитанных для молекулы воды значениях электронной плотности, а также ряд необходимых для корректной работы кода файлов. Результат выполнения кода - .csv файл (две колонки: x_0 - электронная плотность, y - расчитанный обменно-корреляционный потенциал) с генерированными нейросетью данными.

- Директрия _Референсная энергия_ содержит .ipynb файл для расчета референсного значения энергии молекулы воды, используя обменно-корреляционный функционал lda_x+lda_c_chachiyo, посчитанный с помощью программного пакета pycsf.

- Директория _Сравнение энергий полученных функционалов_ содержит .ipynb файл с кодом для вычисления энергии молекулы воды с использованием разных обменно-корреляционных потенциалов (нейросетевой, взятый из работы https://github.com/ml-electron-project/NNfunctional/tree/master; lda_x+lda_c_chachiyo из Meta NN символьной регрессии; lda_x+lda_c_chachiyo из GA символьной регрессии; нейросетевой из Meta NN символьной регрессии и нейросетевой из GA символьной регрессии. Также в директории находятся файлы LSDA_*.py с кодом для непосредственно расчетов энергии, а также ряд других файлов, необходимых для корректной работы кода.

<h2>Прямые ссылки на ноутбуки Google Colab:</h2></br>
- GA предсказание формул известных потенциалов <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/GA%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F/GA%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%20%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2/GA%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%20%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- GA предсказание формулы нейросетевого потенциала <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/GA%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F/GA%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%B0/GA%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%B0.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- NN предсказание формул известных потенциалов <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/Meta%20NN%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F/NN%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%20%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2/NN_%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- NN предсказание формулы нейросетевого потенциала <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/Meta%20NN%20%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F%20%D1%80%D0%B5%D0%B3%D1%80%D0%B5%D1%81%D1%81%D0%B8%D1%8F/NN%20%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%B0/NN_%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5_%D1%84%D0%BE%D1%80%D0%BC%D1%83%D0%BB%D1%8B_%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE_%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%B0_ipynb_.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- Генерация_известных_потенциалов <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D0%B8%D0%B7%D0%B2%D0%B5%D1%81%D1%82%D0%BD%D1%8B%D1%85_%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- Генерация нейросетевого потенциала <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%BE%D0%B2/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE%20%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%B0/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F_%D0%BD%D0%B5%D0%B9%D1%80%D0%BE%D1%81%D0%B5%D1%82%D0%B5%D0%B2%D0%BE%D0%B3%D0%BE_%D0%BF%D0%BE%D1%82%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D0%B0_ipynb_.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- Референсная энергия <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/%D0%A0%D0%B5%D1%84%D0%B5%D1%80%D0%B5%D0%BD%D1%81%D0%BD%D0%B0%D1%8F%20%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B8%D1%8F/%D0%A0%D0%B5%D1%84%D0%B5%D1%80%D0%B5%D0%BD%D1%81%D0%BD%D0%B0%D1%8F_%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B8%D1%8F.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>
- Сравнение полученных функционалов <a target="_blank" href="https://colab.research.google.com/github/wwapper/AIRI_SR_exc_potentials/blob/master/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5%20%D1%8D%D0%BD%D0%B5%D1%80%D0%B3%D0%B8%D0%B9%20%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D1%85%20%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%BE%D0%B2/%D0%A1%D1%80%D0%B0%D0%B2%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5_%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%BD%D1%8B%D1%85_%D1%84%D1%83%D0%BD%D0%BA%D1%86%D0%B8%D0%BE%D0%BD%D0%B0%D0%BB%D0%BE%D0%B2.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a></br>

<h2>Используемые в работе репозитории:</h2></br>

- https://github.com/facebookresearch/symbolicregression/tree/main - нейросеть-трансформер от Meta для решения задачи символьной регрессии;
- https://github.com/trevorstephens/gplearn - генетический алгоритм для решения задачи символьной регрессии;
- https://github.com/ml-electron-project/NNfunctional/tree/master - работа с вычисленным нейросетевым обменно-корреляционным потенциалом.
