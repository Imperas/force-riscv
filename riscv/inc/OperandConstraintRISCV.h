//
// Copyright (C) [2020] Futurewei Technologies, Inc.
//
// FORCE-RISCV is licensed under the Apache License, Version 2.0 (the "License");
//  you may not use this file except in compliance with the License.
//  You may obtain a copy of the License at
//
//  http://www.apache.org/licenses/LICENSE-2.0
//
// THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER
// EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR
// FIT FOR A PARTICULAR PURPOSE.
// See the License for the specific language governing permissions and
// limitations under the License.
//
#ifndef Force_OperandConstraintRISCV_H
#define Force_OperandConstraintRISCV_H

#include <Operand.h>
#include <OperandConstraint.h>

namespace Force {

  /*!
    \class VsetvlVtypeImmediateOperandConstraint
    \brief This class carries dynamic constraint properties for VsetvlVtypeImmediateOperand.
  */
  class VsetvlVtypeImmediateOperandConstraint : public ImmediateOperandConstraint {
  public:
    DEFAULT_CONSTRUCTOR_DEFAULT(VsetvlVtypeImmediateOperandConstraint);
    COPY_CONSTRUCTOR_ABSENT(VsetvlVtypeImmediateOperandConstraint);
    SUBCLASS_DESTRUCTOR_DEFAULT(VsetvlVtypeImmediateOperandConstraint);
    ASSIGNMENT_OPERATOR_ABSENT(VsetvlVtypeImmediateOperandConstraint);

    void Setup(const Generator& rGen, const Instruction& rInstr, const OperandStructure& rOperandStruct) override; //!< Setup dynamic operand constraints.
  };

   /*!
    \class VectorMaskOperandConstraint
    \brief This class carries dynamic constraint properties for VectorMaskOperand.
  */
  class VectorMaskOperandConstraint : public ChoicesOperandConstraint {
  public:
    DEFAULT_CONSTRUCTOR_DEFAULT(VectorMaskOperandConstraint);
    COPY_CONSTRUCTOR_ABSENT(VectorMaskOperandConstraint);
    SUBCLASS_DESTRUCTOR_DEFAULT(VectorMaskOperandConstraint);
    ASSIGNMENT_OPERATOR_ABSENT(VectorMaskOperandConstraint);
  private:
    void GetAdjustedDifferValues(const Instruction& rInstr, const OperandConstraint& rDifferOprConstr, cuint64 differVal, ConstraintSet& rAdjDifferValues) const override; //!< Return a list of values to remove from the constraint set to avoid conflicting with the specified differ operand value.
  };

  class ConstraintSet;

  /*!
    \class BaseOffsetBranchOperandConstraint
    \brief This class carries dynamic constraint properties for BaseOffsetBranchOperand.
  */
  class BaseOffsetBranchOperandConstraint : public BranchOperandConstraint {
  public:
    BaseOffsetBranchOperandConstraint() : BranchOperandConstraint(), mpBase(nullptr), mpOffset(nullptr), mBaseValue(0) { } //!< Constructor.
    COPY_CONSTRUCTOR_ABSENT(BaseOffsetBranchOperandConstraint);
    SUBCLASS_DESTRUCTOR_DEFAULT(BaseOffsetBranchOperandConstraint); //!< Destructor.
    ASSIGNMENT_OPERATOR_ABSENT(BaseOffsetBranchOperandConstraint);

    void Setup(const Generator& rGen, const Instruction& rInstr, const OperandStructure& rOperandStruct) override; //!< Setup dynamic operand constraints.
    RegisterOperand* BaseOperand() const override { return mpBase; } //!< Return pointer to base operand if applicable.
    ImmediateOperand* OffsetOperand() const override { return mpOffset; } //!< Return pointer to immediate offset operand if applicable.
    void GetRegisterOperands(std::vector<const RegisterOperand*>& rRegOps) override { rRegOps.push_back(mpBase); } //!< Return pointer to immediate offset operand if applicable.
    void SetBaseValue(cuint64 baseValue) { mBaseValue = baseValue; } //!< Set base value.
    uint64 BaseValue() const { return mBaseValue; } //!< Return base value.
  private:
    RegisterOperand* mpBase; //!< Base sub operand
    ImmediateOperand* mpOffset; //!< Offset sub operand
    uint64 mBaseValue; //!< Value for base register
  };

