from PIL import Image, ImageFilter

img = Image.open('./Astro/astro.jpg')
img.thumbnail((400,400)) # modifies file saving proportions (always)
img.save('./Astro/astro_thumbnail.jpg', 'jpeg')
print(img.size)