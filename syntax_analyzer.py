import sys
from graphviz import Digraph

# 각 생성 규칙의 RHS의 길이를 담고 있는 리스트
production_rules = [
    2,  # 0. CODE -> DECL CODE
    0,  # 1. CODE -> ''
    2,  # 2. DECL -> VDECL semi
    1,  # 3. DECL -> FDECL
    2,  # 4. VDECL -> vtype id
    2,  # 5. VDECL -> vtype ASSIGN
    3,  # 6. ASSIGN -> id assign RHS
    9,  # 7. FDECL -> vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
    1,  # 8. RHS -> EXPR
    1,  # 9. RHS -> literal
    1,  # 10. RHS -> character
    1,  # 11. RHS -> boolstr
    1,  # 12. EXPR -> TERM
    3,  # 13. EXPR -> EXPR addsub TERM
    1,  # 14. TERM -> FACTOR
    3,  # 15. TERM -> TERM multdiv FACTOR
    3,  # 16. FACTOR -> lparen EXPR rparen
    1,  # 17. FACTOR -> id
    1,  # 18. FACTOR -> num
    3,  # 19. ARG -> vtype id MOREARGS
    0,  # 20. ARG -> ''
    4,  # 21. MOREARGS -> comma vtype id MOREARGS
    0,  # 22. MOREARGS -> ''
    2,  # 23. BLOCK -> STMT BLOCK
    0,  # 24. BLOCK -> ''
    2,  # 25. STMT -> STMT' semi
    8,  # 26. STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE
    7,  # 27. STMT -> while lparen COND rparen lbrace BLOCK rbrace
    1,  # 28. STMT' -> VDECL
    1,  # 29. STMT' -> ASSIGN
    3,  # 30. COND -> COND comp COND'
    1,  # 31. COND -> COND'
    1,  # 32. COND' -> boolstr
    4,  # 33. ELSE -> else lbrace BLOCK rbrace
    0,  # 34. ELSE -> ''
    3   # 35. RETURN -> return RHS semi
]

# 각 생성 규칙의 LHS를 담고 있는 리스트
production_lhs = [
    'CODE', 'CODE', 'DECL', 'DECL', 'VDECL',
    'VDECL', 'ASSIGN', 'FDECL', 'RHS', 'RHS', 
    'RHS', 'RHS', 'EXPR', 'EXPR', 'TERM',
    'TERM', 'FACTOR', 'FACTOR', 'FACTOR', 'ARG',
    'ARG', 'MOREARGS', 'MOREARGS', 'BLOCK', 'BLOCK',
    'STMT', 'STMT', 'STMT', 'STMT\'', 'STMT\'',
    'COND', 'COND', 'COND\'', 'ELSE', 'ELSE',
    'RETURN'
]


