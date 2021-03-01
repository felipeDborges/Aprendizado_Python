# Importando biblioteca e módulo
from windl0toast import ToastNotifier

# instânciando módulo em uma variavel
toast = ToastNotifier()

# Passando os parâmetros para exibição da notificação
toast.show_toast(title="Notificação do LinkdIn",		# Titulo
                 msg="Você tem uma nova notificação!"		# Mensagem
                 duration=20,					# Duração
                 icon_path="linkedin_icon.icon")		# caminho do icone