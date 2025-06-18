🎮 Descrição do Projeto - CupNerd
📌 Funcionalidades do Código
O jogo CupNerd é uma aventura espacial onde o jogador assume o papel de Xicrinho, que precisa salvar seu irmão Caneco, capturado pela vilã Lunar. O jogo possui:

Tela de introdução com história narrada pela Cálice Lendária (imagem e texto).

Tela para digitar o nome do jogador, que é usado posteriormente na mensagem de agradecimento.

Tela de comandos, explicando como jogar.

Trilha sonora contínua durante o jogo.

Sistema de pausa (pressionando Espaço).

Tela de agradecimento personalizada, com a imagem do Caneco e o nome digitado pelo jogador.

Carregamento e redimensionamento de imagens (nave, inimigos, tiros, chefão, explosão, fundo).

Proteção contra erros no carregamento de recursos com try/except.

🕹️ Como Jogar
Digite seu nome quando solicitado.

Leia os comandos na tela de ajuda pressionando Espaço para continuar.

Entenda a missão na tela de introdução: resgatar o Caneco!

Use os seguintes controles:

Setas direcionais (↑ ↓ ← →) para mover a nave.

Z para atirar.

T para trocar a direção do tiro (disponível após 50 pontos).

Espaço para pausar e despausar o jogo.

Destrua inimigos, fuja dos tiros e enfrente o chefão!

Ao derrotar o chefão, aparece a tela final com um agradecimento do Caneco.

🧰 Dependências e Requisitos
Para rodar o jogo corretamente, é necessário:

✅ Bibliotecas
import os, time
import pygame
import sys
import random
import datetime
import os
import speech_recognition as sr
import pyttsx3
from basicos import pulsar_sol
