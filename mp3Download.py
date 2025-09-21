# Primeiro, se ainda não tiver yt-dlp instalado:
# pip install yt-dlp

import yt_dlp

def baixar_audio(link):
    opcoes = {
        'format': 'bestaudio/best',
        'outtmpl': 'QUANTA LUZ - Elizabete Lacerda%(ext)s',  # Nome do arquivo
        'postprocessors': [
            {  
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',   # converte pra mp3
                'preferredquality': '192', # qualidade em kbps (pode usar 128, 192, 320)
            }
        ],
    }

    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download([link])

if __name__ == "__main__":
    link_video = "https://youtu.be/kJdFR5oN09Q?si=kSYwvKyYl9wjgcMW"
    baixar_audio(link_video)
