#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script para processar respostas criptografadas do formulário de avaliação.

Lê todos os arquivos JSON baixados, descriptografa as respostas (Base64)
e consolida em um único arquivo JSON com todas as respostas dos alunos.

Uso:
    python processar_respostas.py [diretório_de_entrada] [arquivo_saida]

Exemplo:
    python processar_respostas.py ./respostas consolidado.json
    python processar_respostas.py . resultado_final.json
"""

import json
import base64
import os
import glob
from pathlib import Path
from datetime import datetime
import sys


def descriptografar_base64(texto_criptografado):
    """
    Descriptografa um texto em Base64.
    
    Args:
        texto_criptografado (str): Texto criptografado em Base64
        
    Returns:
        dict: Dicionário com os dados descriptografados
        
    Raises:
        ValueError: Se a descriptografia falhar
    """
    try:
        texto_decodificado = base64.b64decode(texto_criptografado).decode('utf-8')
        dados = json.loads(texto_decodificado)
        return dados
    except Exception as e:
        raise ValueError(f"Erro ao descriptografar: {str(e)}")


def processar_arquivo_resposta(caminho_arquivo):
    """
    Processa um único arquivo de resposta criptografado.
    
    Args:
        caminho_arquivo (str): Caminho do arquivo JSON
        
    Returns:
        dict: Dados descriptografados do aluno, ou None se falhar
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            dados_arquivo = json.load(f)
        
        if 'encrypted' not in dados_arquivo:
            print(f"⚠️  Aviso: {caminho_arquivo} não contém dados criptografados. Pulando...")
            return None
        
        encrypted_data = dados_arquivo['encrypted']
        dados_descriptografados = descriptografar_base64(encrypted_data)
        
        return dados_descriptografados
        
    except json.JSONDecodeError:
        print(f"❌ Erro: {caminho_arquivo} não é um JSON válido.")
        return None
    except Exception as e:
        print(f"❌ Erro ao processar {caminho_arquivo}: {str(e)}")
        return None


def consolidar_respostas(diretorio_entrada, arquivo_saida):
    """
    Consolida todas as respostas de um diretório em um único arquivo.
    
    Args:
        diretorio_entrada (str): Diretório contendo os arquivos JSON
        arquivo_saida (str): Caminho do arquivo consolidado a ser criado
        
    Returns:
        bool: True se consolidação foi bem-sucedida
    """
    
    # Garantir que o diretório existe
    if not os.path.isdir(diretorio_entrada):
        print(f"❌ Erro: Diretório '{diretorio_entrada}' não encontrado.")
        return False
    
    # Procurar por arquivos JSON
    padrao = os.path.join(diretorio_entrada, 'resposta_*.json')
    arquivos = glob.glob(padrao)
    
    if not arquivos:
        print(f"❌ Erro: Nenhum arquivo 'resposta_*.json' encontrado em '{diretorio_entrada}'")
        return False
    
    print(f"📁 Encontrados {len(arquivos)} arquivo(s) de resposta.\n")
    
    respostas_consolidadas = []
    erros = 0
    
    # Processar cada arquivo
    for i, arquivo in enumerate(sorted(arquivos), 1):
        nome_arquivo = os.path.basename(arquivo)
        print(f"[{i}/{len(arquivos)}] Processando: {nome_arquivo}...", end=" ")
        
        dados = processar_arquivo_resposta(arquivo)
        
        if dados:
            respostas_consolidadas.append(dados)
            print("✅")
        else:
            print("❌")
            erros += 1
    
    print(f"\n{'='*60}")
    print(f"Processamento concluído:")
    print(f"  ✅ Respostas processadas com sucesso: {len(respostas_consolidadas)}")
    print(f"  ❌ Erros encontrados: {erros}")
    
    if not respostas_consolidadas:
        print(f"\n❌ Nenhuma resposta foi processada com sucesso.")
        return False
    
    # Criar estrutura final consolidada
    resultado_final = {
        "metadados": {
            "total_alunos": len(respostas_consolidadas),
            "data_consolidacao": datetime.now().isoformat(),
            "versao": "1.0"
        },
        "respostas": respostas_consolidadas
    }
    
    # Salvar arquivo consolidado
    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            json.dump(resultado_final, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Arquivo consolidado salvo: {arquivo_saida}")
        print(f"\n📊 Estatísticas:")
        print(f"  Total de alunos: {len(respostas_consolidadas)}")
        print(f"  Arquivo de saída: {os.path.abspath(arquivo_saida)}")
        print(f"  Tamanho: {os.path.getsize(arquivo_saida) / 1024:.2f} KB")
        
        return True
        
    except Exception as e:
        print(f"❌ Erro ao salvar arquivo consolidado: {str(e)}")
        return False


def main():
    """Função principal do script."""
    
    # Valores padrão
    diretorio_padrao = "."
    arquivo_saida_padrao = "respostas_consolidadas.json"
    
    # Processar argumentos de linha de comando
    if len(sys.argv) >= 2:
        diretorio_entrada = sys.argv[1]
    else:
        diretorio_entrada = diretorio_padrao
    
    if len(sys.argv) >= 3:
        arquivo_saida = sys.argv[2]
    else:
        arquivo_saida = arquivo_saida_padrao
    
    print("="*60)
    print("🔐 PROCESSADOR DE RESPOSTAS AVALIATIVAS")
    print("="*60)
    print(f"\n📂 Diretório de entrada: {os.path.abspath(diretorio_entrada)}")
    print(f"📄 Arquivo de saída: {os.path.abspath(arquivo_saida)}\n")
    
    # Executar consolidação
    sucesso = consolidar_respostas(diretorio_entrada, arquivo_saida)
    
    print("="*60)
    if sucesso:
        print("✅ Processamento finalizado com sucesso!")
    else:
        print("❌ Processamento finalizado com erros.")
    print("="*60)
    
    return 0 if sucesso else 1


if __name__ == "__main__":
    sys.exit(main())