  /*!
    \class ConditionalBranchOperandRISCVConstraint
    \brief This class carries dynamic constraint properties for ConditionalBranchOperandRISCV.
  */
  class ConditionalBranchOperandRISCVConstraint : public PcRelativeBranchOperandConstraint {
  public:
  ConditionalBranchOperandRISCVConstraint() : PcRelativeBranchOperandConstraint(), mTaken(false) { } //!< Constructor.
    virtual ~ConditionalBranchOperandRISCVConstraint() { } //!< Destructor.

    void Setup(const Generator& gen, const Instruction& instr, const OperandStructure& operandStruct) override; //!< Setup dynamic operand constraints for ConditionalBranchOperandRISCV.
    bool BranchTaken() const { return mTaken; } //!< Return true if branch is taken.
    virtual void SetConditionalBranchTaken(const Generator& gen, const Instruction& instr, const OperandStructure& operandStruct) = 0; //!< set condition branch taken or not taken by the current regsiter context
  protected:
    ConditionalBranchOperandRISCVConstraint(const ConditionalBranchOperandRISCVConstraint& rOther) //!< Copy constructor, not meant to be used.
      : PcRelativeBranchOperandConstraint(rOther), mTaken(false) { }
    
  protected:
    bool mTaken; //!< Indicate if branch is taken.
  };

  /*!
    \class CompressedRegisterOperandRISCVConstraint
    \brief The class (Setup method) translates GPR reserved register indices into Riscv compressed instruction set 'prime' register indices.
  */
  class CompressedRegisterOperandRISCVConstraint : public RegisterOperandConstraint {
  public:
    CompressedRegisterOperandRISCVConstraint() : RegisterOperandConstraint() { } //!< Constructor.
    ~CompressedRegisterOperandRISCVConstraint() { } //!< Destructor.
    ASSIGNMENT_OPERATOR_ABSENT(CompressedRegisterOperandRISCVConstraint);
    void Setup(const Generator& gen, const Instruction& instr, const OperandStructure& operandStruct) override; //!< Setup dynamic operand constraints.
  protected:
    CompressedRegisterOperandRISCVConstraint(const CompressedRegisterOperandRISCVConstraint& rOther) //!!< Copy constructor, not meant to be used.
      : RegisterOperandConstraint(rOther)
    {
    }
  };

  /*!
    \class VsetvlRegisterOperandConstraint
    \brief This class carries dynamic constraint properties for register operands for VSETVL and VSETVLI instructions.
  */
  class VsetvlRegisterOperandConstraint : public RegisterOperandConstraint {
  public:
    DEFAULT_CONSTRUCTOR_DEFAULT(VsetvlRegisterOperandConstraint);
    COPY_CONSTRUCTOR_ABSENT(VsetvlRegisterOperandConstraint);
    SUBCLASS_DESTRUCTOR_DEFAULT(VsetvlRegisterOperandConstraint);
    ASSIGNMENT_OPERATOR_ABSENT(VsetvlRegisterOperandConstraint);

    void Setup(const Generator& rGen, const Instruction& rInstr, const OperandStructure& rOperandStruct) override; //!< Setup dynamic operand constraints.
  };

  class VectorRegisterOperandConstraintRISCV : public VectorRegisterOperandConstraint {
  public:
    VectorRegisterOperandConstraintRISCV();
    COPY_CONSTRUCTOR_ABSENT(VectorRegisterOperandConstraintRISCV);
    SUBCLASS_DESTRUCTOR_DEFAULT(VectorRegisterOperandConstraintRISCV);
    ASSIGNMENT_OPERATOR_ABSENT(VectorRegisterOperandConstraintRISCV);
    void Setup(const Generator& gen, const Instruction& instr, const OperandStructure& operandStruct) override; //!< Setup dynamic operand constraints.
    float GetLayoutMultiple() const { return mLayoutMultiple; } //!< Return the multiple used to adjust the register operand layout.
  private:
    void GetAdjustedDifferValues(const Instruction& rInstr, const OperandConstraint& rDifferOprConstr, cuint64 differVal, ConstraintSet& rAdjDifferValues) const override; //!< Return a list of values to remove from the constraint set to avoid conflicting with the specified differ operand value.
    virtual float CalculateLayoutMultiple(const Generator& rGen, const Instruction& rInstr, const OperandStructure& rOperandStruct) const; //!< Determine the multiple used to adjust the register operand layout for wide and narrow register operands.
  private:
    float mLayoutMultiple; //!< Multiple used to adjust the register operand layout
  };

