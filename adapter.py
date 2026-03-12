import xml.etree.ElementTree as ET
from typing import Dict, Any

# 1. Target (Interface esperada pelo nosso sistema)
class ProcessadorDados:
    """Interface que o código cliente da aplicação sabe utilizar."""
    def processar_dados(self) -> Dict[str, Any]:
        raise NotImplementedError("As subclasses devem implementar este método.")

# 2. Adaptee (O sistema legado ou incompatível)
class FornecedorDadosLegado:
    """Uma API antiga que devolve dados exclusivamente em formato XML."""
    def extrair_dados_xml(self) -> str:
        # Simulando uma resposta XML de uma base de dados antiga
        return "<colaborador><nome>Leandro</nome><cargo>Data Intern</cargo></colaborador>"

# 3. Adapter (O tradutor)
class AdaptadorXMLParaDict(ProcessadorDados):
    """
    O Adaptador envolve a classe legada e traduz o retorno XML 
    para o formato de dicionário esperado pelo sistema moderno.
    """
    def __init__(self, fornecedor_legado: FornecedorDadosLegado):
        self._fornecedor_legado = fornecedor_legado

    def processar_dados(self) -> Dict[str, Any]:
        # 3.1. Obtém os dados no formato incompatível
        dados_xml = self._fornecedor_legado.extrair_dados_xml()
        
        # 3.2. Realiza a tradução/conversão
        raiz = ET.fromstring(dados_xml)
        dados_convertidos = {filho.tag: filho.text for filho in raiz}
        
        return dados_convertidos

# --- Execução do Código Cliente ---
if __name__ == "__main__":
    # O cliente instancia a API legada e passa-a ao adaptador
    api_antiga = FornecedorDadosLegado()
    adaptador = AdaptadorXMLParaDict(api_antiga)

    # O sistema cliente chama o método padrão que já conhece
    dados_finais = adaptador.processar_dados()
    
    print("Dados processados com sucesso pelo Adapter:")
    print(dados_finais) 
    # Saída esperada: {'nome': 'Leandro', 'cargo': 'Data Intern'}