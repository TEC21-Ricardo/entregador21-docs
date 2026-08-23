from PIL import Image, ImageDraw, ImageFilter
import imageio
import os

def pixelize_gif(input_path, output_path, pixelize_zones):
    """Pixelize áreas específicas em cada frame do GIF"""
    
    # Abrir GIF
    gif = imageio.get_reader(input_path)
    frames = []
    durations = []
    
    print(f"🎬 Processando: {os.path.basename(input_path)}")
    print(f"📊 Total de frames: {len(gif)}")
    
    for i, frame in enumerate(gif):
        # Converter para PIL Image
        img = Image.fromarray(frame)
        
        # Pixelizar cada zona definida
        for zone in pixelize_zones:
            x1, y1, x2, y2, intensity = zone
            
            # Extrair área
            area = img.crop((x1, y1, x2, y2))
            
            # Pixelizar (reduzir e ampliar para efeito de pixel)
            size = intensity
            area = area.resize((size, size), Image.Resampling.BILINEAR)
            area = area.resize((x2-x1, y2-y1), Image.Resampling.BILINEAR)
            
            # Colar de volta
            img.paste(area, (x1, y1))
        
        frames.append(img)
        durations.append(gif.get_meta_data(i).get('duration', 50))
        
        if (i + 1) % 10 == 0:
            print(f"  ✓ Processados {i + 1} frames...")
    
    # Salvar GIF processado
    imageio.mimsave(output_path, [np.array(f) for f in frames], duration=durations)
    print(f"✅ Salvo: {os.path.basename(output_path)}\n")

import numpy as np

# Diretório dos GIFs
gifs_dir = r"C:\Users\ricardo\Documents\entregador21-gitbook\docs\03-operacoes\gifs"

# Zonas a pixelizar (x1, y1, x2, y2, intensidade_pixel)
# Pixeliza as áreas onde geralmente aparecem nomes, emails, endereços
zones = [
    (600, 50, 900, 120, 8),    # Área superior direita (nome/destinatário)
    (600, 120, 900, 200, 8),   # Segunda linha
    (400, 50, 600, 120, 8),    # Coluna do meio
]

# Processar GIFs
gifs = [
    "reatribuir-rotas.gif",
    "atribuir-rotas-selecionados.gif"
]

for gif_name in gifs:
    input_file = os.path.join(gifs_dir, gif_name)
    output_file = os.path.join(gifs_dir, gif_name.replace(".gif", "-processado.gif"))
    
    if os.path.exists(input_file):
        pixelize_gif(input_file, output_file, zones)
    else:
        print(f"❌ Arquivo não encontrado: {gif_name}")

print("🎉 Processamento concluído!")
