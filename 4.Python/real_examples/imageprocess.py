from PIL import Image, ImageFilter

image = Image.open('cat.jpeg')

resized_image = image.resize((80, 60))
resized_image.save('small_cat.jpeg')

blurred_image = image.filter(ImageFilter.BLUR)
resized_image.save('blurred_cat.jpeg')
