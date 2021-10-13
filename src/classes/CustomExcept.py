

class MinhaException(Exception):
    pass


class ApiSemAcesso(MinhaException):
    """ Retorna uma Exception quando não houver conectividade """
    pass


class EndPointInvalido(MinhaException):
    """ Retorna uma Exception quando o EndPoint estiver Errado """
    pass


class ErroBancoDeDados(MinhaException):
    """ Erro ao efetuar alguma operação no Banco de Dados """
    pass