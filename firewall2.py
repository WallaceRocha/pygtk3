# coding=utf-8
#Para usar esse código é necessária a instalação do pygtk 3

import func
from func import initial_status
from func import status_switche
from func import initial_status
from func import rules
from func import acquiring_all_rules
from func import acquiring_log_output
from func import changing_log_output
from func import setting

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
from os import system as s

id_db = []
nome_db = []


switch_name = []
aux2 = []
nomes_db = ""
arquivo = open('swt.db','r')
nomes_db = arquivo.readlines()
arquivo = open('swt.db','r')
for i in nomes_db:
   aux = arquivo.readline()
   nome_db.append(aux.split(" ")[0])
   id_db.append(aux.split(" ")[1][:-1])

class Firewall(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Firewall Ryu")

        self.src_ip = ""
        self.dst_ip = ""
        self.id_swt_aux = ""
        self.priori_aux = ""
        self.protocol = ""
        self.action = ""

        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)
        self.set_default_size(500,200)
        self.set_border_width(10)

        self.ligar = Gtk.Switch()
        #self.ligar.set_active(True)
        self.ligar.connect("notify::active",self.Power)

        self.image = Gtk.Image()
        self.image.set_from_file("fogo.png")
#--------------------------Entradas--------------------------------
        self.entry = Gtk.Entry()
        self.entry.connect("activate",self.sourceIp)
        self.entry.set_alignment(0.5)

        self.entry2 = Gtk.Entry()
        self.entry2.connect("activate", self.destinyIp)
        self.entry2.set_alignment(0.5)

        self.switch_entry = Gtk.Entry()
        self.switch_entry.set_alignment(0.5)
        self.switch_entry.connect("activate",self.name_swt)

        self.entry_posit = Gtk.Entry()
        #self.entry_posit.connect("activate",self.position_rule)
        self.entry_posit.set_alignment(0.5)
        self.entry_posit.connect("activate",self.priority)
#------------------------Botões---------------------------------

        button1 = Gtk.Button(label = 'Bloquear')
        button1_2 = Gtk.Button(label = 'Desbloquear')
        button2 = Gtk.Button(label = 'Bloquear')
        button2_2 = Gtk.Button(label = 'Desbloquear')
        button3 = Gtk.Button(label = 'Bloquear')
        button3_2 = Gtk.Button(label = 'Desbloquear')
        button4 = Gtk.Button(label = 'Bloquear')
        button4_2 = Gtk.Button(label = 'Desbloquear')
        button5 = Gtk.Button(label = 'Bloquear')
        button5_2 = Gtk.Button(label = 'Desbloquear')
        separador = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        button1.connect("clicked",self.bloquear)
        button1_2.connect("clicked",self.desbloquear)
        button2.connect("clicked", self.bloquear_ICMP)
        button2_2.connect("clicked", self.desbloquear_ICMP)
        ajuda = Gtk.ToolButton.new_from_stock(Gtk.STOCK_DIALOG_QUESTION)
        info = Gtk.ToolButton.new_from_stock(Gtk.STOCK_INFO)
        info.connect("clicked", self.infoBox)
        ajuda.connect("clicked", self.janela_de_ajuda)
        ajuda.set_size_request(20,20)
        plusButton = Gtk.ToolButton.new_from_stock(Gtk.STOCK_ADD)
        plusButton.connect("clicked", self.MoreFunctions)

#----------------------Labels---------------------------------------
        label0 = Gtk.Label("Origem")
        label1 = Gtk.Label("TCP")
        label2 = Gtk.Label("ICMP")
        label3 = Gtk.Label("SSH")
        label4 = Gtk.Label("SMTP")
        label5 = Gtk.Label("Destino")
        self.id_Label = Gtk.Label("Nome")
        #self.nomeSwitch = Gtk.Label("")
        self.Label_posit = Gtk.Label("Prioridade")
        self.aviso = Gtk.Label('Aperte no botão de "?"')
#----------------------Organização de espaços-------------------------------
        grid = Gtk.Grid()
        grid.set_column_spacing(1)
        grid.set_column_homogeneous(False)
        grid.set_row_homogeneous(False)
        grid.set_row_spacing(5)