# Action 테이블 ('state', 'input symbol') : ('rule', new state)
action_table = {
    (0, 'vtype'): ('shift', 4),
    (1, 'vtype'): ('shift', 4),    (1, '$'): ('reduce', 1),
    (2, 'semi'): ('shift', 6),
    (3, 'vtype'): ('reduce', 3),    (3, '$'): ('reduce', 3),
    (4, 'id'): ('shift', 7),
    (5, '$'): ('accept', None),
    (6, 'vtype'): ('reduce', 2),    (6, '$'): ('reduce', 2),
    (7, 'semi'): ('reduce', 4),    (7, 'assign'): ('shift', 10),    (7, 'lparen'): ('shift', 9),
    (8, 'semi'): ('reduce', 5),
    (9, 'vtype'): ('shift', 12),    (9, 'rparen'): ('reduce', 20),
    (10, 'id'): ('shift', 21),    (10, 'lparen'): ('shift', 20),    (10, 'literal'): ('shift', 15),    (10, 'character'): ('shift', 16),    (10, 'boolstr'): ('shift', 17),    (10, 'num'): ('shift', 22),
    (11, 'rparen'): ('shift', 23),
    (12, 'id'): ('shift', 24),    
    (13, 'semi'): ('reduce', 6), 
    (14, 'semi'): ('reduce', 8),    (14, 'addsub'): ('shift', 25),
    (15, 'semi'): ('reduce', 9),
    (16, 'semi'): ('reduce', 10),
    (17, 'semi'): ('reduce', 11),
    (18, 'semi'): ('reduce', 12),   (18, 'rparen'): ('reduce', 12),    (18, 'addsub'): ('reduce', 12),    (18, 'multdiv'): ('reduce', 26),
    (19, 'semi'): ('reduce', 14),   (19, 'rparen'): ('reduce', 14),    (19, 'addsub'): ('reduce', 14),    (19, 'multdiv'): ('reduce', 14),
    (20, 'id'): ('shift', 21),    (20, 'lparen'): ('shift', 20),    (20, 'num'): ('shift', 22),
    (21, 'semi'): ('reduce', 17),   (21, 'rparen'): ('reduce', 17),    (21, 'addsub'): ('reduce', 17),    (21, 'multdiv'): ('reduce', 17),
    (22, 'semi'): ('reduce', 18),   (22, 'rparen'): ('reduce', 18),    (22, 'addsub'): ('reduce', 18),    (22, 'multdiv'): ('reduce', 18),
    (23, 'lbrace'): ('shift', 28),
    (24, 'rparen'): ('reduce', 22),   (24, 'comma'): ('shift', 30),
    (25, 'id'): ('shift', 21),    (25, 'lparen'): ('shift', 20),   (25, 'num'): ('shift', 22),
    (26, 'id'): ('shift', 21),    (26, 'lparen'): ('shift', 20),   (26, 'num'): ('shift', 22),
    
    (27, 'rparen'): ('shift', 33),    (27, 'addsub'): ('shift', 25),
    (28, 'vtype'): ('shift', 41),    (28, 'id'): ('shift', 42),    (28, 'rbrace'): ('reduce', 24),    (28, 'if'): ('shift', 37),    (28, 'while'): ('shift', 38),    (28, 'return'): ('reduce', 24),
    (29, 'rparen'): ('reduce', 19),
    (30, 'vtype'): ('shift', 43),
    (31, 'semi'): ('reduce', 13),    (31, 'rparen'): ('reduce', 13),    (31, 'addsub'): ('reduce', 13),    (31, 'multdiv'): ('shift', 26),
    (32, 'semi'): ('reduce', 15),    (32, 'rparen'): ('reduce', 15),    (32, 'addsub'): ('reduce', 15),    (32, 'multdiv'): ('reduce', 15),
    (33, 'semi'): ('reduce', 16),    (33, 'rparen'): ('reduce', 16),    (33, 'addsub'): ('reduce', 16),    (33, 'multdiv'): ('reduce', 16),
    (34, 'return'): ('shift', 45),
    (35, 'vtype'): ('shift', 41),    (35, 'id'): ('shift', 42),    (35, 'rbrace'): ('reduce', 24),    (35, 'if'): ('shift', 37),    (35, 'while'): ('shift', 38),    (35, 'return'): ('reduce', 24),
    (36, 'semi'): ('shift', 47),
    (37, 'lparen'): ('shift', 48),
    (38, 'lparen'): ('shift', 49),
    (39, 'semi'): ('reduce', 28),
    (40, 'semi'): ('reduce', 29),
    (41, 'id'): ('shift', 50),
    (42, 'assign'): ('shift', 10),
    (43, 'id'): ('shift', 51),
    (44, 'rbrace'): ('shift', 52),
    (45, 'id'): ('shift', 21),    (45, 'lparen'): ('shift', 20),    (45, 'literal'): ('shift', 15),    (45, 'character'): ('shift', 16),    (45, 'boolstr'): ('shift', 17),    (45, 'num'): ('shift', 22),    
    (46, 'rbrace'): ('reduce', 23),    (46, 'return'): ('reduce', 23),
    (47, 'vtype'): ('reduce', 25),    (47, 'id'): ('reduce', 25),    (47, 'rbrace'): ('reduce', 25), (47, 'if'): ('reduce', 25), (47, 'while'): ('reduce', 25), (47, 'return'): ('reduce', 25),
    (48, 'boolstr'): ('shift', 56),
    (49, 'boolstr'): ('shift', 56),
    (50, 'semi'): ('reduce', 4),    (50, 'assign'): ('shift', 10),
    (51, 'rparen'): ('reduce', 22),    (51, 'comma'): ('shift', 30),    
    (52, 'vtype'): ('reduce', 7),    (52, '$'): ('reduce', 7),
    (53, 'semi'): ('shift', 59),
    (54, 'rparen'): ('shift', 60),    (54, 'comp'): ('shift', 61),
    (55, 'rparen'): ('reduce', 31),    (55, 'comp'): ('reduce', 31),
    (56, 'rparen'): ('reduce', 32),    (56, 'comp'): ('reduce', 32),
    (57, 'rparen'): ('shift', 62),    (57, 'comp'): ('shift', 61),
    (58, 'rparen'): ('reduce', 21),
    (59, 'rbrace'): ('reduce', 35),
    (60, 'lbrace'): ('shift', 63),
    (61, 'boolstr'): ('shift', 56),
    (62, 'lbrace'): ('shift', 65),
    (63, 'vtype'): ('shift', 41),    (63, 'id'): ('shift', 42),    (63, 'rbrace'): ('reduce', 24),    (63, 'if'): ('shift', 37),    (63, 'while'): ('shift', 38),    (63, 'return'): ('reduce', 24),
    (64, 'rparen'): ('reduce', 30),    (64, 'comp'): ('reduce', 30),
    (65, 'semi'): ('shift', 41),    (65, 'id'): ('shift', 42),    (65, 'rbrace'): ('reduce', 24),    (65, 'if'): ('shift', 37),    (65, 'while'): ('shift', 38),    (65, 'return'): ('reduce', 24),
    (66, 'rbrace'): ('shift', 68),
    (67, 'rbrace'): ('shift', 69),
    (68, 'vtype'): ('reduce', 34),    (68, 'id'): ('reduce', 34),    (68, 'rbrace'): ('reduce', 34),    (68, 'if'): ('reduce', 34),    (68, 'while'): ('reduce', 34),    (68, 'else'): ('shift', 71),    (68, 'return'): ('reduce', 34),
    (69, 'vtype'): ('reduce', 27),    (69, 'id'): ('reduce', 27),    (69, 'rbrace'): ('reduce', 27),    (69, 'if'): ('reduce', 27),    (69, 'while'): ('reduce', 27),    (69, 'return'): ('reduce', 27),
    (70, 'vtype'): ('reduce', 26),    (70, 'id'): ('reduce', 26),    (70, 'rbrace'): ('reduce', 26),    (70, 'if'): ('reduce', 26),    (70, 'while'): ('reduce', 26),    (70, 'return'): ('reduce', 26),
    (71, 'lbrace'): ('shift', 72),
    (72, 'vtype'): ('shift', 41),    (72, 'id'): ('shift', 42),    (72, 'rbrace'): ('reduce', 24),    (72, 'if'): ('shift', 37),    (72, 'while'): ('shift', 38),    (72, 'return'): ('reduce', 24),
    (73, 'rbrace'): ('shift', 74),
    (74, 'vtype'): ('reduce', 33),    (74, 'id'): ('reduce', 33),    (74, 'rbrace'): ('reduce', 33),    (74, 'if'): ('reduce', 33),    (74, 'while'): ('reduce', 33),    (74, 'return'): ('reduce', 33),
}

