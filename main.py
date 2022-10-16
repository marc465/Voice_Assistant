import queue, json, words, functions, sounddevice as sd
from vosk import Model, KaldiRecognizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression



q = queue.Queue()

model = Model('model')

device = sd.default.device

samplerate = int(sd.query_devices(device[0], 'input')['default_samplerate'])



def callback(indata, frames, time, status):
    q.put(bytes(indata))


def answer(data: str, vectorizer: CountVectorizer, lrg: LogisticRegression):
    trg = words.trigger.intersection(data.split())
    if not trg:
        return
    data.replace(list(trg)[0], '')

    text_vector = vectorizer.transform([data]).toarray()[0]
    assistant_answer = lrg.predict([text_vector])[0]

    func = assistant_answer.split()[0]
    functions.speaker(assistant_answer.replace(func, ''))
    exec('functions.' + func + '()')


def main():
    
    """ Constantly listens to the microphone, decrypts the information from it.
    If there is a registered command in the received information, it executes it,
    Otherwise it ignores it.
    Self-learning to recognize speech. """

    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.commands.keys()))

    lgr = LogisticRegression()
    lgr.fit(vectors, list(words.commands.values()))

    del words.commands

    with sd.RawInputStream(samplerate=samplerate, blocksize = 16000, device=device[0], \
        dtype="int16", channels=1, callback=callback):

        rec = KaldiRecognizer(model, samplerate)

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                data = json.loads(rec.Result())['text']
                answer(data, vectorizer, lgr)


if __name__ == '__main__':
    main()
