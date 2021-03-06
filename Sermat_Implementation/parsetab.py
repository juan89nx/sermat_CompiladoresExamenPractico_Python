
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'DA7161DBBC6D45DD8A5996447C2A029E'
    
_lr_action_items = {'NULL':([0,3,7,13,19,27,28,31,35,40,41,43,44,45,46,],[5,-19,5,5,5,-26,-24,5,-20,5,5,-25,-23,5,5,]),'FALSE':([0,3,7,13,19,27,28,31,35,40,41,43,44,45,46,],[15,-19,15,15,15,-26,-24,15,-20,15,15,-25,-23,15,15,]),'LEFT_PAR':([11,12,34,36,],[27,28,43,44,]),'RIGHT_BRACE':([1,2,4,5,8,9,10,11,15,18,20,22,24,29,32,33,47,48,49,50,],[-13,-6,-1,-5,-3,22,24,-4,-2,-10,-9,-8,-7,-11,-12,-14,-16,-15,-18,-17,]),'EQUALS':([2,],[17,]),'RIGHT_BRACK':([2,3,4,5,6,7,8,11,15,18,20,21,22,24,29,32,35,37,],[-6,-19,-1,-5,18,20,-3,-4,-2,-10,-9,-22,-8,-7,-11,-12,-20,-21,]),'NUM':([0,3,7,13,19,27,28,31,35,40,41,43,44,45,46,],[8,-19,8,8,8,-26,-24,8,-20,8,8,-25,-23,8,8,]),'COMMA':([2,4,5,6,8,9,11,14,15,18,20,21,22,24,29,30,32,37,42,47,48,49,50,],[-6,-1,-5,19,-3,23,-4,31,-2,-10,-9,-22,-8,-7,-11,-28,-12,-21,-27,-16,-15,-18,-17,]),'LEFT_BRACE':([0,3,7,13,17,19,27,28,31,35,40,41,43,44,45,46,],[1,-19,1,1,33,1,-26,-24,1,-20,1,1,-25,-23,1,1,]),'STR':([0,1,3,7,10,13,17,19,23,27,28,31,33,35,40,41,43,44,45,46,],[11,-13,-19,11,25,11,34,11,38,-26,-24,11,-14,-20,11,11,-25,-23,11,11,]),'RIGHT_PAR':([2,4,5,8,11,13,14,15,18,20,22,24,27,28,29,30,32,42,43,44,],[-6,-1,-5,-3,-4,29,32,-2,-10,-9,-8,-7,-26,-24,-11,-28,-12,-27,-25,-23,]),'COLON':([25,26,38,39,],[40,41,45,46,]),'BINDINGS':([0,3,7,13,19,27,28,31,35,40,41,43,44,45,46,],[2,-19,2,2,2,-26,-24,2,-20,2,2,-25,-23,2,2,]),'LEFT_BRACK':([0,3,7,13,17,19,27,28,31,35,40,41,43,44,45,46,],[3,-19,3,3,35,3,-26,-24,3,-20,3,3,-25,-23,3,3,]),'TRUE':([0,3,7,13,19,27,28,31,35,40,41,43,44,45,46,],[4,-19,4,4,4,-26,-24,4,-20,4,4,-25,-23,4,4,]),'ID':([0,1,3,7,10,13,17,19,23,27,28,31,33,35,40,41,43,44,45,46,],[12,-13,-19,12,26,12,36,12,39,-26,-24,12,-14,-20,12,12,-25,-23,12,12,]),'$end':([2,4,5,8,11,15,16,18,20,22,24,29,32,],[-6,-1,-5,-3,-4,-2,0,-10,-9,-8,-7,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'obj1':([0,7,13,19,31,40,41,45,46,],[9,9,9,9,9,9,9,9,9,]),'obj0':([0,7,13,19,31,40,41,45,46,],[10,10,10,10,10,10,10,10,10,]),'cons1':([0,7,13,19,31,40,41,45,46,],[14,14,14,14,14,14,14,14,14,]),'cons0':([0,7,13,19,31,40,41,45,46,],[13,13,13,13,13,13,13,13,13,]),'array1':([0,7,13,19,31,40,41,45,46,],[6,6,6,6,6,6,6,6,6,]),'array0':([0,7,13,19,31,40,41,45,46,],[7,7,7,7,7,7,7,7,7,]),'value':([0,7,13,19,31,40,41,45,46,],[16,21,30,37,42,47,48,49,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> value","S'",1,None,None,None),
  ('value -> TRUE','value',1,'p_value_boolNumStrNull','sermatParserCup.py',113),
  ('value -> FALSE','value',1,'p_value_boolNumStrNull','sermatParserCup.py',114),
  ('value -> NUM','value',1,'p_value_boolNumStrNull','sermatParserCup.py',115),
  ('value -> STR','value',1,'p_value_boolNumStrNull','sermatParserCup.py',116),
  ('value -> NULL','value',1,'p_value_boolNumStrNull','sermatParserCup.py',117),
  ('value -> BINDINGS','value',1,'p_value_bind','sermatParserCup.py',121),
  ('value -> obj0 RIGHT_BRACE','value',2,'p_value_obj0','sermatParserCup.py',125),
  ('value -> obj1 RIGHT_BRACE','value',2,'p_value_obj1','sermatParserCup.py',129),
  ('value -> array0 RIGHT_BRACK','value',2,'p_value_array0','sermatParserCup.py',133),
  ('value -> array1 RIGHT_BRACK','value',2,'p_value_array1','sermatParserCup.py',137),
  ('value -> cons0 RIGHT_PAR','value',2,'p_value_cons0','sermatParserCup.py',141),
  ('value -> cons1 RIGHT_PAR','value',2,'p_value_cons1','sermatParserCup.py',148),
  ('obj0 -> LEFT_BRACE','obj0',1,'p_obj0','sermatParserCup.py',155),
  ('obj0 -> BINDINGS EQUALS LEFT_BRACE','obj0',3,'p_obj0','sermatParserCup.py',156),
  ('obj1 -> obj0 ID COLON value','obj1',4,'p_obj1_A','sermatParserCup.py',163),
  ('obj1 -> obj0 STR COLON value','obj1',4,'p_obj1_B','sermatParserCup.py',168),
  ('obj1 -> obj1 COMMA ID COLON value','obj1',5,'p_obj1_C','sermatParserCup.py',173),
  ('obj1 -> obj1 COMMA STR COLON value','obj1',5,'p_obj1_D','sermatParserCup.py',178),
  ('array0 -> LEFT_BRACK','array0',1,'p_array0','sermatParserCup.py',184),
  ('array0 -> BINDINGS EQUALS LEFT_BRACK','array0',3,'p_array0','sermatParserCup.py',185),
  ('array1 -> array1 COMMA value','array1',3,'p_array1_COMMA','sermatParserCup.py',192),
  ('array1 -> array0 value','array1',2,'p_array1','sermatParserCup.py',197),
  ('cons0 -> BINDINGS EQUALS ID LEFT_PAR','cons0',4,'p_cons0_ID','sermatParserCup.py',205),
  ('cons0 -> ID LEFT_PAR','cons0',2,'p_cons0_ID','sermatParserCup.py',206),
  ('cons0 -> BINDINGS EQUALS STR LEFT_PAR','cons0',4,'p_cons0_STR','sermatParserCup.py',218),
  ('cons0 -> STR LEFT_PAR','cons0',2,'p_cons0_STR','sermatParserCup.py',219),
  ('cons1 -> cons1 COMMA value','cons1',3,'p_cons1','sermatParserCup.py',230),
  ('cons1 -> cons0 value','cons1',2,'p_cons1','sermatParserCup.py',231),
]