# Goto 테이블 ('state', 'input symbol') : new state
goto_table = {
    (0, 'DECL'): 1,    (0, 'VDECL'): 2,    (0, 'FDECL'): 3,
    (1, 'CODE'): 5,    (1, 'DECL'): 1,    (1, 'VDECL'): 2,     (1, 'FDECL'): 3,
    (4, 'ASSIGN'): 8,
    (9, 'ARG'): 11,
    (10, 'RHS'): 13,    (10, 'EXPR'): 14,    (10, 'TERM'): 18,    (10, 'FACTOR'): 19,
    (20, 'EXPR'): 27,    (20, 'TERM'): 18,    (20, 'FACTOR'): 19,
    (24, 'MOREARGS'): 29,
    (25, 'TERM'): 31,    (25, 'FACTOR'): 19,
    (26, 'FACTOR'): 32,
    (28, 'VDECL'): 39,    (28, 'ASSIGN'): 40,    (28, 'BLOCK'): 34,    (28, 'STMT'): 35,    (28, 'STMT\''): 36,
    (34, 'RETURN'): 44,    
    (35, 'VDECL'): 39,    (35, 'ASSIGN'): 40,    (35, 'BLOCK'): 46,    (35, 'STMT'): 35,    (35, 'STMT\''): 36,
    (41, 'ASSIGN'): 8,
    (45, 'RHS'): 53,    (45, 'EXPR'): 14,    (45, 'TERM'): 18,    (45, 'FACTOR'): 19,
    (48, 'COND'): 54,    (48, 'COND\''): 55,
    (49, 'COND'): 57,    (49, 'COND\''): 55,
    (51, 'MOREARGS'): 58,
    (61, 'COND\''): 64,
    (63, 'VDECL'): 39,    (63, 'ASSIGN'): 40,    (63, 'BLOCK'): 66,    (63, 'STMT'): 35,    (63, 'STMT\''): 36,
    (65, 'VDECL'): 39,    (65, 'ASSIGN'): 40,    (65, 'BLOCK'): 67,    (65, 'STMT'): 35,    (65, 'STMT\''): 36,
    (68, 'ELSE'): 70,
    (72, 'VDECL'): 39,    (72, 'ASSIGN'): 40,    (72, 'BLOCK'): 73,    (72, 'STMT'): 35,    (72, 'STMT\''): 36,
}


