from alu_result import ALU_result

class ALU :
    def __init__(self) -> None:
        super().__init__()
        self.operand1 = -1
        self.operand2 = -1
        self.opcode = ""

    def set_operand1(self, operand1):
        self.operand1 = operand1

    def set_operand2(self, operand2):
        self.operand2 = operand2

    def set_opcode(self, opcode):
        self.opcode = opcode

    def get_result(self, operand1, operand2, opcode):
        if opcode == "ADD":
            return operand1 + operand2
        elif opcode == "MUL":
            return operand1 * operand2
        elif opcode == "SUB":
            return operand1 - operand2
        else:
            return 65535

    def enable_signal(self, r : ALU_result):
        if self.opcode not in ["ADD", "MUL", "SUB"]:
            r.set_result(65535)
            r.set_status(3)
            return
        if self.operand1 == -1:
            r.set_result(65535)
            r.set_status(1)
            return
        if self.operand2 == -1:
            r.set_result(65535)
            r.set_status(2)
            return

        r.set_result(self.get_result(self.operand1, self.operand2, self.opcode))
        r.set_status(0)
