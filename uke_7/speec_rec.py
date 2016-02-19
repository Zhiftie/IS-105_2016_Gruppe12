import speech_recognition as sr
import pyttsx


engine = pyttsx.init() 
engine.setProperty('rate', 170) 
voices = engine.getProperty('voices') #Her defineres stemmen(es) egenskaper, f.eks. alder, kjønn, etnisitet, osv.
engine.setProperty('voice', voices[0].id) 

r = sr.Recognizer() 
m = sr.Microphone()

try:
    print("A moment of silence, please...")
    with m as source: r.adjust_for_ambient_noise(source) 
    print("Set minimum energy threshold to {}".format(r.energy_threshold)) #Justerer terskelen for å oppfatte lyd. 
    while True:
        print("Say something!")
        with m as source: audio = r.listen(source) 
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes: # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
        
            if "hello" in value:
                engine.say('How are you today?')
                engine.runAndWait()
            elif "i'm fine" in value:
                engine.say("Good!")
                engine.runAndWait()
            elif "tell me a story" in value:
                engine.say("Once upon a time there was a dear little girl who was loved by everyone who looked at her,"
                           "but most of all by her grandmother, and there was nothing that she would not have given to the child."
                           "Once she gave her a little riding hood of red velvet, which suited her so well that she would "
                           "never wear anything else; so she was always called 'Little Red Riding Hood.'")
                engine.runAndWait()
            else:
                engine.say("I'm unable to process what you're saying.")
                
        except sr.UnknownValueError:
            print("Oops! Didn't catch that")
        except sr.RequestError as e:
            print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
    
except KeyboardInterrupt: 
    pass   