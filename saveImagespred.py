mc2=mc.Modelsc()
model2=mc2.Autoencoder()

# Display model summary
model2.summary()
model2.fit(train_generator, epochs=1, validation_data=validation_generator)

loss = model2.evaluate(validation_generator)
print("Test loss: ", loss)

generated_images = model2.predict(validation_generator,verbose=2)
print(generated_images.shape)
# plt.imshow(generated_images[0])
# plt.show()
# Resize and convert autoencoded images to RGB
plt.figure(figsize=(20, 4))
generated_images_resized = tf.image.resize(generated_images, (224, 224))
generated_images_resized=generated_images_resized.numpy()
print(generated_images_resized.shape)
# plt.imshow(generated_images_resized[0])
# plt.show()



# Loop through each generated image and save it to the output directory
for i in range(len(generated_images_resized)):
    image = generated_images_resized[i]
    image=image*255
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    filename =f":\\Users\\dell\\PycharmProjex\\deepLearn\\Skill\\genData3\\Img_{i}.jpg"
    cv2.imwrite(filename, image)
