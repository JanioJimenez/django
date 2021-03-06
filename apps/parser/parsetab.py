
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftSUMARESTAleftMULTIPLICACIONDIVICIONrightUMINUSCOMA COMILLA DIVICION DOSPUN IDENTIFICADOR IGUAL LCORCH LLLAVE LPAREN MULTIPLICACION NUMERO RCORCH RESTA RLLAVE RPAREN STRING SUMAstatement : IDENTIFICADOR IGUAL expressionstatement : expressionexpression : expression RESTA expression\n                  | expression SUMA expression\n                  | expression MULTIPLICACION expression\n                  | expression DIVICION expressionexpression : RESTA expression %prec UMINUSexpression : LPAREN expression RPARENexpression : NUMEROexpression : jsonexpression : IDENTIFICADORjson : LLLAVE sentencia RLLAVEsentencia : arreglo COMA sentencia\n                 | arreglo\n                 | objeto COMA sentencia\n                 | objetoarreglo : COMILLA STRING COMILLA DOSPUN LCORCH vector RCORCH\n               | COMILLA STRING COMILLA DOSPUN LCORCH matriz RCORCHvector : objeto COMA vector\n              | objetomatriz : json COMA matriz\n              | jsonobjeto : COMILLA STRING COMILLA DOSPUN COMILLA NUMERO COMILLA\n              | COMILLA STRING COMILLA DOSPUN COMILLA STRING COMILLA'
    
_lr_action_items = {'IDENTIFICADOR':([0,4,5,9,10,11,12,13,],[2,15,15,15,15,15,15,15,]),'RESTA':([0,2,3,4,5,6,7,9,10,11,12,13,14,15,16,21,22,23,24,25,26,27,],[4,-11,10,4,4,-9,-10,4,4,4,4,4,-7,-11,10,10,-3,-4,-5,-6,-8,-12,]),'LPAREN':([0,4,5,9,10,11,12,13,],[5,5,5,5,5,5,5,5,]),'NUMERO':([0,4,5,9,10,11,12,13,35,],[6,6,6,6,6,6,6,6,38,]),'LLLAVE':([0,4,5,9,10,11,12,13,36,50,],[8,8,8,8,8,8,8,8,8,8,]),'$end':([1,2,3,6,7,14,15,21,22,23,24,25,26,27,],[0,-11,-2,-9,-10,-7,-11,-1,-3,-4,-5,-6,-8,-12,]),'IGUAL':([2,],[9,]),'SUMA':([2,3,6,7,14,15,16,21,22,23,24,25,26,27,],[-11,11,-9,-10,-7,-11,11,11,-3,-4,-5,-6,-8,-12,]),'MULTIPLICACION':([2,3,6,7,14,15,16,21,22,23,24,25,26,27,],[-11,12,-9,-10,-7,-11,12,12,12,12,-5,-6,-8,-12,]),'DIVICION':([2,3,6,7,14,15,16,21,22,23,24,25,26,27,],[-11,13,-9,-10,-7,-11,13,13,13,13,-5,-6,-8,-12,]),'RPAREN':([6,7,14,15,16,22,23,24,25,26,27,],[-9,-10,-7,-11,26,-3,-4,-5,-6,-8,-12,]),'COMILLA':([8,28,29,30,34,36,37,38,46,49,54,],[20,20,20,33,35,39,44,45,51,39,35,]),'RLLAVE':([17,18,19,31,32,44,45,47,48,],[27,-14,-16,-13,-15,-24,-23,-17,-18,]),'COMA':([18,19,27,42,43,44,45,47,48,],[28,29,-12,49,50,-24,-23,-17,-18,]),'STRING':([20,35,39,],[30,37,46,]),'RCORCH':([27,40,41,42,43,44,45,52,53,],[-12,47,48,-20,-22,-24,-23,-19,-21,]),'DOSPUN':([33,51,],[34,54,]),'LCORCH':([34,],[36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,4,5,9,10,11,12,13,],[3,14,16,21,22,23,24,25,]),'json':([0,4,5,9,10,11,12,13,36,50,],[7,7,7,7,7,7,7,7,43,43,]),'sentencia':([8,28,29,],[17,31,32,]),'arreglo':([8,28,29,],[18,18,18,]),'objeto':([8,28,29,36,49,],[19,19,19,42,42,]),'vector':([36,49,],[40,52,]),'matriz':([36,50,],[41,53,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> IDENTIFICADOR IGUAL expression','statement',3,'p_statement_assign','parser.py',95),
  ('statement -> expression','statement',1,'p_statement_expr','parser.py',99),
  ('expression -> expression RESTA expression','expression',3,'p_expression_binop','parser.py',103),
  ('expression -> expression SUMA expression','expression',3,'p_expression_binop','parser.py',104),
  ('expression -> expression MULTIPLICACION expression','expression',3,'p_expression_binop','parser.py',105),
  ('expression -> expression DIVICION expression','expression',3,'p_expression_binop','parser.py',106),
  ('expression -> RESTA expression','expression',2,'p_expression_uminus','parser.py',113),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','parser.py',117),
  ('expression -> NUMERO','expression',1,'p_expression_number','parser.py',121),
  ('expression -> json','expression',1,'p_expression_json','parser.py',125),
  ('expression -> IDENTIFICADOR','expression',1,'p_expression_name','parser.py',129),
  ('json -> LLLAVE sentencia RLLAVE','json',3,'p_json_','parser.py',137),
  ('sentencia -> arreglo COMA sentencia','sentencia',3,'p_json_sentencia','parser.py',141),
  ('sentencia -> arreglo','sentencia',1,'p_json_sentencia','parser.py',142),
  ('sentencia -> objeto COMA sentencia','sentencia',3,'p_json_sentencia','parser.py',143),
  ('sentencia -> objeto','sentencia',1,'p_json_sentencia','parser.py',144),
  ('arreglo -> COMILLA STRING COMILLA DOSPUN LCORCH vector RCORCH','arreglo',7,'p_json_arreglo','parser.py',147),
  ('arreglo -> COMILLA STRING COMILLA DOSPUN LCORCH matriz RCORCH','arreglo',7,'p_json_arreglo','parser.py',148),
  ('vector -> objeto COMA vector','vector',3,'p_json_vector','parser.py',151),
  ('vector -> objeto','vector',1,'p_json_vector','parser.py',152),
  ('matriz -> json COMA matriz','matriz',3,'p_json_matriz','parser.py',155),
  ('matriz -> json','matriz',1,'p_json_matriz','parser.py',156),
  ('objeto -> COMILLA STRING COMILLA DOSPUN COMILLA NUMERO COMILLA','objeto',7,'p_json_objeto','parser.py',159),
  ('objeto -> COMILLA STRING COMILLA DOSPUN COMILLA STRING COMILLA','objeto',7,'p_json_objeto','parser.py',160),
]
