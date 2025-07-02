from alu_result import ALU_result
from alu import ALU

def test_test_sum():
    alu = ALU()
    alu.set_operand1(10)
    alu.set_operand2(20)
    alu.set_opcode("ADD")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 30
    assert ret.get_status() == 0

    alu.set_operand1(-1)
    alu.set_operand2(100)
    alu.set_opcode("ADD")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 1

    alu.set_operand1(150)
    alu.set_operand2(-1)
    alu.set_opcode("ADD")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 2

def test_test_mul():
    alu = ALU()
    alu.set_operand1(10)
    alu.set_operand2(20)
    alu.set_opcode("MUL")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 200
    assert ret.get_status() == 0

    alu.set_operand1(-1)
    alu.set_operand2(20)
    alu.set_opcode("MUL")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 1

    alu.set_operand1(10)
    alu.set_operand2(-1)
    alu.set_opcode("MUL")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 2


def test_test_sub():
    alu = ALU()
    alu.set_operand1(10)
    alu.set_operand2(20)
    alu.set_opcode("SUB")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == -10
    assert ret.get_status() == 0

    alu.set_operand1(-1)
    alu.set_operand2(20)
    alu.set_opcode("SUB")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 1

    alu.set_operand1(10)
    alu.set_operand2(-1)
    alu.set_opcode("SUB")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 2


def test_test_not_defined_opcode():
    alu = ALU()
    alu.set_operand1(10)
    alu.set_operand2(20)
    alu.set_opcode("POWER")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 65535
    assert ret.get_status() == 3