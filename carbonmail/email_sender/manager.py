# Aqui estarão todas as funções deste pacote
# Ele vai coordenar este pacote (gerenciador) 

def initialize():
    from carbonmail.email_sender import Email_Sender

    ems = Email_Sender()
    ems.enable_window()
