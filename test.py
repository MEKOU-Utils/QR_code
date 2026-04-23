import qrcode

# 1. 変換したいリンク（アンケートURLやPortalのURL）
data = "https://mekou-project.github.io/FruitCatch/dist/fruitcatch.js"
# 2. QRコードの生成
img = qrcode.make(data)

# 3. 保存
img.save("FruitCatch.png")
#pip install qrcode[pil]
