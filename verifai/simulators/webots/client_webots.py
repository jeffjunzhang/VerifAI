from verifai.client import Client

class ClientWebots(Client):

    def __init__(self, simulation_data):
        port = simulation_data.port
        bufsize = simulation_data.bufsize
        super().__init__(port, bufsize)
        self.task = simulation_data.task

    def simulate(self, sample):
        return self.task.run_task(sample)

    def run_client(self):
        success = super().run_client()
        if success:
            self.task.close()
