import pandas as pd
import matplotlib.pyplot as plt

#Crear a Pandas Dataframe
data = {
    'Partidos': ['Spurs', 'Nets', 'Grizzlies', 'Bulls'],
    'Puntos': [33, 49, 35, 18],
    'Asistencias': [10, 7, 12, 10]
}
df = pd.DataFrame(data)

#Crear una line plot usando Seaborn
plt.plot(df['Partidos'], df['Puntos'])
plt.xlabel('Partifod')
plt.ylabel('Puntos')
plt.title('Puntos por Partido')
plt.show()

#Mostramos los partidos con 30 puntos o más.
treinta_puntos = df[df['Puntos'] > 30]
print(treinta_puntos)

