# Importando biblioteca e módulo
from win10toast import ToastNotifier

# instânciando módulo em uma variavel
toast = ToastNotifier()

# Passando os parâmetros para exibição da notificação
toast.show_toast(title="Notificação do LinkdIn",		    # Titulo
                 msg="Você tem uma nova notificação!",	# Mensagem
                 duration=25,					                  # Duração
                 icon_path="linkedin_icon.ico")			    # caminho do icone
