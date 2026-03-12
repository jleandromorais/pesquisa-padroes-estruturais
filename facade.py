# --- Subsistema Complexo ---
# Estas classes representam operações pesadas e detalhadas.

class ExtratorDados:
    def extrair(self) -> list:
        print("[Extrator] A ligar à base de dados e a extrair registos brutos...")
        return ["registo_1", "registo_2", None, "registo_4"]

class TransformadorDados:
    def limpar_nulos(self, dados: list) -> list:
        print("[Transformador] A aplicar regras de negócio e a remover valores nulos...")
        return [dado for dado in dados if dado is not None]

class CarregadorDados:
    def carregar(self, dados_limpos: list) -> None:
        print(f"[Carregador] A inserir {len(dados_limpos)} registos no Data Warehouse...")

# --- Facade ---

class PipelineDadosFacade:
    """
    A Fachada fornece uma interface unificada e simplificada para 
    executar todo o fluxo do subsistema de dados.
    """
    def __init__(self):
        # A Fachada inicializa e gere as dependências complexas internamente
        self._extrator = ExtratorDados()
        self._transformador = TransformadorDados()
        self._carregador = CarregadorDados()

    def executar_pipeline_diario(self) -> None:
        """Método de alto nível que orquestra a execução das tarefas."""
        print("=== A iniciar o Pipeline de Dados ===")
        
        dados_brutos = self._extrator.extrair()
        dados_limpos = self._transformador.limpar_nulos(dados_brutos)
        self._carregador.carregar(dados_limpos)
        
        print("=== Pipeline concluído com sucesso ===")

# --- Execução do Código Cliente ---
if __name__ == "__main__":
    # O cliente não precisa de saber como o extrator ou o transformador funcionam.
    # Interage apenas com a interface limpa da Facade.
    
    orquestrador = PipelineDadosFacade()
    orquestrador.executar_pipeline_diario()