#-----------------posicionar e ligar widgets--------------------------------

        grid.attach(self.image, 0, 0, 7, 1)#Banner
        grid.attach(label0, 1, 1, 1, 1)
        grid.attach(self.entry2, 2, 2, 2, 1)
        #grid.attach(self.entry_posit, 3, )
        grid.attach(label5, 1, 2, 1, 1)
        grid.attach(self.entry, 2, 1, 2, 1)
        grid.attach(self.switch_entry, 2, 3, 2, 1)
        grid.attach(self.entry_posit, 2, 4, 2, 1)
        grid.attach(self.Label_posit, 1, 4, 1, 1)
        grid.attach(self.id_Label, 1, 3, 1, 1)
        grid.attach(separador, 0, 5, 7, 1 )
        grid.attach(label1, 1, 6, 1, 1)
        grid.attach(label2, 1, 7, 1, 1)
        grid.attach(label3, 1, 8, 1, 1)
        grid.attach(label4, 1, 9, 1, 1)
        grid.attach(button1, 2, 6, 1, 1)
        grid.attach(button1_2, 3, 6, 1, 1)
        grid.attach(button2, 2, 7, 1, 1)
        grid.attach(button2_2, 3, 7, 1, 1)
        grid.attach(button3, 2, 8, 1, 1)
        grid.attach(button3_2, 3, 8, 1, 1)
        grid.attach(button4, 2, 9,1, 1)
        grid.attach(button4_2,3, 9, 1, 1)
        grid.attach(plusButton, 0, 10, 1, 1)
        grid.attach(ajuda, 0, 11, 1, 1)
        grid.attach(info, 0, 12, 1, 1)
        #grid.attach(self.ligar, 6, 11, 1, 1)
        grid.attach(self.aviso, 2, 13, 2, 1)


        self.add(grid)


#-------------------------Janelas------------------------------------
    def janela_de_ajuda(self, widget):
        window = Gtk.Window(title = "Ajuda")
        window.set_position(Gtk.WindowPosition.CENTER)
        window.set_default_size(500,500)
        window.set_resizable(False)
        imageHelp = Gtk.Image()
        imageHelp.set_from_file("green.jpg")

        grid2 = Gtk.Grid()
        window.escreve = Gtk.Label("Ajuda:\n\n\n"
                                    '● Primeiro de tudo, aperte no botão de "+".\n'
                                    "● Logo após, cadastre um switch colocando o id,\n"
                                    "   um nome, e então, clique em validar.\n"
                                    "● Após ter dito que foi validado, confirme em listar.\n"
                                    "● Toda vez que adicionar um switch novo, reinicie o programa.\n"
                                    "● Quando já estiver reiniciado, digite o ip de origem e destino, \n"
                                    "   o nome cadastrado para o switch(pode rever em 'listar'),\n"
                                    "   e a prioridade que a regra vai tomar.\n"
                                    '● Finalmente, escolha a ação que desejar e pronto. Se tudo \n'
                                    '   estiver correto, uma mensagem de confirmação será enviada.\n\n')

        grid2.attach(window.escreve, 2,2,1,1)
        grid2.attach(imageHelp, 0,1,4,1)

        window.add(grid2)
        window.show_all()

    def MoreFunctions(self, widget):
        imageMore = Gtk.Image()
        imageMore.set_from_file("blue2.jpg")
        firewall2 = Gtk.Window(title = "Adicionais")
        firewall2.set_position(Gtk.WindowPosition.CENTER)
        firewall2.set_default_size(100,200)
        firewall2.set_resizable(False)

        grid3 = Gtk.Grid()
        self.switch_entry_id = Gtk.Entry()
        self.id_label = Gtk.Label("id")
        self.switch_entry_nome = Gtk.Entry()
        self.nome_label = Gtk.Label("Nome")
        self.valid_button = Gtk.Button("Validar")
        self.valid_button.connect("clicked",self.dataBase)
        self.listar_button = Gtk.Button("Listar")
        self.listar_button.connect("clicked",self.listar_func)

        grid3.attach(imageMore,0,0,5,1)
        grid3.attach(self.switch_entry_id, 2, 1, 1, 1)
        grid3.attach(self.id_label, 1, 1, 1, 1)
        grid3.attach(self.switch_entry_nome, 2, 2, 1, 1)
        grid3.attach(self.nome_label, 1, 2, 1, 1)
        grid3.attach(self.valid_button, 3, 2, 1, 1)
        grid3.attach(self.ligar,3, 1, 1, 1)
        grid3.attach(self.listar_button,3, 3, 1, 1)
        firewall2.add(grid3)
        firewall2.show_all()
