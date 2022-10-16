Voice_Assistant version 1.0


A simple voice assistant. Written in Python using standard libraries, as well as vosk, scikit-learn and pyttsx3.


Constantly listens to the microphone, transcribes the speech, if there is a trigger word in the speech, analyzes it.
If it finds a registered command, executes it.
Thanks to the scikit-learn library, it trains and learns itself. Therefore, it can understand not only verbatim commands, but also similar ones.



How do I launch the voice assistant?

1. Run the start.bat file
2. Wait until the preparation is finished.
3. Start talking with the assistant via microphone (Ukrainian only). It will execute the registered commands.



Commands are currently registered:
    Weather
    Open the internet
    Open movie listings
    Turn off computer
    Shut down

And also prepared answers to some phrases.



Problems

    The problem:
        Bad voiceover of the Ukrainian language.
        For voice acting the library pyttsx3 is used. Which is not suitable for ukrainian voice acting.
    Solution:
        Find a library for Ukrainian text voiceover.
        During the process...

    The problem:
        Confuses some Ukrainian words, performs wrong commands.
    Solution:
        Change the trigger text, improve the scikit-learn model.
        In the process...
