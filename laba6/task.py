import threading
import time
import uuid


class Worker:
    data = []

    def view(self):
        while True:
            print(self.data)
            time.sleep(2)

    def sort(self):
        while True:
            self.data.sort()
            file = open("out.txt", "w", encoding="utf8")
            file.write("\n".join(self.data))
            file.close()
            time.sleep(5)

    def generate(self):
        while True:
            self.data.append(str(uuid.uuid4().hex))
            time.sleep(2)


worker = Worker()

viewThread = threading.Thread(target=worker.view)
sortThread = threading.Thread(target=worker.sort)

viewThread.daemon = True
viewThread.start()

sortThread.daemon = True
sortThread.start()

worker.generate()
