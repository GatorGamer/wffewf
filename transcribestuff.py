def transcribe():
	audio = pyaudio.PyAudio()

        stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

        frames = []

        # Records while the stop record isn't clicked
        try:
		while True:
		    data = stream.read(1024)
		    frames.append(data)
	
	except KeyboardInterrupt:
		print("Stopped recording.")
	        print("............................................................................................................................")
	        stream.stop_stream()
	        stream.close()
	        audio.terminate()
	
	        sound_file = wave.open("temp/chat.wav", "wb")
	        sound_file.setnchannels(1)
	        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
	        sound_file.setframerate(44100)
	        sound_file.writeframes(b''.join(frames))
	        sound_file.close()
	
	        print("Transcribing Audio...")
	        print("............................................................................................................................")
	
	        # Speech to Text
	        model = whisper.load_model('base')
	        result = model.transcribe('temp/chat.wav', fp16=False)
		return 	result['text']
