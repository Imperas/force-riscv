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
enum_classes_details = [
     ["RegReserveGroup", "unsigned char", "Register reservation group types",
      [("GPR", 0), ("FPRSIMDR", 1), ("VECREG", 2), ("SystemRegister", 3)]
      ],
     ["VmRegimeType", "unsigned char", "Virtual memory translation regime types",
      [("M", 0), ("S", 1), ("HS", 2), ("VS", 3)]
      ],
     ["MemBankType", "unsigned char", "Memory bank types",
      [("Default", 0)]
      ],
     ["VmContextParamType", "unsigned char", "Virtual memory request types",
      [("MODE", 0), ("MPRV", 1), ("MPP", 2), ("SPP", 3), ("MXR", 4), ("SUM", 5), ("MBE", 6), ("SBE", 7), ("UBE", 8), ("TVM", 9)]
      ],
     ["BranchConditionType", "unsigned char", "Branch condition types",
      [("BEQ", 0), ("BNE", 1), ("BLT", 2), ("BLTU", 3), ("BGE", 4), ("BGEU", 5), ("CBEQZ", 6), ("CBNEZ", 7)]
      ],
     ["PteAttributeType", "unsigned char", "Page table entry attribute types",
      [("Address", 0), ("IGNORED", 1), ("RES0", 2), ("SystemPage", 3), ("RSW", 4), ("DA", 5), ("G", 6), ("U", 7), ("X", 8), ("WR", 9), ("V", 10)]
      ],
     ["PageGranuleType", "unsigned char", "Page granule types",
      [("G4K", 0)]
      ],
     ["PageGenBoolAttrType", "unsigned char", "Boolean type GenPageRequest attributes for configuring page generation",
      [("FlatMap", 0), ("InstrAddr", 1), ("Regulated", 2), ("ViaException", 3), ("Privileged", 4), ("Atomic", 5), ("CanAlias", 6), ("ForceAlias", 7), ("ForceMemAttrs", 8), ("ForceNewAddr", 9), ("NoDataPageFault", 10), ("NoInstrPageFault", 11)]
      ],
     ["PagingExceptionType", "unsigned char", "Paging exception types.",
      [("InstructionAccessFault", 0), ("LoadAccessFault", 1), ("StoreAmoAccessFault", 2), ("InstructionPageFault", 3), ("LoadPageFault", 4), ("StoreAmoPageFault", 5)]
      ],
     ["VmConstraintType", "unsigned char", "Virtual memory constraint types.",
      [("Existing", 0), ("AddressError", 1), ("ReadOnly", 2), ("NoExecute", 3), ("PrivilegedNoExecute", 4), ("UnprivilegedNoExecute", 5), ("NoUserAccess", 6), ("PageTable", 7), ("UserAccess", 8), ("PageFault", 9), ("FlatMap", 10), ("AccessFault", 11)]
      ],
     ["PrivilegeLevelType", "unsigned char", "Exception level types",
      [("U", 0), ("S", 1), ("H", 2), ("M", 3)]
      ],
     ["MemAttributeImplType", "unsigned char", "Memory attribute implementation defined types",
      [("Unpredictable", 0)]
      ],
     ["SystemOptionType", "unsigned char", "System option types",
      [("PrivilegeLevel", 0), ("DisablePaging", 1), ("NoHandler", 2), ("NoSkip", 3), ("FlatMap", 4), ("MatchedHandler", 5), ("SkipBootCode", 6)]
      ],
     ["ExceptionClassType", "unsigned char", "Types of exception classes.",
      [("InstrAddrMisaligned", 0), ("InstrAccessFault", 1), ("IllegalInstr", 2), ("Breakpoint", 3), ("LoadAddrMisaligned", 4), ("LoadAccessFault", 5), ("StoreAmoAddrMisaligned", 6), ("StoreAmoAccessFault", 7), ("EnvCallFromUMode", 8), ("EnvCallFromSMode", 9), ("EnvCallFromMMode", 11), ("InstrPageFault", 12), ("LoadPageFault", 13), ("StoreAmoPageFault", 15)]
      ],
     ["InstructionGroupType", "unsigned char", "Types of instruction groups.",
      [("General", 0), ("Float", 1), ("System", 2), ("Vector", 3)]
      ],
     ["InstructionExtensionType", "unsigned char", "RISCV Extensions types for instructions.",
      [("Default", 0), ("RV32I", 1), ("RV64I", 2), ("RV32A", 3), ("RV64A", 4), ("RV32M", 5), ("RV64M", 6), ("RV32F", 7), ("RV64F", 8), ("RV32D", 9), ("RV64D", 10), ("RV32Q", 11), ("RV64Q", 12), ("Zicsr", 13), ("Zifencei", 14), ("RV32C", 15), ("RV64C", 16), ("RV128C", 17), ("RV64Priv", 18), ("RV32H", 19), ("RV64H", 20) ]
      ],
     ["MemOrderingType", "unsigned char", "Types of memory access ordering",
      [("Init", 0), ("Atomic", 1), ("AtomicRW", 2), ("Ordered", 3), ("LimitedOrdered", 4), ("OrderedRW", 5)]
      ],
     ["ExceptionVectorType", "unsigned char", "Types of exception vector",
      [("DefaultMachineModeVector", 0), ("DefaultSupervisorModeVector", 1)]
     ],
     ["SystemOpType", "unsigned char", "Types of System Operation",
      [("None", 0)]
     ],
     ["MemoryAttributeType", "unsigned char", "Types of memory attributes for physical memory segments",
      [("Device", 0), ("NormalCacheable", 1), ("NormalNonCacheable", 2)]
     ],
     ["VmInfoBoolType", "unsigned char", "VmInfo boolean attribute types (M should be the last one)",
      [("MODE", 1), ("MPRV", 2), ("TVM", 4)]
      ],

]
