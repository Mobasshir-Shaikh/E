import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

(X, y), (Xt, yt) = tf.keras.datasets.mnist.load_data()

X, Xt = X/255.0, Xt/255.0

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X, y, epochs=3)
print("Accuracy:", model.evaluate(Xt, yt)[1])

p = np.argmax(model.predict(Xt[:1]), axis=1)[0]
plt.imshow(Xt[0], cmap='gray')
plt.title("Predicted Digit: " + str(p))
plt.show()