  /**!
    \class CompressedConditionalBranchOperandConstraint
    \brief Implements special behavior in SetConditionalBranchTaken(...) and branch type specific methods for the Compressed extension branch instructions.
  */
  class CompressedConditionalBranchOperandConstraint : public ConditionalBranchOperandRISCVConstraint {
  public:
    CompressedConditionalBranchOperandConstraint() : ConditionalBranchOperandRISCVConstraint() {} //!< Constructor
    ~CompressedConditionalBranchOperandConstraint() {} //!< Destructor

    void SetConditionalBranchTaken(const Generator& gen, const Instruction& instr, const OperandStructure& operandStruct) override; //!< set condition branch taken or not taken by the current regsiter context

  protected:
    void SetBranchTakenForCBEQZ(uint64 rs1Val); //!< Branch if rs1 is equal zero
    void SetBranchTakenForCBNEZ(uint64 rs1Val); //!< Branch if rs1 is not equal zero
  };

  /**!
    \class FullsizeConditionalBranchOperandConstraint
    \brief Implements special behavior in SetConditionalBranchTaken(...) and branch type speific methods for the RV64 full sized branch instructions. 
  */
  class FullsizeConditionalBranchOperandConstraint : public ConditionalBranchOperandRISCVConstraint {
  public:
    FullsizeConditionalBranchOperandConstraint() : ConditionalBranchOperandRISCVConstraint() {} //!< Constructor
    ~FullsizeConditionalBranchOperandConstraint() {} //!< Destructor

    void SetConditionalBranchTaken(const Generator& gen, const Instruction& instr, const OperandStructure& operandStruct) override; //!< set condition branch taken or not taken by the current regsiter context
  
  protected:
    void SetBranchTakenForBEQ(uint64 rs1Val, uint64 rs2Val); //!< Branch if rs1 and rs2 are equal
    void SetBranchTakenForBNE(uint64 rs1Val, uint64 rs2Val); //!< Branch if rs1 is not equal to rs2                                                     
    void SetBranchTakenForBLT(int64 rs1Val, int64 rs2Val); //!< Branch if rs1 is less than rs2, interpreting them as signed values                      
    void SetBranchTakenForBLTU(uint64 rs1Val, uint64 rs2Val); //!< Branch if rs1 is less than rs2, interpreting them as unsigned values                 
    void SetBranchTakenForBGE(int64 rs1Val, int64 rs2Val); //!< Branch if rs1 is greater than or equal to rs2, interpreting them as signed values
    void SetBranchTakenForBGEU(uint64 rs1Val, uint64 rs2Val); //!< Branch if rs1 is greater than or equal to rs2, interpreting them as unsigned values}
  };

  /*!
    \class VectorIndexedDataRegisterOperandConstraint
    \brief This class carries dynamic constraint properties for VectorIndexedDataRegisterOperand.
  */
  class VectorIndexedDataRegisterOperandConstraint : public VectorRegisterOperandConstraintRISCV {
  public:
    DEFAULT_CONSTRUCTOR_DEFAULT(VectorIndexedDataRegisterOperandConstraint);
    COPY_CONSTRUCTOR_ABSENT(VectorIndexedDataRegisterOperandConstraint);
    SUBCLASS_DESTRUCTOR_DEFAULT(VectorIndexedDataRegisterOperandConstraint);
    ASSIGNMENT_OPERATOR_ABSENT(VectorIndexedDataRegisterOperandConstraint);
  private:
    float CalculateLayoutMultiple(const Generator& rGen, const Instruction& rInstr, const OperandStructure& rOperandStruct) const override; //!< Determine the multiple used to adjust the register operand layout for wide and narrow register operands.
  };

}

#endif
