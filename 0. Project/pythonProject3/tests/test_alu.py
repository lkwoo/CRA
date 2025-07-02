import pytest
from alu_result import ALU_result
from alu import ALU

def test_test1():
    alu = ALU()
    alu.set_operand1(10)
    alu.set_operand2(20)
    alu.set_opcode("ADD")

    ret = ALU_result()
    alu.enable_signal(ret)

    assert ret.get_result() == 30
    assert ret.get_status() == 0