#-------------------------Fim janelas/Inicio...----------------------------------------
    def infoBox(self, widget):
        infoBox = Gtk.Window(title = "Sobre")
        infoBox.set_position(Gtk.WindowPosition.CENTER)

        grid5 = Gtk.Grid()
        info = ("Programa criado por:\n"\
                "Ismael Lima: Implementação do firewall Ryu.\n"\
                "Wallace Rocha: Interface gráfica.")
        informacao = Gtk.Label(info)
        grid5.attach(informacao,0,0,1,1)
        infoBox.add(grid5)
        infoBox.show_all()

#------------------Funções-------------------------
    def sourceIp(self, entry):
        if len(self.entry.get_text()) == 0:

            self.aviso.set_text("Falta parametros")

        else:

            self.src_ip = self.entry.get_text()
            nome = self.entry.get_text()+" configurado"
            self.aviso.set_text(nome)
            print(self.src_ip)

    def destinyIp(self, entry):
        if len(self.entry2.get_text()) == 0:
            self.aviso.set_text("Falta parametros")
        else:
            self.dst_ip = self.entry2.get_text()
            self.Host = (self.entry2.get_text() + " configurado")
            self.aviso.set_text(self.Host)
            print(self.dst_ip)

    def name_swt(self, entry):
            nomeaux = self.switch_entry.get_text()
            if nomeaux in nome_db:
                indx = nome_db.index(nomeaux)
                self.id_swt_aux = id_db[indx]
            print(self.id_swt_aux)
    def priority(self, entry):
            self.priori_aux = self.entry_posit.get_text()
            print(self.priori_aux)
    def dataBase(self, widget):

        id_db = []
        nome_db = []
        nomes_db = ""
        arquivo = open('swt.db','r')
        nomes_db = arquivo.readlines()
        arquivo = open('swt.db','r')
        for i in nomes_db:
           aux = arquivo.readline()
           nome_db.append(aux.split(" ")[0])
           id_db.append(aux.split(" ")[1][:-1])

        add_to_db = (self.switch_entry_nome.get_text()+" "+self.switch_entry_id.get_text()+"\n")
        nomes_db.append(add_to_db)

        arquivo = open('swt.db','w')
        arquivo.writelines(nomes_db)
        arquivo.close()


        self.aviso.set_text(add_to_db[:-1])

    def listar_func(self, widget):
        list_win = Gtk.Window(title = "Informações de switchs")
        list_win.set_position(Gtk.WindowPosition.CENTER)
        list_win.set_default_size(300,500)
        #list_win.set_resizable(False)
        imageList = Gtk.Image()
        imageList.set_from_file("branco.png")
        arquivo = open("swt.db","r")
        listar_swt = Gtk.Label(arquivo.read())
        scroll = Gtk.ScrolledWindow()
        scroll.set_border_width(10)
        scroll.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)
        scroll.add_with_viewport(listar_swt)
        list_win.add(scroll)
        list_win.show_all()
    def bloquear(self, widget):
        print("botão funcionando.")
    def desbloquear(self, widget):
        print("botão funcionando.")

    def bloquear_ICMP(self, widget):
        self.protocol = "ICMP"
        self.action = "ALLOW"
        print(self.protocol)
        print(self.action)
        self.aviso.set_text("ICMP bloqueado")

        setting(self.src_ip,self.dst_ip, self.action, self.priori_aux,self.id_swt_aux,self.protocol)

        initial_status()
        status_switche()
        
        rules()

    def desbloquear_ICMP(self, widget):
        protocol = "ICMP"
        action = "ALLOW"
        self.aviso.set_text("ICMP desbloqueado")


    def Power(self, button, active):
        if button.get_active():
            self.aviso.set_text('Switch ligado')
        else:
            self.aviso.set_text('Switch desligado')






window = Firewall()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
