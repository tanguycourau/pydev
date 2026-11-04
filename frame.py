# -*-coding:utf-8 -*-
# 
import pandas as pd

index = [
    (1, 2.3, 3, 'EOC', 5),
    (1, 2.7, 3, 'FDC', 6),
]

vecteurs = [
    range(38),
    range(100, 138),
]

df = pd.DataFrame(
    vecteurs,
    index=pd.MultiIndex.from_tuples(
        index,
        names=['p1', 'p2', 'p3', 'p4', 'p5']
    ),
    columns=[f'c{i}' for i in range(38)]
)

print(df)
df.loc[(1, 2.3, 3, 'EOC',5)]
df[df.index.get_level_values('p4') == 'EOC']
