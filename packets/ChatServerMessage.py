# from packets.DofusPacket import DofusPacket

class Packet:
    dofusPacket = None

    def __init__(self, dofusPacket):
        self.dofusPacket = dofusPacket

    def deserialize(self):
        print(str(self.dofusPacket))
        # IN PROGRESS