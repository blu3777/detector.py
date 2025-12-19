# # SSH Brute Force Detection Tool

Script em Python criado para detectar possíveis ataques de brute force em SSH a partir da análise de logs de autenticação.

## Descrição

Este projeto monitora arquivos de log do SSH em tempo real e identifica múltiplas tentativas de login falhas vindas do mesmo endereço IP dentro de um intervalo de tempo definido.

O objetivo é praticar conceitos básicos de segurança, análise de logs e detecção de ataques.

## Funcionalidades

- Monitoramento contínuo de logs SSH  
- Detecção de múltiplas falhas de autenticação  
- Agrupamento de tentativas por endereço IP  
- Janela de tempo configurável  
- Alerta quando o limite de tentativas é atingido  

## Como usar

Clone o repositório e execute com Python 3:
python detector.py --log log_file.txt --limit 5 --window 30
