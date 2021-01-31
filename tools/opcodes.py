opcodes = {
    0x00: {'name': 'CBC_EXT_OPCODE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x01: {'name': 'CBC_JUMP_FORWARD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x02: {'name': 'CBC_JUMP_FORWARD_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x03: {'name': 'CBC_JUMP_FORWARD_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x04: {'name': 'CBC_POP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x05: {'name': 'CBC_JUMP_BACKWARD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x06: {'name': 'CBC_JUMP_BACKWARD_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x07: {'name': 'CBC_JUMP_BACKWARD_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x08: {'name': 'CBC_POP_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x09: {'name': 'CBC_BRANCH_IF_TRUE_FORWARD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x0A: {'name': 'CBC_BRANCH_IF_TRUE_FORWARD_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x0B: {'name': 'CBC_BRANCH_IF_TRUE_FORWARD_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x0C: {'name': 'CBC_THROW', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x0D: {'name': 'CBC_BRANCH_IF_TRUE_BACKWARD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x0E: {'name': 'CBC_BRANCH_IF_TRUE_BACKWARD_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x0F: {'name': 'CBC_BRANCH_IF_TRUE_BACKWARD_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x10: {'name': 'CBC_CONTEXT_END', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x11: {'name': 'CBC_BRANCH_IF_FALSE_FORWARD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x12: {'name': 'CBC_BRANCH_IF_FALSE_FORWARD_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x13: {'name': 'CBC_BRANCH_IF_FALSE_FORWARD_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x14: {'name': 'CBC_CREATE_OBJECT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x15: {'name': 'CBC_BRANCH_IF_FALSE_BACKWARD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x16: {'name': 'CBC_BRANCH_IF_FALSE_BACKWARD_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x17: {'name': 'CBC_BRANCH_IF_FALSE_BACKWARD_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x18: {'name': 'CBC_SET_PROPERTY', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x19: {'name': 'CBC_JUMP_FORWARD_EXIT_CONTEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x1A: {'name': 'CBC_JUMP_FORWARD_EXIT_CONTEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x1B: {'name': 'CBC_JUMP_FORWARD_EXIT_CONTEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x1C: {'name': 'CBC_CREATE_ARRAY', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x1D: {'name': 'CBC_BRANCH_IF_LOGICAL_TRUE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x1E: {'name': 'CBC_BRANCH_IF_LOGICAL_TRUE_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x1F: {'name': 'CBC_BRANCH_IF_LOGICAL_TRUE_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x20: {'name': 'CBC_ARRAY_APPEND', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x21: {'name': 'CBC_BRANCH_IF_LOGICAL_FALSE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x22: {'name': 'CBC_BRANCH_IF_LOGICAL_FALSE_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x23: {'name': 'CBC_BRANCH_IF_LOGICAL_FALSE_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x24: {'name': 'CBC_PUSH_ELISION', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x25: {'name': 'CBC_BRANCH_IF_STRICT_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x26: {'name': 'CBC_BRANCH_IF_STRICT_EQUAL_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x27: {'name': 'CBC_BRANCH_IF_STRICT_EQUAL_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x28: {'name': 'CBC_PUSH_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x29: {'name': 'CBC_PUSH_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x2A: {'name': 'CBC_PUSH_THIS_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x2B: {'name': 'CBC_PUSH_THREE_LITERALS', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x2C: {'name': 'CBC_PUSH_UNDEFINED', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x2D: {'name': 'CBC_PUSH_TRUE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x2E: {'name': 'CBC_PUSH_FALSE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x2F: {'name': 'CBC_PUSH_NULL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x30: {'name': 'CBC_PUSH_THIS', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x31: {'name': 'CBC_PUSH_NUMBER_0', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x32: {'name': 'CBC_PUSH_NUMBER_POS_BYTE', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x33: {'name': 'CBC_PUSH_NUMBER_NEG_BYTE', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x34: {'name': 'CBC_PUSH_PROP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x35: {'name': 'CBC_PUSH_PROP_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x36: {'name': 'CBC_PUSH_PROP_LITERAL_LITERAL', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x37: {'name': 'CBC_PUSH_PROP_THIS_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x38: {'name': 'CBC_PUSH_IDENT_REFERENCE', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x39: {'name': 'CBC_PUSH_PROP_REFERENCE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x3A: {'name': 'CBC_PUSH_PROP_LITERAL_REFERENCE', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x3B: {'name': 'CBC_PUSH_PROP_LITERAL_LITERAL_REFERENCE', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x3C: {'name': 'CBC_PUSH_PROP_THIS_LITERAL_REFERENCE', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x3D: {'name': 'CBC_NEW', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x3E: {'name': 'CBC_NEW0', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x3F: {'name': 'CBC_NEW1', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x40: {'name': 'CBC_EVAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x41: {'name': 'CBC_DEFINE_VARS', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x42: {'name': 'CBC_INITIALIZE_VAR', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x43: {'name': 'CBC_INITIALIZE_VARS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x44: {'name': 'CBC_SET_BYTECODE_PTR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x45: {'name': 'CBC_RETURN', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x46: {'name': 'CBC_RETURN_WITH_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x47: {'name': 'CBC_RETURN_WITH_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x48: {'name': 'CBC_SET_LITERAL_PROPERTY', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x49: {'name': 'CBC_BREAKPOINT_ENABLED', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x4A: {'name': 'CBC_BREAKPOINT_DISABLED', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x4B: {'name': 'CBC_PLUS', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x4C: {'name': 'CBC_PLUS_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x4D: {'name': 'CBC_NEGATE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x4E: {'name': 'CBC_NEGATE_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x4F: {'name': 'CBC_LOGICAL_NOT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x50: {'name': 'CBC_LOGICAL_NOT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x51: {'name': 'CBC_BIT_NOT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x52: {'name': 'CBC_BIT_NOT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x53: {'name': 'CBC_VOID', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x54: {'name': 'CBC_VOID_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x55: {'name': 'CBC_TYPEOF', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x56: {'name': 'CBC_TYPEOF_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x57: {'name': 'CBC_BIT_OR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x58: {'name': 'CBC_BIT_OR_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x59: {'name': 'CBC_BIT_OR_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x5A: {'name': 'CBC_BIT_XOR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x5B: {'name': 'CBC_BIT_XOR_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x5C: {'name': 'CBC_BIT_XOR_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x5D: {'name': 'CBC_BIT_AND', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x5E: {'name': 'CBC_BIT_AND_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x5F: {'name': 'CBC_BIT_AND_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x60: {'name': 'CBC_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x61: {'name': 'CBC_EQUAL_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x62: {'name': 'CBC_EQUAL_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x63: {'name': 'CBC_NOT_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x64: {'name': 'CBC_NOT_EQUAL_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x65: {'name': 'CBC_NOT_EQUAL_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x66: {'name': 'CBC_STRICT_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x67: {'name': 'CBC_STRICT_EQUAL_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x68: {'name': 'CBC_STRICT_EQUAL_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x69: {'name': 'CBC_STRICT_NOT_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x6A: {'name': 'CBC_STRICT_NOT_EQUAL_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x6B: {'name': 'CBC_STRICT_NOT_EQUAL_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x6C: {'name': 'CBC_LESS', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x6D: {'name': 'CBC_LESS_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x6E: {'name': 'CBC_LESS_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x6F: {'name': 'CBC_GREATER', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x70: {'name': 'CBC_GREATER_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x71: {'name': 'CBC_GREATER_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x72: {'name': 'CBC_LESS_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x73: {'name': 'CBC_LESS_EQUAL_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x74: {'name': 'CBC_LESS_EQUAL_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x75: {'name': 'CBC_GREATER_EQUAL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x76: {'name': 'CBC_GREATER_EQUAL_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x77: {'name': 'CBC_GREATER_EQUAL_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x78: {'name': 'CBC_IN', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x79: {'name': 'CBC_IN_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x7A: {'name': 'CBC_IN_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x7B: {'name': 'CBC_INSTANCEOF', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x7C: {'name': 'CBC_INSTANCEOF_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x7D: {'name': 'CBC_INSTANCEOF_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x7E: {'name': 'CBC_LEFT_SHIFT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x7F: {'name': 'CBC_LEFT_SHIFT_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x80: {'name': 'CBC_LEFT_SHIFT_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x81: {'name': 'CBC_RIGHT_SHIFT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x82: {'name': 'CBC_RIGHT_SHIFT_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x83: {'name': 'CBC_RIGHT_SHIFT_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x84: {'name': 'CBC_UNS_RIGHT_SHIFT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x85: {'name': 'CBC_UNS_RIGHT_SHIFT_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x86: {'name': 'CBC_UNS_RIGHT_SHIFT_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x87: {'name': 'CBC_ADD', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x88: {'name': 'CBC_ADD_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x89: {'name': 'CBC_ADD_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x8A: {'name': 'CBC_SUBTRACT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x8B: {'name': 'CBC_SUBTRACT_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x8C: {'name': 'CBC_SUBTRACT_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x8D: {'name': 'CBC_MULTIPLY', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x8E: {'name': 'CBC_MULTIPLY_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x8F: {'name': 'CBC_MULTIPLY_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x90: {'name': 'CBC_DIVIDE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x91: {'name': 'CBC_DIVIDE_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x92: {'name': 'CBC_DIVIDE_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x93: {'name': 'CBC_MODULO', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x94: {'name': 'CBC_MODULO_RIGHT_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x95: {'name': 'CBC_MODULO_TWO_LITERALS', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x96: {'name': 'CBC_DELETE_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x97: {'name': 'CBC_DELETE_IDENT_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x98: {'name': 'CBC_PRE_INCR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x99: {'name': 'CBC_PRE_INCR_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x9A: {'name': 'CBC_PRE_INCR_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x9B: {'name': 'CBC_PRE_INCR_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x9C: {'name': 'CBC_PRE_INCR_IDENT_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x9D: {'name': 'CBC_PRE_INCR_IDENT_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x9E: {'name': 'CBC_PRE_DECR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x9F: {'name': 'CBC_PRE_DECR_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xA0: {'name': 'CBC_PRE_DECR_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xA1: {'name': 'CBC_PRE_DECR_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xA2: {'name': 'CBC_PRE_DECR_IDENT_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xA3: {'name': 'CBC_PRE_DECR_IDENT_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xA4: {'name': 'CBC_POST_INCR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xA5: {'name': 'CBC_POST_INCR_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xA6: {'name': 'CBC_POST_INCR_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xA7: {'name': 'CBC_POST_INCR_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xA8: {'name': 'CBC_POST_INCR_IDENT_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xA9: {'name': 'CBC_POST_INCR_IDENT_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xAA: {'name': 'CBC_POST_DECR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xAB: {'name': 'CBC_POST_DECR_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xAC: {'name': 'CBC_POST_DECR_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xAD: {'name': 'CBC_POST_DECR_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xAE: {'name': 'CBC_POST_DECR_IDENT_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xAF: {'name': 'CBC_POST_DECR_IDENT_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xB0: {'name': 'CBC_CALL', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0xB1: {'name': 'CBC_CALL_PUSH_RESULT', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0xB2: {'name': 'CBC_CALL_BLOCK', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0xB3: {'name': 'CBC_CALL_PROP', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0xB4: {'name': 'CBC_CALL_PROP_PUSH_RESULT', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0xB5: {'name': 'CBC_CALL_PROP_BLOCK', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0xB6: {'name': 'CBC_CALL0', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xB7: {'name': 'CBC_CALL0_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xB8: {'name': 'CBC_CALL0_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xB9: {'name': 'CBC_CALL0_PROP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xBA: {'name': 'CBC_CALL0_PROP_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xBB: {'name': 'CBC_CALL0_PROP_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xBC: {'name': 'CBC_CALL1', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xBD: {'name': 'CBC_CALL1_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xBE: {'name': 'CBC_CALL1_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xBF: {'name': 'CBC_CALL1_PROP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC0: {'name': 'CBC_CALL1_PROP_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC1: {'name': 'CBC_CALL1_PROP_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC2: {'name': 'CBC_CALL2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC3: {'name': 'CBC_CALL2_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC4: {'name': 'CBC_CALL2_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC5: {'name': 'CBC_CALL2_PROP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC6: {'name': 'CBC_CALL2_PROP_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC7: {'name': 'CBC_CALL2_PROP_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC8: {'name': 'CBC_ASSIGN', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xC9: {'name': 'CBC_ASSIGN_PUSH_RESULT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xCA: {'name': 'CBC_ASSIGN_BLOCK', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0xCB: {'name': 'CBC_ASSIGN_SET_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xCC: {'name': 'CBC_ASSIGN_SET_IDENT_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xCD: {'name': 'CBC_ASSIGN_SET_IDENT_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xCE: {'name': 'CBC_ASSIGN_LITERAL_SET_IDENT', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0xCF: {'name': 'CBC_ASSIGN_LITERAL_SET_IDENT_PUSH_RESULT', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0xD0: {'name': 'CBC_ASSIGN_LITERAL_SET_IDENT_BLOCK', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0xD1: {'name': 'CBC_ASSIGN_PROP_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xD2: {'name': 'CBC_ASSIGN_PROP_LITERAL_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xD3: {'name': 'CBC_ASSIGN_PROP_LITERAL_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xD4: {'name': 'CBC_ASSIGN_PROP_THIS_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xD5: {'name': 'CBC_ASSIGN_PROP_THIS_LITERAL_PUSH_RESULT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xD6: {'name': 'CBC_ASSIGN_PROP_THIS_LITERAL_BLOCK', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0xD7: {'name': 'CBC_MOV_IDENT', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
}

opcodes_ext = {
    0x00: {'name': 'CBC_EXT_NOP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x01: {'name': 'CBC_EXT_WITH_CREATE_CONTEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x02: {'name': 'CBC_EXT_WITH_CREATE_CONTEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x03: {'name': 'CBC_EXT_WITH_CREATE_CONTEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x04: {'name': 'CBC_EXT_FOR_IN_GET_NEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x05: {'name': 'CBC_EXT_FOR_IN_CREATE_CONTEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x06: {'name': 'CBC_EXT_FOR_IN_CREATE_CONTEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x07: {'name': 'CBC_EXT_FOR_IN_CREATE_CONTEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x08: {'name': 'CBC_EXT_SET_GETTER', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x09: {'name': 'CBC_EXT_BRANCH_IF_FOR_IN_HAS_NEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x0A: {'name': 'CBC_EXT_BRANCH_IF_FOR_IN_HAS_NEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x0B: {'name': 'CBC_EXT_BRANCH_IF_FOR_IN_HAS_NEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x0C: {'name': 'CBC_EXT_FOR_OF_GET_NEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x0D: {'name': 'CBC_EXT_FOR_OF_CREATE_CONTEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x0E: {'name': 'CBC_EXT_FOR_OF_CREATE_CONTEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x0F: {'name': 'CBC_EXT_FOR_OF_CREATE_CONTEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x10: {'name': 'CBC_EXT_PUSH_NAMED_FUNC_EXPRESSION', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x11: {'name': 'CBC_EXT_BRANCH_IF_FOR_OF_HAS_NEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x12: {'name': 'CBC_EXT_BRANCH_IF_FOR_OF_HAS_NEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x13: {'name': 'CBC_EXT_BRANCH_IF_FOR_OF_HAS_NEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x14: {'name': 'CBC_EXT_SET_SETTER', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x15: {'name': 'CBC_EXT_TRY_CREATE_CONTEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x16: {'name': 'CBC_EXT_TRY_CREATE_CONTEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x17: {'name': 'CBC_EXT_TRY_CREATE_CONTEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x18: {'name': 'CBC_EXT_THROW_REFERENCE_ERROR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x19: {'name': 'CBC_EXT_CATCH', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x1A: {'name': 'CBC_EXT_CATCH_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x1B: {'name': 'CBC_EXT_CATCH_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x1C: {'name': 'CBC_EXT_PUSH_UNDEFINED_BASE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x1D: {'name': 'CBC_EXT_FINALLY', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x1E: {'name': 'CBC_EXT_FINALLY_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x1F: {'name': 'CBC_EXT_FINALLY_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x20: {'name': 'CBC_EXT_CLASS_EXPR_CONTEXT_END', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x21: {'name': 'CBC_EXT_SUPER_CLASS_CREATE_CONTEXT', 'literal_args': 0, 'byte_args': 0, 'branch_args': 1},
    0x22: {'name': 'CBC_EXT_SUPER_CLASS_CREATE_CONTEXT_2', 'literal_args': 0, 'byte_args': 0, 'branch_args': 2},
    0x23: {'name': 'CBC_EXT_SUPER_CLASS_CREATE_CONTEXT_3', 'literal_args': 0, 'byte_args': 0, 'branch_args': 3},
    0x24: {'name': 'CBC_EXT_PUSH_LITERAL_PUSH_NUMBER_0', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x25: {'name': 'CBC_EXT_PUSH_LITERAL_PUSH_NUMBER_POS_BYTE', 'literal_args': 1, 'byte_args': 1, 'branch_args': 0},
    0x26: {'name': 'CBC_EXT_PUSH_LITERAL_PUSH_NUMBER_NEG_BYTE', 'literal_args': 1, 'byte_args': 1, 'branch_args': 0},
    0x27: {'name': 'CBC_EXT_RESOURCE_NAME', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x28: {'name': 'CBC_EXT_LINE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x29: {'name': 'CBC_EXT_SET_COMPUTED_PROPERTY', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x2A: {'name': 'CBC_EXT_SET_COMPUTED_PROPERTY_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x2B: {'name': 'CBC_EXT_SET_COMPUTED_GETTER', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x2C: {'name': 'CBC_EXT_SET_COMPUTED_SETTER', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x2D: {'name': 'CBC_EXT_SET_STATIC_PROPERTY_LITERAL', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x2E: {'name': 'CBC_EXT_SET_STATIC_COMPUTED_PROPERTY_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x2F: {'name': 'CBC_EXT_SET_STATIC_GETTER', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x30: {'name': 'CBC_EXT_SET_STATIC_SETTER', 'literal_args': 2, 'byte_args': 0, 'branch_args': 0},
    0x31: {'name': 'CBC_EXT_SET_STATIC_COMPUTED_GETTER', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x32: {'name': 'CBC_EXT_SET_STATIC_COMPUTED_SETTER', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x33: {'name': 'CBC_EXT_RESOLVE_BASE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x34: {'name': 'CBC_EXT_INHERIT_AND_SET_CONSTRUCTOR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x35: {'name': 'CBC_EXT_PUSH_CLASS_CONSTRUCTOR_AND_PROTOTYPE', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x36: {'name': 'CBC_EXT_IMPLICIT_CONSTRUCTOR_CALL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x37: {'name': 'CBC_EXT_SET_CLASS_LITERAL', 'literal_args': 1, 'byte_args': 0, 'branch_args': 0},
    0x38: {'name': 'CBC_EXT_CLASS_EVAL', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x39: {'name': 'CBC_EXT_SUPER_CALL', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x3A: {'name': 'CBC_EXT_SUPER_CALL_PUSH_RESULT', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x3B: {'name': 'CBC_EXT_SUPER_CALL_BLOCK', 'literal_args': 0, 'byte_args': 1, 'branch_args': 0},
    0x3C: {'name': 'CBC_EXT_PUSH_CONSTRUCTOR_SUPER', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x3D: {'name': 'CBC_EXT_PUSH_CONSTRUCTOR_SUPER_PROP', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x3E: {'name': 'CBC_EXT_PUSH_SUPER', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x3F: {'name': 'CBC_EXT_PUSH_STATIC_SUPER', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x40: {'name': 'CBC_EXT_PUSH_CONSTRUCTOR_THIS', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x41: {'name': 'CBC_EXT_SUPER_PROP_CALL', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x42: {'name': 'CBC_EXT_SUPER_PROP_ASSIGN', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x43: {'name': 'CBC_EXT_CONSTRUCTOR_RETURN', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
    0x44: {'name': 'CBC_EXT_ERROR', 'literal_args': 0, 'byte_args': 0, 'branch_args': 0},
}
