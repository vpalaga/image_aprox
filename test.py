from PIL import Image, ImageDraw


img = Image.new("RGBA", (500, 500), (255, 255, 255, 255))
draw = ImageDraw.Draw(img, "RGBA")

draw.line((0, 0, 500, 500), fill=(255, 0, 0, 128), width=50)
draw.line((500, 0, 0, 500), fill=(128, 128, 128, 128), width=50)

img.show()