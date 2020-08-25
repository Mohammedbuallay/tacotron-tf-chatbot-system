from synthesizer import Synthesizer
from playsound import playsound
from hparams import hparams, hparams_debug_string

hparams.parse('')
checkpoint = 'new/model.ckpt-517000'
synth = Synthesizer()
hparams_debug_string()
synth.load(checkpoint)
  
def generate_voice(text):
  path = 'test.wav'
  with open(path, 'wb') as f:
    f.write(synth.synthesize(text))
  playsound(path)


for i in range(4):
  generate_voice(input('please enter the sentance'))



