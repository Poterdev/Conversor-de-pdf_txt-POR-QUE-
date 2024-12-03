import os
import PyPDF2

class PDFConverter:
    def __init__(self, input_folder=None, output_folder='./txts'):
        """Inicializa o conversor de PDFs"""
        self.input_folder = input_folder
        self.output_folder = output_folder
        
    def validate_input_folder(self):
        """Valida se a pasta de entrada existe"""
        if not os.path.exists(self.input_folder):
            raise FileNotFoundError(f"Pasta não encontrada: {self.input_folder}")
        
    def create_output_folder(self):
        """Cria pasta de saída se não existir"""
        os.makedirs(self.output_folder, exist_ok=True)
        
    def convert_pdfs(self, merge_files=False):
        """
        Converte PDFs para txt
        
        Args:
            merge_files (bool): Unir todos os txts em um único arquivo
        """
        self.validate_input_folder()
        self.create_output_folder()
        
        # Lista para armazenar conteúdos dos txts
        txt_contents = []
        conversoes = 0
        
        # Percorre PDFs
        for filename in os.listdir(self.input_folder):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(self.input_folder, filename)
                txt_filename = os.path.splitext(filename)[0] + '.txt'
                txt_path = os.path.join(self.output_folder, txt_filename)
                
                try:
                    with open(pdf_path, 'rb') as pdf_file:
                        pdf_reader = PyPDF2.PdfReader(pdf_file)
                        
                        # Se não for merge, salva em arquivo individual
                        if not merge_files:
                            with open(txt_path, 'w', encoding='utf-8') as txt_file:
                                for page in pdf_reader.pages:
                                    txt_file.write(page.extract_text())
                        else:
                            # Para merge, acumula conteúdo
                            txt_content = ''
                            for page in pdf_reader.pages:
                                txt_content += page.extract_text()
                            txt_contents.append(txt_content)
                    
                    conversoes += 1
                    print(f"Convertido: {filename} -> {txt_filename}")
                
                except Exception as e:
                    print(f"Erro ao converter {filename}: {e}")
        
        # Merge de arquivos, se solicitado
        if merge_files and txt_contents:
            merge_path = os.path.join(self.output_folder, 'merged_pdfs.txt')
            with open(merge_path, 'w', encoding='utf-8') as merge_file:
                for content in txt_contents:
                    merge_file.write(content + '\n\n')  # Separa com duas quebras
            print(f"Arquivo unificado criado: {merge_path}")
        
        print(f"Total de PDFs convertidos: {conversoes}")