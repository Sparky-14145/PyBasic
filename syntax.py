'''
File:
    Statement

Statement:
    INPUT ("TEXT";)Variable, Variable
    PRINT ("TEXT";)Variable, Variable
{
    IF Expression THEN
        Statement
(
    ELSE IF Expression THEN
        Statement
    ELSE
        Statement
    END IF
)
}
{
    DO
        Statement
    LOOP UNTIL Expression
}
{
    WHILE Expression
        Statement
    WEND
}
    Expression
    END

Expression:
    Variable
    Value
    Variable = Expression
'''

def statement():
    pass

def expression():
    pass

