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
from VectorTestSequence import VectorLoadStoreTestSequence

## This test verifies that unit-stride load and store instructions can be generated and executed
# successfully.
class MainSequence(VectorLoadStoreTestSequence):

    def __init__(self, aGenThread, aName=None):
        super().__init__(aGenThread, aName)

        self._mInstrList = (
            'VLE16.V##RISCV',
            'VLE32.V##RISCV',
            'VLE64.V##RISCV',
            'VLE8.V##RISCV',
            'VSE16.V##RISCV',
            'VSE32.V##RISCV',
            'VSE64.V##RISCV',
            'VSE8.V##RISCV',
        )

    ## Return a list of test instructions to randomly choose from.
    def _getInstructionList(self):
        return self._mInstrList


MainSequenceClass = MainSequence
GenThreadClass = GenThreadRISCV
EnvClass = EnvRISCV
