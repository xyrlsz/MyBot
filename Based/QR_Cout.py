from PIL import Image

# 获取QRCode中的模块数据
# qr_code = qr.make_image(fill_color="black", back_color="white")
# qr_code = Image.open("QR.png")
# 获取二维码的大小


def print_QR(qr_code):
    width, height = qr_code.size
    cell = get_cell(qr_code)
    for y in range(int(height / cell)):
        for x in range(int(width / cell)):
            if qr_code.getpixel((x * cell, y * cell)) == 0:
                # 0表示黑色
                print("██", end="")
            else:
                # 非0表示白色
                print("  ", end="")
        print(" ")  # 换行

    # 输出完成消息
    # print("二维码已输出到控制台")


# 在控制台中输出二维码
def get_cell_size(qr_code, x, y, x2, y2):
    for j in range(x, x2):
        for i in range(y, y2):
            pix = qr_code.getpixel((j, i))
            if pix == 255:  # 如果颜色为白色
                return j - x  # 每个黑色格子的像素点大小


def get_cell(qr_code):
    width, height = qr_code.size
    flag = 0
    for y in range(height):
        for x in range(width):
            pix = qr_code.getpixel((x, y))

            if pix == 0 and flag == 0:  # 出现第一个黑色像素
                x1 = x
                flag = 1

            if pix == 255 and flag == 1:  # 出现第一个白色像素（意味着左上角的标记方块横向结束）
                flag = 2
                cell = get_cell_size(qr_code, x1, x1, x, x)
                return cell
