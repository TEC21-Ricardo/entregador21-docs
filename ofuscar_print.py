from PIL import Image, ImageDraw
import os

# Caminho do print
print_path = r"C:\Users\ricardo\Documents\entregador21-gitbook\Procedimentos\Função agrupamento.png"
output_path = r"C:\Users\ricardo\Documents\entregador21-gitbook\Procedimentos\Função agrupamento.png"

# Abrir imagem
img = Image.open(print_path)

# Criar desenho
draw = ImageDraw.Draw(img)

# Cores para pixelize/blur (usar retângulos pretos)
# Estas são áreas aproximadas onde podem estar: nome, CPF, endereço
blur_areas = [
    (0, 100, 400, 150),      # Área superior esquerda
    (400, 100, 800, 150),    # Área superior direita
    (0, 150, 800, 200),      # Segunda linha
    (0, 200, 800, 250),      # Terceira linha
    (0, 250, 600, 300),      # Quarta linha (CPF/dados)
]

# Pixelize cada área (usando retângulos com padrão de pixel)
for x1, y1, x2, y2 in blur_areas:
    # Extrair área
    area = img.crop((x1, y1, x2, y2))
    
    # Pixelizar (reduzir e ampliar)
    size = 10
    area = area.resize((size, size), Image.Resampling.BILINEAR)
    area = area.resize((x2-x1, y2-y1), Image.Resampling.BILINEAR)
    
    # Colar de volta
    img.paste(area, (x1, y1))

# Salvar
img.save(output_path)
print(f"✅ Print ofuscado salvo!")

