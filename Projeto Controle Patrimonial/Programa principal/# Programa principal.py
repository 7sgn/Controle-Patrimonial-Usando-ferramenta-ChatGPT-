# Programa principal
import Variaveis
import tkinter as tk
import pickle

# Cria uma janela
janela = tk.Tk()

# Adiciona um título à janela
janela.title("Controle Patrimonial")

# Define as dimensões da janela
janela.geometry("700x600")

# Cria caixas de texto para inserir as informações dos equipamentos
numero_patrimonio_label = tk.Label(janela, text="Número de patrimônio:")
numero_patrimonio_entry = tk.Entry(janela)
setor_label = tk.Label(janela, text="Setor:")
setor_entry = tk.Entry(janela)
equipamento_label = tk.Label(janela, text="Equipamento:")
equipamento_entry = tk.Entry(janela)

# Define o layout dos widgets na janela
numero_patrimonio_label.pack()
numero_patrimonio_entry.pack()
setor_label.pack()
setor_entry.pack()
equipamento_label.pack()
equipamento_entry.pack()

# Declaração de variáveis

Contratos, GEINFRA, Jurídico, Compras, Estágio, Capacitação, Pesquisa, Tesouraria, Comunicação, ProcessoSeletivo, Controladoria, Núcleodeacessodecrédito, SesiApoio, Ouvidoria, Térreo, Eventos, Diretoria, Presidencia, JuridicoFIBRA, AssessoriaSindical, CIN, AssessoriaAmbiental, AssessoriaLegislativa, AssessoriaPresidencia, Motoristas = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

# Define uma função para ser executada quando o botão for clicado
def cadastrar_equipamento():
    # Obtém as informações inseridas pelo usuário
    numero_patrimonio = numero_patrimonio_entry.get()
    setor = setor_entry.get()
    equipamento = equipamento_entry.get()
    print("Equipamento cadastrado:")
    print("Número de patrimônio:", numero_patrimonio)
    print("Setor:", setor)
    print("Equipamento:", equipamento)
    print("-------------------------")
        # Adiciona as informações ao dicionário correspondente ao setor
    print("-------------------------")
    
    # Adiciona as informações ao dicionário correspondente ao setor
    if setor == "Contratos":
        Contratos[numero_patrimonio] = equipamento
    elif setor == "GEINFRA":
        GEINFRA[numero_patrimonio] = equipamento
    elif setor == "Jurídico":
        Jurídico[numero_patrimonio] = equipamento
    elif setor == "Compras":
        Compras[numero_patrimonio] = equipamento
    elif setor == "Estágio":
        Estágio[numero_patrimonio] = equipamento
    elif setor == "Capacitação":
        Capacitação[numero_patrimonio] = equipamento
    elif setor == "Pesquisa":
        Pesquisa[numero_patrimonio] = equipamento
    elif setor == "Tesouraria":
        Tesouraria[numero_patrimonio] = equipamento
    elif setor == "Comunicação":
        Comunicação[numero_patrimonio] = equipamento
    elif setor == "Processo Seletivo":
        ProcessoSeletivo[numero_patrimonio] = equipamento
    elif setor == "Controladoria":
        Controladoria[numero_patrimonio] = equipamento
    elif setor == "Núcleo de acesso de crédito":
        Núcleodeacessodecrédito[numero_patrimonio] = equipamento
    elif setor == "Sesi Apoio":
        SesiApoio[numero_patrimonio] = equipamento
    elif setor == "Ouvidoria":
        Ouvidoria[numero_patrimonio] = equipamento
    elif setor == "Térreo":
        Térreo[numero_patrimonio] = equipamento
    elif setor == "Eventos":
        Eventos[numero_patrimonio] = equipamento
    elif setor == "Diretoria":
        Diretoria[numero_patrimonio] = equipamento
    elif setor == "Presidencia":
        Presidencia[numero_patrimonio] = equipamento
    elif setor == "Juridico FIBRA":
        JuridicoFIBRA[numero_patrimonio] = equipamento
    elif setor == "Assessoria Sindical":
        AssessoriaSindical[numero_patrimonio] = equipamento
    elif setor == "CIN":
        CIN[numero_patrimonio] = equipamento
    elif setor == "Assessoria Ambiental":
        AssessoriaAmbiental[numero_patrimonio] = equipamento
    elif setor == "Assessoria Legislativa":
        AssessoriaLegislativa[numero_patrimonio] = equipamento
    elif setor == "Assessoria Presidencia":
        AssessoriaPresidencia[numero_patrimonio] = equipamento
    elif setor == "Motoristas":
        Motoristas[numero_patrimonio] = equipamento
        
    # Salva os dicionários em um arquivo
    with open('patrimonio.pickle', 'wb') as f:
        pickle.dump({
            'Contratos': Contratos,
            'GEINFRA': GEINFRA,
            'Jurídico': Jurídico,
            'Compras': Compras,
            'Estágio': Estágio,
            'Capacitação': Capacitação,
            'Pesquisa': Pesquisa,
            'Tesouraria': Tesouraria,
            'Comunicação': Comunicação,
            'Processo Seletivo': ProcessoSeletivo,
            'Controladoria': Controladoria,
            'Núcleo de acesso de crédito': Núcleodeacessodecrédito,
            'Sesi Apoio': SesiApoio,
            'Ouvidoria': Ouvidoria,
            'Térreo': Térreo,
            'Eventos': Eventos,
            'Diretoria': Diretoria,
            'Presidencia': Presidencia,
            'Juridico FIBRA': JuridicoFIBRA,
            'Assessoria Sindical': AssessoriaSindical,
            'CIN': CIN,
            'Assessoria Ambiental': AssessoriaAmbiental,
            'Assessoria Legislativa': AssessoriaLegislativa,
            'Assessoria Presidencia': AssessoriaPresidencia,
            'Motoristas': Motoristas
        }, f)
        # Cria um botão para ver os equipamentos cadastrados para o setor
        ver_equipamentos_button = tk.Button(janela, text="Ver equipamentos cadastrados para este setor", command=lambda: ver_equipamentos_por_setor(setor))
        ver_equipamentos_button.pack()
        
def ver_equipamentos_por_setor(setor):
    # Cria a nova janela
    janela_equipamentos = tk.Toplevel(janela)
    janela_equipamentos.title("Equipamentos cadastrados para o setor {}".format(setor))
    
    # Cria um Listbox para exibir os equipamentos cadastrados
    equipamentos_listbox = tk.Listbox(janela_equipamentos)
    equipamentos_listbox.pack()
    
    # Recupera os equipamentos cadastrados para o setor selecionado
    equipamentos = eval(setor)
    
    # Adiciona os equipamentos ao Listbox
    for patrimonio, equipamento in equipamentos.items():
        equipamentos_listbox.insert(tk.END, "Patrimônio {}: {}".format(patrimonio, equipamento))
    

# Cria um botão para cadastrar os dados
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_equipamento)
botao_cadastrar.pack()

janela.mainloop()
        

    
