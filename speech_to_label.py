from google.cloud import speech_v1p1beta1
import io,os
import argparse
from tqdm import tqdm

from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
import io

def sample_recognize(local_file_path):
    text_file = open(os.path.join(args.data_dir,"label.txt"), "a")
    client = speech_v1.SpeechClient()

    language_code = "en"

    sample_rate_hertz = 44100

    encoding = 'LINEAR16'
    config = {
        "language_code": language_code,
        "sample_rate_hertz": sample_rate_hertz,
        "encoding": encoding,
        "audio_channel_count": 2,
    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    response = client.recognize(config, audio)
    new_text = []
    for result in response.results:
        new_text.append(result.alternatives[0].transcript)
    name = local_file_path.replace(filepath+'/','')
    name = name.replace('.wav','') 
    text_file.write(name+"|"+"".join(new_text)+"\n")
    #print (name+"|"+"".join(new_text))
    text_file.close()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', required=True)
    parser.add_argument('--gcp_json_file',required=True)
    args = parser.parse_args()
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= args.gcp_json_file
    filepath = os.path.join(args.data_dir,"Wave")
    for filename in tqdm(sorted(os.listdir(filepath))):
        sample_recognize(os.path.join(filepath,filename))