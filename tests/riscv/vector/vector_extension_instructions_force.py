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
from VectorTestSequence import VectorTestSequence
from base.ChoicesModifier import ChoicesModifier

## This test verifies that vector sign and zero extension instructions are generated legally.
class MainSequence(VectorTestSequence):

    def __init__(self, aGenThread, aName=None):
        super().__init__(aGenThread, aName)

        self._mInstrList = (
            'VSEXT.VF2##RISCV',
            'VSEXT.VF4##RISCV',
            'VSEXT.VF8##RISCV',
            'VZEXT.VF2##RISCV',
            'VZEXT.VF4##RISCV',
            'VZEXT.VF8##RISCV',
        )

    ## Set up the environment prior to generating the test instructions.
    def _setUpTest(self):
        choices_mod = ChoicesModifier(self.genThread)

        # TODO(Noah): Remove the restriction on SEW when a mechanism to skip instructions with
        # illegal vector layouts is implemented. For now, SEW = 64 ensures all applicable
        # instructions can be legally generated.
        choice_weights = {'0x0': 0, '0x1': 0, '0x2': 0, '0x3': 10, '0x4': 0, '0x5': 0, '0x6': 0, '0x7': 0}
        choices_mod.modifyRegisterFieldValueChoices('vtype.VSEW', choice_weights)

        choices_mod.commitSet()

    ## Return the maximum number of test instructions to generate.
    def _getMaxInstructionCount(self):
        return 1000

    ## Return a list of test instructions to randomly choose from.
    def _getInstructionList(self):
        return self._mInstrList

    ## Verify additional aspects of the instruction generation and execution.
    #
    #  @param aInstr The name of the instruction.
    #  @param aInstrRecord A record of the generated instruction.
    def _performAdditionalVerification(self, aInstr, aInstrRecord):
        vs2_val = aInstrRecord['Srcs']['vs2']
        vd_val = aInstrRecord['Dests']['vd']
        if vs2_val == vd_val:
            self.error('Instruction %s used overlapping source and destination registers' % aInstr)

        vm_val = aInstrRecord['Imms']['vm']
        if (vm_val == 0) and (vd_val == 0):
            self.error('Instruction %s is masked with v0 as the destination register' % aInstr)


MainSequenceClass = MainSequence
GenThreadClass = GenThreadRISCV
EnvClass = EnvRISCV
