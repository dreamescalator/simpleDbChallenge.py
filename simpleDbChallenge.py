#!/usr/bin/python

# Simple Database Challenge v1.0
# Author: Lewis Black
#
# Data Commands:
# SET        : Sets variable = value
# GET        : prints out value of variable name; or null
# UNSET      : Unsets variable name
# NUMEQUALTO : Print # of vars set to 'value'; If none, print 0
# END        : Exit the program

#Transaction Commands
# BEGIN    : Start a new transaction block
# ROLLBACK : Undoes most recent transaction block
# COMMIT   : commits all transaction blocks

def simpleDb():
    db ={}
    t_block = []
    
    #Helper Function
    def write_to_(_db, k, v):
        _db[k]= v

    #Input Flow/Control Fucntions
    def evaluate(command):
        if command[0:4] in {'SET ', 'GET '}:
            if command[0:4] == 'SET ':
                write_to_(db, set_(command)[0], set_(command)[1])
            else:
                get_(command)
        elif command[0:6] == 'UNSET ':
            unset_(command)
        elif command[0:11] == 'NUMEQUALTO ':
            numequalto_(command)
        elif command[0:5] == 'BEGIN':
            begin_()
        elif command[0:7] == 'COMMIT':
            commit_()
        elif command[0:9] == 'ROLLBACK':
            rollback_()
        else:
            print "Command not understood :-/"
        do_again()
    
    def c_evaluate(command):
        if command[0:4] in {'SET ', 'GET '}:
            if command[0:4] == 'SET ':
                write_to_(db, set_(command)[0], set_(command)[1])
            else:
                get_(command)
        elif command[0:6] == 'UNSET ':
            unset_(command)
        elif command[0:11] == 'NUMEQUALTO ':
            numequalto_(command)
        elif command[0:5] == 'BEGIN':
            begin_()
        elif command[0:7] == 'COMMIT':
            commit_()
        elif command[0:9] == 'ROLLBACK':
            rollback_()
        else:
            print "Command not understood :-/"

    def do_again():
        next_input = raw_input()
        if next_input != 'END':
            evaluate(next_input)
        else:
            print 'Goodbye :-)'
            exit()
    
    #Data Commands   
    def set_(_input):
        name =''
        value =''
        if len(_input) >= 5:
            if _input[0:4] == 'SET ':
                if ' ' in _input[3]:
                    if ' ' not in _input[4:]:
                        name = _input[4:]
                        value = None
                    elif _input[4:].index(' ') > 0:
                        name = _input[4:_input[4:].index(' ')+4:]
                        value = _input[_input[4:].index(' ')+5:]
                    #do stuff
                return name, value #
           
    def get_(_input):
        if len(_input) > 4:
            if _input[0:4] == 'GET ':   
                key = _input[4:]
                if key in db:
                    print db[key]
                else:
                    print "Please Enter a valid key"

    def unset_(_input):
        if len(_input) > 6:
            if _input[0:6] == 'UNSET ':   
                key = _input[6:]
                db.pop(key, "None")
     
    def numequalto_(_input):
        count = 0
        if len(_input) > 11:
            if _input[0:11] == 'NUMEQUALTO ':
                if ' ' not in _input[11:]:
                    value = _input[11:]
                    print db.values().count(value)

    
    #Transaction Commands
    def begin_():
        _command = raw_input()
        do_trans_block_(_command)
    
    def do_trans_block_(_command):
        new_tb = []
        while _command not in {'END', 'COMMIT', 'ROLLBACK', 'BEGIN'}:
            new_tb.append(_command)
            _command = raw_input()
        t_block.append(new_tb)
        evaluate(_command)
        
    def commit_():
        if len(t_block) == 0:
            print "NO TRANSACTION"
        else:
            print t_block
            for t_list in t_block:
                for row in t_list:
                    c_evaluate(str(row))
            del t_block[:]
            print db
            do_again()
    
    def rollback_():
        if len(t_block) == 0:
            print "NO TRANSACTION"
        else:
            t_block.pop()
        do_again()
            
    evaluate(raw_input())    
simpleDb()   
        
 