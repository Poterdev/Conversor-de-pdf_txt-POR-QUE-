from converter import PDFConverter

def main():
    """Função principal para executar conversão"""
    print("Conversor de PDFs para Texto")
    input_folder = input("Digite o caminho da pasta com PDFs: ")
    merge_option = input("Deseja unir todos os txts em um único arquivo? (s/n): ").lower() == 's'
    
    # Instancia conversor
    converter = PDFConverter(input_folder)
    
    try:
        converter.convert_pdfs(merge_files=merge_option)
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

if __name__ == "__main__":
    main()