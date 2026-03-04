import tensorflow as tf

model = tf.keras.models.load_model("mobilenetv2_best.keras", compile=False)
model.save("model_fixed.h5")
