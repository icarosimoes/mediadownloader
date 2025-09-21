# Primeiro, se ainda não tiver yt-dlp instalado:
# pip install yt-dlp

import yt_dlp

def baixar_video(link):
    opcoes = {
        'format': 'bestvideo+bestaudio/best',  # baixa vídeo + áudio
        'merge_output_format': 'mp4',          # garante saída em MP4
        'outtmpl': 'Dani Black - Maior feat. Milton Nascimento.mp4',  
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    link_video = "https://youtu.be/mc1ANOYexlI?si=0SVAwrQ54TG0ZyEP"
    baixar_video(link_video)
