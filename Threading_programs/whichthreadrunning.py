import threading
print("Current thread which is running now:",threading.current_thread().getName())
if threading.current_thread()==threading.main_thread():
    print("main thread")
else:
    print("some othe thread")