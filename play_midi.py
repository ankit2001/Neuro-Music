import pygame as pg

def play(file):
	time_in = pg.time.Clock()
	pg.mixer.music.load(file)
	print(str(file) + ":  Music file is loaded")
	pg.mixer.music.play()
	while pg.mixer.music.get_busy():
		time_in.tick(35)

if __name__ == "__main__":
  midi_file = 'dataset/aguado-op03n02.mid'
  freq = 45000
  bitsize = -16
  channels = 4
  buffer = 1024
  pg.mixer.init(freq, bitsize, channels, buffer)
  pg.mixer.music.set_volume(0.9)
  try:
    play(midi_file)
  except KeyboardInterrupt:
    pg.mixer.music.fadeout(1000)
    pg.mixer.music.stop()
    raise SystemExit

