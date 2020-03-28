from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img_2 = img.convert('L').rotate(90)  # BlackWhite, rotated 90 degrees
resized_img = img.resize((300, 300))
#  print(dir(img))  # all properties and methods
print(img.format)
print(img.size)
print(img.mode)
filtered_img.save('./Pokedex/sharpen_pikachu.png', 'png')
filtered_img_2.save('./Pokedex/black_white_pikachu.png', 'png')
resized_img.save('./Pokedex/resized_pikachu.png', 'png')
filtered_img.show()
filtered_img_2.show()
resized_img.show()

# cropping image
box = (100, 100, 400, 400)
region = img.crop(box)

region.save('./Pokedex/cropped_pikachu.png', 'png')
region.show()
