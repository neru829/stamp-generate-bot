from PIL import Image, ImageDraw, ImageFont
import os

text = ["ああああああ"]
image_size = (128, 128)
font_path = "/Users/nishine/Library/Fonts/NotoSansJP-Bold.otf"
font_size = 20
ratio = len(text[0])
# x_start = 0
# y_start = 0

class stamp:
    font = ImageFont.truetype(font_path, font_size)


def main():
    # 背景色を指定してImageオブジェクトを生成
    image = Image.new("RGBA", (128*ratio, font_size*ratio), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    # 文字の描画サイズ
    # width = image_size[0] - x_start
    # height = image_size[1] - y_start
    # out_text_size = (width + 1, height + 1)
    # font_size_offset = 0
    # font = None
    # while width < out_text_size[0] or height < out_text_size[1]:
    #     font = ImageFont.truetype(font_path, image_size[0] - font_size_offset)
    #     xL, yT, xR, yB = draw.textbbox((0, 0), text[0], font=font)
    #     out_text_size = (xR - xL, yB - yT)
    #     print(out_text_size)
    #     font_size_offset += 1

    # フォントとフォントサイズを指定
    font = ImageFont.truetype(font_path, font_size*ratio)
    draw = ImageDraw.Draw(image)


    # xL, yT, xR, yB = draw.textbbox((0, 0), text[0], font=font)

    # x = (image_size[0] - (xR - xL)) / 2
    # y = (image_size[1] / 2 - (yB - yT)) / 2
    x = 0
    y = 0

    # for i in text:
    #     draw.text((x, y), i, fill=(0, 0, 255, 255), font=font)
    draw.text((x, y), text[0], fill=(0, 0, 255, 255), font=font)


    image2 = image.resize(image_size)
    image.save("text_image.png")
    image2.save("text_image2.png")

if __name__ == "__main__":
    main()