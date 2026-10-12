import matplotlib.pyplot as plt

epochs = [1, 2, 3, 4, 5]
train_loss = [1.2, 0.9, 0.7, 0.5, 0.4]
val_loss = [1.3, 1.0, 0.8, 0.9, 1.1]

plt.plot(epochs, train_loss, marker="o", label="Train Loss")
plt.plot(epochs, val_loss, marker="s", label="Validation Loss")

plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training vs Validation Loss")
plt.legend()
plt.show()