import ply.lex as lex

import sys

# Implementation of lexical analyzer

# Create Tokens

keywords = {
    'subscribe': 'SUBSCRIBE',
    'unsubscribe': 'UNSUBSCRIBE',
    'provides_service': 'PROVIDES_SERVICE',
    'create_node': 'CREATE_NODE',
    'load': 'LOAD',
    'to': 'TO',
    'with': 'WITH',
    'default': 'DEFAULT',
    'input': 'INPUT',
    'from': 'FROM',
    'of': 'OF',
    'and': 'AND',
    'message_type': 'MESSAGE_TYPE',
    'stop_publishing': 'STOP_PUBLISHING',
    'stop_service': 'STOP_SERVICE',
    'publish': 'PUBLISH',
    'generate_node': 'GENERATE_NODE',
    'service_type': 'SERVICE_TYPE',
    'stop_request': 'STOP_REQUEST',
    'client_requests': 'CLIENT_REQUESTS',
    'create_message': 'CREATE_MESSAGE',
    'none': 'NONE',
    'as': 'AS',
    'node': 'NODE',

    'generate_launch': 'GENERATE_LAUNCH',  # maybe
    'create_custom_message': 'CREATE_CUSTOM_MESSAGE',

    'String': 'STRING',
    'Pose': 'POSE',
    'Point': 'POINT',
    'Quaternion': 'QUATERNION',
    'Twist': 'TWIST',
    'Vector3': 'VECTOR3',
    'Temperature': 'TEMPERATURE',
    'Imu': 'IMU',
    'Char': 'CHAR',
    'Int32': 'INT32',
    'Float32': 'FLOAT32',

    'AddTwoInts': 'ADDTWOINTS',
    'Empty': 'EMPTY',
    'SetBool': 'SETBOOL',
    'Trigger': 'TRIGGER',
    'WaypointClear': 'WAYPOINTCLEAR',
    'WaypointPull': 'WAYPOINTPULL',
    'CommandInt': 'COMMANDINT',
    'SetCameraInfo': 'SETCAMERAINFO',
    'GetMap': 'GETMAP',
    'AddDiagnostics': 'ADDDIAGNOSTICS',
    'SelfTest': 'SELFTEST',
}

tokens = [
             'NAME',
             'PATH',
             'TOPIC_SERVICE',
             'COMMA',
             'INT',
             'STRING_LITERAL',
             'NODE_VAR',
             'CHAR_LITERAL',  # maybe
         ] + list(keywords.values())

# t_NODE_VAR = r'\'[a-zA-Z][a-zA-Z0-9_]*\''

t_COMMA = r'\,'

t_STRING_LITERAL = r'\"([^\\\n]|(\\.))*?\"'
# t_CHAR_LITERAL = r'\'([^\\\n]|(\\.))*?\''

t_ignore_COMMENT = '//.*'
t_ignore = ' \t\n'

t_TOPIC_SERVICE = r'\'((/?[a-zA-Z][a-zA-Z0-9_]*)+)\''

t_PATH = r'((/?[a-zA-Z][a-zA-Z0-9_]*)+)(.py)'


def t_NAME(t):
    r'[a-zA-Z][a-zA-Z0-9_]*'
    t.type = keywords.get(t.value, 'NAME')
    return t


def t_INT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


def t_BLOCK_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
