Function UpdateCode(newCode String) Uint64
1 IF ADDRESS_STRING(SIGNER()) == "" || LOAD("owner") != SIGNER() THEN GOTO 10
2 IF STRLEN(newCode) == 0 THEN GOTO 7
3 IF STRLEN(newCode) == 1 THEN GOTO 9
4 IF EXISTS("nCode") == 1 THEN GOTO 6
5 RETURN STORE("nCode", newCode) == 0
6 RETURN STORE("nCode", LOAD("nCode") + "\n" + newCode) == 0
7 IF STRLEN(LOAD("nCode")) == 0 THEN GOTO 10
8 UPDATE_SC_CODE(LOAD("nCode"))
9 RETURN STORE("nCode", "") == 0
10 RETURN 1
End Function