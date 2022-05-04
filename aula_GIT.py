from datetime import date, datetime
from dateutil.relativedelta import relativedelta

nome = input('Digite seu primeiro nome:')
ano_nascimento_String = input('Data de nascimento:')
ano_nascimento_date = datetime.strptime(ano_nascimento_String,'%d/%m/%Y').date()
# ano_nascimento_formatado = ano_nascimento_date.strftime('%d/%m/%Y')

data_hoje = date.today()
# data_hoje_formatada = data_hoje.strftime('%d/%m/%Y')

idade = relativedelta(data_hoje, ano_nascimento_date)
print(f'{nome} tem {idade.years} anos!')