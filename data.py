import datetime

# Função para verificar se a data está dentro do limite de 15 dias
def agendar_evento(data_evento):

    # Obter a data atual
    data_atual = datetime.datetime.now()
    
    # Calcular a data máxima (15 dias à frente)
    data_maxima = data_atual + datetime.timedelta(days=15)
    
    # Verificar se o evento está dentro do limite de 15 dias
    if data_evento > data_maxima:
        print(f"Não é possível agendar o evento para {data_evento.strftime('%d/%m %H:%M:%S')}.")
        print(f"O evento deve ser agendado até {data_maxima.strftime('%d/%m %H:%M:%S')}.")
        return False
    else:
        return True

# Função para agendar um evento
def agendar():
    # Solicitar ao usuário para inserir a data e hora desejada
    data_str = input("Digite a data e hora do evento (formato: dd/mm HH:MM): ")
    
    try:
        # Converter a string para um objeto datetime
        data_evento = datetime.datetime.strptime(data_str, "%d/%m %H:%M")
        
        # Verificar se o evento está dentro do limite de 15 dias
        if agendar_evento(data_evento):
            print(f"Evento agendado para {data_evento.strftime('%d/%m %H:%M:%S')}")
            return data_evento
        else:
            return None
    except ValueError:
        print("Formato de data inválido. Tente novamente com o formato dd/mm HH:MM.")
        return None

# Função principal para agendar múltiplos eventos
def main():
    eventos_agendados = []
    
    while True:
        print("\n--- Agendamento de Eventos ---")
        evento = agendar()
        
        if evento:
            eventos_agendados.append(evento)
        
        # Perguntar se o usuário deseja agendar outro evento
        continuar = input("Deseja agendar outro evento? (s/n): ")
        if continuar.lower() != 's':
            break
    
    # Exibir todos os eventos agendados
    print("\nEventos agendados:")
    for evento in eventos_agendados:
        print(evento.strftime("%d/%m %H:%M:%S"))

# Chamar a função principal
if __name__ == "__main__":
    main()