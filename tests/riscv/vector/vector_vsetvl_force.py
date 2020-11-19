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
from VectorTestSequence import VectorVsetvlTestSequence
from riscv.Utils import LoadGPR64

## This test verifies the VSETVL instruction sets the vl and vtype registers as expected.
class MainSequence(VectorVsetvlTestSequence):

    def __init__(self, aGenThread, aName=None):
        super().__init__(aGenThread, aName)

        self._mInstrList = ('VSETVL##RISCV',)

    ## Return a list of test instructions to randomly choose from.
    def _getInstructionList(self):
        return self._mInstrList

    ## Generate parameters to be passed to Sequence.genInstruction() and load register operands.
    def _generateInstructionParameters(self):
        instr_params = {}

        load_gpr64_seq = LoadGPR64(self.genThread)
        (avl_reg_index, vtype_reg_index) = self.getRandomGPRs(2, exclude='0')
        load_gpr64_seq.load(avl_reg_index, self.mAvl)
        instr_params['rs1'] = avl_reg_index
        load_gpr64_seq.load(vtype_reg_index, self.mVtype)
        instr_params['rs2'] = vtype_reg_index

        return instr_params


MainSequenceClass = MainSequence
GenThreadClass = GenThreadRISCV
EnvClass = EnvRISCV
