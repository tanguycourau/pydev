# -*-coding:utf-8 -*-
import numpy as np
"""
Oui. La SVD (Singular Value Decomposition) est particulièrement intéressante pour les données météorologiques car elle est souvent plus robuste que l'ACP classique lorsque l'on manipule de grands champs spatiaux.

Mathématiquement :

X=UΣVᵀ 

où :

U contient les modes temporels,
Σ (Sigma) contient les valeurs singulières,
Vᵀ contient les modes spatiaux,
les plus grandes valeurs singulières représentent l'essentiel de l'information.
"""
# Données
# Supposons un jeu de données de 6 observations et 4 variables :
X = np.array([
    [2.5, 2.4, 1.0, 0.5],
    [0.5, 0.7, 0.3, 0.2],
    [2.2, 2.9, 1.2, 0.7],
    [1.9, 2.2, 1.1, 0.4],
    [3.1, 3.0, 1.5, 0.9],
    [2.3, 2.7, 1.3, 0.6]
])

# Centrage
Xc = X - np.mean(X, axis=0)

print("Matrice centrée:")
print(Xc)

# Décomposition SVD
U, S, VT = np.linalg.svd(Xc, full_matrices=False)

print("\nU :")
print(U)

print("\nValeurs singulières :")
print(S)

print("\nVT :")
print(VT)

## Les valeurs singulières permettent de calculer l'équivalent de la variance expliquée de l'ACP :
variance = S**2

explained_variance_ratio = variance / np.sum(variance)

print("\nVariance expliquée :")
for i, r in enumerate(explained_variance_ratio):
    print(f"Composante {i+1}: {100*r:.2f}%")



## Reduction de dimension

k = 2

U_k = U[:, :k]
S_k = np.diag(S[:k])

X_reduit = U_k @ S_k

print(X_reduit)


## Reconstruction

VT_k = VT[:k, :]

X_approx = U_k @ S_k @ VT_k

# Remettre la moyenne
X_approx += np.mean(X, axis=0)

print("\nMatrice reconstruite :")
print(X_approx)
