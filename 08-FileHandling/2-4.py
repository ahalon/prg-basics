employees_file = 'it_company.csv'
position_file = 'software_engineer.txt'
job_title = 'Software Engineer'

print(f"Filtruję pracowników '{job_title}' z '{employees_file}' do '{position_file}'...")

# Otwieramy plik wyjściowy (do zapisu) w trybie 'w'
with open(position_file, 'w') as output_file:
    # Otwieramy plik wejściowy (do odczytu) w trybie 'r'
    with open(employees_file, 'r') as input_file:
        
        # Iterujemy przez plik wejściowy linia po linii
        for line in input_file:
            
            # Sprawdzamy, czy szukane stanowisko znajduje się w linii
            if job_title in line:
                
                # JeśliS tak, zapisujemy całą linię (wraz ze znakiem nowej linii \n)
                # do pliku wyjściowego
                output_file.write(line)

print("Zakończono. Pasujące rekordy zapisano w pliku 'software_engineer.txt'.")