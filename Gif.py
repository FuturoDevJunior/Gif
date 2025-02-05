import sysb 
import os
import subprocess
 
    """
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", nome, "--quiet"])
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar o pacote {nome}: {e}")
        sys.exit(1)

def verificar_ffmpeg():
    """
    Verifica se o ffmpeg está disponível no sistema.
    """
    from shutil import which
    if which("ffmpeg") is None:
        print("Erro: ffmpeg não encontrado. Instale o ffmpeg e verifique se ele está no PATH do sistema.")
        sys.exit(1)

# Verificação e instalação automática da dependência moviepy
try:
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
except ImportError:
    instalar_pacote("moviepy")
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def converter_video_para_gif(caminho_video, gif_saida, fps, output_width, output_height, watermark_pos, watermark_opacity, optimize):
    clip = None
    clip_composto = None
    try:
        clip = VideoFileClip(caminho_video)
        
        # Redimensiona o vídeo se tamanho de saída for especificado
        if output_width > 0 or output_height > 0:
            current_width, current_height = clip.size
            if output_width > 0 and output_height > 0:
                new_width, new_height = output_width, output_height
            elif output_width > 0:
                ratio = output_width / current_width
                new_width = output_width
                new_height = int(current_height * ratio)
            else:  # output_height > 0
                ratio = output_height / current_height
                new_height = output_height
                new_width = int(current_width * ratio)
            clip = clip.resize(newsize=(new_width, new_height))
        
        # Cria a marca d'água com o texto profissional
        watermark = TextClip("DevFerreiraG", fontsize=24, color="white", font="Arial-Bold", method="caption")
        watermark = watermark.set_duration(clip.duration).set_opacity(watermark_opacity)
        
        # Define a posição da marca d'água: se não especificada, usa o padrão (inferior direita, com margem 10)
        if watermark_pos:
            try:
                pos_coords = tuple(int(coord.strip()) for coord in watermark_pos.split(","))
                if len(pos_coords) != 2:
                    raise ValueError
                pos = pos_coords
            except Exception:
                print("Aviso: Parâmetro 'watermark_pos' inválido. Usando posição padrão (inferior direita).")
                pos = (clip.w - watermark.w - 10, clip.h - watermark.h - 10)
        else:
            pos = (clip.w - watermark.w - 10, clip.h - watermark.h - 10)
        watermark = watermark.set_pos(pos)
        
        # Compõe o vídeo com a marca d'água
        clip_composto = CompositeVideoClip([clip, watermark])
        
        # Configura os parâmetros de escrita do GIF
        write_gif_params = {"fps": fps, "program": "ffmpeg"}
        if optimize:
            write_gif_params["opt"] = "Optimize"
        
        clip_composto.write_gif(gif_saida, **write_gif_params)
        print("GIF criado com sucesso:", gif_saida)
    except Exception as e:
        print("Erro durante a conversão do vídeo para GIF. Detalhes:", e)
        sys.exit(1)
    finally:
        if clip:
            clip.close()
        if clip_composto:
            clip_composto.close()

if __name__ == "__main__":
    import argparse
    verificar_ffmpeg()  # Verifica se o ffmpeg está instalado
    
    parser = argparse.ArgumentParser(
        description="Conversor de Vídeo para GIF com marca d'água DevFerreiraG - Automatiza a instalação de dependências."
    )
    parser.add_argument("caminho_video", help="Caminho do arquivo de vídeo de origem.")
    parser.add_argument("gif_saida", help="Nome do arquivo GIF de saída.")
    parser.add_argument("--fps", type=int, default=10, help="Frames por segundo do GIF (padrão: 10).")
    parser.add_argument("--width", type=int, default=0, help="Largura desejada do GIF (opcional).")
    parser.add_argument("--height", type=int, default=0, help="Altura desejada do GIF (opcional).")
    parser.add_argument("--watermark_pos", type=str, default="", help="Posição da marca d'água no formato 'x,y' (opcional).")
    parser.add_argument("--watermark_opacity", type=float, default=0.7, help="Opacidade da marca d'água (padrão: 0.7).")
    parser.add_argument("--optimize", action="store_true", help="Otimiza a saída para reduzir o tamanho do arquivo.")
    args = parser.parse_args()
    
    if not os.path.exists(args.caminho_video):
        print("Arquivo de vídeo não encontrado:", args.caminho_video)
        sys.exit(1)
    
    converter_video_para_gif(
        args.caminho_video,
        args.gif_saida,
        args.fps,
        args.width,
        args.height,
        args.watermark_pos,
        args.watermark_opacity,
        args.optimize
    )