class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    # 콘솔 창에 트리를 출력하는 함수
    def print_tree(self, prefix='', is_last=True):
        if self.parent is None:
            print(self.symbol)
        else:
            connector = '└── ' if is_last else '├── '
            print(f"{prefix}{connector}{self.symbol}")
            prefix += "    " if is_last else "|   "

        child_count = len(self.children)
        for i, child in enumerate(self.children):
            child.print_tree(prefix, i == child_count - 1)

    # 그래픽으로 트리를 시각화하여 파일로 저장하는 함수
    def render_tree(self, graph=None, parent_id=None):
        if graph is None:
            graph = Digraph()
            graph.attr('node', shape='ellipse')

        node_id = str(id(self))
        graph.node(node_id, label=self.symbol)

        if parent_id is not None:
            graph.edge(parent_id, node_id)

        for child in self.children:
            child.render_tree(graph, node_id)

        return graph

def parse(tokens):
    stack = [0]
    tree_stack = []
    last_line_number = tokens[-1][1]  # 마지막 토큰의 줄 번호
    tokens.append(('$', last_line_number))
    cursor = 0

    while True:
        current_state = stack[-1]
        current_token, line_number = tokens[cursor]
        action_key = (current_state, current_token)
        
        if action_key in action_table:
            action, next_state = action_table[action_key]
            # shift일 경우
            # - 현재 입력 토큰을 기반으로 새로운 노드를 생성, 트리 스택(tree_stack)에 추가
            # - 파싱 스택에 새 상태 push
            # - 입력 토큰 인덱스(cursor)를 1 증가시켜 다음 토큰으로 이동
            if action == 'shift':
                stack.append(next_state)
                new_node = Node(current_token)
                tree_stack.append(new_node)
                cursor += 1
            # reduce일 경우
            # - 해당 생성 규칙의 RHS의 길이를 의미하는 production_rule_length 만큼 스택에서 상태를 pop
            # - 각 pop된 상태에 해당하는 노드들을 트리 스택에서 pop하여 새로운 노드의 자식으로 설정
            # - 해당 생성 규칙의 LHS에 해당하는 새로운 노드를 생성하고, 위에서 꺼낸 자식 노드들을 이 노드의 자식 노드로 연결
            # - 만약 규칙 길이가 0인 경우(입실론 ε), 'ε' 노드를 추가로 생성하고 자식 노드로 추가
            # - 최종적으로 이 노드를 트리 스택에 다시 추가하고, goto_table을 사용하여 새로운 상태로 스택을 업데이트 
            elif action == 'reduce':
                production_rule_length = production_rules[next_state]
                children = []
                for _ in range(production_rule_length):
                    stack.pop()
                    children.append(tree_stack.pop())

                lhs = production_lhs[next_state]
                node = Node(lhs)

                for child in reversed(children):
                    node.add_child(child)

                if production_rule_length == 0:
                    epsilon_node = Node('ε')
                    node.add_child(epsilon_node)

                tree_stack.append(node)
                
                top_state = stack[-1]
                goto_key = (top_state, lhs)
                if goto_key in goto_table:
                    stack.append(goto_table[goto_key])
                else:
                    print(f"Syntax error: Missing goto entry for {goto_key} at token index {cursor} and line number {line_number}")
                    return
            # accept일 경우
            # 트리 스택에 저장된 노드들을 트리의 루트 노드(CODE)에 연결
            # 트리를 콘솔에 출력
            # graphviz 라이브러리를 사용하여 그래픽으로 트리를 시각화하여 파일로 저장
            elif action == 'accept':
                root = Node('CODE')
                for node in tree_stack:
                    root.add_child(node)
                print("Parsing successful!")
                root.print_tree()
                graph = root.render_tree()
                graph.render('output', view=True)
                return
            else:
                print(f"Syntax error at state {current_state} with token {current_token} at token index {cursor} and line number {line_number}")
                return
        else:
            print(f"Syntax error at state {current_state} with token {current_token} at token index {cursor} and line number {line_number}")
            return
        

def read_input_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            tokens = []
            for line_number, line in enumerate(lines, start=1):
                for token in line.split():
                    tokens.append((token, line_number))
            return tokens
    except FileNotFoundError:
        print("Error: File not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main(filename):
    tokens = read_input_file(filename)
    parse(tokens)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: syntax_analyzer <input file>")
        sys.exit(1)
    
    filename = sys.argv[1]
    main(filename)