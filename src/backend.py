import pandas as pd
from contrato import Vendas

def process_excel(uploaded_file):
    try:
        df = pd.read_excel(uploaded_file)

        # Verificando se há colunas extras
        extras_cols = set(df.columns) - set(Vendas.model_fields.keys())
        if extras_cols:
            return False, f"Existem mais colunas que o necessário: {', '.join(extras_cols)}"

        # Validar cada linha com o contrato
        for index, row in df.iterrows():
            try:
                _ = Vendas(**row.to_dict())
            except Exception as e:
                raise ValueError(f"Erro na linha {index + 2}: {e}")
            
        return True, None
    except ValueError as ve:
        return False, str(ve)
    except Exception as e:
        return False, f"Erro Inesperado: {str(e)}"
