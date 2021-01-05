import pytube

url = input("Qual URL? ")

try:
	youtube = pytube.YouTube(url)
	video = youtube.streams.get_highest_resolution()
	video.download()
	
	print("Video foi gravado com sucesso!")

except Exception as e:
	print("Video não baixado!")
