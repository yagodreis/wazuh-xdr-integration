import datetime
import json

def walkoff_main(input_data):
    # Captura o JSON bruto do nó anterior
    nodevalue = r"""$exec"""
    
    try:
        data = json.loads(nodevalue)
        raw_date = data.get("timestamp")
        
        # Limpeza e formatação
        clean_date = raw_date.split(".")[0].replace("T", " ")
        date_obj = datetime.datetime.strptime(clean_date, '%Y-%m-%d %H:%M:%S')
        
        # O RETURN é o que envia o dado para o próximo nó
        return date_obj.strftime("%d/%m/%Y %H:%M:%S")
        
    except Exception as e:
        return f"Erro: {str(e)}"

print(walkoff_main(""))
