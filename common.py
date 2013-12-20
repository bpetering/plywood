def lex_shell(lexer, prompt='> '):
    x = raw_input(prompt)
    lexer.input(x)
    while True:
        tok = lexer.token()
        if not tok: break
        print tok
