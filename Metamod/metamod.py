import torch
import torch.nn as nn
import torch.optim as optim

# --------------------------------------------------
# Données d'exemple
# --------------------------------------------------
n_samples = 1000

# 5 paramètres d'entrée
X = torch.rand(n_samples, 5)

# Fonction simulant un modèle coûteux
Y = torch.zeros(n_samples, 38)

for i in range(38):
    Y[:, i] = (
        torch.sin((i+1) * X[:, 0])
        + X[:, 1]**2
        - 0.5 * X[:, 2]
        + 0.1 * i * X[:, 3]
        + torch.exp(-X[:, 4])
    )

# --------------------------------------------------
# Métamodèle
# --------------------------------------------------
class MetaModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Linear(5, 64),
            nn.ReLU(),
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 38)
        )

    def forward(self, x):
        return self.net(x)

model = MetaModel()

# --------------------------------------------------
# Apprentissage
# --------------------------------------------------
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

n_epochs = 500

for epoch in range(n_epochs):

    optimizer.zero_grad()

    y_pred = model(X)

    loss = criterion(y_pred, Y)

    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"epoch={epoch:4d} loss={loss.item():.6f}")

# --------------------------------------------------
# Test
# --------------------------------------------------
x_new = torch.tensor([[0.3, 0.5, 0.7, 0.2, 0.9]])

with torch.no_grad():
    y_new = model(x_new)

print(y_new.shape)
print(y_new)
