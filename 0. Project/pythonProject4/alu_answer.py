from alu_result import ALU_result


class ALU:
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

    def enable_signal(self, r: ALU_result):
        if self.is_invalid_opcode():
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

        r.set_result(self.calc_opcode())
        r.set_status(0)

    def is_invalid_opcode(self):
        return self.opcode != "ADD" and self.opcode != "MUL" and self.opcode != "SUB"

    def calc_opcode(self):
        if self.opcode == "ADD":
            return self.operand1 + self.operand2
        elif self.opcode == "MUL":
            return self.operand1 * self.operand2
        elif self.opcode == "SUB":
            return self.operand1 - self.operand2
        return 65535