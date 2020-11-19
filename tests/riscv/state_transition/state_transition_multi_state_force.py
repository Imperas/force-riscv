#
# Copyright (C) [2020] Futurewei Technologies, Inc.
#
# FORCE-RISCV is licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR
# FIT FOR A PARTICULAR PURPOSE.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from riscv.EnvRISCV import EnvRISCV
from riscv.GenThreadRISCV import GenThreadRISCV
from base.Sequence import Sequence
import state_transition_test_utils
from Enums import EStateElementType, EStateTransitionOrderMode
from State import State
import RandomUtils
import StateTransition

## This test verifies that multiple StateTransitions can be executed within a single test with
# interleaved instructions.
class MainSequence(Sequence):

    def __init__(self, aGenThread, aName=None):
        super().__init__(aGenThread, aName)

        self._mExpectedStateData = {}

    def generate(self, **kargs):
        state_a = self._createStateA()
        StateTransition.transitionToState(state_a, EStateTransitionOrderMode.ByPriority)
        state_transition_test_utils.verifyState(self, self._mExpectedStateData)

        instructions = ('ADDI##RISCV', 'ADDW##RISCV', 'LUI##RISCV', 'SLLI#RV64I#RISCV', 'SRLI#RV64I#RISCV')
        for _ in range(RandomUtils.random32(200, 500)):
            self.genInstruction(self.choice(instructions))

        state_b = self._createStateB()
        StateTransition.transitionToState(state_b)
        state_transition_test_utils.verifyState(self, self._mExpectedStateData)

        for _ in range(RandomUtils.random32(200, 500)):
            self.genInstruction('SD##RISCV')

        state_c = self._createStateC()
        StateTransition.transitionToState(state_c)
        state_transition_test_utils.verifyState(self, self._mExpectedStateData)

        for _ in range(RandomUtils.random32(200, 500)):
            self.genInstruction('FMUL.D#Double-precision#RISCV')

    ## Create a State in M privilege level configured to trigger a timer interrupt.
    def _createStateA(self):
        state = State()

        self._mExpectedStateData = {}

        state.addPrivilegeLevelStateElementByName('M')
        self._mExpectedStateData[EStateElementType.PrivilegeLevel] = 3

        expected_sys_reg_state_data = []

        # TODO(Noah): Uncomment adding the system register StateElements when the relevant system
        # registers are defined correctly in the system_registers.xml file.
        #mip_name = 'mip'
        #state.addSystemRegisterStateElementByField(mip_name, 'MTIE', 0x1, aPriority=10)
        #state.addSystemRegisterStateElementByField(mip_name, 'MTIP', 0x0, aPriority=10)
        #self.randomInitializeRegister(mip_name)
        #(mip_val, valid) = self.readRegister(mip_name)
        #state_transition_test_utils.assertValidRegisterValue(self, mip_name, valid)
        #mip_val = state_transition_test_utils.combineRegisterValueWithFieldValue(self, mip_name, mip_val, 'MTIE', 0x1)
        #mip_val = state_transition_test_utils.combineRegisterValueWithFieldValue(self, mip_name, mip_val, 'MTIP', 0x0)
        #expected_sys_reg_state_data.append((mip_name, mip_val))

        #state.addRegisterStateElement('mtime', (0,), aPriority=5)
        #expected_sys_reg_state_data.append(('mtime', 0))
        #state.addRegisterStateElement('mtimecmp', (50,), aPriority=5)
        #expected_sys_reg_state_data.append(('mtimecmp', 50))

        self._mExpectedStateData[EStateElementType.SystemRegister] = expected_sys_reg_state_data

        return state

    ## Create a State in S privilege level with the Sv39 virtual memory system enabled. Half of the
    # GPRs are specified with a value of -1.
    def _createStateB(self):
        state = State()

        self._mExpectedStateData = {}

        state.addPrivilegeLevelStateElementByName('S')
        self._mExpectedStateData[EStateElementType.PrivilegeLevel] = 1

        # TODO(Noah): Uncomment specifying the satp.MODE value when switching to the Sv39 virtual
        # memory system is supported.
        #state.addVmContextStateElement('satp', 'MODE', 8)
        #self._mExpectedStateData[EStateElementType.VmContext] = [('satp', 'MODE', 8)]

        expected_gpr_state_data = []
        for gpr_index in range(1, 32, 2):
            gpr_name = 'x%d' % gpr_index
            gpr_val = 0xFFFFFFFFFFFFFFFF
            state.addRegisterStateElement(gpr_name, (gpr_val,))
            expected_gpr_state_data.append((gpr_name, gpr_val))

        self._mExpectedStateData[EStateElementType.GPR] = expected_gpr_state_data

        return state

    ## Create a State with the rounding mode set to round towards 0 and all of the floating point
    # registers with values in the interval [0, 1.0).
    def _createStateC(self):
        state = State()

        self._mExpectedStateData = {}

        expected_sys_reg_state_data = []

        fcsr_name = 'fcsr'
        state.addSystemRegisterStateElementByField(fcsr_name, 'FRM', 1)
        (fcsr_val, valid) = self.readRegister(fcsr_name)
        state_transition_test_utils.assertValidRegisterValue(self, fcsr_name, valid)
        fcsr_val = state_transition_test_utils.combineRegisterValueWithFieldValue(self, fcsr_name, fcsr_val, 'FRM', 1)

        # TODO(Noah): Enable verification of setting the fcsr register when the readRegister()
        # method reads the correct value for fcsr. Currently, the top 58 bits are being initialized
        # to a non-zero value by Force, which is not legal.
        #expected_sys_reg_state_data.append((fcsr_name, fcsr_val))

        expected_fp_reg_state_data = []
        for fp_reg_index in range(0, 32):
            fp_reg_val = RandomUtils.random64(0, 0x3FFFFFFFFFFFFFFF)
            state.addRegisterStateElement(('D%d' % fp_reg_index), (fp_reg_val,))

        self._mExpectedStateData[EStateElementType.FloatingPointRegister] = expected_fp_reg_state_data

        sstatus_name = 'sstatus'
        fs_val = RandomUtils.random32(1, 3)
        state.addSystemRegisterStateElementByField(sstatus_name, 'FS', fs_val)
        (sstatus_val, valid) = self.readRegister(sstatus_name)
        state_transition_test_utils.assertValidRegisterValue(self, sstatus_name, valid)
        sstatus_val = state_transition_test_utils.combineRegisterValueWithFieldValue(self, sstatus_name, sstatus_val, 'FS', fs_val)

        # Adjust expected value of SD bit according to architecture rules
        (xs_val, valid) = self.readRegister(sstatus_name, field='XS')
        state_transition_test_utils.assertValidRegisterValue(self, sstatus_name, valid)
        (vs_val, valid) = self.readRegister(sstatus_name, field='VS')
        state_transition_test_utils.assertValidRegisterValue(self, sstatus_name, valid)
        if (fs_val == 3) or (xs_val == 3) or (vs_val == 3):
            sstatus_val = state_transition_test_utils.combineRegisterValueWithFieldValue(self, sstatus_name, sstatus_val, 'SD', 1)
        else:
            sstatus_val = state_transition_test_utils.combineRegisterValueWithFieldValue(self, sstatus_name, sstatus_val, 'SD', 0)

        expected_sys_reg_state_data.append((sstatus_name, sstatus_val))

        self._mExpectedStateData[EStateElementType.SystemRegister] = expected_sys_reg_state_data

        return state


MainSequenceClass = MainSequence
GenThreadClass = GenThreadRISCV
EnvClass = EnvRISCV

